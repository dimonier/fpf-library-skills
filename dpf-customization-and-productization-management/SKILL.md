---
name: dpf-customization-and-productization-management
description: |
  Customization and Productization Management (CUST) — Use when you need to handle client differences while developing repeatable offerings, delivery and compatible transitions for existing clients.
license: CC-BY-4.0
---

# DPF: Customization and Productization Management (CUST)

**Depends on:** `fpf-core`
**Bounded context:** Make customer-specific results and repeatable offerings supportable together.
**Source of truth:** `references/` — a source-faithful decomposition of *Customization and Productization Management Principles Framework* (see `NOTICE.md` for the source/edition citation).
**Readiness mode:** `source-faithful` — full bodies reproduced from an approved source; no card has passed a heterogeneous-case evaluation (`E.21`). `status` on each card is the source's own status.

## When to load which pattern

| Situation | Load |
|---|---|
| Use this method when a customer difference affects both a particular result and the offering you expect to provide again. | `references/CUST.1.md` |
| Use this method when “the customer needs customization” conceals several different changes, or when a completed deployment contains unexplai … | `references/CUST.2.md` |
| Use this method when several local solutions suggest a common contribution, when a current family has accumulated exceptions, or when a new … | `references/CUST.3.md` |
| Use this method when a supported family offers meaningful choices, but selecting a valid configuration or arranging customer-specific work r … | `references/CUST.4.md` |
| Use this method when work in a customer setting can resolve an uncertainty that matters to local delivery and to a possible shared contribut … | `references/CUST.5.md` |
| Use this method when a successful deployment or service should become obtainable by another prepared performer, but repetition still depends … | `references/CUST.6.md` |
| Use this method when a customization, common contribution or provider change is justified by growth, repeatability or economics, but the ful … | `references/CUST.7.md` |
| Use this method when an offering-family change affects customers, recipients, partners or performers who already rely on its meaning, behavi … | `references/CUST.8.md` |

## Publication units

Non-pattern sections of the framework, reproduced as reference cards:

- `references/CUST.Reference.md` — Architectural Reference
- `references/CUST.Reminder.md` — Publication unit

## Navigation rule

Start from the working difficulty, not file order. Follow each card's `Governing patterns` line and frontmatter `dependencies` when a needed result is missing.

## Single surface

`references/` is the canonical surface. `SKILL.md` is routing-only; there is no monolith to read. `INDEX.md` is reference-only.

## Lookup rules

- **Index first, then "no".** Check `references/INDEX.md` before searching. If an id is not listed there, the pattern does not exist — answer "no" and do not open files.
- **Read once.** Do not reopen a card you have already read.
