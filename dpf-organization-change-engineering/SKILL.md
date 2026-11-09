---
name: dpf-organization-change-engineering
description: |
  Organization Change Engineering (OCE) — Use when you need to construct and qualify organizational changes to contributions, roles, authority, interfaces, capabilities and culture.
license: CC-BY-4.0
---

# DPF: Organization Change Engineering (OCE)

**Depends on:** `fpf-core`
**Bounded context:** A domain pattern language for changing an organization's contributions, working relations, and capability while its work continues.
**Source of truth:** `references/` — a source-faithful decomposition of *Organization Change Engineering Principles Framework* (see `NOTICE.md` for the source/edition citation).
**Readiness mode:** `source-faithful` — full bodies reproduced from an approved source; no card has passed a heterogeneous-case evaluation (`E.21`). `status` on each card is the source's own status.

## When to load which pattern

| Situation | Load |
|---|---|
| Organization change is often named from the inside: a reporting line, function, headcount, technology introduction, merger programme, or lea … | `references/OCE.1.md` |
| Formal descriptions support authorization, communication, administration, or staffing. | `references/OCE.2.md` |
| Organization concepts arrive with persuasive forms. Charts foreground reporting; team topologies interaction; provider proposals service bou … | `references/OCE.3.md` |
| Organization design often begins with grouping: functions, products, customers, regions, programmes, professions, or platforms. | `references/OCE.4.md` |
| Organizations need persistent contribution loci that survive ordinary holder changes. | `references/OCE.5.md` |
| Organization change becomes operational when actual Systems hold effective assignments and the other relations needed for their contribution … | `references/OCE.6.md` |
| Products and services are produced, operated, supported, assured, and changed through organizations. | `references/OCE.7.md` |
| A bounded organization unit cannot reliably obtain a needed contribution. | `references/OCE.8.md` |
| A change practitioner and the participating workers must make a designed contribution possible while the organization continues working. | `references/OCE.9.md` |
| A practitioner and the affected participants need to make a selected contribution workable in the target organization. | `references/OCE.10.md` |
| A change practitioner and the receiving service owner must agree what can change while current users still depend on the organization. | `references/OCE.11.md` |
| The person, current work owner, receiving work owner, learning provider and provider of shared personnel services can be different participa … | `references/OCE.18.md` |
| a decision about an organization change needs to know what changed, for whom and under which conditions. | `references/OCE.13.md` |
| a qualified result challenges an organization relation or condition that was previously selected or put into use. | `references/OCE.14.md` |
| Recognizable schools and recipes make communication cheap but hide unlike functions: diagnosis, participation, strategy, process guidance, d … | `references/OCE.15.md` |
| Each change can look locally plausible while the conjunction is not. One effort can promise autonomy while another introduces a new approval … | `references/OCE.16.md` |
| an organization-change practice seems to be spreading, fading or changing among practitioners, and that difference matters to their next wor … | `references/OCE.17.md` |

## Publication units

Non-pattern sections of the framework, reproduced as reference cards:

- `references/OCE.Reference.md` — Architectural Reference
- `references/OCE.Application.md` — Worked cases / cross-pattern applications
- `references/OCE.Sources.md` — Source arguments and refresh

## Navigation rule

Start from the working difficulty, not file order. Follow each card's `Governing patterns` line and frontmatter `dependencies` when a needed result is missing.

## Single surface

`references/` is the canonical surface. `SKILL.md` is routing-only; there is no monolith to read. `INDEX.md` is reference-only.

## Lookup rules

- **Index first, then "no".** Check `references/INDEX.md` before searching. If an id is not listed there, the pattern does not exist — answer "no" and do not open files.
- **Read once.** Do not reopen a card you have already read.
