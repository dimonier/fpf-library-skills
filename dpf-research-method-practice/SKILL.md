---
name: dpf-research-method-practice
description: |
  Research Method Practice (RMP) — Use when you need to frame and design research, obtain and criticize evidence, synthesize sources, and return a warranted knowledge contribution.
license: CC-BY-4.0
---

# DPF: Research Method Practice (RMP)

**Depends on:** `fpf-core`
**Bounded context:** A research repertoire for qualifying a question, choosing and conducting a defensible inquiry, examining and returning its knowledge contribution, and retaining or improving the Methods that serve it.
**Source of truth:** `references/` — a source-faithful decomposition of *Research Method Practice Principles Framework* (see `NOTICE.md` for the source/edition citation).
**Readiness mode:** `source-faithful` — full bodies reproduced from an approved source; no card has passed a heterogeneous-case evaluation (`E.21`). `status` on each card is the source's own status.

## When to load which pattern

| Situation | Load |
|---|---|
| Many activities appear on both sides of the research boundary. A laboratory test can execute an already qualified engineering Method or chal … | `references/RMP.1.md` |
| Research questions do not determine one universal design. The same practical use can be served by a controlled comparison, a field observati … | `references/RMP.2.md` |
| a research design has been selected but someone still has to decide which specimens, encounters, sources, observations or computations will … | `references/RMP.3.md` |
| research material must remain inspectable, or when a colleague receives an apparent result but cannot recover how the work produced it. | `references/RMP.4.md` |
| research material, an analysis or an emerging interpretation is available and someone needs to say **what claim it supports and what critici … | `references/RMP.5.md` |
| a bounded research claim is available and someone needs to decide **which credibility examination could change its interpretation or propose … | `references/RMP.6.md` |
| several research reports, source interpretations or an existing synthesis bear on a question, and someone needs to determine **what their co … | `references/RMP.7.md` |
| research analysis, criticism, a credibility result or a synthesis changes what a knowledge account may assert, or when its recipient needs a … | `references/RMP.8.md` |
| A research team can encounter the same visible failure for different reasons. | `references/RMP.9.md` |
| Ordinary records show only part of practice. Logs favor tool-visible events, procedures favor intended behavior, interviews favor memorable … | `references/RMP.10.md` |
| An account of professional Method change relates variants recorded in successive sources to changes in institutions, tools, regulation and l … | `references/RMP.11.md` |

## Publication units

Non-pattern sections of the framework, reproduced as reference cards:

- `references/RMP.Reference.md` — Architectural Reference
- `references/RMP.Application.md` — Worked cases / cross-pattern applications
- `references/RMP.Sources.md` — Source arguments and refresh

## Navigation rule

Start from the working difficulty, not file order. Follow each card's `Governing patterns` line and frontmatter `dependencies` when a needed result is missing.

## Single surface

`references/` is the canonical surface. `SKILL.md` is routing-only; there is no monolith to read. `INDEX.md` is reference-only.

## Lookup rules

- **Index first, then "no".** Check `references/INDEX.md` before searching. If an id is not listed there, the pattern does not exist — answer "no" and do not open files.
- **Read once.** Do not reopen a card you have already read.
