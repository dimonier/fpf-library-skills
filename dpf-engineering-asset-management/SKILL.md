---
name: dpf-engineering-asset-management
description: |
  Engineering Asset Management (EAM) — Use when you need to compare use, renewal, replacement and other asset changes over time, including shared risk, cost and capacity.
license: CC-BY-4.0
---

# DPF: Engineering Asset Management (EAM)

**Depends on:** `fpf-core`
**Bounded context:** A domain pattern language for making and revising value-oriented decisions about engineered assets over their lives, for one asset, an interacting asset System or a portfolio.
**Source of truth:** `references/` — a source-faithful decomposition of *Engineering Asset Management Principles Framework* (see `NOTICE.md` for the source/edition citation).
**Readiness mode:** `source-faithful` — full bodies reproduced from an approved source; no card has passed a heterogeneous-case evaluation (`E.21`). `status` on each card is the source's own status.

## When to load which pattern

| Situation | Load |
|---|---|
| an asset decision lacks a clear service or value question. A pump has become expensive to maintain, an asset register has been completed, or … | `references/EAM.1.md` |
| a desired outcome has been translated directly into an asset purchase or renewal, or when an existing asset's continuing contribution is unc … | `references/EAM.2.md` |
| a choice depends on matching asset, condition, cost and intervention records. | `references/EAM.3.md` |
| an asset choice depends on how much service will be needed, where and when. | `references/EAM.4.md` |
| condition observations or service performance can change an asset decision. | `references/EAM.5.md` |
| an asset option must meet demand through a particular arrangement, outage or disruption. | `references/EAM.6.md` |
| a needed service contribution has become a proposal to acquire or modify an asset. | `references/EAM.7.md` |
| an engineered asset's future use is in question: retain it with maintenance, renew it, replace it, repurpose it or withdraw it. | `references/EAM.8.md` |
| a proposed asset choice must satisfy different technical, service, financial or operating conditions, or when individually reasonable decisi … | `references/EAM.9.md` |
| asset choices compete for shared funding, service, people, outages or other resources. | `references/EAM.10.md` |
| the timing of an asset intervention can change whether the service or portfolio plan is feasible. | `references/EAM.11.md` |
| an asset recommendation or decision must combine specialist answers. Finance reports affordability, maintenance recommends an intervention a … | `references/EAM.12.md` |
| observations can change an asset plan or the explanation for its results. | `references/EAM.13.md` |
| the arrangement performing asset management repeatedly prevents useful decisions: information is joined incorrectly, responsibility is uncle … | `references/EAM.14.md` |
| the reusable way of making asset decisions no longer answers current questions, or when a new technique could improve it. | `references/EAM.15.md` |
| the question concerns how a bounded population generates, transmits, uses, recognizes, selects, retains or loses an asset-management practic … | `references/EAM.16.md` |

## Publication units

Non-pattern sections of the framework, reproduced as reference cards:

- `references/EAM.Reference.md` — Architectural Reference
- `references/EAM.Application.md` — Worked cases / cross-pattern applications
- `references/EAM.Sources.md` — Source arguments and refresh

## Navigation rule

Start from the working difficulty, not file order. Follow each card's `Governing patterns` line and frontmatter `dependencies` when a needed result is missing.

## Single surface

`references/` is the canonical surface. `SKILL.md` is routing-only; there is no monolith to read. `INDEX.md` is reference-only.

## Lookup rules

- **Index first, then "no".** Check `references/INDEX.md` before searching. If an id is not listed there, the pattern does not exist — answer "no" and do not open files.
- **Read once.** Do not reopen a card you have already read.
