---
name: dpf-human-capability-development
description: |
  Human Capability Development (HCD) — Use when you need to connect later work to capability demand, personal programmes, learning products, individual and shared practice, feedback, assessment, transfer and retention.
license: CC-BY-4.0
---

# DPF: Human Capability Development (HCD)

**Depends on:** `fpf-core`
**Bounded context:** HCD is a pattern language for deriving human capability demand from later Work, designing and sustaining development arrangements, judging human contribution, transfer and retention, and evaluating instructional material under stated audience, task, support and time conditions.
**Source of truth:** `references/` — a source-faithful decomposition of *Human Capability Development Principles Framework* (see `NOTICE.md` for the source/edition citation).
**Readiness mode:** `source-faithful` — full bodies reproduced from an approved source; no card has passed a heterogeneous-case evaluation (`E.21`). `status` on each card is the source's own status.

## When to load which pattern

| Situation | Load |
|---|---|
| Human development is often commissioned from a visible carrier: a course catalogue, certification, role framework, AI platform, assessment d … | `references/HCD.1.md` |
| When Work goes badly, the visible human is often the easiest place to intervene. | `references/HCD.3.md` |
| A person can be strong in three contributions and weak in a fourth. One contribution may be safe only with a specialist return; another may … | `references/HCD.4.md` |
| A person may need to recognize when a professional Method applies, retrieve a precise rule, perform a calculation, challenge an AI proposal … | `references/HCD.2.md` |
| The same poor result can arise from different action failures. A person may lack a usable explanation, make a recurrent calculation error, f … | `references/HCD.5.md` |
| A practice task can look realistic while testing the wrong contribution. | `references/HCD.6.md` |
| Use this method when a learner can hear a term or follow a direction but cannot yet notice the difference on which the action depends. | `references/HCD.6.1.md` |
| A programme can describe excellent practice and still be impossible to run. | `references/HCD.7.md` |
| A development design can fail after its activities are selected because the arrangement itself cannot do the work. | `references/HCD.8.md` |
| Practice is often recorded as exposure: pages completed, hours logged, cases submitted, or sessions attended. | `references/HCD.9.md` |
| A learner can succeed repeatedly while the task, timing, sources, help, and answer structure remain unchanged. | `references/HCD.10.md` |
| a person's document, course grade, helped answer or successful task is about to support a claim about what that person can contribute in lat … | `references/HCD.11.md` |
| a person has demonstrated a contribution in familiar work and someone wants to rely on it after a meaningful change in task, data, tool, set … | `references/HCD.12.md` |
| earlier success is being relied upon after an interval, or when the person now performs differently with changed tools or support. | `references/HCD.13.md` |
| an observation of performance, unfamiliar transfer, delayed performance or support dependence changes an assumption behind a person's develo … | `references/HCD.14.md` |
| one named person's programme has ended, a development assumption has changed, or a successful work episode raises a worthwhile question abou … | `references/HCD.15.md` |
| one exact Human Capability Development Method or status-preserved candidate and one human-development claim face evidence that can change th … | `references/HCD.16.md` |
| a bounded provider, learner, practitioner, or mixed Human Capability Development population intends to continue or change one observable way … | `references/HCD.17.md` |
| A time-accounting handout tells a learner to count from a task's first start to handoff. | `references/HCD.18.md` |
| An editor receives two apparently conflicting results. A prepared reader solves an interrupted-task exercise correctly, while the handout de … | `references/HCD.19.md` |
| A provider chooses four-person groups because the platform makes them convenient. | `references/HCD.20.md` |
| A programme assembles people from different projects to compare diagnostic reasoning. | `references/HCD.21.md` |
| A request to “discuss the case and submit one answer” permits efficient division of labour. | `references/HCD.22.md` |
| An instructor asks pairs to compare answers. One confident participant states the answer and the other agrees. | `references/HCD.23.md` |
| A learner writes that a peer's analysis is clear and convincing. The analysis has selected a cause that its observations do not distinguish. … | `references/HCD.24.md` |
| An engineer, product manager and organiser discuss their projects. Each can describe a local success. | `references/HCD.25.md` |
| Four participants intend to compare model grounds. Halfway through the meeting, they are editing the wording of one person's answer. | `references/HCD.26.md` |
| A paid distributed programme assigns annotations before a meeting. Some participants submit conclusions without grounds; others have not rec … | `references/HCD.27.md` |
| A prospective audience can be described before any member is known. That permits useful design: an author can qualify a task, compare explan … | `references/HCD.28.md` |

## Publication units

Non-pattern sections of the framework, reproduced as reference cards:

- `references/HCD.Reference.md` — Architectural Reference
- `references/HCD.Application.md` — Worked cases / cross-pattern applications
- `references/HCD.Sources.md` — Source arguments and refresh

## Navigation rule

Start from the working difficulty, not file order. Follow each card's `Governing patterns` line and frontmatter `dependencies` when a needed result is missing.

## Single surface

`references/` is the canonical surface. `SKILL.md` is routing-only; there is no monolith to read. `INDEX.md` is reference-only.

## Lookup rules

- **Index first, then "no".** Check `references/INDEX.md` before searching. If an id is not listed there, the pattern does not exist — answer "no" and do not open files.
- **Read once.** Do not reopen a card you have already read.
