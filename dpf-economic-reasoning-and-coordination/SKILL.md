---
name: dpf-economic-reasoning-and-coordination
description: |
  Economic Reasoning and Coordination (ECO) — Use when you need to reason about exchange, commitments, incentives, shared resources and coordination under changing information and demand.
license: CC-BY-4.0
---

# DPF: Economic Reasoning and Coordination (ECO)

**Depends on:** `fpf-core`
**Bounded context:** A pattern language for connecting different plans and knowledge with scarce means through calculation, exchange, commitments and economic arrangements.
**Source of truth:** `references/` — a source-faithful decomposition of *Economic Reasoning and Coordination Principles Framework* (see `NOTICE.md` for the source/edition citation).
**Readiness mode:** `source-faithful` — full bodies reproduced from an approved source; no card has passed a heterogeneous-case evaluation (`E.21`). `status` on each card is the source's own status.

## When to load which pattern

| Situation | Load |
|---|---|
| a calculation ranks production or service plans but you cannot tell whether its prices and other weights represent exchanges and resource us … | `references/ECO.1.md` |
| a changed price or offer can alter how you use, substitute or supply a resource. Begin by identifying the exchange whose terms changed. | `references/ECO.2.md` |
| a need, available resource or possible combination is visible, but the parties' current plans do not yet connect through a workable exchange … | `references/ECO.3.md` |
| a worthwhile proposal cannot proceed because the necessary customers, suppliers, performers or funders each depend on another party committi … | `references/ECO.4.md` |
| an exchange depends on quality, circumstances or future action that one party knows or controls and another cannot cheaply observe or verify … | `references/ECO.5.md` |
| investment, location, integration or acquired know-how makes a trading relationship difficult to leave, and future changes cannot all be agr … | `references/ECO.6.md` |
| several parties depend on a resource whose useful condition is undermined by their separate uses or by insufficient contribution to its upke … | `references/ECO.7.md` |
| a plan or rule works among closely cooperating participants but fails when carried into wider exchange, or when commercial terms undermine t … | `references/ECO.8.md` |
| a change to a rule for access, exchange, contribution or adaptation is being considered, but it is unclear what useful coordination would be … | `references/ECO.9.md` |
| a method or technology uses less of a resource per useful result and you need to know whether total resource use will also fall. | `references/ECO.10.md` |

## Publication units

Non-pattern sections of the framework, reproduced as reference cards:

- `references/ECO.Reference.md` — Architectural Reference

## Navigation rule

Start from the working difficulty, not file order. Follow each card's `Governing patterns` line and frontmatter `dependencies` when a needed result is missing.

## Single surface

`references/` is the canonical surface. `SKILL.md` is routing-only; there is no monolith to read. `INDEX.md` is reference-only.

## Lookup rules

- **Index first, then "no".** Check `references/INDEX.md` before searching. If an id is not listed there, the pattern does not exist — answer "no" and do not open files.
- **Read once.** Do not reopen a card you have already read.
