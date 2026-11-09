---
name: dpf-human-resource-management
description: |
  Human Resource Management (HRM) — Use when you need to construct and revise workforce conditions, assessment and selection, reward, voice, protection and continuing participation.
license: CC-BY-4.0
---

# DPF: Human Resource Management (HRM)

**Depends on:** `fpf-core`
**Bounded context:** Constructing and revising the conditions through which people participate in organizational work: personnel assessment and selection, remuneration, voice, protection and continuing participation.
**Source of truth:** `references/` — a source-faithful decomposition of *Human Resource Management Principles Framework* (see `NOTICE.md` for the source/edition citation).
**Readiness mode:** `source-faithful` — full bodies reproduced from an approved source; no card has passed a heterogeneous-case evaluation (`E.21`). `status` on each card is the source's own status.

## When to load which pattern

| Situation | Load |
|---|---|
| a workforce proposal or existing practice changes conditions on which another personnel practice relies: a new job changes selection and pay … | `references/HRM.1.md` |
| recruitment, promotion, allocation or another personnel choice relies on a claim about a person's suitability for actual work. | `references/HRM.2.md` |
| remuneration, benefits or progression need a justified design or revision: job demands have changed, external rates differ, pay relationship … | `references/HRM.3.md` |
| affected people need to influence a work or personnel decision, raise a concern, negotiate terms, or challenge how a personnel rule or decis … | `references/HRM.4.md` |
| a person's current work arrangement needs to continue differently, pause, resume, move or end. | `references/HRM.5.md` |

## Publication units

Non-pattern sections of the framework, reproduced as reference cards:

- `references/HRM.Reference.md` — Architectural Reference
- `references/HRM.Source.md` — Source arguments and refresh

## Navigation rule

Start from the working difficulty, not file order. Follow each card's `Governing patterns` line and frontmatter `dependencies` when a needed result is missing.

## Single surface

`references/` is the canonical surface. `SKILL.md` is routing-only; there is no monolith to read. `INDEX.md` is reference-only.

## Lookup rules

- **Index first, then "no".** Check `references/INDEX.md` before searching. If an id is not listed there, the pattern does not exist — answer "no" and do not open files.
- **Read once.** Do not reopen a card you have already read.
