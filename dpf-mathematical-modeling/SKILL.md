---
name: dpf-mathematical-modeling
description: |
  Mathematical Modeling (MMP) — Use when you need to relate a subject question to mathematics; infer, predict, compare interventions, design observations and revise or combine models.
license: CC-BY-4.0
---

# DPF: Mathematical Modeling (MMP)

**Depends on:** `fpf-core`
**Bounded context:** Methods for constructing mathematical representations of a question, connecting unknown relations, observations and available actions, and revising the resulting models.
**Source of truth:** `references/` — a source-faithful decomposition of *Mathematical Modeling DPF* (see `NOTICE.md` for the source/edition citation).
**Readiness mode:** `source-faithful` — full bodies reproduced from an approved source; no card has passed a heterogeneous-case evaluation (`E.21`). `status` on each card is the source's own status.

## When to load which pattern

| Situation | Load |
|---|---|
| you know conditions that a possible object or situation must satisfy, but still need to express its possibilities mathematically. | `references/MMP.10.md` |
| part of a model is supported, but a function or other relation is still unknown. | `references/MMP.11.md` |
| a mathematical problem mixes quantities you may choose with quantities you do not control, or when a proposed solution depends on informatio … | `references/MMP.8.md` |
| **Use this when a choice changes what can be done or learned later, and comparing its immediate result does not settle the useful course of … | `references/MMP.8.SD.md` |
| inference depends on how events, responses or quantities become records, and that procedure has not yet been expressed in the probability mo … | `references/MMP.7.md` |
| you can predict records from a proposed state or model, but recovering the needed unknown from the records is ambiguous or too sensitive to … | `references/MMP.12.md` |
| a probability model describes how records arise, and the work needs an estimate, an interval or a probability about something not directly k … | `references/MMP.13.md` |
| a mathematical model's predictions leave a consequential feature of the available observations unexplained, or when a proposed use makes suc … | `references/MMP.14.md` |
| the work asks what changing an action, operating condition or working method would do, and available observations or experiments might alrea … | `references/MMP.15.md` |
| the question concerns the same case under another action, a joint comparison of its possible responses, or a specified pathway through which … | `references/MMP.19.md` |
| several mathematical accounts remain possible and the next useful answer depends on a difference between them. | `references/MMP.16.md` |
| a supplied model describes how a state changes, but predicting the quantities you need would be easier with less state, shorter memory or a … | `references/MMP.9.md` |
| repeated use of a model is too costly or cumbersome, and the next calculation needs only some of its responses. | `references/MMP.17.md` |
| the required answer combines models whose shared quantities, representations or scales differ. | `references/MMP.18.md` |
| component equations describe a physical system in several modes, but changing the active constraints leaves the next computation undefined … | `references/MMP.20.md` |
| materially different ways of ordering, combining or allocating method contributions are plausible, and their interaction can change the rece … | `references/MMP.21.md` |
| a mathematical transformation suggests a different way of doing recurring work. | `references/MMP.22.md` |

## Publication units

Non-pattern sections of the framework, reproduced as reference cards:

- `references/MMP.Reference.md` — Architectural Reference

## Navigation rule

Start from the working difficulty, not file order. Follow each card's `Governing patterns` line and frontmatter `dependencies` when a needed result is missing.

## Single surface

`references/` is the canonical surface. `SKILL.md` is routing-only; there is no monolith to read. `INDEX.md` is reference-only.

## Lookup rules

- **Index first, then "no".** Check `references/INDEX.md` before searching. If an id is not listed there, the pattern does not exist — answer "no" and do not open files.
- **Read once.** Do not reopen a card you have already read.
