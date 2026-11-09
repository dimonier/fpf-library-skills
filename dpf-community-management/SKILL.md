---
name: dpf-community-management
description: |
  Community Management (CB) — Use when you need to develop useful participation, relationships, shared practices and contributions in organizations or voluntary communities.
license: CC-BY-4.0
---

# DPF: Community Management (CB)

**Depends on:** `fpf-core`
**Bounded context:** Develop useful participation, relationships, shared practices and contributions in organizations or voluntary communities.
**Source of truth:** `references/` — a source-faithful decomposition of *Community Management Principles Framework* (see `NOTICE.md` for the source/edition citation).
**Readiness mode:** `source-faithful` — full bodies reproduced from an approved source; no card has passed a heterogeneous-case evaluation (`E.21`). `status` on each card is the source's own status.

## When to load which pattern

| Situation | Load |
|---|---|
| you want to help a practice spread, enable people to help one another, or create a place where a particular group can participate meaningful … | `references/CB.1.md` |
| a group could benefit from mutual help or shared activity, but people have not yet found a workable way to participate together. | `references/CB.2.md` |
| a person wants to enter, return to, or change their participation in a community, but the next useful action or its conditions are unclear. | `references/CB.3.md` |
| people have a worthwhile reason to interact, but the setting or activity does not yet let them do the relevant work together. | `references/CB.4.md` |
| a community has a real question or piece of work that participants could help with, but useful contributions are not yet reaching a recipien … | `references/CB.5.md` |
| someone has made a useful contribution but cannot see what it helped, or when an organiser must choose how to acknowledge it. | `references/CB.6.md` |
| useful participation depends on one organiser, when capable organisers cannot attend to several emerging needs at once, when a local group n … | `references/CB.7.md` |
| participants cannot tell what conduct is expected, when different organisers apply a rule differently, or when an incident requires a respon … | `references/CB.8.md` |
| a useful community activity depends on contributions that have not been secured, when organisers are carrying work beyond what they agreed … | `references/CB.9.md` |
| people need to decide whether a cultural or community arrangement is useful, what to change, or what support to continue, and visible activi … | `references/CB.10.md` |
| the purpose, people or support of a cultural or community arrangement changes enough that its continuation needs a decision. | `references/CB.11.md` |
| a person wants to repeat a useful action of participation, but the intended action does not reliably happen in the situations where it would … | `references/CB.12.md` |
| people need decisions about a common activity but have not established who may make them, or when the mandate of an existing decision-maker … | `references/CB.13.md` |
| practitioners repeatedly encounter a difficulty that their ordinary exchanges do not resolve, useful ways of working remain scattered among … | `references/CB.14.md` |
| a practical result depends on people from different communities understanding and using one another's contribution. | `references/CB.15.md` |
| a community needs to contribute to a decision that affects its practice, but individual comments do not adequately carry the shared concern. … | `references/CB.16.md` |

## Publication units

Non-pattern sections of the framework, reproduced as reference cards:

- `references/CB.Reference.md` — Architectural Reference
- `references/CB.Application.md` — Worked cases / cross-pattern applications
- `references/CB.Sources.md` — Source arguments and refresh
- `references/CB.Edition.md` — Edition and reuse

## Navigation rule

Start from the working difficulty, not file order. Follow each card's `Governing patterns` line and frontmatter `dependencies` when a needed result is missing.

## Single surface

`references/` is the canonical surface. `SKILL.md` is routing-only; there is no monolith to read. `INDEX.md` is reference-only.

## Lookup rules

- **Index first, then "no".** Check `references/INDEX.md` before searching. If an id is not listed there, the pattern does not exist — answer "no" and do not open files.
- **Read once.** Do not reopen a card you have already read.
