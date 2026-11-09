---
name: dpf-physical-thinking
description: |
  Physical Thinking (PHY) — Use when you need to construct and test physical accounts; select interactions and idealizations, derive consequences and distinguish them by observation.
license: CC-BY-4.0
---

# DPF: Physical Thinking (PHY)

**Depends on:** `fpf-core`
**Bounded context:** A pattern language for forming physical accounts, deriving usable consequences, constructing observations and revising the physical assumptions.
**Source of truth:** `references/` — a source-faithful decomposition of *Physical Thinking DPF* (see `NOTICE.md` for the source/edition citation).
**Readiness mode:** `source-faithful` — full bodies reproduced from an approved source; no card has passed a heterogeneous-case evaluation (`E.21`). `status` on each card is the source's own status.

## When to load which pattern

| Situation | Load |
|---|---|
| an observed or proposed physical effect needs an account, but the interaction law is not supplied. | `references/PHY.4.md` |
| a physical question leaves you uncertain which motions, interactions or material details its description must retain. | `references/PHY.5.md` |
| you can identify physical participants and their interactions, but cannot yet say how their coupled situation will evolve. | `references/PHY.6.md` |
| you need to derive physical evolution from a principle that compares possible histories. | `references/PHY.7.md` |
| you need to explain or predict collective physical behavior from possible microscopic states or histories. | `references/PHY.8.md` |
| you want to learn about a physical situation through another arrangement, but changing its size, material, speed or surroundings changes the … | `references/PHY.1.md` |
| you want to understand or investigate a physical situation through another arrangement, and the needed analogue must be built or changed. | `references/PHY.2.md` |
| a physical difference matters to the work, but the available arrangement does not make that difference observable. | `references/PHY.9.md` |
| competing physical accounts remain compatible with what has been observed, and the work needs a distinction between them. | `references/PHY.10.md` |
| you need to determine what a physical process or device could accomplish before choosing its detailed mechanism, or when a familiar physical … | `references/PHY.3.md` |

## Publication units

Non-pattern sections of the framework, reproduced as reference cards:

- `references/PHY.Reference.md` — Architectural Reference

## Navigation rule

Start from the working difficulty, not file order. Follow each card's `Governing patterns` line and frontmatter `dependencies` when a needed result is missing.

## Single surface

`references/` is the canonical surface. `SKILL.md` is routing-only; there is no monolith to read. `INDEX.md` is reference-only.

## Lookup rules

- **Index first, then "no".** Check `references/INDEX.md` before searching. If an id is not listed there, the pattern does not exist — answer "no" and do not open files.
- **Read once.** Do not reopen a card you have already read.
