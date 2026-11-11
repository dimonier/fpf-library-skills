from __future__ import annotations

import hashlib
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

PATTERN_ID_RE = re.compile(r"\b((?:CC-)?[A-Z][A-Za-z]*(?:\.[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*)+)\b")

_DASH_RUN = re.compile(r"-{4,}")
_SPACE_RUN = re.compile(r" {3,}")


@dataclass
class SizeStats:
    raw_bytes: int = 0
    optimized_bytes: int = 0


@dataclass
class ExtractedUnit:
    pid: str
    title: str
    body: str
    start_line: int
    end_line: int
    metadata: dict[str, Any] = field(default_factory=dict)
    # True when this unit is a pattern (its PID appears in the pattern index/ToC),
    # False for publication units ({Code}.Reference/.Sources/.Application/...). The
    # pattern index is authoritative — some DPF PIDs are non-numeric (e.g. KCAE.USE)
    # or carry a letter sub-suffix (e.g. MMP.8.SD), so a numeric-suffix heuristic is
    # NOT the test.
    is_pattern: bool = False


@dataclass
class DecomposeReport:
    spec_path: str
    spec_type: str
    total_patterns: int
    patterns_extracted: int
    toc_parsed: bool
    toc_entries: int
    warnings: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    non_extractable: list[str] = field(default_factory=list)
    size_stats: SizeStats = field(default_factory=SizeStats)

    def to_dict(self) -> dict[str, Any]:
        return {
            "spec_path": self.spec_path,
            "type": self.spec_type,
            "total_patterns": self.total_patterns,
            "patterns_extracted": self.patterns_extracted,
            "toc_parsed": self.toc_parsed,
            "toc_entries": self.toc_entries,
            "warnings": self.warnings,
            "errors": self.errors,
            "non_extractable_sections": self.non_extractable,
            "size_stats": {
                "raw_bytes": self.size_stats.raw_bytes,
                "optimized_bytes": self.size_stats.optimized_bytes,
                "saved_bytes": self.size_stats.raw_bytes - self.size_stats.optimized_bytes,
            },
        }

    def print(self):
        json.dump(self.to_dict(), sys.stdout, indent=2, ensure_ascii=False)
        sys.stdout.write("\n")


def slugify(pid: str) -> str:
    return f"{pid}.md"


def sha256(content: str) -> str:
    return hashlib.sha256(content.encode("utf-8")).hexdigest()


def yaml_frontmatter(meta: dict[str, Any]) -> str:
    lines = ["---"]
    for key, value in meta.items():
        lines.extend(_yaml_kv(key, value))
    lines.append("---")
    return "\n".join(lines) + "\n"


def _yaml_kv(key: str, value: Any, indent: int = 0) -> list[str]:
    prefix = "  " * indent
    if isinstance(value, dict):
        result = [f"{prefix}{key}:"]
        for k, v in value.items():
            result.extend(_yaml_kv(k, v, indent + 1))
        return result
    elif isinstance(value, list):
        if not value:
            return [f"{prefix}{key}: []"]
        result = [f"{prefix}{key}:"]
        for item in value:
            result.append(f"{prefix}  - {_yaml_scalar(item)}")
        return result
    elif value is None:
        return [f"{prefix}{key}: "]
    else:
        return [f"{prefix}{key}: {_yaml_scalar(value)}"]


def _yaml_scalar(value: Any) -> str:
    s = str(value)
    if any(ch in s for ch in (":", "#", "{", "}", "[", "]", ",", "&", "*", "?", "|", "-", "<", ">", "=", "!", "%", "@", "`")):
        return f'"{s}"'
    if s and s[0] in ("'", '"'):
        return s
    return s


def optimize_body(text: str) -> str:
    """Compress table separator lines and excessive whitespace."""
    lines = text.splitlines(keepends=True)
    result: list[str] = []
    for line in lines:
        stripped = line.rstrip("\n\r")
        if _is_table_sep(stripped):
            stripped = _DASH_RUN.sub("---", stripped)
        stripped = _SPACE_RUN.sub("  ", stripped)
        result.append(stripped + "\n")
    return "".join(result)


_TABLE_SEP_RE = re.compile(r"^\|[-: |]+\|$")


def _is_table_sep(line: str) -> bool:
    return bool(_TABLE_SEP_RE.match(line))


def _extract_section_lead(body: str, pid: str, section: str, *, descend: bool = False) -> str:
    """First non-empty paragraph of the canonical section `### {pid}:{section}`.

    Matches the top-level section only (e.g. `:0`, not `:0.1`). When `descend` is
    true, skip immediately nested sub-sections (`{pid}:{section}.x`) and return the
    first paragraph of the section's subtree — used for `Solution`, which often
    opens with sub-headings rather than a direct paragraph (E.8:4.1)."""
    esc = re.escape(pid)
    sec = re.escape(section)
    heading = re.compile(rf"^#{{2,5}}\s+{esc}:{sec}(?![\d.])[^\n]*", re.MULTILINE)
    nested = re.compile(rf"^#{{2,5}}\s+{esc}:{sec}\.[^\n]*", re.MULTILINE)
    m = heading.search(body)
    if not m:
        return ""
    collected: list[str] = []
    for raw in body[m.end() :].splitlines():
        stripped = raw.strip()
        if stripped.startswith("#"):
            if descend and nested.match(stripped):
                continue
            break
        if not stripped:
            if collected:
                break
            continue
        collected.append(stripped)
    return " ".join(collected)


def _clip_sentence(text: str, max_chars: int = 240) -> str:
    """Truncate prose to at most `max_chars`, cutting at a sentence boundary."""
    text = " ".join(text.split())
    if len(text) <= max_chars:
        return text
    cut = text[:max_chars]
    ends = [pos for sep in (". ", "? ", "! ") if (pos := cut.rfind(sep)) > max_chars // 2]
    if ends:
        return cut[: max(ends) + 1]
    return cut.rstrip(" ,;:-") + " …"


def _governing_paths(meta: dict[str, Any]) -> list[str]:
    """Governing-pattern reference paths from frontmatter `dependencies` (ToC
    Builds-on / Coordinates-with / etc. per E.11.PFP:4.2), bounded to keep the
    entry block a cheap first read."""
    deps = meta.get("dependencies")
    if not isinstance(deps, dict):
        return []
    ids: list[str] = []
    for rel_ids in deps.values():
        if isinstance(rel_ids, str):
            rel_ids = [rel_ids]
        if not isinstance(rel_ids, (list, tuple)):
            continue
        for pid in rel_ids:
            pid = str(pid).strip()
            # A file-like token would produce `references/Spec.md.md`; reject it even
            # if a caller hands us raw frontmatter written before the parser fix.
            if pid and not pid.lower().endswith(".md") and pid not in ids:
                ids.append(pid)
    return [f"`references/{pid}.md`" for pid in ids[:8]]


def format_reference(
    unit: ExtractedUnit,
) -> str:
    pid = unit.pid
    title = unit.title or pid
    meta = dict(unit.metadata)
    meta.pop("dependencies_raw", None)  # index-only; the frontmatter already has structured `dependencies`
    meta.setdefault("id", pid)
    meta.setdefault("title", title)

    body = unit.body.rstrip("\n")
    if body.endswith("---"):
        body = body[:-3].rstrip("\n")

    # Entry block (P1/P5): a cheap first read auto-extracted from the pattern body's
    # canonical §-sections (E.8:4.1), so a cold reader can select the pattern without
    # loading the whole body. Empty fields are omitted (context units carry none).
    trigger = _extract_section_lead(body, pid, "0")
    problem = _extract_section_lead(body, pid, "1")
    first_move = _extract_section_lead(body, pid, "4", descend=True)
    governing = _governing_paths(meta)

    raw_len = len(body.encode("utf-8"))
    body = optimize_body(body)
    opt_len = len(body.encode("utf-8"))

    lines: list[str] = []
    lines.append(yaml_frontmatter(meta).rstrip())
    lines.append("")
    lines.append(f"# {pid}: {title}")
    lines.append("")

    if trigger:
        lines.append(f"> **Trigger:** {_clip_sentence(trigger)}")
    if problem:
        lines.append(f"> **Problem frame:** {_clip_sentence(problem)}")
    if first_move:
        lines.append(f"> **First move:** {_clip_sentence(first_move)}")
    if governing:
        if trigger or problem or first_move:
            lines.append(">")
        lines.append("> **Governing patterns:** " + " ".join(governing))
    if trigger or problem or first_move or governing:
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append(body)

    return "\n".join(lines), raw_len, opt_len


_INDEX_TITLE_OVERRIDES: dict[str, str] = {
    # FPF.Preface has no bare `## FPF.Preface` opening (only chapter headings
    # `## FPF.Preface:1..21`), so its title otherwise falls back to a chapter heading.
    "FPF.Preface": "Preface",
}

_DEP_LABELS: list[tuple[str, str]] = [
    ("builds_on", "Builds on"),
    ("coordinates_with", "Coordinates with"),
    ("constrains", "Constrains"),
    ("prerequisite_for", "Prerequisite for"),
    ("refines", "Refines"),
    ("informs", "Informs"),
    ("used_by", "Used by"),
]


def _format_dependencies(deps: Any) -> str:
    """Render the frontmatter `dependencies` dict back into the monolith ToC's inline
    `**Builds on:** … **Coordinates with:** …` form (E.11.PFP:4.2)."""
    if not isinstance(deps, dict) or not deps:
        return "—"
    parts: list[str] = []
    for key, label in _DEP_LABELS:
        ids = deps.get(key)
        if not ids:
            continue
        if isinstance(ids, str):
            ids = [ids]
        parts.append(f"**{label}:** " + ", ".join(str(i) for i in ids) + ".")
    return " ".join(parts) if parts else "—"


def generate_index(
    entries: list[ExtractedUnit],
    skill_name: str,
    spec_filename: str,
    *,
    has_relations: bool = False,
) -> str:
    # Authoritative pattern-index header per E.11.PFP:4.2. `size` is intentionally
    # absent — it is a derived technical detail, not a canonical index column.
    lines: list[str] = []
    lines.append(f"# {skill_name} — Pattern Index")
    lines.append("")
    lines.append("| § | ID & Title | Status | Keywords & Search Queries | Dependencies |")
    lines.append("| :--- | :--- | :--- | :--- | :--- |")

    for unit in entries:
        pid = unit.pid
        title = _INDEX_TITLE_OVERRIDES.get(pid, unit.title or pid)
        status = unit.metadata.get("status") or "—"
        keywords_list = unit.metadata.get("keywords", [])
        keywords = ", ".join(keywords_list) if keywords_list else "—"
        dependencies = unit.metadata.get("dependencies_raw") or _format_dependencies(
            unit.metadata.get("dependencies")
        )
        lines.append(f"| {pid} | **{title}** | {status} | {keywords} | {dependencies} |")

    lines.append("")
    lines.append("## Cross-references")
    if has_relations:
        lines.append("- See `relations.md` for pattern relation records (E.4.PFR)")
    lines.append(f"- Full monolith: `{spec_filename}`")
    lines.append("")

    return "\n".join(lines)


def idempotent_write(filepath: Path, content: str, dry_run: bool = False) -> bool:
    if filepath.exists():
        existing_hash = sha256(filepath.read_text(encoding="utf-8"))
        if existing_hash == sha256(content):
            return False

    if dry_run:
        print(f"[DRY-RUN] Would write: {filepath}", file=sys.stderr)
        return False

    filepath.parent.mkdir(parents=True, exist_ok=True)
    filepath.write_text(content, encoding="utf-8")
    return True


def remove_trivial(filepath: Path, min_non_empty: int = 3, dry_run: bool = False) -> bool:
    """Remove file if it has fewer than min_non_empty non-empty lines. Returns True if removed."""
    if not filepath.exists():
        return False
    text = filepath.read_text(encoding="utf-8")
    non_empty = [ln for ln in text.splitlines() if ln.strip()]
    if len(non_empty) < min_non_empty:
        if dry_run:
            print(f"[DRY-RUN] Would remove trivial: {filepath}", file=sys.stderr)
        else:
            filepath.unlink()
        return True
    return False


def retire_stale_context_refs(refs_dir: Path, dry_run: bool = False) -> int:
    """Retire `_ctx.*` files left in references/ — context units now live in context/.

    One-time migration + safety net: after the move, references/ holds patterns +
    INDEX only. Returns the number of files retired."""
    removed = 0
    if not refs_dir.is_dir():
        return removed
    for f in refs_dir.glob("_ctx.*.md"):
        if not f.is_file():
            continue
        if dry_run:
            print(f"[DRY-RUN] Would retire: {f}", file=sys.stderr)
        else:
            f.unlink()
        removed += 1
    return removed


def retire_stale_pattern_refs(
    refs_dir: Path,
    kept_names: set[str],
    *,
    dry_run: bool = False,
) -> int:
    """Retire generated pattern files no longer produced by the current decomposition
    (a pattern removed or renamed upstream). Preserves INDEX.md and relations.md.
    Returns the number of files retired.

    `*.fpf-narrative.md` files are NOT preserved: they are one-off derived renderings
    with no producer wired into this sync pipeline, and they can silently go stale
    (e.g. citing a pattern that was later removed upstream). So they are retired like
    any other unproduced file."""
    if not refs_dir.is_dir():
        return 0
    retained = {"INDEX.md", "relations.md"}
    removed = 0
    for f in refs_dir.glob("*.md"):
        if not f.is_file():
            continue
        name = f.name
        if name in kept_names or name in retained:
            continue
        if dry_run:
            print(f"[DRY-RUN] Would retire stale pattern: {f}", file=sys.stderr)
        else:
            f.unlink()
        removed += 1
    return removed


def write_context_units(
    ctx_dir: Path,
    context_units: list[ExtractedUnit],
    report: DecomposeReport,
    *,
    dry_run: bool = False,
) -> tuple[int, int, int]:
    """Write non-pattern context units into ctx_dir (sibling of references/).

    Returns (written, skipped, trivial). Retires generated context files that are
    no longer produced (e.g. a dropped section), preserving non-generated files
    such as a bundled USING-FPF.md."""
    ctx_dir.mkdir(parents=True, exist_ok=True)
    kept_names: set[str] = set()
    written = skipped = trivial = 0
    for ct_unit in context_units:
        body_lines = [ln for ln in ct_unit.body.splitlines() if ln.strip()]
        if len(body_lines) <= 1:
            trivial += 1
            continue
        content, raw_len, opt_len = format_reference(ct_unit)
        report.size_stats.raw_bytes += raw_len
        report.size_stats.optimized_bytes += opt_len
        name = slugify(ct_unit.pid)
        kept_names.add(name)
        if idempotent_write(ctx_dir / name, content, dry_run=dry_run):
            written += 1
        else:
            skipped += 1
    for stale in ctx_dir.glob("_ctx.*.md"):
        if stale.name not in kept_names:
            if dry_run:
                print(f"[DRY-RUN] Would retire stale: {stale}", file=sys.stderr)
            else:
                stale.unlink()
    return written, skipped, trivial
