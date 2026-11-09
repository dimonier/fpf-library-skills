---
name: dpf-notational-engineering
description: |
  Notational Engineering (NOT) — Use when you need to design expressions, interpretations and transformations that make operations usable and changes recoverable.
license: CC-BY-4.0
---

# DPF: Notational Engineering (NOT)

**Depends on:** `fpf-core`
**Bounded context:** A pattern language for designing expressions that people and computational agents can interpret, manipulate, translate and use together.
**Source of truth:** `references/` — a source-faithful decomposition of *Notational Engineering DPF* (see `NOTICE.md` for the source/edition citation).
**Readiness mode:** `source-faithful` — full bodies reproduced from an approved source; no card has passed a heterogeneous-case evaluation (`E.21`). `status` on each card is the source's own status.

## When to load which pattern

| Situation | Load |
|---|---|
| you are choosing or designing a notation and cannot yet say what its users must be able to express, recognize or do with an expression. | `references/NOT.1.md` |
| a notation needs rules for combining expressions or referring to their parts, and the proposed marks leave those rules unclear. | `references/NOT.2.md` |
| a notation can form expressions, but its users lack a clear way to obtain the consequence those expressions are supposed to support. | `references/NOT.3.md` |
| an expression is difficult to read, derive from or change, and you need a rule for turning it into a more useful expression without losing t … | `references/NOT.4.md` |
| work must continue in another notation and you need to construct or repair the translation. | `references/NOT.5.md` |
| different representations support different parts of the work, but a reader cannot reliably combine their results or carry a change between … | `references/NOT.6.md` |
| a notation can express the required content, yet reading or changing that content is unnecessarily difficult. | `references/NOT.7.md` |
| a notation carries important distinctions through timing, sound, gesture or bodily position, and recognizing its individual signs does not y … | `references/NOT.8.md` |

## Publication units

Non-pattern sections of the framework, reproduced as reference cards:

- `references/NOT.Reference.md` — Architectural Reference

## Navigation rule

Start from the working difficulty, not file order. Follow each card's `Governing patterns` line and frontmatter `dependencies` when a needed result is missing.

## Single surface

`references/` is the canonical surface. `SKILL.md` is routing-only; there is no monolith to read. `INDEX.md` is reference-only.

## Lookup rules

- **Index first, then "no".** Check `references/INDEX.md` before searching. If an id is not listed there, the pattern does not exist — answer "no" and do not open files.
- **Read once.** Do not reopen a card you have already read.
