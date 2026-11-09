---
name: dpf-control-architecture-design
description: |
  Control Architecture Design (CAD) — Use when you need to choose observations and memory; construct a planning-and-feedback arrangement when useful; connect information error, command limits and execution conditions.
license: CC-BY-4.0
---

# DPF: Control Architecture Design (CAD)

**Depends on:** `fpf-core`
**Bounded context:** Use this framework when a control design must reconcile what can be observed in time, what the controller must remember, how decisions are divided, which commands remain feasible, and what the implementation can execute. It helps construct and compare those arrangements for an engineered dynamical system, including the choice to keep one sufficient controller.
**Source of truth:** `references/` — a source-faithful decomposition of *Control Architecture Design Principles Framework* (see `NOTICE.md` for the source/edition citation).
**Readiness mode:** `source-faithful` — full bodies reproduced from an approved source; no card has passed a heterogeneous-case evaluation (`E.21`). `status` on each card is the source's own status.

## When to load which pattern

| Situation | Load |
|---|---|
| an engineered controller has to act before a complete, accurate observation is available. | `references/CAD.5.md` |
| a control problem seems to call for different planning and reaction times, but “add a strategic, tactical and operational layer” does not te … | `references/CAD.1.md` |
| a planner and a lower controller have been chosen, but their combined behavior is not determined by their separate models. | `references/CAD.2.md` |
| a connected controller must respect state, output or actuator limits while following commands from another computation. | `references/CAD.3.md` |
| several control architectures appear feasible, or a change of model, hardware, rate or operating demand can invalidate an existing arrangeme … | `references/CAD.4.md` |

## Publication units

Non-pattern sections of the framework, reproduced as reference cards:

- `references/CAD.Reference.md` — Architectural Reference

## Navigation rule

Start from the working difficulty, not file order. Follow each card's `Governing patterns` line and frontmatter `dependencies` when a needed result is missing.

## Single surface

`references/` is the canonical surface. `SKILL.md` is routing-only; there is no monolith to read. `INDEX.md` is reference-only.

## Lookup rules

- **Index first, then "no".** Check `references/INDEX.md` before searching. If an id is not listed there, the pattern does not exist — answer "no" and do not open files.
- **Read once.** Do not reopen a card you have already read.
