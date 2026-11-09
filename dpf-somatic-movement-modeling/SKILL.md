---
name: dpf-somatic-movement-modeling
description: |
  Somatic Movement Modeling (SOM) — Use when you need to connect bodily experience, regulated effort and coordinated movement; adapt within a familiar movement practice as support or load changes.
license: CC-BY-4.0
---

# DPF: Somatic Movement Modeling (SOM)

**Depends on:** `fpf-core`
**Bounded context:** A pattern language for understanding, learning and changing the bodily contribution to a skilled human movement.
**Source of truth:** `references/` — a source-faithful decomposition of *Somatic Movement Modeling DPF* (see `NOTICE.md` for the source/edition citation).
**Readiness mode:** `source-faithful` — full bodies reproduced from an approved source; no card has passed a heterogeneous-case evaluation (`E.21`). `status` on each card is the source's own status.

## When to load which pattern

| Situation | Load |
|---|---|
| a movement instruction names a visible result but leaves you unable to decide what to change in your own bodily action, or when a familiar b … | `references/SOM.1.md` |
| a bodily instruction cannot guide action because the performer cannot distinguish the location, direction or developing change it names. | `references/SOM.2.md` |
| a performer can distinguish a task-relevant bodily change but cannot increase, reduce or release it with the control the movement requires. | `references/SOM.3.md` |
| bodily changes are separately available, but reconstructing them one by one interrupts the movement that needs them together. | `references/SOM.4.md` |
| a bodily coordination works under one support or load relation but fails as that relation changes. | `references/SOM.5.md` |

## Publication units

Non-pattern sections of the framework, reproduced as reference cards:

- `references/SOM.Reference.md` — Architectural Reference

## Navigation rule

Start from the working difficulty, not file order. Follow each card's `Governing patterns` line and frontmatter `dependencies` when a needed result is missing.

## Single surface

`references/` is the canonical surface. `SKILL.md` is routing-only; there is no monolith to read. `INDEX.md` is reference-only.

## Lookup rules

- **Index first, then "no".** Check `references/INDEX.md` before searching. If an id is not listed there, the pattern does not exist — answer "no" and do not open files.
- **Read once.** Do not reopen a card you have already read.
