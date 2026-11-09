---
name: dpf-leadership
description: |
  Leadership (LDR) — Use when you need to direct personal action; develop joint direction, participation and responsibility; obtain feasible contributions and first useful work.
license: CC-BY-4.0
---

# DPF: Leadership (LDR)

**Depends on:** `fpf-core`
**Bounded context:** Developing direction, participation and responsibility in one's own action and joint work, from an unsettled concern to useful work and renewed practice.
**Source of truth:** `references/` — a source-faithful decomposition of *Leadership Principles Framework* (see `NOTICE.md` for the source/edition citation).
**Readiness mode:** `source-faithful` — full bodies reproduced from an approved source; no card has passed a heterogeneous-case evaluation (`E.21`). `status` on each card is the source's own status.

## When to load which pattern

| Situation | Load |
|---|---|
| joint work needs an explanation, challenge, role conversation, allocation of help or other leadership contribution that is missing or depend … | `references/LDR.1.md` |
| participants need one another's contributions but their proposed scopes, dates, costs or conditions cannot yet coexist. | `references/LDR.2.md` |
| a promising proposal must become understandable, examinable and supported by real contributions before joint work can begin, or when an anno … | `references/LDR.4.md` |
| people are connected by a concern, opportunity or changing situation but cannot yet undertake a sufficiently understood course together. | `references/LDR.5.md` |

## Publication units

Non-pattern sections of the framework, reproduced as reference cards:

- `references/LDR.Reference.md` — Architectural Reference

## Navigation rule

Start from the working difficulty, not file order. Follow each card's `Governing patterns` line and frontmatter `dependencies` when a needed result is missing.

## Single surface

`references/` is the canonical surface. `SKILL.md` is routing-only; there is no monolith to read. `INDEX.md` is reference-only.

## Lookup rules

- **Index first, then "no".** Check `references/INDEX.md` before searching. If an id is not listed there, the pattern does not exist — answer "no" and do not open files.
- **Read once.** Do not reopen a card you have already read.
