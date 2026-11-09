---
name: dpf-operations-management
description: |
  Operations Management (OPS) — Use when you need to understand, construct and revise operating arrangements; manage work, provision, service and improvement under actual conditions.
license: CC-BY-4.0
---

# DPF: Operations Management (OPS)

**Depends on:** `fpf-core`
**Bounded context:** A domain pattern language for understanding, arranging and managing continuing production and service, and for improving the ways that obtain their results.
**Source of truth:** `references/` — a source-faithful decomposition of *Operations Management Principles Framework* (see `NOTICE.md` for the source/edition citation).
**Readiness mode:** `source-faithful` — full bodies reproduced from an approved source; no card has passed a heterogeneous-case evaluation (`E.21`). `status` on each card is the source's own status.

## When to load which pattern

| Situation | Load |
|---|---|
| individually plausible answers about local work, delivery, capacity, service, money or people's working conditions do not yet explain what t … | `references/OPS.23.md` |
| Operations work begins in the middle. Demand has arrived, commitments already exist, cases are open, resources are shared, records disagree … | `references/OPS.1.md` |
| Project, process, and case management are often offered as competing descriptions of reality. | `references/OPS.2.md` |
| Operational tools compress the world so people can coordinate. That compression is useful until one row is read as the customer, order, case … | `references/OPS.3.md` |
| Continuing operation needs a present account because the operation outlives one meeting, screen, shift, or model session. | `references/OPS.4.md` |
| Continuing operation usually receives more apparent demand than it can honestly start. | `references/OPS.5.md` |
| Continuing cases do not simply advance because a standard sequence exists. | `references/OPS.6.md` |
| Time matters in operations because delay can alter consequences, commitments, dependencies, recoverability, and the usefulness of later acti … | `references/OPS.7.md` |
| An operation may contain several queues and joins. A release needs a tested configuration, a safety result and an authorized decision; a shi … | `references/OPS.8.md` |
| finishing one operation can trigger new work even though the previous result may still need correction, another visit or downstream acceptan … | `references/OPS.8.1.md` |
| a person, machine or computing resource has idle intervals reserved for another service, and useful auxiliary work could occupy those interv … | `references/OPS.8.2.md` |
| A queue can be long because service capacity is scarce, inputs arrive in bursts, prerequisites are incomplete, acceptance is delayed, or ear … | `references/OPS.9.md` |
| Capacity is useful only relative to a service, resource capability, operating conditions and time window. | `references/OPS.10.md` |
| a capacity decision has a service question and an operating arrangement, but the calculation needed to compare its alternatives is missing o … | `references/OPS.10.1.md` |
| a team must deliver particular results by particular times, but a list of tasks and estimated durations does not establish whether the work … | `references/OPS.10.2.md` |
| An operation depends on several actual structures. Its resource participation, material transformation, case and commitment relations, infor … | `references/OPS.11.md` |
| the operation needs a way to obtain a required result, or an operating change looks useful in one account of the work but its consequence ca … | `references/OPS.11.1.md` |
| an operating choice changes people's workload, exposure, attention, discretion, support or recovery. | `references/OPS.12.md` |
| someone needs a credible service promise, an existing commitment has become doubtful, or a resource change could alter what the operation ca … | `references/OPS.13.md` |
| an operating alternative appears worthwhile because it raises output, lowers unit cost, releases capacity or brings money sooner. | `references/OPS.14.md` |
| an operating decision cannot be supported by the available account: figures disagree, a denominator excludes important work, events from dif … | `references/OPS.15.md` |
| a decision depends on waiting, unfinished work, output or resource use, but the available totals do not make clear what was counted. | `references/OPS.15.1.md` |
| Operating Methods need revision when demand, services, constraints, technologies, participants, or protection conditions change. | `references/OPS.16.md` |
| the current way of running an operation repeatedly misses its purpose, a changed condition defeats one of its assumptions, or a serious alte … | `references/OPS.17.md` |
| an operating result may no longer meet its requirement, observed service failures exceed the agreed allowance, a recurring process changes … | `references/OPS.18.md` |
| Continuing operation brings several Work wholes and decision structures together. | `references/OPS.19.md` |
| Operations depend on practices that cross shifts, sites, providers, and generations of practitioners. | `references/OPS.20.md` |
| an operating team needs to decide what improvement to pursue and how to recognize it, or when a supplied target encourages the wrong work. | `references/OPS.21.md` |
| an operating result must inform a judgement and response, but a target-attainment ratio or dashboard color cannot explain the contribution. | `references/OPS.22.md` |

## Publication units

Non-pattern sections of the framework, reproduced as reference cards:

- `references/OPS.Reference.md` — Architectural Reference
- `references/OPS.Application.md` — Worked cases / cross-pattern applications
- `references/OPS.Sources.md` — Source arguments and refresh

## Navigation rule

Start from the working difficulty, not file order. Follow each card's `Governing patterns` line and frontmatter `dependencies` when a needed result is missing.

## Single surface

`references/` is the canonical surface. `SKILL.md` is routing-only; there is no monolith to read. `INDEX.md` is reference-only.

## Lookup rules

- **Index first, then "no".** Check `references/INDEX.md` before searching. If an id is not listed there, the pattern does not exist — answer "no" and do not open files.
- **Read once.** Do not reopen a card you have already read.
