---
name: dpf-corporate-governance
description: |
  Corporate Governance (CGOV) — Use when you need to constitute and exercise corporate powers, decisions, controls and accountability under applicable governing rules.
license: CC-BY-4.0
---

# DPF: Corporate Governance (CGOV)

**Depends on:** `fpf-core`
**Bounded context:** A pattern language for making corporate decisions, arranging governing contributions, protecting rights and improving how this work is performed.
**Source of truth:** `references/` — a source-faithful decomposition of *Corporate Governance Principles Framework* (see `NOTICE.md` for the source/edition citation).
**Readiness mode:** `source-faithful` — full bodies reproduced from an approved source; no card has passed a heterogeneous-case evaluation (`E.21`). `status` on each card is the source's own status.

## When to load which pattern

| Situation | Load |
|---|---|
| a request such as “get the owners' approval”, “the group will guarantee it”, or “improve governance” leaves unclear whose act is needed and … | `references/CGOV.1.md` |
| a proposed vote, financing, appointment or change of ownership depends on who can receive returns, cast votes, give consent or influence the … | `references/CGOV.2.md` |
| a practitioner must determine who may appoint or remove a holder, authorize a corporate matter, delegate a power, or act under an existing d … | `references/CGOV.3.md` |
| a corporation's board and executive management cannot explain what they need from one another, when directors take over delegated work, or w … | `references/CGOV.4.md` |
| a board cannot obtain a needed oversight contribution, when a committee lacks the remit or support to provide it, or when new committees are … | `references/CGOV.5.md` |
| a corporate matter may be influenced by a participant's other interests or duties, when a transaction involves a connected party, or when a … | `references/CGOV.6.md` |
| a corporate matter needs review or decision participation protected from an identified interest, when a required independent contribution is … | `references/CGOV.7.md` |
| a director, shareholder or other entitled recipient lacks corporate information needed for a decision; when a disclosure duty has arisen; or … | `references/CGOV.8.md` |
| a corporation's objectives depend on controls that do not operate, leave a consequential exposure untreated, impose needless burden or give … | `references/CGOV.9.md` |
| a corporate decision or reporting duty depends on an audit or assurance conclusion, when its scope is unclear, or when an existing report is … | `references/CGOV.10.md` |
| a corporation needs an act by a board, shareholders or another authorized holder, and preparation must become a decision made under the appl … | `references/CGOV.11.md` |
| a corporate transaction or governance action may bypass a minority holder's information, participation, consent or other protected right; wh … | `references/CGOV.12.md` |
| a board or another authorized corporate organ must follow implementation, performance or exposure and decide how those responsible should re … | `references/CGOV.13.md` |
| a corporation is considering a change to its governing instruments, powers or arrangements. | `references/CGOV.14.md` |
| a recurring difficulty calls for a different way of preparing, deciding, overseeing or accounting for a corporate matter. | `references/CGOV.15.md` |
| a corporate-governance action appears correctly performed in isolation but does not accomplish the work it belongs to: a correct sum does no … | `references/CGOV.16.md` |
| corporate participants need to preserve, transmit or change a shared way of governing. | `references/CGOV.17.md` |

## Publication units

Non-pattern sections of the framework, reproduced as reference cards:

- `references/CGOV.Reference.md` — Architectural Reference

## Navigation rule

Start from the working difficulty, not file order. Follow each card's `Governing patterns` line and frontmatter `dependencies` when a needed result is missing.

## Single surface

`references/` is the canonical surface. `SKILL.md` is routing-only; there is no monolith to read. `INDEX.md` is reference-only.

## Lookup rules

- **Index first, then "no".** Check `references/INDEX.md` before searching. If an id is not listed there, the pattern does not exist — answer "no" and do not open files.
- **Read once.** Do not reopen a card you have already read.
