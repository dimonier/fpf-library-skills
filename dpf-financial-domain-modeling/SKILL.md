---
name: dpf-financial-domain-modeling
description: |
  Financial Domain Modeling (FDM) — Use when you need to model financial positions, rights, obligations, events and payment flows without confusing their different effects.
license: CC-BY-4.0
---

# DPF: Financial Domain Modeling (FDM)

**Depends on:** `fpf-core`
**Bounded context:** Financial Domain Modeling helps a financial practitioner, business modeler or service designer establish whose financial position a model describes, what events can change it and how a service contributes to a participant's result. Its five methods connect parties, rights and obligations, contractual flows, actual effects and service use.
**Source of truth:** `references/` — a source-faithful decomposition of *Financial Domain Modeling Principles Framework* (see `NOTICE.md` for the source/edition citation).
**Readiness mode:** `source-faithful` — full bodies reproduced from an approved source; no card has passed a heterogeneous-case evaluation (`E.21`). `status` on each card is the source's own status.

## When to load which pattern

| Situation | Load |
|---|---|
| Financial systems hold statements about parties and their positions. The word “claim” can refer either to an assertion in a report or to a c … | `references/FDM.1.md` |
| One fund tracks investments by individual legal entity. Another groups startups associated with the same founders. | `references/FDM.2.md` |
| “Loan amount 100” does not say whether 100 is the advance, current principal or payment due. | `references/FDM.3.md` |
| A lending decision can authorize a next step without funding a borrower. An agreement can create a duty before funding. | `references/FDM.4.md` |
| A scoring team can improve predictive accuracy while leaving lending decisions unchanged. | `references/FDM.5.md` |

## Publication units

Non-pattern sections of the framework, reproduced as reference cards:

- `references/FDM.Reference.md` — Architectural Reference
- `references/FDM.Sources.md` — Source arguments and refresh

## Navigation rule

Start from the working difficulty, not file order. Follow each card's `Governing patterns` line and frontmatter `dependencies` when a needed result is missing.

## Single surface

`references/` is the canonical surface. `SKILL.md` is routing-only; there is no monolith to read. `INDEX.md` is reference-only.

## Lookup rules

- **Index first, then "no".** Check `references/INDEX.md` before searching. If an id is not listed there, the pattern does not exist — answer "no" and do not open files.
- **Read once.** Do not reopen a card you have already read.
