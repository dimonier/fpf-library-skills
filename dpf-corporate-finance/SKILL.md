---
name: dpf-corporate-finance
description: |
  Corporate Finance (FIN) — Use when you need to understand financial relations, construct financing terms and group arrangements, and compare value, liquidity, capital uses and exposure.
license: CC-BY-4.0
---

# DPF: Corporate Finance (FIN)

**Depends on:** `fpf-core`
**Bounded context:** The financial relations of corporate activity and methods for valuing investments, constructing financing, preserving liquidity, managing exposure and changing financial arrangements.
**Source of truth:** `references/` — a source-faithful decomposition of *Corporate Finance Principles Framework* (see `NOTICE.md` for the source/edition citation).
**Readiness mode:** `source-faithful` — full bodies reproduced from an approved source; no card has passed a heterogeneous-case evaluation (`E.21`). `status` on each card is the source's own status.

## When to load which pattern

| Situation | Load |
|---|---|
| Corporate finance includes value, financing, liquidity, risk and distributions. | `references/FIN.1.md` |
| The treasurer or analyst is preparing a liquidity account for a named paying entity, currency and horizon. | `references/FIN.2.md` |
| The working object is an arrangement governing inventory and trade-related receipts and payments. | `references/FIN.3.md` |
| The analyst prepares a decision-specific financial projection from reporting, operating and financial-position inputs. | `references/FIN.4.md` |
| The analyst estimates the return capital providers require for the claim being valued and identifies relevant financing constraints. | `references/FIN.5.md` |
| The analyst values a specified project alternative against a feasible baseline. | `references/FIN.6.md` |
| An income valuation requires familiarity with present value and required returns; market and asset approaches require comparable or asset-va … | `references/FIN.7.md` |
| The valuation requires familiarity with present value and payoffs that depend on later events or choices. | `references/FIN.8.md` |
| The object is a capital-use choice or combination for a named corporation. | `references/FIN.9.md` |
| Calculating an effective financing rate requires familiarity with compounding and discounting timed payments. | `references/FIN.10.md` |
| The object is a financing mix for the corporation or a specified financing need. | `references/FIN.11.md` |
| The object is the corporation's compliance and usable financing capacity under specified terms and dates. | `references/FIN.12.md` |
| The object is a retention or distribution choice for a named corporation and ownership interests. | `references/FIN.21.md` |
| Discounting recoveries to a common date requires familiarity with present value and risk-adjusted required returns. | `references/FIN.22.md` |
| The object is the financial arrangement among specified existing or proposed entities and external providers: where capital enters, which en … | `references/FIN.23.md` |
| The object is the sensitivity of specified corporate value, cash or claims to financial changes over a chosen horizon. | `references/FIN.13.md` |
| The object is a protection arrangement for a specified exposure. It can change the underlying activity, use a natural offset, or introduce a … | `references/FIN.14.md` |
| The object is a treasury action and the resulting financial position at its effective time. | `references/FIN.15.md` |
| The object is a financial recommendation for a specified receiving decision. A memo, conversation or dashboard can carry it. | `references/FIN.16.md` |
| The object is a financial model, projection or conclusion together with the grounds on which someone relies on it. | `references/FIN.17.md` |
| The object is the choice or improvement of a corporate-finance method for a stated use. | `references/FIN.18.md` |
| The object is the organization of simultaneous corporate-finance practice around actual claims, decisions and horizons. | `references/FIN.19.md` |
| The object is the continuation or change of finance practices across a named population and period. | `references/FIN.20.md` |

## Publication units

Non-pattern sections of the framework, reproduced as reference cards:

- `references/FIN.Reference.md` — Architectural Reference
- `references/FIN.Sources.md` — Source arguments and refresh

## Navigation rule

Start from the working difficulty, not file order. Follow each card's `Governing patterns` line and frontmatter `dependencies` when a needed result is missing.

## Single surface

`references/` is the canonical surface. `SKILL.md` is routing-only; there is no monolith to read. `INDEX.md` is reference-only.

## Lookup rules

- **Index first, then "no".** Check `references/INDEX.md` before searching. If an id is not listed there, the pattern does not exist — answer "no" and do not open files.
- **Read once.** Do not reopen a card you have already read.
