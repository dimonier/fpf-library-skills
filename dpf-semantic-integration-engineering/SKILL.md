---
name: dpf-semantic-integration-engineering
description: |
  Semantic Integration Engineering (SIE) — Use when you need to make separately governed meanings usable together through models, mappings, interfaces, validation and response to change.
license: CC-BY-4.0
---

# DPF: Semantic Integration Engineering (SIE)

**Depends on:** `fpf-core`
**Bounded context:** A domain pattern language for making separately governed meanings and representations usable together for a named receiving use.
**Source of truth:** `references/` — a source-faithful decomposition of *Semantic Integration Engineering Principles Framework* (see `NOTICE.md` for the source/edition citation).
**Readiness mode:** `source-faithful` — full bodies reproduced from an approved source; no card has passed a heterogeneous-case evaluation (`E.21`). `status` on each card is the source's own status.

## When to load which pattern

| Situation | Load |
|---|---|
| a request says “integrate the data”, “align the models”, “build the knowledge graph”, or “make one source of truth”, but the intended receiv … | `references/SIE.1.md` |
| a bounded integration use exists, yet endpoint meanings are being inferred from labels, column names, class names, diagrams, sample values … | `references/SIE.2.md` |
| an integration needs to express a meaning or answer a question and the adequacy of its available models is unsettled. | `references/SIE.3.md` |
| two or more governed sources contain concepts, types, relations, fields, codes, model elements, or claims that appear to match and a receivi … | `references/SIE.4.md` |
| an integration needs to decide whether records or identifiers from different sources concern the same entity, a part, a version, a variant … | `references/SIE.5.md` |
| a receiving answer must combine claims from separately governed sources and a simple union, priority rule, average, overwrite, or “golden re … | `references/SIE.6.md` |
| accepted semantic correspondences must become repeatable extraction or transformation behavior, or existing code contains joins, conversions … | `references/SIE.7.md` |
| accepted semantic mappings exist and the current question is whether to evaluate them at query time, persist integrated results, or combine … | `references/SIE.8.md` |
| semantic mappings or integrated state exist but the receiving Work still cannot obtain, interpret, challenge, or return the bounded result. | `references/SIE.9.md` |
| a candidate semantic interface or mapping package exists and somebody asks whether it is ready, correct, valid, trustworthy, or fit for use. … | `references/SIE.10.md` |
| a relied-on source definition, model commitment, identifier meaning, mapping premise, or interface interpretation changes and the integratio … | `references/SIE.11.md` |
| independently governed participants depend on shared semantic modules and need an arrangement for maintaining them. | `references/SIE.12.md` |
| a query, decision or operation needs separately governed information to work together, but obtaining the individual meanings, correspondence … | `references/SIE.13.md` |

## Publication units

Non-pattern sections of the framework, reproduced as reference cards:

- `references/SIE.Reference.md` — Architectural Reference
- `references/SIE.Application.md` — Worked cases / cross-pattern applications
- `references/SIE.Sources.md` — Source arguments and refresh

## Navigation rule

Start from the working difficulty, not file order. Follow each card's `Governing patterns` line and frontmatter `dependencies` when a needed result is missing.

## Single surface

`references/` is the canonical surface. `SKILL.md` is routing-only; there is no monolith to read. `INDEX.md` is reference-only.

## Lookup rules

- **Index first, then "no".** Check `references/INDEX.md` before searching. If an id is not listed there, the pattern does not exist — answer "no" and do not open files.
- **Read once.** Do not reopen a card you have already read.
