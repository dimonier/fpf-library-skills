---
name: dpf-explanation-design
description: |
  Explanation Design (EXD) — Use when you need to design an explanation, worked example or dialogue that helps its recipient understand and perform the needed operation.
license: CC-BY-4.0
---

# DPF: Explanation Design (EXD)

**Depends on:** `fpf-core`
**Bounded context:** Help a recipient recover and use a warranted connection by choosing the question, account, expression and support that the situation needs.
**Source of truth:** `references/` — a source-faithful decomposition of *Explanation Design Principles Framework* (see `NOTICE.md` for the source/edition citation).
**Readiness mode:** `source-faithful` — full bodies reproduced from an approved source; no card has passed a heterogeneous-case evaluation (`E.21`). `status` on each card is the source's own status.

## When to load which pattern

| Situation | Load |
|---|---|
| someone needs an explanation and the needed connection, contrast or use is still unclear, or when a contribution changes what the explanatio … | `references/EXD.1.md` |
| a recipient needs to connect a principle, definition or claim with a particular instance. | `references/EXD.2.md` |
| a warranted account is available but the recipient has difficulty following its relations through the chosen words, symbols, diagram, demons … | `references/EXD.3.md` |
| Use this pattern while explaining with another participant when their contribution can change the question, the account, the help needed or … | `references/EXD.4.md` |
| an instructional purpose requires the recipient to construct and use an explanation: connect a worked step to a principle, explain an error … | `references/EXD.5.md` |
| a proposed explanation change competes with an available explanation and the comparison can change what you retain, repair or stop. | `references/EXD.6.md` |

## Publication units

Non-pattern sections of the framework, reproduced as reference cards:

- `references/EXD.Reference.md` — Architectural Reference
- `references/EXD.Profiles.md` — Publication unit
- `references/EXD.Sources.md` — Source arguments and refresh
- `references/EXD.Edition.md` — Edition and reuse

## Navigation rule

Start from the working difficulty, not file order. Follow each card's `Governing patterns` line and frontmatter `dependencies` when a needed result is missing.

## Single surface

`references/` is the canonical surface. `SKILL.md` is routing-only; there is no monolith to read. `INDEX.md` is reference-only.

## Lookup rules

- **Index first, then "no".** Check `references/INDEX.md` before searching. If an id is not listed there, the pattern does not exist — answer "no" and do not open files.
- **Read once.** Do not reopen a card you have already read.
