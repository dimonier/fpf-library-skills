---
name: fpf-library-sync
description: |
  Build and refresh the FPF agent-skill fleet from the Levenchuk FPF Library monoliths:
  fpf-core from FPF-Spec.md, and each dpf-* skill from FPF/DPFs/**. Use when (1) the FPF
  specification or a DPF framework is added/updated and its skill is stale, (2) pattern-index
  metadata (status/keywords/dependencies) must be re-extracted, (3) running scheduled
  maintenance on the skill fleet. Self-contained — bundles decompose.py + _common.py;
  requires Python 3.10+ and, for the fpf-core path, git in PATH.
license: MIT
---

# FPF Library Skill Sync

**Bounded context:** keeping the two kinds of skills in sync with the Levenchuk FPF Library —
`fpf-core` from the canonical `FPF-Spec.md`, and every `dpf-*` skill from a DPF monolith under
`DPFs/**`. One unified parser (`decompose.py`) serves both targets; two orchestrators drive them.

**Self-contained** — all decomposition logic is bundled in `scripts/`. No external skill
dependencies. Requires Python 3.10+; `sync_fpf_core.py` also needs `git` in PATH.

## Two build paths

| Target | Orchestrator | Source | What it does |
|---|---|---|---|
| `fpf-core` | `scripts/sync_fpf_core.py` | `../../FPF-Spec.md` (git-tracked) | git pull → hash compare → copy to `assets/` → decompose → refresh `SKILL.md` counters → author `NOTICE.md`/`LICENSE` → bundle `USING-FPF.md` |
| `dpf-*` (36 + 4) | `scripts/sync_library.py` | `../../DPFs/**` (local files) | discovery → title-derived naming → copy to `assets/` → decompose → deterministic `SKILL.md` authoring → `NOTICE.md`/`LICENSE` |

## Quick Start — fpf-core

```bash
cd fpf-library-sync/scripts
python sync_fpf_core.py --check      # exit 0=up-to-date, 1=update needed
python sync_fpf_core.py              # full sync (git pull + rebuild)
python sync_fpf_core.py --dry-run    # preview without writing
python sync_fpf_core.py --no-git     # skip git pull (use local state)
python sync_fpf_core.py --force      # rebuild even when the monolith is unchanged
```

## Quick Start — DPF library

```bash
cd fpf-library-sync/scripts
python sync_library.py --dry-run     # discover 36+4, in-memory decompose, no writes
python sync_library.py --validate    # counts vs README, orphans, idempotency
python sync_library.py --check       # exit 0=up-to-date, 1=build needed
python sync_library.py               # full build (copy assets + decompose)
python sync_library.py dpf-strategy  # one skill by slug / DocID / filename
```

## Scripts

| File | Role |
|---|---|
| `sync_fpf_core.py` | fpf-core orchestrator: git pull → hash compare → copy monolith → decompose → update `SKILL.md` counters → `NOTICE.md`/`LICENSE` → bundle `USING-FPF.md` |
| `sync_library.py` | DPF orchestrator: discovery over `DPFs/**` (36 frameworks + 4 Suite References), title-derived naming, `assets/` copy, decompose, deterministic `SKILL.md` authoring, report |
| `decompose.py` | Unified monolith parser (single entry `parse_spec`): accepts both ToC schemes (FPF PID-in-first-cell; DPF §-ordinal + linked PID), `:End` boundaries, reference + context extraction |
| `_common.py` | Shared utilities: YAML frontmatter, `format_reference`, `generate_index`, idempotent writes, `ExtractedUnit.is_pattern` |

## Status

- **fpf-core:** done and in use — `sync_fpf_core.py` rebuilds `fpf-core` source-faithfully from
  `FPF-Spec.md`.
- **DPF (Phases 0–3 done):** parser, orchestrator, deterministic `SKILL.md`, validation pass
  (524/524 patterns, 0 orphans, idempotent).
- **DPF next (Phases 4–5):** reconcile the minified `dpf-systems-engineering` /
  `dpf-organization-change-engineering` skills (DEC-0010), then a full build of all 36
  frameworks + 4 Suite References.

## Key structural difference between the two sources

The DPF pattern index puts a §-ordinal in the first cell and the PatternID inside a markdown
link in the second (`| 1 | [SYSE.1 - Title](#…) | …`), whereas `FPF-Spec` puts the PID in the
first cell. `parse_spec` accepts both; only the ToC row parser differs per scheme — the
`:End` boundary and heading-extraction logic is shared.

## Evolution

If the user is dissatisfied with a result or the FPF-Spec / DPF structure changes, offer to
update the relevant script or this SKILL.md.

## License

Copyright (c) 2026 Dmitry Ulanov. Licensed under the MIT License — see `LICENSE`.
This tool does not bundle FPF framework text; see `NOTICE.md`.