---
name: dpf-music-and-dance-practice-engineering
description: |
  Music and Dance Practice Engineering (MDPE) — Use when you need to create, configure, perform, learn and transmit music and dance practices, including changes in tools, environments and styles.
license: CC-BY-4.0
---

# DPF: Music and Dance Practice Engineering (MDPE)

**Depends on:** `fpf-core`
**Bounded context:** A domain pattern language for creating, performing, transmitting, and deliberately developing music and dance practices and the environments that sustain them.
**Source of truth:** `references/` — a source-faithful decomposition of *Music and Dance Practice Engineering Principles Framework* (see `NOTICE.md` for the source/edition citation).
**Readiness mode:** `source-faithful` — full bodies reproduced from an approved source; no card has passed a heterogeneous-case evaluation (`E.21`). `status` on each card is the source's own status.

## When to load which pattern

| Situation | Load |
|---|---|
| Ordinary domain words often join unlike objects and activities: | `references/MDPE.8.md` |
| Music-and-Dance projects often begin with a compact phrase: “make a piece”, “launch a dance style”, “build an AI music practice”, “run a fes … | `references/MDPE.1.md` |
| A style-development project commonly starts from one of four incomplete moves: | `references/MDPE.21.md` |
| Music and Dance make new-whole claims especially tempting. A named practice can have its own vocabulary, followers, visual identity, press c … | `references/MDPE.24.md` |
| Music-and-Dance creation never starts from an empty possibility space. Learned Methods, bodies, instruments, software, partners, venues, aud … | `references/MDPE.9.md` |
| a physical relation or scientific image has suggested interesting movement, but you still need a phrase, its variations and a composed whole … | `references/MDPE.29.md` |
| a performer or arranger has promising cyclic rhythmic material but still needs a part that places sounds and actions in the right relation t … | `references/MDPE.30.md` |
| Capability-development projects often start from an available intervention instead of the Work that must become possible. | `references/MDPE.10.md` |
| Music-and-Dance projects optimize parts and discover incompatibility late. | `references/MDPE.3.md` |
| Use this method when a pair can perform some familiar movements but cannot yet obtain a wanted movement quality, respond to a musical change … | `references/MDPE.26.md` |
| Prepared and responsive performance coexist across Music and Dance. A classical musician realizes notated material differently on each occas … | `references/MDPE.11.md` |
| Use this method when either participant wants to finish a voluntary partnered encounter and the pair needs to turn that decision into an act … | `references/MDPE.27.md` |
| Use this method when an invitation to voluntary partnered performance has been declined and the inviter needs to end that invitation and dec … | `references/MDPE.28.md` |
| The central subject in this pattern is one bounded Music-or-Dance `U.Work` occurrence performed by named Agents. | `references/MDPE.5.md` |
| Music and Dance can be observed through different access relations. A microphone records sound but not visible movement or partner pressure. … | `references/MDPE.12.md` |
| A physical difference can exist without being available to a particular observer. | `references/MDPE.23.md` |
| Music and Dance cultures are shaped by many overlapping arrangements. A partner responds during a dance; a teacher chooses material for a cl … | `references/MDPE.13.md` |
| Music and Dance results cross conditions constantly. A phrase moves between instruments. Movement is translated between bodies. | `references/MDPE.6.md` |
| Methods do not travel as files. Descriptions, demonstrations, scores, recordings, exercises, prompts, instruments, software, and models can … | `references/MDPE.17.md` |
| Music and Dance leave selective traces. A recording can preserve sound while losing fingering, actuation, ensemble cues, room interaction, o … | `references/MDPE.18.md` |
| Music and Dance practices are reproduced by arrangements of actual Work, Methods, performer and audience capabilities, bodies and instrument … | `references/MDPE.19.md` |
| A Music-or-Dance practice is produced and reproduced through more than performers and material. | `references/MDPE.22.md` |
| During one performance or practice situation, several results matter together. | `references/MDPE.14.md` |
| Use this method when an organizer, teacher, ensemble, association or collaborating group can change part of a music or movement practice, bu … | `references/MDPE.25.md` |
| Music and Dance projects often make change look easier than it is. A score is edited, a phrase is renamed, a robot gains a technical ability … | `references/MDPE.15.md` |
| Music and Dance practices develop through variation, performance, comparison, repair, recombination, teaching, transmission, selective use … | `references/MDPE.16.md` |
| Music and Dance practices change through many relations at once. Performers vary material and Methods. | `references/MDPE.20.md` |
| Music and Dance projects produce heterogeneous evidence. A performer feels more fluent, a partner can read a cue, a technical metric improve … | `references/MDPE.7.md` |

## Publication units

Non-pattern sections of the framework, reproduced as reference cards:

- `references/MDPE.Reference.md` — Architectural Reference
- `references/MDPE.Application.md` — Worked cases / cross-pattern applications
- `references/MDPE.Sources.md` — Source arguments and refresh

## Navigation rule

Start from the working difficulty, not file order. Follow each card's `Governing patterns` line and frontmatter `dependencies` when a needed result is missing.

## Single surface

`references/` is the canonical surface. `SKILL.md` is routing-only; there is no monolith to read. `INDEX.md` is reference-only.

## Lookup rules

- **Index first, then "no".** Check `references/INDEX.md` before searching. If an id is not listed there, the pattern does not exist — answer "no" and do not open files.
- **Read once.** Do not reopen a card you have already read.
