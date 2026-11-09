---
name: dpf-decision-design
description: |
  Decision Design (PSDA) — Use when you need to formulate a decision problem, construct alternatives, compare consequences and uncertainty, and connect a recommendation to its use.
license: CC-BY-4.0
---

# DPF: Decision Design (PSDA)

**Depends on:** `fpf-core`
**Bounded context:** A domain pattern language for constructing problem formulations, decision alternatives and models, and qualifying their interpretation and use in bounded inquiry, including professional participation and advice.
**Source of truth:** `references/` — a source-faithful decomposition of *Decision Design Principles Framework* (see `NOTICE.md` for the source/edition citation).
**Readiness mode:** `source-faithful` — full bodies reproduced from an approved source; no card has passed a heterogeneous-case evaluation (`E.21`). `status` on each card is the source's own status.

## When to load which pattern

| Situation | Load |
|---|---|
| one wording of “the problem” is becoming naturalized even though materially different accounts would change what is included, what evidence … | `references/PSDA.1.md` |
| a decision-support inquiry either expands toward everything connected with the situation or excludes a concern, bearer, relation, horizon, o … | `references/PSDA.2.md` |
| one diagram, spreadsheet, simulation, or agreed story is being asked to explain a contested situation, represent everyone's concerns, predic … | `references/PSDA.3.md` |
| a favorite workshop recipe, analytical technique, or problem-structuring method is being proposed before anyone has tested whether it can pr … | `references/PSDA.4.md` |
| an inquiry has clarified what matters but the proposed decision still contains only the incumbent, a sponsor's preferred project, or two lab … | `references/PSDA.5.md` |
| a scorecard's criteria came from a template, “importance” weights have no stated meaning, or the same benefit appears under several headings … | `references/PSDA.6.md` |
| a point estimate, “high confidence” label, or model output makes a decision look more settled than its evidence permits. | `references/PSDA.7.md` |
| alternatives have been named or ranked but nobody can reconstruct what each would change, for whom, over what time, and under which assumpti … | `references/PSDA.8.md` |
| a favored alternative depends on a forecast, weight, model, or threshold that might change, or when a precise ranking hides plausible revers … | `references/PSDA.9.md` |
| Decision-support practice often begins before there is a stable “problem”. | `references/PSDA.11.md` |
| Contested situations rarely present a neutral list of stakeholders. Sponsors, operators, specialists, residents, customers, regulators, futu … | `references/PSDA.12.md` |
| participants need to work on a decision-support question but disagree about its meaning, evidence, consequences, or acceptable action. | `references/PSDA.13.md` |
| analysis is available, or its decisive gap is known, but the recipient still cannot tell what the decision-support performer recommends and … | `references/PSDA.14.md` |
| a recommendation or decision depends on conditions that may change, but nobody can yet say which observations matter, who will interpret the … | `references/PSDA.15.md` |
| a practice needs to decide which problem-structuring and decision-support Methods to retain, change or withdraw from its offering for future … | `references/PSDA.16.md` |
| useful activities in a decision-support engagement obstruct one another. | `references/PSDA.17.md` |
| a decision-support practice needs to decide whether to retain or change how its ways of working are passed on, recognized, chosen or kept al … | `references/PSDA.18.md` |
| someone asks a distinct adviser which development direction to consider for a person, organization, or other identified subject, but the ter … | `references/PSDA.19.md` |
| a proposed change looks useful from one participant's position, but you cannot explain what it would require or change for the others. | `references/PSDA.20.md` |

## Publication units

Non-pattern sections of the framework, reproduced as reference cards:

- `references/PSDA.Reference.md` — Architectural Reference
- `references/PSDA.Advising.md` — Development-direction advising
- `references/PSDA.Application.md` — Worked cases / cross-pattern applications
- `references/PSDA.Sources.md` — Source arguments and refresh

## Navigation rule

Start from the working difficulty, not file order. Follow each card's `Governing patterns` line and frontmatter `dependencies` when a needed result is missing.

## Single surface

`references/` is the canonical surface. `SKILL.md` is routing-only; there is no monolith to read. `INDEX.md` is reference-only.

## Lookup rules

- **Index first, then "no".** Check `references/INDEX.md` before searching. If an id is not listed there, the pattern does not exist — answer "no" and do not open files.
- **Read once.** Do not reopen a card you have already read.
