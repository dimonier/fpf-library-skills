---
name: dpf-marketing
description: |
  Marketing (MKT) — Use when you need to connect customer inquiry, offers, advertising, acquisition, distribution and use; construct workable provision and revise it from experience.
license: CC-BY-4.0
---

# DPF: Marketing (MKT)

**Depends on:** `fpf-core`
**Bounded context:** Understand a customer's situation, develop an offer that can be delivered, and change commercial work in light of the result.
**Source of truth:** `references/` — a source-faithful decomposition of *Marketing Principles Framework* (see `NOTICE.md` for the source/edition citation).
**Readiness mode:** `source-faithful` — full bodies reproduced from an approved source; no card has passed a heterogeneous-case evaluation (`E.21`). `status` on each card is the source's own status.

## When to load which pattern

| Situation | Load |
|---|---|
| a team must decide whose difficulty to address, which customers can reasonably receive the same offer, or whether an apparent market opportu … | `references/MKT.1.md` |
| people cannot tell what a proposed product or service will do for them, why it is worth considering against their actual alternatives, or wh … | `references/MKT.2.md` |
| a useful offer or invitation is not reaching the people for whom it could matter, when recipients infer a different proposal, or when attent … | `references/MKT.3.md` |
| a person or organisation is considering an offer but cannot yet compare it meaningfully, make an authorised choice, arrange the transition o … | `references/MKT.4.md` |
| the way customers encounter a product or service is inconsistent with the intended relationship or promise, or when several contributors nee … | `references/MKT.5.md` |
| the useful result of a proposed contribution is unclear or contested, or when an acquired product or service is not yet producing that resul … | `references/MKT.6.md` |
| the next useful contribution in a customer relationship is uncertain, an expected continuation does not occur, or a failure requires recover … | `references/MKT.7.md` |
| understanding an activity across several contacts, people or periods could change a marketing decision. | `references/MKT.8.md` |
| a known offer or form of help must be matched to a particular customer's circumstances, or when that comparison reveals that no suitable var … | `references/MKT.9.md` |
| a decision to continue, change, expand or stop marketing work depends on what that work contributes and what it consumes. | `references/MKT.10.md` |
| a customer promise depends on several people, teams or organisations, or when customer evidence reveals a mismatch between a promise and act … | `references/MKT.11.md` |
| a product, offer or customer decision depends on something you do not yet understand about people's work, choice, use or experience. | `references/MKT.12.md` |
| deciding which part of a commercial way of working can be repeated or expanded, and which part still needs discovery, repair or a bounded tr … | `references/MKT.13.md` |
| commercial work with named customer organisations requires a continuing programme: choosing where to invest attention, joining several oppor … | `references/MKT.14.md` |

## Publication units

Non-pattern sections of the framework, reproduced as reference cards:

- `references/MKT.Reference.md` — Architectural Reference
- `references/MKT.Application.md` — Worked cases / cross-pattern applications
- `references/MKT.Sources.md` — Source arguments and refresh

## Navigation rule

Start from the working difficulty, not file order. Follow each card's `Governing patterns` line and frontmatter `dependencies` when a needed result is missing.

## Single surface

`references/` is the canonical surface. `SKILL.md` is routing-only; there is no monolith to read. `INDEX.md` is reference-only.

## Lookup rules

- **Index first, then "no".** Check `references/INDEX.md` before searching. If an id is not listed there, the pattern does not exist — answer "no" and do not open files.
- **Read once.** Do not reopen a card you have already read.
