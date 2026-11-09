"""
Sync the DPF Library skills (skills/dpf-*) from FPF/DPFs/** monoliths.

Self-contained orchestrator over the FPF Library DPF monoliths. Complements
`decompose.py` (single-monolith parser); this script discovers the whole
Library, classifies frameworks vs Suite References (DEC-0011/0012), derives each
skill's directory name from the monolith title (owner decision, 2026-11-06),
copies the monolith into `assets/` and decomposes it into `references/` +
`context/` + `INDEX.md`.

Does NOT: run `git pull` (sources are local files) or reconcile the pre-existing
minified `dpf-systems-engineering` / `dpf-organization-change-engineering` skills
(Phase 4, DEC-0010). `NOTICE.md` and `LICENSE` are authored during the build (see
`generate_notice_md`). All derived paths come from this script's location, so the
working directory is irrelevant.

Usage:
  python sync_library.py                 # full sync (all frameworks + suite refs)
  python sync_library.py --check         # exit 0=up-to-date, 1=build needed
  python sync_library.py --dry-run       # discover + decompose in-memory, no writes
  python sync_library.py --force         # rebuild even when unchanged (apply generator changes)
  python sync_library.py <slug>          # one skill by slug / DocID / filename
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from dataclasses import dataclass
from pathlib import Path

import decompose
from _common import (
    _clip_sentence,
    _extract_section_lead,
    format_reference,
    generate_index,
    idempotent_write,
    retire_stale_context_refs,
    retire_stale_pattern_refs,
    slugify,
    write_context_units,
)

SCRIPT_DIR = Path(__file__).resolve().parent
FPF_REPO = SCRIPT_DIR.parent.parent.parent
DPF_DIR = FPF_REPO / "DPFs"
SKILLS_DIR = FPF_REPO / "skills"

SUITE_REF_SUFFIX = "SUITE-REFERENCE.md"

# Fixed report order: README Suite order, then standalone ("Further") frameworks.
SUITE_ORDER = (
    "Engineering",
    "Management",
    "Foundational Thinking",
    "Human Capability Engineering",
    "Further",
)

# DocID lives on the third line: `**DocID:** \`PSDA\` within ...` (with backticks)
# or `**DocID:** GOALS within ...` (bare). `CAD` hides it in the `**Edition:**`
# line instead: `**Edition:** [CAD, 23 October 2026](#...)`.
DOCID_RE = re.compile(r"\*\*DocID:\*\*\s*`?([A-Za-z0-9]+)`?")
EDITION_DOCID_RE = re.compile(r"\*\*Edition:\*\*\s*\[([A-Za-z0-9]+)")

# Title suffixes stripped to derive the human-readable field/suite name (owner
# rule: skill name from the `# <Title>` heading). Longest-first so a multi-word
# suffix wins over a shorter one ("DPF Suite Architectural Reference" before "DPF").
TITLE_SUFFIXES = (
    "Principles Framework",
    "DPF Suite Architectural Reference",
    "Suite Architectural Reference",
    "DPF",
)

# Suite grouping label from the parent directory name ("" = top-level "Further").
SUITE_DIR_SUFFIX = " DPF Suite"


@dataclass
class Monolith:
    path: Path
    kind: str            # "framework" | "suite"
    suite: str           # "Engineering" | "Management" | "Foundational Thinking" | "Human Capability Engineering" | "Further"
    title: str
    docid: str
    slug: str            # skill directory name (dpf-*)
    work_on: str = ""    # author-authored "What you can work on" (from the Library READMEs)


def sha256_file(path: Path) -> str:
    chunks = []
    with path.open("rb") as f:
        h = hashlib.sha256()
        while True:
            block = f.read(65536)
            if not block:
                break
            h.update(block)
    return h.hexdigest()


def read_title_docid(path: Path) -> tuple[str, str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    title = path.stem
    for line in lines[:4]:
        s = line.strip()
        if s.startswith("# ") and title == path.stem:
            title = s[2:].strip()
    head = "\n".join(lines[:6])
    docid = "?"
    m = DOCID_RE.search(head)
    if m:
        docid = m.group(1)
    else:
        m2 = EDITION_DOCID_RE.search(head)
        if m2:
            docid = m2.group(1)
    return title, docid


def strip_suffixes(title: str) -> str:
    t = title.strip()
    lower = t.lower()
    for suffix in TITLE_SUFFIXES:
        s = suffix.lower()
        if lower.endswith(s):
            t = t[: len(t) - len(suffix)].rstrip()
            break
    return t.strip()


def skill_slug(title: str, kind: str) -> str:
    base = strip_suffixes(title)
    base = re.sub(r"[^A-Za-z0-9]+", "-", base).strip("-").lower()
    if kind == "suite":
        return f"dpf-{base}-reference"
    return f"dpf-{base}"


def suite_label(parent: Path, dpf_dir: Path) -> str:
    if parent == dpf_dir:
        return "Further"
    return parent.name[: -len(SUITE_DIR_SUFFIX)] if parent.name.endswith(SUITE_DIR_SUFFIX) else parent.name


def _load_work_on_map(dpfs_dir: Path) -> dict[str, str]:
    """DocID → "What you can work on" sentence, parsed from the Library + Suite READMEs.

    The README framework tables carry an author-authored "What you can work on"
    column — the field's own trigger vocabulary — covering all 36 frameworks."""
    result: dict[str, str] = {}
    for readme in sorted(dpfs_dir.rglob("README.md")):
        for line in readme.read_text(encoding="utf-8", errors="replace").splitlines():
            if not line.strip().startswith("|"):
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 2:
                continue
            name, work = cells[0], cells[1]
            m = re.search(r"\(([A-Z][A-Z0-9]+)\)", name)
            if m:
                result[m.group(1)] = work
    return result


def _load_pattern_map(dpfs_dir: Path) -> dict[str, int]:
    """DocID → expected full-pattern-body count, from the Library READMEs' "Patterns" column.

    The root README's "Further" table and each Suite README's "Constituent DPFs"
    table carry a "Patterns" column (cells[2]) — the author-authored count of full
    pattern bodies per framework. Suite-total rows (root "Suites" table) carry no
    `(DOCID)` in the name cell and are skipped."""
    result: dict[str, int] = {}
    for readme in sorted(dpfs_dir.rglob("README.md")):
        for line in readme.read_text(encoding="utf-8", errors="replace").splitlines():
            if not line.strip().startswith("|"):
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 3:
                continue
            m = re.search(r"\(([A-Z][A-Z0-9]+)\)", cells[0])
            if not m:
                continue
            docid = m.group(1)
            if len(docid) > 7:
                continue  # URL slug, not a DocID (e.g. "SYSTEMS-ENGINEERING-PRINCIPLES..." is hyphenated anyway)
            if cells[2].isdigit():
                result[docid] = int(cells[2])
    return result


def validate(monoliths: list[Monolith]) -> tuple[list[str], list[str], bool]:
    """Validate the Library decomposition. Returns (failures, summary, idempotent).

    Checks, per DEC-0009's "Проверка выполнения":
      1. counts — each framework's pattern count equals its README "Patterns" figure
         (and the whole-Library total), suite references yield exactly one reference;
      2. orphans — no full pattern body is missing its pattern-index entry;
      3. idempotency — a second in-memory decompose reproduces byte-identical output.

    Framework warnings other than suite "ToC not found" are treated as failures (a
    parser gap would show up there); suite references legitimately have no pattern
    index."""
    failures: list[str] = []
    summary: list[str] = []
    pattern_map = _load_pattern_map(DPF_DIR)

    n_fw = sum(1 for m in monoliths if m.kind == "framework")
    n_suite = sum(1 for m in monoliths if m.kind == "suite")
    summary.append(f"Discovery: {len(monoliths)} monoliths ({n_fw} frameworks, {n_suite} suite references)")

    actual_total = 0
    actual_by_suite: dict[str, int] = {}
    expected_by_suite: dict[str, int] = {}
    idempotent = True
    for m in monoliths:
        report, units, _ctx, _name = decompose.parse_spec(m.path)
        patterns = [u for u in units if u.is_pattern]
        n = len(patterns)
        orphans = [w for w in report.warnings if w.startswith("ORPHAN")]
        others = [w for w in report.warnings if not w.startswith("ORPHAN")]

        # Idempotency: a second parse must yield byte-identical reference content.
        _r2, u2, _c2, _n2 = decompose.parse_spec(m.path)
        if [u.pid for u in units] != [u.pid for u in u2]:
            failures.append(f"{m.docid}: decompose is not idempotent (unit list changed on re-parse)")
            idempotent = False

        if m.kind == "framework":
            expected = pattern_map.get(m.docid)
            if expected is None:
                failures.append(f"{m.docid}: no README 'Patterns' count for this DocID")
            elif n != expected:
                failures.append(f"{m.docid}: {n} patterns != README {expected}")
            actual_total += n
            actual_by_suite[m.suite] = actual_by_suite.get(m.suite, 0) + n
            if expected is not None:
                expected_by_suite[m.suite] = expected_by_suite.get(m.suite, 0) + expected
            if orphans:
                failures.extend(f"{m.docid}: {w}" for w in orphans)
            if others:
                failures.extend(f"{m.docid}: unexpected warning — {w}" for w in others)
        else:
            refs = [u for u in units if not u.is_pattern]
            if len(refs) != 1 or patterns:
                failures.append(
                    f"{m.suite} Reference: expected 1 reference unit, "
                    f"got {len(refs)} ref(s) / {len(patterns)} pattern(s)"
                )
            if orphans:
                failures.extend(f"{m.suite}: {w}" for w in orphans)
            # Suite references legitimately warn "ToC not found".

    for suite in sorted(expected_by_suite):
        exp = expected_by_suite[suite]
        got = actual_by_suite.get(suite, 0)
        summary.append(f"  {suite}: {got}/{exp} patterns")
    summary.append(f"  Total: {actual_total}/{sum(expected_by_suite.values())} patterns")

    missing = set(pattern_map) - {m.docid for m in monoliths if m.kind == "framework"}
    if missing:
        failures.append(f"README Documents not discovered: {sorted(missing)}")

    return failures, summary, idempotent


def _load_suite_subject_map(dpfs_dir: Path) -> dict[str, str]:
    """Suite name → "Working subject", parsed from the root README's Suites table.

    The Suite-Reference monoliths' own opening is not uniform (two open with
    "First Suite edition"), so the root README's Suites table is the reliable,
    author-authored per-Suite description."""
    result: dict[str, str] = {}
    root = dpfs_dir / "README.md"
    if not root.is_file():
        return result
    for line in root.read_text(encoding="utf-8", errors="replace").splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 5:
            continue
        m = re.match(r"\[([^\]]+)\]\(([^)]*Suite[^)]*)\)", cells[0])
        if m:
            result[m.group(1)] = cells[1]
    return result


def match_selector(monoliths: list[Monolith], selector: str) -> list[Monolith]:
    sel = selector.lower()
    matched = [
        m for m in monoliths
        if sel in (m.slug.lower(), m.docid.lower(), m.path.stem.lower(), m.path.name.lower())
    ]
    if matched:
        return matched
    if sel.startswith("dpf-"):
        sel = sel[len("dpf-"):]
    return [m for m in monoliths if sel in m.slug.lower()]


def discover(dpfs_dir: Path) -> list[Monolith]:
    work_on_map = _load_work_on_map(dpfs_dir)
    suite_subject_map = _load_suite_subject_map(dpfs_dir)
    frameworks: list[Monolith] = []
    suite_refs: list[Monolith] = []
    for path in sorted(dpfs_dir.rglob("*.md")):
        if path.name == "README.md":
            continue
        title, docid = read_title_docid(path)
        suite = suite_label(path.parent, dpfs_dir)
        if path.name.upper().endswith(SUITE_REF_SUFFIX.upper()):
            subject = suite_subject_map.get(suite, "")
            suite_refs.append(Monolith(path, "suite", suite, title, docid, skill_slug(title, "suite"), subject))
        else:
            work_on = work_on_map.get(docid, "")
            frameworks.append(Monolith(path, "framework", suite, title, docid, skill_slug(title, "framework"), work_on))
    # Sort suites into README order, frameworks alphabetically, suite reference last within a suite.
    def suite_key(m: Monolith) -> tuple[int, bool, str]:
        idx = SUITE_ORDER.index(m.suite) if m.suite in SUITE_ORDER else len(SUITE_ORDER)
        return (idx, m.kind != "suite", m.title.lower())
    return sorted(frameworks + suite_refs, key=suite_key)


def asset_target(monolith: Monolith) -> Path:
    return SKILLS_DIR / monolith.slug / "assets" / monolith.path.name


def status_of(monolith: Monolith) -> str:
    skill_dir = SKILLS_DIR / monolith.slug
    if not skill_dir.exists():
        return "new"
    asset = asset_target(monolith)
    if not asset.is_file():
        return "minified-existing"
    if sha256_file(asset) != sha256_file(monolith.path):
        return "stale"
    return "current"


def decompose_counts(monolith: Monolith) -> tuple[int, int, int, int]:
    """In-memory parse; returns (total_units, ref_units, toc_entries, warnings)."""
    report, units, _ctx, _name = decompose.parse_spec(monolith.path)
    return report.total_patterns, len(units), report.toc_entries, len(report.warnings)


def run_decompose(monolith: Monolith, *, dry_run: bool) -> str:
    """Copy monolith to assets/ and decompose it into the skill dir. Returns status line."""
    skill_dir = SKILLS_DIR / monolith.slug
    refs_dir = skill_dir / "references"
    ctx_dir = skill_dir / "context"
    asset = asset_target(monolith)

    if dry_run:
        # In-memory parse for the plan; no filesystem writes.
        total, refs, toc, warns = decompose_counts(monolith)
        return f"[DRY-RUN] {monolith.slug}: {total} units ({refs} refs, {toc} ToC, {warns} warns)"

    # Real run.
    asset.parent.mkdir(parents=True, exist_ok=True)
    if not asset.is_file() or sha256_file(asset) != sha256_file(monolith.path):
        asset.write_bytes(monolith.path.read_bytes())

    text = monolith.path.read_text(encoding="utf-8", errors="replace")
    refs_dir.mkdir(parents=True, exist_ok=True)
    report, units, context_units, spec_filename = decompose.parse_spec(monolith.path)

    retired = retire_stale_context_refs(refs_dir)
    ctx_written, ctx_skipped, ctx_trivial = write_context_units(ctx_dir, context_units, report)

    written = skipped = 0
    if units:
        for unit in units:
            content, raw_len, opt_len = format_reference(unit)
            report.size_stats.raw_bytes += raw_len
            report.size_stats.optimized_bytes += opt_len
            if idempotent_write(refs_dir / slugify(unit.pid), content):
                written += 1
            else:
                skipped += 1
        index_content = generate_index(units, monolith.path.stem, spec_filename, has_relations=False)
        idempotent_write(refs_dir / "INDEX.md", index_content)
        kept = {slugify(u.pid) for u in units} | {"INDEX.md"}
        retired_patterns = retire_stale_pattern_refs(refs_dir, kept)

    # Author the routing SKILL.md deterministically from the pattern index +
    # each pattern's ":1 - Problem frame" trigger clause (no LLM).
    skill_md = generate_skill_md_dispatch(monolith, units, text)
    idempotent_write(skill_dir / "SKILL.md", skill_md)
    idempotent_write(skill_dir / "NOTICE.md", generate_notice_md(monolith))
    # LICENSE: CC BY 4.0 text, copied verbatim from the sample skill (canonical copy).
    license_src = SKILLS_DIR / "dpf-decision-design" / "LICENSE"
    if license_src.is_file():
        idempotent_write(skill_dir / "LICENSE", license_src.read_text(encoding="utf-8"))

    status = f"{monolith.slug}: {written} refs written+{skipped} skipped"
    if report.warnings:
        status += f", {len(report.warnings)} warnings"
    return status


# --- Deterministic SKILL.md authoring (Phase 2) ---

PUB_LABELS = {
    "Reference": "Architectural Reference",
    "Sources": "Source arguments and refresh",
    "Source": "Source arguments and refresh",
    "Application": "Worked cases / cross-pattern applications",
    "Use": "Worked cases / connected use",
    "Advising": "Development-direction advising",
    "Edition": "Edition and reuse",
    "Readme": "Readme",
}


def _opening_purpose(text: str) -> str:
    """The framework's own first purpose sentence, or "" when the header has none.

    Skips the title, `**DocID:**`/`**Edition:**`/`**Author:**` and list metadata,
    author/license attribution lines, and edition/version markers; strips a leading
    blockquote `>`; stops at the next `#` heading (`# Table of Contents`)."""
    seen_title = False
    for ln in text.splitlines():
        s = ln.strip()
        if not s:
            continue
        if s.startswith("#"):
            if not seen_title:
                seen_title = True
                continue
            break
        if s.startswith(">"):
            s = s[1:].strip()
        if not s:
            continue
        if s.startswith("**") or s.startswith("- ") or s.startswith("* "):
            continue
        if "Levenchuk" in s or "©" in s or "CC BY" in s or "licensed under" in s:
            continue
        if re.match(r"^(First edition|Working edition|Edition|Release|Version)\b", s, re.I):
            continue
        return " ".join(s.split())
    return ""


def _situation_cell(unit) -> str:
    """A routing-table Situation cell from the pattern's `:1 - Problem frame` trigger.

    Normalizes the three trigger-prefix variants seen across the Library:
    `Use this pattern when …`, `**Use this when** …`, and a bare descriptive lead."""
    trigger = _extract_section_lead(unit.body, unit.pid, "1")
    situation = trigger.strip()
    situation = re.sub(r"^\*\*Use this (?:pattern )?when\*\*\s*", "", situation, flags=re.I)
    situation = re.sub(r"^Use this (?:pattern )?when\s*", "", situation, flags=re.I)
    situation = situation.strip()
    if not situation:
        situation = unit.title
    situation = _clip_sentence(situation, max_chars=140)
    return situation.replace("|", "\\|")


def generate_skill_md(monolith: Monolith, units: list, text: str) -> str:
    field = strip_suffixes(monolith.title)
    intro = _opening_purpose(text) or monolith.work_on or "a domain principle framework from the FPF Library"
    patterns = [u for u in units if u.is_pattern]
    pubs = [u for u in units if not u.is_pattern]

    lines: list[str] = []
    lines.append("---")
    lines.append(f"name: {monolith.slug}")
    lines.append("description: |")
    if monolith.work_on:
        w = monolith.work_on.strip()
        w = w[0].lower() + w[1:]
        lines.append(f"  {field} ({monolith.docid}) — Use when you need to {w.rstrip('.')}.")
    else:
        lines.append(f"  {field} ({monolith.docid}) — {intro}.")
    lines.append("license: CC-BY-4.0")
    lines.append("---")
    lines.append("")
    lines.append(f"# DPF: {field} ({monolith.docid})")
    lines.append("")
    lines.append("**Depends on:** `fpf-core`")
    lines.append(f"**Bounded context:** {intro}")
    lines.append(f"**Source of truth:** `references/` — a source-faithful decomposition of *{monolith.title}* (see `NOTICE.md` for the source/edition citation).")
    lines.append("**Readiness mode:** `source-faithful` — full bodies reproduced from an approved source; no card has passed a heterogeneous-case evaluation (`E.21`). `status` on each card is the source's own status.")
    lines.append("")
    lines.append("## When to load which pattern")
    lines.append("")
    lines.append("| Situation | Load |")
    lines.append("|---|---|")
    for u in patterns:
        lines.append(f"| {_situation_cell(u)} | `references/{u.pid}.md` |")
    lines.append("")
    if pubs:
        lines.append("## Publication units")
        lines.append("")
        lines.append("Non-pattern sections of the framework, reproduced as reference cards:")
        lines.append("")
        for u in pubs:
            label = PUB_LABELS.get(u.pid.rsplit(".", 1)[-1], "Publication unit")
            lines.append(f"- `references/{u.pid}.md` — {label}")
        lines.append("")
    lines.append("## Navigation rule")
    lines.append("")
    lines.append("Start from the working difficulty, not file order. Follow each card's `Governing patterns` line and frontmatter `dependencies` when a needed result is missing.")
    lines.append("")
    lines.append("## Single surface")
    lines.append("")
    lines.append("`references/` is the canonical surface. `SKILL.md` is routing-only; there is no monolith to read. `INDEX.md` is reference-only.")
    lines.append("")
    lines.append("## Lookup rules")
    lines.append("")
    lines.append('- **Index first, then "no".** Check `references/INDEX.md` before searching. If an id is not listed there, the pattern does not exist — answer "no" and do not open files.')
    lines.append("- **Read once.** Do not reopen a card you have already read.")
    lines.append("")
    return "\n".join(lines)


def generate_suite_skill_md(monolith: Monolith, units: list, text: str) -> str:
    suite = monolith.suite
    refs = [u for u in units if not u.is_pattern]
    pid = refs[0].pid if refs else f"{monolith.docid}.Reference"

    lines: list[str] = []
    lines.append("---")
    lines.append(f"name: {monolith.slug}")
    lines.append("description: |")
    subject = (monolith.work_on or "").strip().rstrip(".")
    if subject:
        lines.append(f"  {suite} Suite Reference — {subject}.")
    else:
        lines.append(f"  {suite} Suite Reference — a DPF Suite Architectural Reference of the FPF Library.")
    lines.append("license: CC-BY-4.0")
    lines.append("---")
    lines.append("")
    lines.append(f"# DPF: {suite} Suite Reference")
    lines.append("")
    lines.append("**Depends on:** `fpf-core`")
    lines.append(f"**Bounded context:** the {suite} Suite — how its constituent domain frameworks connect and how to combine their contributions.")
    lines.append(f"**Source of truth:** `references/` — a source-faithful decomposition of *{monolith.title}* (see `NOTICE.md` for the source/edition citation).")
    lines.append("**Readiness mode:** `source-faithful` — full text reproduced from an approved source.")
    lines.append("")
    lines.append("## Reference")
    lines.append("")
    lines.append(f"- `references/{pid}.md` — the Suite Architectural Reference.")
    lines.append("")
    lines.append("## Single surface")
    lines.append("")
    lines.append("`references/` is the canonical surface. `SKILL.md` is routing-only; there is no monolith to read. `INDEX.md` is reference-only.")
    lines.append("")
    lines.append("## Lookup rules")
    lines.append("")
    lines.append('- **Index first, then "no".** Check `references/INDEX.md` before searching. If an id is not listed there, the pattern does not exist — answer "no" and do not open files.')
    lines.append("- **Read once.** Do not reopen a card you have already read.")
    lines.append("")
    return "\n".join(lines)


def generate_skill_md_dispatch(monolith: Monolith, units: list, text: str) -> str:
    if monolith.kind == "suite":
        return generate_suite_skill_md(monolith, units, text)
    return generate_skill_md(monolith, units, text)


def generate_notice_md(monolith: Monolith) -> str:
    """Deterministic NOTICE.md — source citation + change record (CC BY 4.0)."""
    lines = [
        "# Notices",
        "",
        "## Source framework (all `references/*.md` and `context/*.md`)",
        "",
        "Source-faithfully decomposed from:",
        "",
        f"> Anatoly Levenchuk. *{monolith.title}*. DocID `{monolith.docid}`, FPF Library.",
        "> Working edition. GitHub repository: https://github.com/ailev/FPF",
        "",
        "Copyright (c) Anatoly Levenchuk. Licensed under CC BY 4.0,",
        "https://creativecommons.org/licenses/by/4.0/. Provided \"as is\", without warranties of",
        "any kind.",
        "",
        "**Changes:** (1) decomposed the monolithic framework into one file per pattern, plus one",
        "file per publication unit; (2) reproduced pattern bodies **verbatim** (source-faithful, no",
        "abridgement or minification); (3) added frontmatter (`id`, `title`, `status`, `keywords`,",
        "`dependencies`) derived from the source pattern index; (4) added a routing `SKILL.md`,",
        "`references/INDEX.md`, and the reader-help `context/` extraction. PatternIDs and titles",
        "follow the source.",
        "",
        "## Original text of this skill",
        "",
        "`SKILL.md` routing, `description`, and `INDEX.md` are original presentation work by Dmitry Ulanov,",
        "licensed under CC BY 4.0 as well.",
        "",
        "## Tooling",
        "",
        "The generating parser lives in the sibling tool skill `fpf-library-sync`",
        "(`scripts/decompose.py`, `scripts/sync_library.py`); scripts are not bundled in this",
        "skill. They carry their own license (MIT) and are not covered by this CC BY 4.0.",
        "",
        "## Third-party material quoted inside the source framework",
        "",
        "Remains subject to its rights holders' terms; see the source credits in the published",
        "DPF.",
        "",
    ]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Sync DPF Library skills from FPF/DPFs/** monoliths")
    parser.add_argument("selector", nargs="?", help="Skill slug / DocID / filename to limit to one")
    parser.add_argument("--check", action="store_true", help="Exit 0=up-to-date, 1=build needed")
    parser.add_argument("--dry-run", action="store_true", help="Discover + decompose in-memory, no writes")
    parser.add_argument("--validate", action="store_true", help="Validate counts vs README, orphans, idempotency (exit 0=valid)")
    parser.add_argument("--force", action="store_true", help="Rebuild even when unchanged")
    args = parser.parse_args()

    if not DPF_DIR.is_dir():
        print(f"ERROR: DPF directory not found: {DPF_DIR}", file=sys.stderr)
        sys.exit(2)

    all_monoliths = discover(DPF_DIR)
    if args.selector:
        selected = match_selector(all_monoliths, args.selector)
        if not selected:
            print(f"Unknown selector: {args.selector}", file=sys.stderr)
            sys.exit(2)
        monoliths = selected
    else:
        monoliths = all_monoliths

    print(f"DPF Library: {DPF_DIR}")
    print(f"Discovered: {len(all_monoliths)} monoliths "
          f"({sum(1 for m in all_monoliths if m.kind == 'framework')} frameworks, "
          f"{sum(1 for m in all_monoliths if m.kind == 'suite')} suite references)")
    print()

    if args.validate:
        failures, summary, idempotent = validate(monoliths)
        for s in summary:
            print(s)
        print()
        if idempotent:
            print("Idempotency: PASS (re-parse yields identical units)")
        if not failures:
            print("=== Validation PASSED ===")
            sys.exit(0)
        print(f"=== Validation FAILED ({len(failures)}) ===")
        for f in failures:
            print(f"  - {f}")
        sys.exit(1)

    rows: list[str] = []
    needs_update = False
    for m in monoliths:
        status = status_of(m)
        if status in ("new", "stale"):
            needs_update = True
        if args.dry_run or not args.check:
            total, refs, toc, warns = decompose_counts(m)
            rows.append((m, status, total, refs, toc, warns))
        else:
            rows.append((m, status, 0, 0, 0, 0))

    # Print the plan table.
    print(f"{'Suite':<24} {'Title':<44} {'DocID':<7} {'Skill dir':<42} {'Units':>5} {'ToC':>5} {'Warn':>4} Status")
    print("-" * 160)
    for m, status, total, refs, toc, warns in rows:
        suite = m.suite[:24]
        title = m.title[:44]
        print(f"{suite:<24} {title:<44} {m.docid:<7} {m.slug:<42} {total:>5} {toc:>5} {warns:>4} {status}")
    print()

    if args.check:
        if needs_update:
            print("Build needed — one or more skills are new or stale.")
            sys.exit(1)
        print("Up-to-date — no framework or suite reference needs rebuilding.")
        sys.exit(0)

    if args.dry_run:
        print("[DRY-RUN] No files written. Run without --dry-run to build the skills.")
        sys.exit(0)

    # Real sync.
    print("=== Building skills ===")
    built = skipped_minified = 0
    for m in monoliths:
        status = status_of(m)
        if status == "current" and not args.force:
            continue
        if status == "minified-existing" and not args.force:
            print(f"SKIP {m.slug}: minified skill present (no assets/) — move it to skills-compact, "
                  f"then rebuild with --force (DEC-0010)")
            skipped_minified += 1
            continue
        print(run_decompose(m, dry_run=False))
        built += 1

    print()
    print("=== Sync complete ===")
    print(f"Built: {built}; skipped minified (DEC-0010): {skipped_minified}")


if __name__ == "__main__":
    main()