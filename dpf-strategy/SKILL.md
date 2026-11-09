---
name: dpf-strategy
description: |
  Strategy (STR) — Use when you need to find a worthwhile direction; compare options, capabilities, investments and business models; revise commitments when conditions change.
license: CC-BY-4.0
---

# DPF: Strategy (STR)

**Depends on:** `fpf-core`
**Bounded context:** Find a worthwhile direction; compare options, capabilities, investments and business models; revise commitments when conditions change.
**Source of truth:** `references/` — a source-faithful decomposition of *Strategy Principles Framework* (see `NOTICE.md` for the source/edition citation).
**Readiness mode:** `source-faithful` — full bodies reproduced from an approved source; no card has passed a heterogeneous-case evaluation (`E.21`). `status` on each card is the source's own status.

## When to load which pattern

| Situation | Load |
|---|---|
| plausible answers about a worthwhile contribution, its obtaining way, available means and commitments do not yet form a defensible strategic … | `references/STR.18.md` |
| a request such as “respond to AI”, “find a growth strategy”, or “develop the organization” leaves people working on different decisions. | `references/STR.1.md` |
| a price, customer behaviour, capability, constraint, strategic objective or relied-on source has changed and someone asks, “Does this change … | `references/STR.2.md` |
| participants disagree about what a strategic change means, or when “we need a new strategy” has not yet become a question that can guide a c … | `references/STR.3.md` |
| a strategic choice depends on future conditions that one forecast cannot responsibly settle. | `references/STR.4.md` |
| the current direction no longer answers the strategic concern, when promising ideas do not yet express different contributions, or when some … | `references/STR.5.md` |
| a strategic direction is clear enough to explore but no credible way of obtaining its contribution is yet known, when the available list mix … | `references/STR.6.md` |
| a consequential strategic question remains and someone proposes a trial, pilot or experiment to answer it. | `references/STR.7.md` |
| a promising direction depends on an ability, partner, platform or initiative that nobody has yet connected to an obtainable result. | `references/STR.8.md` |
| a preferred strategic option depends on uncertain conditions, or when keeping a later choice open is part of its attraction. | `references/STR.9.md` |
| a strategic option looks attractive but its actual obligations, displaced work or consequences for others remain unclear. | `references/STR.10.md` |
| the strategic comparison is sufficient for a choice, but the proposed decision does not yet say what has been selected and what anyone is ac … | `references/STR.11.md` |
| a material observation may change a strategic assumption, comparison, selection rule or commitment, or when a chosen commitment lacks a feas … | `references/STR.12.md` |
| a strategic practitioner must choose, retain, adapt or retire a way of doing strategic work, or when later users cannot recover which method … | `references/STR.13.md` |
| individually plausible strategic commitments cannot coexist because current service, exploration, capability development, enabling means or … | `references/STR.14.md` |
| a strategic-practice variant is being transmitted, enacted, recognized, selected, retained or lost, and the present question is what to cont … | `references/STR.15.md` |
| an organization or provider must combine independently justified undertakings and their support, but cannot yet explain which research, prod … | `references/STR.16.md` |
| a strategic question depends on discovering where technology is making different results attainable, but the relevant change is not yet a kn … | `references/STR.17.md` |

## Publication units

Non-pattern sections of the framework, reproduced as reference cards:

- `references/STR.Reference.md` — Architectural Reference
- `references/STR.Application.md` — Worked cases / cross-pattern applications
- `references/STR.Sources.md` — Source arguments and refresh

## Navigation rule

Start from the working difficulty, not file order. Follow each card's `Governing patterns` line and frontmatter `dependencies` when a needed result is missing.

## Single surface

`references/` is the canonical surface. `SKILL.md` is routing-only; there is no monolith to read. `INDEX.md` is reference-only.

## Lookup rules

- **Index first, then "no".** Check `references/INDEX.md` before searching. If an id is not listed there, the pattern does not exist — answer "no" and do not open files.
- **Read once.** Do not reopen a card you have already read.
