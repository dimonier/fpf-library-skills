---
name: dpf-narrativization-and-narrative-studies
description: |
  Narrativization and Narrative Studies (NSTD) — Use when you need to develop and interpret followable narratives; construct working accounts and fictional or hypothetical events; preserve relations, uncertainty and useful returns to source material.
license: CC-BY-4.0
---

# DPF: Narrativization and Narrative Studies (NSTD)

**Depends on:** `fpf-core`
**Bounded context:** Develop and interpret followable narratives; construct working accounts and fictional or hypothetical events; preserve relations, uncertainty and useful returns to source material.
**Source of truth:** `references/` — a source-faithful decomposition of *Narrativization and Narrative Studies Principles Framework* (see `NOTICE.md` for the source/edition citation).
**Readiness mode:** `source-faithful` — full bodies reproduced from an approved source; no card has passed a heterogeneous-case evaluation (`E.21`). `status` on each card is the source's own status.

## When to load which pattern

| Situation | Load |
|---|---|
| a writer, narrator, teacher, architect, researcher, commentator, story designer, or tool starts with a message, lesson, theme, persuasive ef … | `references/NSTD.1.md` |
| a graph, mechanism, evidence set, architecture structure, candidate set, mathematical dependency structure, canon structure, or source tradi … | `references/NSTD.2.md` |
| locally fluent narrative passages fail because readers cannot build a coherent model of source mechanism, event flow, dependency structure … | `references/NSTD.3.md` |
| a rewrite conveys the facts but no longer sounds like the intended author, when a new narrator needs a distinctive way of speaking, or when … | `references/NSTD.4.md` |
| readers lose attention before reaching a needed distinction, remember the wrong feature, or draw unwarranted confidence from an engaging acc … | `references/NSTD.5.md` |
| a team must decide whether one narrative rendering version, including an unaccepted candidate, is good enough for one declared reader or lis … | `references/NSTD.6.md` |
| LLM, NLG, graph-to-text, data-to-text, story-planning, schema-governed generation, or search is used to produce or repair narrative renderin … | `references/NSTD.7.md` |
| a complex source structure must be taught, explained, or learned through a narrative route, and the route must preserve enough structure for … | `references/NSTD.8.md` |
| observations, recollections, documents, images or a narrative are available, but the account of what they show or mean is not yet adequate. | `references/NSTD.9.md` |
| an author has a situation, image, premise, character, desired effect or prospective ending but the events and relationships needed for the s … | `references/NSTD.10.md` |

## Publication units

Non-pattern sections of the framework, reproduced as reference cards:

- `references/NSTD.Reference.md` — Architectural Reference
- `references/NSTD.Sources.md` — Source arguments and refresh

## Navigation rule

Start from the working difficulty, not file order. Follow each card's `Governing patterns` line and frontmatter `dependencies` when a needed result is missing.

## Single surface

`references/` is the canonical surface. `SKILL.md` is routing-only; there is no monolith to read. `INDEX.md` is reference-only.

## Lookup rules

- **Index first, then "no".** Check `references/INDEX.md` before searching. If an id is not listed there, the pattern does not exist — answer "no" and do not open files.
- **Read once.** Do not reopen a card you have already read.
