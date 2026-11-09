---
name: dpf-defense-and-transmission-modeling
description: |
  Defense and Transmission Modeling (DTM) — Use when you need to explain how practices persist and spread, how they help or impair work, and how protective action changes those outcomes.
license: CC-BY-4.0
---

# DPF: Defense and Transmission Modeling (DTM)

**Depends on:** `fpf-core`
**Bounded context:** A pattern language for explaining how practices continue and spread, how they help or impair work, and how protective action changes those outcomes.
**Source of truth:** `references/` — a source-faithful decomposition of *Defense and Transmission Modeling DPF* (see `NOTICE.md` for the source/edition citation).
**Readiness mode:** `source-faithful` — full bodies reproduced from an approved source; no card has passed a heterogeneous-case evaluation (`E.21`). `status` on each card is the source's own status.

## When to load which pattern

| Situation | Load |
|---|---|
| a spreading practice, component or tool relies on other participants' resources and someone concludes that this dependence makes it harmful— … | `references/DTM.1.md` |
| a model predicts the spread of a way of working from contacts, messages or downloads, yet these events do not reliably produce use. | `references/DTM.2.md` |
| a practice changes its participants, and those changes affect whether, what or how they pass it on—or when wider adoption changes the condit … | `references/DTM.3.md` |
| early growth, a fitted trend or a single threshold is being used to claim that a practice will establish itself, disappear, or return after … | `references/DTM.4.md` |
| a variant becomes more common within each participating group, yet its overall prevalence changes differently—or when a claimed advantage of … | `references/DTM.5.md` |
| a method spreads, persists or works differently in the presence of another variant, and treating the two independently would change the deci … | `references/DTM.6.md` |
| a shared arrangement keeps granting access, attention, resources or further use, yet the resulting activity fails the work it was meant to s … | `references/DTM.7.md` |
| several proposed protective actions promise a similar improvement but act on different parts of a continuing or spreading practice. | `references/DTM.8.md` |
| a protective response depends on the activity it encounters and, in turn, changes that activity, useful work or subsequent transmission. | `references/DTM.9.md` |

## Publication units

Non-pattern sections of the framework, reproduced as reference cards:

- `references/DTM.Reference.md` — Architectural Reference

## Navigation rule

Start from the working difficulty, not file order. Follow each card's `Governing patterns` line and frontmatter `dependencies` when a needed result is missing.

## Single surface

`references/` is the canonical surface. `SKILL.md` is routing-only; there is no monolith to read. `INDEX.md` is reference-only.

## Lookup rules

- **Index first, then "no".** Check `references/INDEX.md` before searching. If an id is not listed there, the pattern does not exist — answer "no" and do not open files.
- **Read once.** Do not reopen a card you have already read.
