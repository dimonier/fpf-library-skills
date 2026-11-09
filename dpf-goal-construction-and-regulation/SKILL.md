---
name: dpf-goal-construction-and-regulation
description: |
  Goal Construction and Regulation (GOALS) — Use when you need to construct worthwhile goals and achievement evidence, coordinate their pursuit and revise the practice; complete OKR/CFR and human and AI applications.
license: CC-BY-4.0
---

# DPF: Goal Construction and Regulation (GOALS)

**Depends on:** `fpf-core`
**Bounded context:** Part of the [Management DPF Suite](./).
**Source of truth:** `references/` — a source-faithful decomposition of *Goal Construction and Regulation Principles Framework* (see `NOTICE.md` for the source/edition citation).
**Readiness mode:** `source-faithful` — full bodies reproduced from an approved source; no card has passed a heterogeneous-case evaluation (`E.21`). `status` on each card is the source's own status.

## When to load which pattern

| Situation | Load |
|---|---|
| a wish, target or assignment must become an intelligible basis for action, or participants are using the same goal words with different expe … | `references/GOALS.1.md` |
| people need to tell whether a goal has been achieved, whether progress supports a response, or whether a proposed set of key results would e … | `references/GOALS.2.md` |
| several aims or participants depend on the same means, one goal can defeat another, or a proposed priority would alter existing reliance. | `references/GOALS.3.md` |
| progress information, a changed need or a failed dependency calls for a decision about pursuing a goal. | `references/GOALS.4.md` |
| an organization needs a recurring way to select consequential changes, make their evidence and dependencies visible, coordinate pursuit and … | `references/GOALS.5.md` |
| a person wants or is expected to pursue a professional goal, yet adopting it, beginning, continuing or changing course remains difficult. | `references/GOALS.6.md` |
| an AI system is to pursue a result through reasoning, tools, multiple actions or later continuation, and an ordinary one-response instructio … | `references/GOALS.7.md` |
| goal information will support help, reflection, recognition or a decision about a person. | `references/GOALS.8.md` |
| people or an organization need to become able to use the goal methods, repeated goal-work failures persist, or the present practice should b … | `references/GOALS.9.md` |

## Publication units

Non-pattern sections of the framework, reproduced as reference cards:

- `references/GOALS.Reference.md` — Architectural Reference
- `references/GOALS.Source.md` — Source arguments and refresh

## Navigation rule

Start from the working difficulty, not file order. Follow each card's `Governing patterns` line and frontmatter `dependencies` when a needed result is missing.

## Single surface

`references/` is the canonical surface. `SKILL.md` is routing-only; there is no monolith to read. `INDEX.md` is reference-only.

## Lookup rules

- **Index first, then "no".** Check `references/INDEX.md` before searching. If an id is not listed there, the pattern does not exist — answer "no" and do not open files.
- **Read once.** Do not reopen a card you have already read.
