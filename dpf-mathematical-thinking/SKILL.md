---
name: dpf-mathematical-thinking
description: |
  Mathematical Thinking (MATH) — Use when you need to construct mathematical objects, operations and alternatives; derive consequences and meet proof obligations.
license: CC-BY-4.0
---

# DPF: Mathematical Thinking (MATH)

**Depends on:** `fpf-core`
**Bounded context:** A pattern language for constructing mathematical objects, operations and arguments, using their results, and developing the next useful question.
**Source of truth:** `references/` — a source-faithful decomposition of *Mathematical Thinking DPF* (see `NOTICE.md` for the source/edition citation).
**Readiness mode:** `source-faithful` — full bodies reproduced from an approved source; no card has passed a heterogeneous-case evaluation (`E.21`). `status` on each card is the source's own status.

## When to load which pattern

| Situation | Load |
|---|---|
| you need a mathematical object but have not decided how to construct it. | `references/MATH.16.md` |
| the rule for constructing or transforming something has itself become the object of work. | `references/MATH.17.md` |
| you know elementary steps and their permitted connections, but still need mathematical objects for their finite combinations. | `references/MATH.1.md` |
| you want to treat several mathematical objects as one because a working question appears not to distinguish them. | `references/MATH.2.md` |
| you know what the basic elements of a mathematical construction should become and need a compatible map on everything built from them. | `references/MATH.5.md` |
| another representation makes a mathematical construction easier to work with and you need to carry its operations and results across a rever … | `references/MATH.7.md` |
| two mathematical descriptions appear to address the same construction or question but use different objects, primitive operations, relations … | `references/MATH.18.md` |
| you have a mathematical claim to establish and some relevant definitions or results, but no argument connecting them. | `references/MATH.19.md` |
| an input is given as a finite construction from smaller inputs, and you need a way to produce an object with a required property for every s … | `references/MATH.4.md` |
| a mathematical proof says that an object can be obtained, but you still need the operation that obtains it. | `references/MATH.12.md` |
| a proposed mathematical implication might fail and you need a construction that settles the failure. | `references/MATH.6.md` |
| obtaining a mathematical value or object is difficult, but a justified comparison could already answer the receiving question. | `references/MATH.20.md` |
| a mathematical construction can take many steps and you need a relation that survives every allowed step. | `references/MATH.11.md` |
| a transformation appears to preserve the structure relevant to a problem, and you need to turn that observation into a useful restriction, a … | `references/MATH.13.md` |
| a mathematical solution is known and transformations that preserve its defining conditions can produce further useful solutions. | `references/MATH.8.md` |
| a mathematical rule must choose an answer and transforming the input should transform that answer in the corresponding way. | `references/MATH.9.md` |
| you have a candidate allocation, shape, history or other mathematical construction under constraints, and need to find an improving change o … | `references/MATH.10.md` |
| a number, function, infinite structure or other mathematical object is to be obtained from increasingly informative constructions, and the w … | `references/MATH.21.md` |
| a mathematical assumption excludes a construction you need, a theorem uses a stronger premise than its intended application supplies, or two … | `references/MATH.22.md` |
| a mathematical construction works in some cases, fails after a change, or reveals a relation that could support a new theorem. | `references/MATH.23.md` |

## Publication units

Non-pattern sections of the framework, reproduced as reference cards:

- `references/MATH.Reference.md` — Architectural Reference

## Navigation rule

Start from the working difficulty, not file order. Follow each card's `Governing patterns` line and frontmatter `dependencies` when a needed result is missing.

## Single surface

`references/` is the canonical surface. `SKILL.md` is routing-only; there is no monolith to read. `INDEX.md` is reference-only.

## Lookup rules

- **Index first, then "no".** Check `references/INDEX.md` before searching. If an id is not listed there, the pattern does not exist — answer "no" and do not open files.
- **Read once.** Do not reopen a card you have already read.
