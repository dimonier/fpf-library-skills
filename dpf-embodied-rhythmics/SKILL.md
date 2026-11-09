---
name: dpf-embodied-rhythmics
description: |
  Embodied Rhythmics (RHY) — Use when you need to recognize, represent, alter and perform rhythmic relations; coordinate sound, movement, reference and simultaneous layers.
license: CC-BY-4.0
---

# DPF: Embodied Rhythmics (RHY)

**Depends on:** `fpf-core`
**Bounded context:** A pattern language for recognizing, representing, shaping, performing, learning and observing rhythmic relations.
**Source of truth:** `references/` — a source-faithful decomposition of *Embodied Rhythmics Principles Framework* (see `NOTICE.md` for the source/edition citation).
**Readiness mode:** `source-faithful` — full bodies reproduced from an approved source; no card has passed a heterogeneous-case evaluation (`E.21`). `status` on each card is the source's own status.

## When to load which pattern

| Situation | Load |
|---|---|
| an instruction such as “keep the rhythm,” “find the pulse” or “make it clearer” leaves a performer unsure what to change. | `references/RHY.1.md` |
| a score, count, waveform, movement trace or list of attacks leaves out something needed to explain, reproduce or change the rhythm. | `references/RHY.2.md` |
| clearer attacks, accents or steps interrupt a continuous motion or sound that the performance needs. | `references/RHY.3.md` |
| two apparently correct timing judgements disagree, or when aligning one recorded event fails to make the performance usable. | `references/RHY.4.md` |
| a count, syllable sequence, score, diagram or recording makes one rhythmic operation easy but leaves another difficult. | `references/RHY.5.md` |
| rhythmic material must move between conventions or carriers and the receiving user needs more than a familiar-looking sequence. | `references/RHY.6.md` |
| a rhythmic variant is called simpler, more complex, more similar, more interesting or easier to perform, but the comparison does not yet jus … | `references/RHY.7.md` |
| a rhythmic passage needs a new variant that retains a useful relation: an ending must arrive at the agreed point, an accent should move whil … | `references/RHY.8.md` |
| a passage is individually performable but its participants cannot receive or act on the timing information they need while doing their own p … | `references/RHY.9.md` |
| performers can receive one another's cues yet disagree about entry, beat or cycle position, drift during a passage, or lose their relationsh … | `references/RHY.10.md` |
| a performer or group can produce parts separately but loses their intended relationship when they occur together. | `references/RHY.11.md` |
| a learner can count, describe or perform parts of a passage but loses a needed rhythmic relation when performing the passage: the beat chang … | `references/RHY.12.md` |
| the next performance or development decision depends on whether a demonstrated rhythmic contribution remains available under a meaningful ch … | `references/RHY.13.md` |
| a rhythmic comparison needs observations that the available score, calculation or impression does not supply. | `references/RHY.14.md` |

## Publication units

Non-pattern sections of the framework, reproduced as reference cards:

- `references/RHY.Reference.md` — Architectural Reference
- `references/RHY.Edition.md` — Edition and reuse

## Navigation rule

Start from the working difficulty, not file order. Follow each card's `Governing patterns` line and frontmatter `dependencies` when a needed result is missing.

## Single surface

`references/` is the canonical surface. `SKILL.md` is routing-only; there is no monolith to read. `INDEX.md` is reference-only.

## Lookup rules

- **Index first, then "no".** Check `references/INDEX.md` before searching. If an id is not listed there, the pattern does not exist — answer "no" and do not open files.
- **Read once.** Do not reopen a card you have already read.
