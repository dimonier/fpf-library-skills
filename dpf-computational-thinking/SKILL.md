---
name: dpf-computational-thinking
description: |
  Computational Thinking (CMP) — Use when you need to construct algorithms that obtain the required answer within correctness, resource and interaction conditions.
license: CC-BY-4.0
---

# DPF: Computational Thinking (CMP)

**Depends on:** `fpf-core`
**Bounded context:** A pattern language for constructing, understanding, analyzing and transforming algorithms, including their interpretation and interaction.
**Source of truth:** `references/` — a source-faithful decomposition of *Computational Thinking DPF* (see `NOTICE.md` for the source/edition citation).
**Readiness mode:** `source-faithful` — full bodies reproduced from an approved source; no card has passed a heterogeneous-case evaluation (`E.21`). `status` on each card is the source's own status.

## When to load which pattern

| Situation | Load |
|---|---|
| an unfamiliar computational problem might be solved through another problem, or when you need to determine what an assumed solver would make … | `references/CMP.1.md` |
| you can state the answer required from a finite input, but a procedure for obtaining it is missing or unaffordable. | `references/CMP.2.md` |
| a procedure repeatedly obtains the same intermediate answer, or retains so many intermediate values that it cannot finish within the availab … | `references/CMP.3.md` |
| an answer must be constructed by choosing among alternatives, direct enumeration is too costly, and information about a partial choice can e … | `references/CMP.4.md` |
| an optimization problem is difficult to solve directly, but weakening some of its restrictions or costs gives a more accessible problem. | `references/CMP.5.md` |
| a desired result is hard to construct directly, but the current candidate reveals a computable improvement: a beneficial local replacement … | `references/CMP.6.md` |
| examples or feedback are available and the required rule for further cases is missing, or an existing learning procedure must be changed for … | `references/CMP.7.md` |
| computing the requested answer without approximation is unavailable or too expensive, and a cheaper computation can retain enough informatio … | `references/CMP.8.md` |
| a computation needs a sample from a specified law, or an estimate that would be expensive to obtain by enumeration, and the sampling or esti … | `references/CMP.9.md` |
| a computation spends too much effort finding, updating, combining or storing information, and changing its representation could improve thos … | `references/CMP.10.md` |
| repeated attempts to accelerate a computation leave a question about what any algorithm could achieve under the available access. | `references/CMP.11.md` |
| a calculation, rule language or program description has an intended meaning, but an effective way to execute it is missing, too costly or mu … | `references/CMP.12.md` |
| computing every relevant state or execution is unaffordable, but the question needs only some of their properties. | `references/CMP.13.md` |
| computations that work separately must run together, but shared state, communication or scheduling can change their results. | `references/CMP.14.md` |
| different contributors must add new forms of data and new operations on those forms without repeatedly changing one another's modules. | `references/CMP.15.md` |
| you can state behavior that a computation must obtain, but the available units and operations do not yet give a workable way to obtain it. | `references/CMP.16.md` |

## Publication units

Non-pattern sections of the framework, reproduced as reference cards:

- `references/CMP.Reference.md` — Architectural Reference

## Navigation rule

Start from the working difficulty, not file order. Follow each card's `Governing patterns` line and frontmatter `dependencies` when a needed result is missing.

## Single surface

`references/` is the canonical surface. `SKILL.md` is routing-only; there is no monolith to read. `INDEX.md` is reference-only.

## Lookup rules

- **Index first, then "no".** Check `references/INDEX.md` before searching. If an id is not listed there, the pattern does not exist — answer "no" and do not open files.
- **Read once.** Do not reopen a card you have already read.
