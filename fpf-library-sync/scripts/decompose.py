from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from _common import (
    PATTERN_ID_RE,
    DecomposeReport,
    ExtractedUnit,
    format_reference,
    generate_index,
    idempotent_write,
    retire_stale_context_refs,
    slugify,
    write_context_units,
)


END_RE = re.compile(r"^(#{1,6})\s+(.+):End\s*$", re.MULTILINE)
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+)$")


def parse_spec(spec_path: Path) -> tuple[DecomposeReport, list[ExtractedUnit], list[ExtractedUnit], str]:
    """Decompose one FPF Library monolith (FPF-Spec.md or a DPF framework file) into reference units.

    Returns (report, units, context_units, spec_filename).

    A DPF monolith differs from FPF-Spec in one relevant place: its pattern index
    rows carry a §-ordinal in the first cell and the PatternID inside a markdown link
    in the second cell (e.g. `| 1 | [SYSE.1 - Title](#…) | Stable | … |`), whereas
    FPF-Spec puts the PID in the first cell. The `:End` boundary + heading-extraction
    logic is shared, only the ToC row parser is generalized."""
    text = spec_path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines(keepends=True)
    spec_filename = spec_path.name

    report = DecomposeReport(
        spec_path=str(spec_path),
        spec_type="DPF",
        total_patterns=0,
        patterns_extracted=0,
        toc_parsed=False,
        toc_entries=0,
    )

    end_markers = _collect_end_markers(lines)
    end_marker_ids = {pid for pid, _ in end_markers}
    report.total_patterns = len(end_markers)

    all_headings = _build_heading_list(lines)

    heading_pids = {
        pid
        for pid in {h[0] for h in all_headings}
        if pid not in end_marker_ids
        and not any(pid.startswith(p + ".") for p in end_marker_ids)
    } | end_marker_ids

    toc_data = _parse_toc(text, report)

    units: list[ExtractedUnit] = []
    consumed: list[tuple[int, int]] = []
    section_headings = _collect_section_headings(lines)
    for pid, end_line in end_markers:
        candidates = [(ln, ht) for hpid, ln, ht in all_headings if hpid == pid and ln < end_line]
        if candidates:
            exact = [(ln, ht) for ln, ht in candidates if ht.split()[0].rstrip("`") == pid]
            if exact:
                start_line, heading_text = max(exact, key=lambda x: x[0])
            else:
                start_line, heading_text = min(candidates, key=lambda x: x[0])
        else:
            # Publication unit opened by a human-title heading carrying no PatternID
            # token (e.g. RHY: `## RHY.Edition:End` opened by `# Edition and reuse`).
            # Fall back to the nearest preceding H1/H2 not already consumed by a unit.
            prior = [
                (ln, ht)
                for ln, level, ht in section_headings
                if ln < end_line and not any(s <= ln <= e for s, e in consumed)
            ]
            if not prior:
                report.warnings.append(f"PID {pid}: :End marker found at L{end_line} but no opening heading found")
                continue
            start_line, heading_text = max(prior, key=lambda x: x[0])

        title = heading_text
        if pid in toc_data:
            title = toc_data[pid].get("title", title)

        raw_lines = lines[start_line - 1 : end_line]
        body = "".join(raw_lines)

        meta: dict = {"id": pid, "title": title}
        if pid in toc_data:
            t = toc_data[pid]
            if "status" in t:
                meta["status"] = t["status"]
            if "keywords" in t:
                meta["keywords"] = t["keywords"]
            if "dependencies" in t and t["dependencies"]:
                meta["dependencies"] = t["dependencies"]
            if t.get("dependencies_raw"):
                meta["dependencies_raw"] = t["dependencies_raw"]

        units.append(ExtractedUnit(
            pid=pid,
            title=title,
            body=body,
            start_line=start_line,
            end_line=end_line,
            metadata=meta,
            is_pattern=pid in toc_data,
        ))
        consumed.append((start_line, end_line))

    # Warn on Stable pattern openings without :End (best effort, same discipline as FPF).
    def _is_stable(pid: str) -> bool:
        if pid not in toc_data:
            return True
        return toc_data[pid].get("status", "") == "Stable"

    for pid in heading_pids - end_marker_ids:
        if not re.search(r"\.\d+$", pid):
            continue  # publication/reader section (e.g. LDR.Use, IS.Readme), not a pattern
        if _is_stable(pid):
            candidates = [(ln, ht) for hpid, ln, ht in all_headings if hpid == pid]
            if candidates:
                report.warnings.append(f"PID {pid}: opening heading at L{candidates[0][0]} has no :End marker")

    for pid in toc_data:
        if pid not in end_marker_ids and pid not in heading_pids:
            if _is_stable(pid):
                report.warnings.append(f"PID {pid}: listed in ToC but no :End marker found")

    # Orphan detection: a full pattern body (:End unit with a numeric PID) that has
    # no pattern-index entry — the generated reference would carry no status/keywords/
    # dependencies and its §-position would be missing from the index (DEC-0009 check).
    for pid in sorted(end_marker_ids):
        if not re.search(r"\.\d+$", pid):
            continue  # publication unit (e.g. {Code}.Reference/.Sources), not indexed by design
        if pid not in toc_data:
            report.warnings.append(f"ORPHAN {pid}: pattern body has no pattern-index entry")

    report.patterns_extracted = len(units)

    context_units = _extract_non_pattern_sections(lines, section_headings, consumed)

    return report, units, context_units, spec_filename


def _parse_toc(text: str, report: DecomposeReport) -> dict[str, dict]:
    """Parse the DPF pattern index.

    The DPF monolith opens with `# Table of Contents` (reader-navigation table, 2-col
    "Public unit | Reader use"), followed by a `## Pattern index` of 6-slot rows
    `| § | [PID - Title](#anchor) | Status | Keywords | Dependencies |` repeated across
    Part banners. The FPF-style 5-slot row (`| PID | **Title** | …`) is also accepted for
    robustness."""
    result: dict[str, dict] = {}

    toc_start = text.find("# Table of Content")  # matches "Contents" by prefix
    if toc_start < 0:
        report.warnings.append("ToC not found: '# Table of Content(s)' heading missing")
        return result

    first_end = END_RE.search(text)
    if not first_end:
        report.warnings.append("ToC parsing failed: no :End markers in spec")
        return result

    toc_section = text[toc_start:first_end.start()]

    entry_count = 0
    for line in toc_section.splitlines():
        line_stripped = line.strip()
        if not line_stripped.startswith("|"):
            continue
        cells = _split_toc_row(line_stripped)
        if len(cells) < 5:
            continue
        parsed = _parse_toc_row(cells)
        if parsed is None:
            continue
        pid, title, status, keywords, dependencies = parsed
        result[pid] = {
            "title": title,
            "status": status,
            "keywords": keywords,
            "dependencies": dependencies,
            "dependencies_raw": cells[4].strip() if len(cells) > 4 else "",
        }
        entry_count += 1

    report.toc_parsed = True
    report.toc_entries = entry_count
    return result


def _parse_toc_row(cells: list[str]) -> tuple[str, str, str, list[str], dict] | None:
    """Parse one ToC/index row into (pid, title, status, keywords, dependencies).

    Returns None for non-pattern rows (header/separator, cluster, reader-navigation 2-col).

    Two schemes:
      DPF: `| § | [PID - Title](#anchor) | Status | Keywords | Dependencies |`
           (after split: cells[0] = ordinal int, cells[1] = link, cells[2..4] = rest)
      FPF: `| PID | **Title** | Status | Keywords | Dependencies |`
           (cells[0] = PID)
    """
    col0 = cells[0].strip()
    col1 = cells[1].strip()
    status = cells[2].strip() if len(cells) > 2 else ""
    kw = cells[3].strip() if len(cells) > 3 else ""
    dep = cells[4].strip() if len(cells) > 4 else ""

    # DPF scheme: § column is a bare integer (1) or a Part-letter ordinal (A.1/B.1),
    # and the PatternID lives inside a markdown link in the second column.
    is_ordinal = col0.isdigit() or bool(re.fullmatch(r"[A-Z]+\.\d+", col0))
    if is_ordinal and col1.startswith("["):
        m = PATTERN_ID_RE.search(col1)
        if m is None:
            return None
        pid = m.group(1)
        inner = _link_text(col1)
        title = _strip_pid_prefix(inner, pid)
        return pid, title, status, _parse_keywords(kw), _parse_dependencies(dep)

    # FPF scheme: PID in the first cell. Skip cluster/header/non-PID rows (e.g. a
    # "Core" cross-reference row whose first cell carries no PatternID at all).
    pid_raw = col0.strip("*").strip()
    if not pid_raw or pid_raw.startswith("*") or pid_raw.endswith("*"):
        return None
    if not re.search(r"[A-Za-z]", pid_raw):
        return None
    pid = _extract_id(pid_raw)
    if not pid:
        return None
    title = re.sub(r"\*\*(.+?)\*\*", r"\1", col1)
    return pid, title, status, _parse_keywords(kw), _parse_dependencies(dep)


def _link_text(cell: str) -> str:
    m = re.match(r"\[([^\]]+)\]", cell)
    return m.group(1) if m else cell


def _strip_pid_prefix(text: str, pid: str) -> str:
    t = text.strip()
    if t.startswith(pid):
        rest = t[len(pid):].lstrip(" -–—").strip()
        return rest or t
    return t


def _parse_keywords(cell: str) -> list[str]:
    """Extract keywords from a DPF Keywords & Search Queries cell.

    Labeled form (`*Keywords:* a, b. *Queries:* "…"`) — shared with FPF; plain form
    (bare `a, b, c. Which …?`) — PSDA-style, no labels."""
    keywords: list[str] = []
    if "*Keywords:" in cell:
        for part in cell.split("*Keywords:")[1:]:
            kw_text = part.split("*Queries:")[0]
            kw_text = kw_text.replace("**", "").replace("*", "")
            for word in re.split(r"[;,]", kw_text):
                word = word.strip().strip('"').strip("'")
                if word and len(word) > 1:
                    keywords.append(word)
    else:
        # Plain form (PSDA-style): keep everything before the trailing query sentence
        # ("Which/What/... ?"), then split on commas/semicolons.
        parts = re.split(r"(?<=[.?!])\s+(?=(?:Which|What|How|When|Where|Who)\b)", cell)
        text = parts[0].rstrip(".?! ")
        for word in re.split(r"[;,]", text):
            word = word.strip().strip('"').strip("'").rstrip(".")
            if word and len(word) > 1:
                keywords.append(word)
    return keywords


def _parse_dependencies(cell: str) -> dict[str, list[str]]:
    """Parse dependencies from the Dependencies cell.

    FPF form uses `**Builds on:** … **Coordinates with:** …` markers; DPF form is a
    plain PID list (e.g. `SYSE.1, SYSE.16; FPF A.1.CSD, C.28`). Fallback collects every
    PatternID under `references`; the raw cell is always preserved separately."""
    result: dict[str, list[str]] = {}
    dep_patterns = [
        (r"\*\*Builds on:\*\*\s*(.+?)(?=\*\*|$)", "builds_on"),
        (r"\*\*Coordinates with:\*\*\s*(.+?)(?=\*\*|$)", "coordinates_with"),
        (r"\*\*Constrains:\*\*\s*(.+?)(?=\*\*|$)", "constrains"),
        (r"\*\*Prerequisite for:\*\*\s*(.+?)(?=\*\*|$)", "prerequisite_for"),
        (r"\*\*Refines:\*\*\s*(.+?)(?=\*\*|$)", "refines"),
        (r"\*\*Informs:\*\*\s*(.+?)(?=\*\*|$)", "informs"),
        (r"\*\*Used by:\*\*\s*(.+?)(?=\*\*|$)", "used_by"),
    ]
    for pattern, key in dep_patterns:
        m = re.search(pattern, cell)
        if m:
            raw = m.group(1).strip()
            ids = _extract_dep_ids(raw)
            if ids:
                result[key] = ids
    if not result:
        ids = _extract_dep_ids(cell)
        if ids:
            result["references"] = ids
    return result


def _extract_dep_ids(text: str) -> list[str]:
    """Extract PatternIDs (incl. hyphenated compound and FPF A.x codes) from raw text."""
    return [m for m in PATTERN_ID_RE.findall(text)]


def _collect_end_markers(lines: list[str]) -> list[tuple[str, int]]:
    result: list[tuple[str, int]] = []
    for line_no, line in enumerate(lines, start=1):
        m = END_RE.match(line.rstrip("\n\r"))
        if m:
            result.append((m.group(2).strip(), line_no))
    return result


def _build_heading_list(lines: list[str]) -> list[tuple[str, int, str]]:
    result: list[tuple[str, int, str]] = []
    for line_no, line in enumerate(lines, start=1):
        raw = line.rstrip("\n\r")
        m = HEADING_RE.match(raw)
        if not m:
            continue
        heading_text = m.group(2).strip()
        if heading_text.endswith(":End"):
            continue
        pid = _extract_id(heading_text)
        if pid is None:
            continue
        result.append((pid, line_no, heading_text))
    return result


def _extract_id(heading: str) -> str | None:
    candidates = PATTERN_ID_RE.findall(heading)
    if not candidates:
        return None
    stripped = heading.lstrip("#*` ").strip()
    first_word = stripped.split()[0] if stripped.split() else ""
    for c in candidates:
        if first_word.startswith(c):
            return c
        if stripped.startswith(c):
            return c
    return None


def _collect_section_headings(lines: list[str]) -> list[tuple[int, int, str]]:
    """All H1/H2 section headings (excluding `:End`), as (line_no, level, text).

    Unlike `_build_heading_list` (which only keeps headings carrying a PatternID
    token), this keeps every top-level heading so a publication unit opened by a
    human-title heading (e.g. RHY's `# Edition and reuse` before `## RHY.Edition:End`)
    can still be located."""
    result: list[tuple[int, int, str]] = []
    SEC_RE = re.compile(r"^(#{1,2})\s+(.+)$")
    for line_no, line in enumerate(lines, start=1):
        raw = line.rstrip("\n\r")
        m = SEC_RE.match(raw)
        if not m:
            continue
        heading_text = m.group(2).strip()
        if heading_text.endswith(":End"):
            continue
        result.append((line_no, len(m.group(1)), heading_text))
    return result


def _extract_non_pattern_sections(
    lines: list[str],
    section_headings: list[tuple[int, int, str]],
    consumed: list[tuple[int, int]],
) -> list[ExtractedUnit]:
    """Extract `#`/`##` reader-help sections (Readme, "What … Is", etc.) as context units.

    A top-level heading that falls inside an extracted reference unit's [start, end]
    range is that reference card's own `:N` sub-section and is skipped. Everything
    else at H1/H2 — including non-`:End`-closed publication units and reader sections
    such as `LDR.Use`/`LDR.Source` or `IS.Readme` — is preserved as context, so no
    source text is dropped."""
    top_headings: list[tuple[int, int, str]] = []
    skip_boundaries: set[int] = set()
    for line_no, level, heading_text in section_headings:
        if any(s <= line_no <= e for s, e in consumed):
            continue
        if heading_text.startswith("Table of Content"):
            skip_boundaries.add(line_no)
            continue
        if heading_text in ("Pattern index", "Public units") or heading_text.startswith(("Pattern index", "Public units")):
            # Pattern-index / reader-navigation tables duplicate INDEX.md — drop, keep boundary.
            skip_boundaries.add(line_no)
            continue
        top_headings.append((level, line_no, heading_text))

    unit_open_lines = {s for s, _ in consumed}
    all_stops = sorted(set(unit_open_lines) | {ln for _, ln, _ in top_headings} | skip_boundaries)

    context_units: list[ExtractedUnit] = []
    for _level, start_line, heading_text in top_headings:
        end_line = len(lines)
        for stop in all_stops:
            if stop > start_line:
                end_line = stop - 1
                break
        body = "".join(lines[start_line - 1 : end_line]).rstrip()
        if not body.strip():
            continue
        slug = heading_text.strip("#* ").split(" - ")[0].split(" — ")[0].strip()
        slug = re.sub(r"[^A-Za-z0-9]+", "-", slug).strip("-")
        if not slug:
            slug = f"section-{start_line}"
        pid = f"_ctx.{slug}"
        context_units.append(ExtractedUnit(
            pid=pid,
            title=heading_text,
            body=body,
            start_line=start_line,
            end_line=end_line,
            metadata={"id": pid, "title": heading_text},
        ))
    return context_units


def _split_toc_row(line: str) -> list[str]:
    if line.startswith("| "):
        line = line[2:]
    if line.endswith(" |"):
        line = line[:-2]
    return [c.strip() for c in line.split("|")]


def main():
    parser = argparse.ArgumentParser(description="Decompose an FPF Library monolith (FPF-Spec or DPF) into skill references")
    parser.add_argument("spec_path", type=Path, help="Path to an FPF Library monolith .md file")
    parser.add_argument("--skills-dir", type=Path, required=True, help="Skill root (references/ + context/ are written inside)")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing")
    args = parser.parse_args()

    spec_path = args.spec_path.expanduser().resolve()
    if not spec_path.is_file():
        print(f"Error: spec file not found: {spec_path}", file=sys.stderr)
        sys.exit(1)

    skills_dir = args.skills_dir.expanduser().resolve()
    refs_dir = skills_dir / "references"
    ctx_dir = skills_dir / "context"

    print(f"Decomposing DPF spec: {spec_path}", file=sys.stderr)
    print(f"References directory: {refs_dir}", file=sys.stderr)
    print(f"Context directory:   {ctx_dir}", file=sys.stderr)

    report, units, context_units, spec_filename = parse_spec(spec_path)

    print(f"Total :End-delimited units: {report.total_patterns}")
    print(f"Reference units extracted:  {len(units)}")
    print(f"ToC entries (patterns+):    {report.toc_entries}")

    refs_dir.mkdir(parents=True, exist_ok=True)

    retired = retire_stale_context_refs(refs_dir, dry_run=args.dry_run)
    ctx_written, ctx_skipped, ctx_trivial = write_context_units(ctx_dir, context_units, report, dry_run=args.dry_run)
    if context_units:
        status = f"{ctx_written} written, {ctx_skipped} skipped (unchanged)"
        if ctx_trivial:
            status += f", {ctx_trivial} trivial skipped"
        if retired:
            status += f", {retired} retired from references/"
        print(f"Context sections: {status}")

    if units:
        written = skipped = 0
        for unit in units:
            content, raw_len, opt_len = format_reference(unit)
            report.size_stats.raw_bytes += raw_len
            report.size_stats.optimized_bytes += opt_len
            filepath = refs_dir / slugify(unit.pid)
            if idempotent_write(filepath, content, dry_run=args.dry_run):
                written += 1
            else:
                skipped += 1

        index_content = generate_index(units, spec_path.stem, spec_filename, has_relations=False)
        idempotent_write(refs_dir / "INDEX.md", index_content, dry_run=args.dry_run)
        print(f"References: {written} written, {skipped} skipped (unchanged)")
    else:
        print("No reference units extracted!", file=sys.stderr)

    if report.warnings:
        print(f"\nWarnings ({len(report.warnings)}):", file=sys.stderr)
        for w in report.warnings:
            print(f"  - {w}", file=sys.stderr)

    report.print()


if __name__ == "__main__":
    main()