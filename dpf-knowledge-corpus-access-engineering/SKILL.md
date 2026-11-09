---
name: dpf-knowledge-corpus-access-engineering
description: |
  Knowledge-Corpus Access Engineering (KCAE) — Use when you need to engineer arrangements for finding, reading and using documentary knowledge, including links back to source passages, delivery and coherent updates.
license: CC-BY-4.0
---

# DPF: Knowledge-Corpus Access Engineering (KCAE)

**Depends on:** `fpf-core`
**Bounded context:** Methods for designing, using and changing access to documentary knowledge.
**Source of truth:** `references/` — a source-faithful decomposition of *Knowledge-Corpus Access Engineering Principles Framework* (see `NOTICE.md` for the source/edition citation).
**Readiness mode:** `source-faithful` — full bodies reproduced from an approved source; no card has passed a heterogeneous-case evaluation (`E.21`). `status` on each card is the source's own status.

## When to load which pattern

| Situation | Load |
|---|---|
| you are constructing, buying or changing access to a documentary corpus and several technically feasible arrangements would serve different … | `references/KCAE.USE.md` |
| documents must become searchable or machine-readable, when a hit cannot be opened reliably, or when extracted text can lose a decisive relat … | `references/KCAE.SOURCE.md` |
| repeated questions concern a large corpus and the useful source, phrase or contribution is often unknown. | `references/KCAE.INDEX.md` |
| a question has no sufficient known source, when a first result leaves a consequential gap, when new reading changes what should be sought, o … | `references/KCAE.SEARCH.md` |
| a retrieved passage, document or method description might contribute to a concrete result, or when an automated score is to affect reading … | `references/KCAE.ASSESS.md` |
| the work needs several contributions, one candidate leaves a required result unprovided, or individually suitable methods interact through a … | `references/KCAE.COMPOSE.md` |
| a found contribution must cross to another person, model call, tool or later occasion, and its source conditions may not survive that crossi … | `references/KCAE.DELIVER.md` |
| sources, extraction, permissions, representations or cached judgements change while access continues or resumes after an interruption. | `references/KCAE.CHANGE.md` |
| useful knowledge is not being requested because the person doing the work has no occasion to notice the question. | `references/KCAE.ENCOUNTER.md` |
| repeated inquiries recreate the same source-to-work connection, or an unresolved observation should remain available for a later source, que … | `references/KCAE.MEMORY.md` |
| adopting, replacing or repairing an access arrangement requires evidence of its practical gain, or a failure needs attribution to the operat … | `references/KCAE.EVAL.md` |

## Publication units

Non-pattern sections of the framework, reproduced as reference cards:

- `references/KCAE.Reference.md` — Architectural Reference
- `references/KCAE.Application.md` — Worked cases / cross-pattern applications
- `references/KCAE.Profiles.md` — Publication unit

## Navigation rule

Start from the working difficulty, not file order. Follow each card's `Governing patterns` line and frontmatter `dependencies` when a needed result is missing.

## Single surface

`references/` is the canonical surface. `SKILL.md` is routing-only; there is no monolith to read. `INDEX.md` is reference-only.

## Lookup rules

- **Index first, then "no".** Check `references/INDEX.md` before searching. If an id is not listed there, the pattern does not exist — answer "no" and do not open files.
- **Read once.** Do not reopen a card you have already read.
