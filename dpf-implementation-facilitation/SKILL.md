---
name: dpf-implementation-facilitation
description: |
  Implementation Facilitation (IS) — Use when you need to help participants put an evidence-informed practice to use under local conditions, adapt the assistance and develop their capacity for further change.
license: CC-BY-4.0
---

# DPF: Implementation Facilitation (IS)

**Depends on:** `fpf-core`
**Bounded context:** Help participants put an evidence-informed practice to use under local conditions, adapt the assistance and develop their capacity for further change.
**Source of truth:** `references/` — a source-faithful decomposition of *Implementation Facilitation Principles Framework* (see `NOTICE.md` for the source/edition citation).
**Readiness mode:** `source-faithful` — full bodies reproduced from an approved source; no card has passed a heterogeneous-case evaluation (`E.21`). `status` on each card is the source's own status.

## When to load which pattern

| Situation | Load |
|---|---|
| someone requests implementation help, offers a service or sponsors a change, but the participants do not yet share a workable account of wha … | `references/IS.1.md` |
| intended practice cannot begin, later use fails or current help is ineffective, and different explanations would lead to different action. | `references/IS.2.md` |
| the useful contribution is sufficiently understood but several forms, combinations or intensities of help remain plausible. | `references/IS.3.md` |
| Implementation support changes while the target practice continues. Temporary experts leave, licences expire, workloads grow, evidence chang … | `references/IS.5.md` |
| Use this Method when a practice change depends on parties whose knowledge, decisions or resources do not reach each other, and unequal influ … | `references/IS.6.md` |
| Use this Method when a proposed practice cannot become useful through delivery of its instructions alone: what it asks people to do interact … | `references/IS.7.md` |
| Use this Method when people or organizations receiving implementation help are expected to recognize and conduct a subsequent change, rather … | `references/IS.8.md` |

## Publication units

Non-pattern sections of the framework, reproduced as reference cards:

- `references/IS.Reference.md` — Architectural Reference
- `references/IS.Application.md` — Worked cases / cross-pattern applications
- `references/IS.Sources.md` — Source arguments and refresh
- `references/IS.Edition.md` — Edition and reuse

## Navigation rule

Start from the working difficulty, not file order. Follow each card's `Governing patterns` line and frontmatter `dependencies` when a needed result is missing.

## Single surface

`references/` is the canonical surface. `SKILL.md` is routing-only; there is no monolith to read. `INDEX.md` is reference-only.

## Lookup rules

- **Index first, then "no".** Check `references/INDEX.md` before searching. If an id is not listed there, the pattern does not exist — answer "no" and do not open files.
- **Read once.** Do not reopen a card you have already read.
