"""
Sync fpf-core skill from the canonical FPF-Spec.md monolith.

Self-contained — bundles decompose.py + _common.py directly. `decompose`
is the unified parser: `parse_spec` handles both the FPF-Spec ToC scheme
(PID in the first cell) and the DPF scheme (ordinal + linked PID).
No external dependencies beyond Python stdlib + git.
All paths are derived from this script's location — portable across machines.

Workflow:
  1. git pull in FPF repo root
  2. Compare FPF-Spec.md with skills/fpf-core/assets/FPF-Spec.md
  3. If changed: copy monolith -> decompose -> update SKILL.md

Usage:
  python sync_fpf_core.py              # full sync
  python sync_fpf_core.py --check      # only check, exit 0=up-to-date, 1=needs update
  python sync_fpf_core.py --dry-run    # preview without writing
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

import decompose
from _common import (
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
SPEC_NAME = "FPF-Spec.md"
SPEC_SOURCE = FPF_REPO / SPEC_NAME
SKILL_DIR = FPF_REPO / "skills" / "fpf-core"
SPEC_ASSET = SKILL_DIR / "assets" / SPEC_NAME
SKILL_MD = SKILL_DIR / "SKILL.md"
REFERENCES_DIR = SKILL_DIR / "references"
CONTEXT_DIR = SKILL_DIR / "context"

LINES_RE = re.compile(r"(canonical specification \()(\d+K\+)( lines\))")
REFS_RE = re.compile(r"(\*\*Ready\*\* — )(\d+)( pattern reference files \+ INDEX \+ )(\d+)( context sections\.)")


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def count_lines(path: Path) -> int:
    raw = path.read_text(encoding="utf-8", errors="replace")
    return len(raw.splitlines())


def count_references(refs_dir: Path, ctx_dir: Path) -> tuple[int, int]:
    """Return (pattern_ref_count, context_section_count).

    Patterns live in references/; context (non-pattern) units live in context/.
    A bundled static file like USING-FPF.md (no `_ctx.` prefix) is not a context section."""
    pattern_count = 0
    if refs_dir.is_dir():
        for f in refs_dir.iterdir():
            if not f.is_file() or f.suffix != ".md":
                continue
            if f.name in ("INDEX.md", "relations.md"):
                continue
            if f.name.startswith("_ctx."):
                continue  # stale leftover from before the context/ move
            pattern_count += 1
    ctx_count = 0
    if ctx_dir.is_dir():
        for f in ctx_dir.iterdir():
            if f.is_file() and f.suffix == ".md" and f.name.startswith("_ctx."):
                ctx_count += 1
    return pattern_count, ctx_count


def git_pull(repo: Path) -> tuple[bool, str]:
    """Run git pull. Returns (ok, output_text)."""
    try:
        result = subprocess.run(
            ["git", "-C", str(repo), "pull"],
            capture_output=True, text=True, timeout=60,
        )
        output = (result.stdout + result.stderr).strip()
        return result.returncode == 0, output
    except Exception as e:
        return False, str(e)


def run_decompose(spec_path: Path, skills_dir: Path, *, dry_run: bool = False) -> tuple[str, dict | None]:
    """Decompose monolith into references/. Returns (status_text, report_dict)."""
    refs_dir = skills_dir / "references"
    ctx_dir = skills_dir / "context"
    refs_dir.mkdir(parents=True, exist_ok=True)

    report, units, context_units, spec_filename = decompose.parse_spec(
        spec_path, plain_keywords=False
    )

    output_lines: list[str] = []
    output_lines.append(f"Decomposing FPF spec: {spec_path}")
    output_lines.append(f"Output directory: {refs_dir}")
    output_lines.append(f"Context directory: {ctx_dir}")
    output_lines.append(f"Total patterns (with :End markers): {report.total_patterns}")
    output_lines.append(f"Patterns extracted: {len(units)}")
    output_lines.append(f"ToC entries: {report.toc_entries}")

    if report.warnings:
        output_lines.append(f"\nWarnings ({len(report.warnings)}):")
        for w in report.warnings:
            output_lines.append(f"  - {w}")

    # Write context sections (non-pattern ##/# headings) into context/, not references/
    retired = retire_stale_context_refs(refs_dir, dry_run=dry_run)
    ctx_written, ctx_skipped, ctx_trivial = write_context_units(
        ctx_dir, context_units, report, dry_run=dry_run
    )

    ctx_status = f"{ctx_written} written, {ctx_skipped} skipped (unchanged)"
    if ctx_trivial:
        ctx_status += f", {ctx_trivial} trivial skipped"
    if retired:
        ctx_status += f", {retired} retired from references/"
    output_lines.append(f"Context sections: {ctx_status}")

    # Write pattern references
    if units:
        written = 0
        skipped = 0
        for unit in units:
            content, raw_len, opt_len = format_reference(unit)
            report.size_stats.raw_bytes += raw_len
            report.size_stats.optimized_bytes += opt_len
            filepath = refs_dir / slugify(unit.pid)
            if idempotent_write(filepath, content, dry_run=dry_run):
                written += 1
            else:
                skipped += 1

        index_content = generate_index(units, spec_path.stem, spec_filename, has_relations=False)
        index_path = refs_dir / "INDEX.md"
        if idempotent_write(index_path, index_content, dry_run=dry_run):
            output_lines.append(f"INDEX.md written ({len(units)} entries)")
        else:
            output_lines.append(f"INDEX.md unchanged ({len(units)} entries)")

        kept = {slugify(unit.pid) for unit in units} | {"INDEX.md"}
        retired_patterns = retire_stale_pattern_refs(refs_dir, kept, dry_run=dry_run)
        if retired_patterns:
            output_lines.append(f"{retired_patterns} stale pattern file(s) retired from references/")

        output_lines.append(f"References: {written} written, {skipped} skipped (unchanged)")
    else:
        output_lines.append("No patterns extracted!")

    report_dict = report.to_dict()
    output_lines.append("")
    output_lines.append(json.dumps(report_dict, indent=2, ensure_ascii=False))

    return "\n".join(output_lines), report_dict


def update_skill_md(skill_md: Path, line_count: int, pattern_count: int, ctx_count: int) -> bool:
    """Update line count and reference counts in SKILL.md. Returns True if changed."""
    text = skill_md.read_text(encoding="utf-8")

    thousands = max(1, (line_count + 500) // 1000)
    text, n1 = LINES_RE.subn(rf"\g<1>{thousands}K+\g<3>", text)

    text, n2 = REFS_RE.subn(rf"\g<1>{pattern_count}\g<3>{ctx_count}\g<5>", text)

    if n1 == 0 and n2 == 0:
        return False

    skill_md.write_text(text, encoding="utf-8")
    return True


def generate_notice_md() -> str:
    """Deterministic NOTICE.md — source citation + change record (CC BY 4.0)."""
    lines = [
        "# Notices",
        "",
        "## Source framework (`assets/FPF-Spec.md`, `references/*.md`, `context/*.md`)",
        "",
        "Source-faithfully decomposed from:",
        "",
        "> Anatoly Levenchuk. *First Principles Framework (FPF)*. FPF Library.",
        "> Working edition. GitHub repository: https://github.com/ailev/FPF",
        "",
        "Copyright (c) Anatoly Levenchuk. Licensed under CC BY 4.0,",
        "https://creativecommons.org/licenses/by/4.0/. Provided \"as is\", without warranties of",
        "any kind.",
        "",
        "**Changes:** (1) `assets/FPF-Spec.md` is redistributed **verbatim**; (2) the monolithic",
        "specification was decomposed into one file per pattern (`references/*.md`) plus an",
        "`INDEX.md`; (3) reader-help sections were extracted into `context/`; (4) routing",
        "`SKILL.md` and per-reference frontmatter were added. PatternIDs and section addresses",
        "follow the source.",
        "",
        "## Original text of this skill",
        "",
        "`SKILL.md` routing, `description`, and `README.md` are original presentation work",
        "by Dmitry Ulanov, licensed under CC BY 4.0 as well.",
        "",
        "## Third-party material quoted inside the source framework",
        "",
        "Remains subject to its rights holders' terms; see the source credits in the published",
        "FPF text.",
        "",
    ]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Sync fpf-core skill from FPF monolith")
    parser.add_argument("--check", action="store_true", help="Exit 0=up-to-date, 1=update needed")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing")
    parser.add_argument("--no-git", action="store_true", help="Skip git pull")
    parser.add_argument("--force", action="store_true", help="Re-decompose even if the monolith is unchanged (apply generator changes)")
    args = parser.parse_args()

    errors: list[str] = []

    # 1. git pull
    if not args.no_git:
        print("=== Step 1: git pull ===")
        ok, output = git_pull(FPF_REPO)
        print(output)
        if not ok and "fatal" not in output and "error" not in output.lower():
            pass
        elif not ok:
            print("WARNING: git pull had issues — continuing with local state")

    # 2. Check if update needed
    print("\n=== Step 2: Checking for changes ===")
    if not SPEC_SOURCE.is_file():
        print(f"ERROR: Source spec not found: {SPEC_SOURCE}")
        sys.exit(2)

    source_hash = sha256_file(SPEC_SOURCE)
    source_lines = count_lines(SPEC_SOURCE)

    asset_exists = SPEC_ASSET.is_file()
    asset_hash = sha256_file(SPEC_ASSET) if asset_exists else ""
    asset_lines = count_lines(SPEC_ASSET) if asset_exists else 0

    print(f"Source: {source_lines} lines, sha256={source_hash[:16]}...")
    print(f"Asset:  {asset_lines} lines, sha256={asset_hash[:16]}..." if asset_exists else "Asset:  MISSING")

    if asset_exists and source_hash == asset_hash and not args.force:
        print("\nFPF-Spec.md is up-to-date. Nothing to do.")
        sys.exit(0)

    if args.check and not args.force:
        print("\nUpdate needed — source has changed.")
        sys.exit(1)

    if args.dry_run:
        print("\n[DRY-RUN] Would update the skill. Stopping.")
        sys.exit(0)

    # 3. Copy monolith to assets
    print("\n=== Step 3: Copying monolith to assets ===")
    SPEC_ASSET.parent.mkdir(parents=True, exist_ok=True)
    SPEC_ASSET.write_bytes(SPEC_SOURCE.read_bytes())
    print(f"Copied: {SPEC_SOURCE} -> {SPEC_ASSET}")

    # 4. Run decomposition
    print("\n=== Step 4: Running decomposition ===")
    output, report = run_decompose(SPEC_ASSET, SKILL_DIR, dry_run=args.dry_run)
    print(output)
    if report:
        if report.get("errors"):
            errors.extend(report["errors"])
        if report.get("warnings"):
            for w in report["warnings"]:
                print(f"WARNING: {w}")

    # 4.5 Bundle the USING-FPF.md operating instruction into context/
    print("\n=== Step 4.5: Bundling USING-FPF.md ===")
    using_src = FPF_REPO / "USING-FPF.md"
    context_dir = SKILL_DIR / "context"
    context_dir.mkdir(parents=True, exist_ok=True)
    if using_src.is_file():
        if idempotent_write(context_dir / "USING-FPF.md", using_src.read_text(encoding="utf-8"), dry_run=args.dry_run):
            print("USING-FPF.md copied to context/")
        else:
            print("USING-FPF.md already in place (unchanged)")
    else:
        print("WARNING: USING-FPF.md not found at repo root — skipped")

    # 5. Count and update SKILL.md
    print("\n=== Step 5: Updating SKILL.md ===")
    pattern_count, ctx_count = count_references(REFERENCES_DIR, CONTEXT_DIR)
    line_count = count_lines(SPEC_SOURCE)
    thousands = max(1, (line_count + 500) // 1000)

    print(f"Pattern references: {pattern_count}")
    print(f"Context sections:  {ctx_count}")
    print(f"Monolith lines:    {line_count} (~{thousands}K)")

    updated = update_skill_md(SKILL_MD, line_count, pattern_count, ctx_count)
    if updated:
        print("SKILL.md updated.")
    else:
        print("SKILL.md already up-to-date.")

    # 5.5 Author NOTICE.md and ensure LICENSE are present
    print("\n=== Step 5.5: Licensing files ===")
    notice_path = SKILL_DIR / "NOTICE.md"
    if idempotent_write(notice_path, generate_notice_md(), dry_run=args.dry_run):
        print("NOTICE.md written.")
    else:
        print("NOTICE.md unchanged.")

    license_src = FPF_REPO / "LICENSE"
    license_path = SKILL_DIR / "LICENSE"
    if license_src.is_file():
        if idempotent_write(license_path, license_src.read_text(encoding="utf-8"), dry_run=args.dry_run):
            print("LICENSE copied from repo root.")
        else:
            print("LICENSE already in place.")
    else:
        print("WARNING: LICENSE not found at repo root — skipped.")

    # 6. Report
    print("\n=== Sync complete ===")
    if errors:
        print(f"Errors ({len(errors)}):")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print("SUCCESS — fpf-core skill is in sync with canonical FPF-Spec.md")


if __name__ == "__main__":
    main()
