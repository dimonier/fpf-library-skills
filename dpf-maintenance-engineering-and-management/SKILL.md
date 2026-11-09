---
name: dpf-maintenance-engineering-and-management
description: |
  Maintenance Engineering and Management (MNT) — Use when you need to select maintenance policy from condition and failure knowledge; prepare interventions, restore functioning and qualify return to use.
license: CC-BY-4.0
---

# DPF: Maintenance Engineering and Management (MNT)

**Depends on:** `fpf-core`
**Bounded context:** Select maintenance policy from condition and failure knowledge; prepare interventions, restore functioning and qualify return to use.
**Source of truth:** `references/` — a source-faithful decomposition of *Maintenance Engineering and Management Principles Framework* (see `NOTICE.md` for the source/edition citation).
**Readiness mode:** `source-faithful` — full bodies reproduced from an approved source; no card has passed a heterogeneous-case evaluation (`E.21`). `status` on each card is the source's own status.

## When to load which pattern

| Situation | Load |
|---|---|
| a maintenance request names equipment but leaves unclear what must keep working, in which configuration, for whom or under whose control. | `references/MNT.1.md` |
| a recurring maintenance task, inspection interval or proposed technology needs a reason to be retained or changed. | `references/MNT.2.md` |
| a fault code, alarm or repair history leaves the mechanism or consequence needed for a maintenance decision unclear. | `references/MNT.3.md` |
| a measurement, inspection or prediction needs interpretation for a maintenance question. | `references/MNT.4.md` |
| a maintenance policy or intervention depends on support that may not be ready at the required time. | `references/MNT.5.md` |
| current condition raises a maintenance choice: repair, replace, adjust, inspect, defer, restrict use or stop. | `references/MNT.6.md` |
| maintenance and operation need one feasible arrangement for access, service continuity and return to use. | `references/MNT.7.md` |
| a selected maintenance intervention will expose people, equipment or the environment to a hazard that requires controlled access, isolation … | `references/MNT.8.md` |
| a selected maintenance intervention is being performed and later decisions depend on what actually happened. | `references/MNT.9.md` |
| a performed maintenance task is being used to claim that the System can again support its required use. | `references/MNT.10.md` |
| maintenance control is being returned to operation and the receiving person needs a supported basis to resume use. | `references/MNT.11.md` |
| a maintenance decision depends on connecting service history to the correct unit, installed part, configuration or applicable description. | `references/MNT.12.md` |
| maintenance decisions span a population of equipment and repeated work: which policies to retain, where support is inadequate and what can b … | `references/MNT.13.md` |
| an established way of doing maintenance may no longer be the best answer for the current failure, equipment or operating setting. | `references/MNT.14.md` |
| individually plausible maintenance, operating and support plans cannot be performed together. | `references/MNT.15.md` |
| the question concerns how maintenance practice is actually continued or changed among people: a hand-back Method is taught, a new diagnostic … | `references/MNT.16.md` |

## Publication units

Non-pattern sections of the framework, reproduced as reference cards:

- `references/MNT.Reference.md` — Architectural Reference
- `references/MNT.Application.md` — Worked cases / cross-pattern applications
- `references/MNT.Sources.md` — Source arguments and refresh

## Navigation rule

Start from the working difficulty, not file order. Follow each card's `Governing patterns` line and frontmatter `dependencies` when a needed result is missing.

## Single surface

`references/` is the canonical surface. `SKILL.md` is routing-only; there is no monolith to read. `INDEX.md` is reference-only.

## Lookup rules

- **Index first, then "no".** Check `references/INDEX.md` before searching. If an id is not listed there, the pattern does not exist — answer "no" and do not open files.
- **Read once.** Do not reopen a card you have already read.
