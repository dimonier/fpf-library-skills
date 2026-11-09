---
name: dpf-management-accounting
description: |
  Management Accounting (MA) — Use when you need to explain costs, capacity and economic consequences; forecast outcomes; develop activity designs from economic requirements and arrange how accounting information is used.
license: CC-BY-4.0
---

# DPF: Management Accounting (MA)

**Depends on:** `fpf-core`
**Bounded context:** Management Accounting develops and uses economic knowledge of an organization's activity: what its results require, whom its resource use and commitments affect, and how different arrangements can sustain the intended work. It helps a controller, accountant or manager explain what happened, anticipate consequences, construct economically supportable changes, and arrange the use of information in decisions. A small account can be sufficient. A cost ceiling defines a condition; participants still need a feasible way of doing the work.
**Source of truth:** `references/` — a source-faithful decomposition of *Management Accounting Principles Framework* (see `NOTICE.md` for the source/edition citation).
**Readiness mode:** `source-faithful` — full bodies reproduced from an approved source; no card has passed a heterogeneous-case evaluation (`E.21`). `status` on each card is the source's own status.

## When to load which pattern

| Situation | Load |
|---|---|
| A service can use a machine, qualified staff, consumables and a supplier's processing service to deliver one accepted result. | `references/MA.1.md` |
| A team pays for a resource arrangement that supplies capability over time. | `references/MA.2.md` |
| A shared resource supports several recipients. Some consumption can be traced to a recipient; some sustains the group or cannot be separated … | `references/MA.3.md` |
| Production, sale, recognition of an expense and payment can occur at different times. | `references/MA.4.md` |
| An operation needs to anticipate demand, material use, capacity and payment timing. | `references/MA.5.md` |
| A team may expect demand of 100, aspire to serve 120 and seek resources adequate for 130 under a higher-demand scenario. | `references/MA.6.md` |
| A period's material cost can rise because more units were produced, the mix changed, more material was consumed per accepted unit or the pri … | `references/MA.7.md` |
| A service can earn a positive margin from an active customer this month while still failing to recover acquisition spending. | `references/MA.8.md` |
| People act within measurement and decision arrangements. A lower reported unit cost can earn approval while consuming more cash and producin … | `references/MA.9.md` |
| A team knows the result it wants to deliver and what it can charge, spend or commit. Its current design misses that condition. | `references/MA.10.md` |

## Publication units

Non-pattern sections of the framework, reproduced as reference cards:

- `references/MA.Reference.md` — Architectural Reference
- `references/MA.Sources.md` — Source arguments and refresh

## Navigation rule

Start from the working difficulty, not file order. Follow each card's `Governing patterns` line and frontmatter `dependencies` when a needed result is missing.

## Single surface

`references/` is the canonical surface. `SKILL.md` is routing-only; there is no monolith to read. `INDEX.md` is reference-only.

## Lookup rules

- **Index first, then "no".** Check `references/INDEX.md` before searching. If an id is not listed there, the pattern does not exist — answer "no" and do not open files.
- **Read once.** Do not reopen a card you have already read.
