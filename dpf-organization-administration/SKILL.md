---
name: dpf-organization-administration
description: |
  Organization Administration (ADM) — Use when you need to make requests, permissions, obligations, provision, records and provider coordination effective without unnecessary burden.
license: CC-BY-4.0
---

# DPF: Organization Administration (ADM)

**Depends on:** `fpf-core`
**Bounded context:** ADM helps administrators examine administrative requests, give justified refusals and provide usable results under the organization's rules. Its fifteen patterns also help improve the arrangements supporting this work by connecting organizational rules, participants, permissions, work and records. Establish any permission required for the action being taken; specialist decisions remain with the people authorized to make them.
**Source of truth:** `references/` — a source-faithful decomposition of *Organization Administration Principles Framework* (see `NOTICE.md` for the source/edition citation).
**Readiness mode:** `source-faithful` — full bodies reproduced from an approved source; no card has passed a heterogeneous-case evaluation (`E.21`). `status` on each card is the source's own status.

## When to load which pattern

| Situation | Load |
|---|---|
| A participant asks for travel, access, reimbursement, an appointment or another administrative result because it makes some work possible. | `references/ADM.1.md` |
| An administrator works with people in several capacities. The requester can act for a beneficiary. | `references/ADM.2.md` |
| An organization can approve an appointment before it takes effect. A directory can be updated before or after that date. | `references/ADM.3.md` |
| Several participants can be involved in one transfer, appointment or provision. Each keeps records for its own decisions. | `references/ADM.4.md` |
| The designer is working on how a class of administrative requests will be handled. | `references/ADM.5.md` |
| A handler is working on a particular request for an administrative condition. | `references/ADM.6.md` |
| A handler, deciding person or provider is about to rely on a claim. The claim concerns an identified participant, event, relation, amount or … | `references/ADM.7.md` |
| A person or organization proposes an action for which the applicable institutional arrangement requires authority. | `references/ADM.8.md` |
| A beneficiary, relevant permission and intended administrative condition are known sufficiently to act, or the outstanding prerequisite is e … | `references/ADM.9.md` |
| The handler is comparing what one participant owed another, what actually happened and what the participants recorded. | `references/ADM.10.md` |
| The practitioner is arranging contributions to a particular administrative result or a bounded class of such results. | `references/ADM.11.md` |
| The practitioner is maintaining records used in administration. A record may contain a request, rule edition, decision, grant, provider inst … | `references/ADM.13.md` |
| The practitioner is examining a reusable control arrangement. Its purpose may be to prevent unauthorized expenditure, establish eligibility … | `references/ADM.14.md` |
| The practitioner is assessing a service or proposed change for an identified population, arrangement and period. | `references/ADM.15.md` |
| The practitioner is considering or implementing a change to a policy, control, provider arrangement, handling instruction or supporting syst … | `references/ADM.16.md` |

## Publication units

Non-pattern sections of the framework, reproduced as reference cards:

- `references/ADM.Reference.md` — Architectural Reference
- `references/ADM.Sources.md` — Source arguments and refresh

## Navigation rule

Start from the working difficulty, not file order. Follow each card's `Governing patterns` line and frontmatter `dependencies` when a needed result is missing.

## Single surface

`references/` is the canonical surface. `SKILL.md` is routing-only; there is no monolith to read. `INDEX.md` is reference-only.

## Lookup rules

- **Index first, then "no".** Check `references/INDEX.md` before searching. If an id is not listed there, the pattern does not exist — answer "no" and do not open files.
- **Read once.** Do not reopen a card you have already read.
