---
name: dpf-systems-engineering
description: |
  Systems Engineering (SYSE) — Use when you need to define the system and intended use; compare designs and ways to obtain them; realize, integrate, qualify and change the result.
license: CC-BY-4.0
---

# DPF: Systems Engineering (SYSE)

**Depends on:** `fpf-core`
**Bounded context:** A domain pattern language for bringing about and changing engineered Systems, from their intended use and architecture to realization, assurance, and continuing development.
**Source of truth:** `references/` — a source-faithful decomposition of *Systems Engineering Principles Framework* (see `NOTICE.md` for the source/edition citation).
**Readiness mode:** `source-faithful` — full bodies reproduced from an approved source; no card has passed a heterogeneous-case evaluation (`E.21`). `status` on each card is the source's own status.

## When to load which pattern

| Situation | Load |
|---|---|
| participants use a familiar project name but cannot say which system's intended use gives their joint work its purpose. | `references/SYSE.1.md` |
| Engineering choices—such as choices about System functions, architecture, interfaces, offerings, assurance, or change—depend on larger worki … | `references/SYSE.16.md` |
| Engineering decisions and descriptions guide realization, operation, maintenance, and modernization Work. | `references/SYSE.17.md` |
| a project has selected an actual System, retained an intended System referent, or bounded another engineering subject, but the proposed conc … | `references/SYSE.2.md` |
| people involved in the same service or product describe incompatible accounts of what happens, why it happens and what should happen next. | `references/SYSE.54.md` |
| Engineering problems and System concepts develop together. For example, an architecture can expose a manufacturing constraint; a prototype c … | `references/SYSE.22.md` |
| An engineered System participates in a use situation through interactions under stated conditions. | `references/SYSE.5.md` |
| Engineering architecture decisions coordinate many later choices without deciding every detail. | `references/SYSE.6.md` |
| Engineering decisions rarely depend on one self-sufficient description. A controller-architecture decision can depend on a plant model and a … | `references/SYSE.7.md` |
| Many engineered results are usable only through an arrangement that continues beyond transfer of a product. | `references/SYSE.8.md` |
| Whole-System decisions combine results from unlike practices. For example, controller selection may depend on refrigeration performance, ele … | `references/SYSE.9.md` |
| Engineering decisions often precede complete knowledge. Models make alternatives cheap to explore; experiments and trials expose selected pa … | `references/SYSE.10.md` |
| Several recurring failures make this difficulty visible, often only after commitment. | `references/SYSE.24.md` |
| An architecture can name suitable bearers for required functioning while fabrication, adaptation, integration, configuration, installation o … | `references/SYSE.3.md` |
| Engineering Work often produces local completion before it produces a usable whole. | `references/SYSE.11.md` |
| Engineering results depend on more than the architecture of the project system-of-interest. | `references/SYSE.12.md` |
| For example, district drainage can depend on separately governed pump stations, gates, drainage networks, dispatch Systems, provider organiz … | `references/SYSE.18.md` |
| An engineered System does not become easier to evolve in isolation. A replaceable module may still require a fixture the factory lacks. | `references/SYSE.23.md` |
| Continuing engineering keeps several configurations relevant at once—for example, candidate architectures, manufactured variants, installed … | `references/SYSE.13.md` |
| One controller change can alter actual Systems, interfaces, and behaviour; change needed manufacturing or service Work; and invalidate descr … | `references/SYSE.14.md` |
| Engineering decisions depend on changing sources. For example, a supplier can revise a material limit, a standard can change an interface cl … | `references/SYSE.19.md` |
| an engineering decision depends on a claim from project focus, use and system concepts, architecture, realization, or a specialist practice … | `references/SYSE.4.md` |
| Systems Engineering is not one Method. Engineering different Systems—for example, a software-intensive controller, ship, building, electrica … | `references/SYSE.15.md` |
| Engineering does not normally proceed as one total sequence. Modeling can overlap implementation, evidence review can begin before a test fi … | `references/SYSE.20.md` |
| Systems Engineering changes through Methods, descriptions, tools, platforms, assignments, evidence arrangements, and practitioner population … | `references/SYSE.21.md` |
| practitioners repeatedly wait, redo work or ask for help through a platform, but the next investment is justified only by a preferred tool … | `references/SYSE.25.md` |
| a practitioner knows the engineering result needed next but must repeatedly discover how to request it, which inputs are acceptable, what a … | `references/SYSE.26.md` |
| independent changes by platform users, contributors or providers can break a supported interaction, or when every useful variation waits for … | `references/SYSE.27.md` |
| a justified constraint already exists but engineers must decide where and how a supported path will check or enforce it. | `references/SYSE.28.md` |
| a supported provision is changing or disappearing and users, retained state, dependencies or support promises still rely on it. | `references/SYSE.29.md` |
| a set of independently released components must work together and selecting each component separately leaves an unresolved dependency, share … | `references/SYSE.53.md` |
| two builds of “the same source” produce unexplained differences, a package cannot be rebuilt after a worker disappears, or nobody can recove … | `references/SYSE.30.md` |
| developers wait too long to learn whether a change works, rerun failures until they disappear, or receive green checks that do not answer th … | `references/SYSE.31.md` |
| a tested software package must cross an environment, storage service or provider boundary and someone needs to rely on it being the same qua … | `references/SYSE.32.md` |
| development or a test works only on one prepared machine, fails because of shared mutable state, or cannot be repeated after an environment … | `references/SYSE.33.md` |
| a software change can alter stored information, its interpretation, or which old and new consumers can use it. | `references/SYSE.34.md` |
| a software change can reach a bounded population before wider use, and observations from that population can change the next exposure decisi … | `references/SYSE.35.md` |
| a software service looks healthy in its infrastructure dashboard while users cannot complete their tasks, or when a reliability target exist … | `references/SYSE.36.md` |
| alerts for a software-service loss arrive too often, too late or without an action someone can take. | `references/SYSE.37.md` |
| a practitioner cannot obtain a supported result from a software platform, or receives an uncertain result after a failed attempt. | `references/SYSE.38.md` |
| a recurring manual or interrupt-driven platform activity grows with demand but produces little enduring improvement. | `references/SYSE.39.md` |
| bursts, expensive work or a failing dependency prevent other users from obtaining supported platform results. | `references/SYSE.40.md` |
| a verified software artifact must become an actual configured runtime on a named target. | `references/SYSE.41.md` |
| a person or technical agent has selected an external aid and the task depends on applying it to the intended input and using the actual resu … | `references/SYSE.42.md` |
| a person or technical agent resumes without a needed premise, or repeated work keeps reconstructing usable experience. | `references/SYSE.43.md` |
| people or technical agents could usefully divide a needed result, but preparation, dependencies or joining errors may consume the gain. | `references/SYSE.44.md` |
| a recurring task warrants changing model parameters or adapters, and qualified interaction experience can teach the targeted behavior. | `references/SYSE.45.md` |
| someone proposes relying on a person or technical agent with a particular support arrangement, or a change may alter useful performance. | `references/SYSE.46.md` |
| a person or technical agent needs a practicable procedure connecting available operations, or an existing procedure repeatedly fails to use … | `references/SYSE.47.md` |
| repeated work or a missing operation may justify a reusable tool or procedural aid. | `references/SYSE.48.md` |
| a named agent-development or comparison question lacks useful interaction experience. | `references/SYSE.49.md` |
| a person or technical agent repeatedly obtains unhelpful assistance, misses a needed contribution, or makes help decisions from poorly quali … | `references/SYSE.50.md` |
| a person or technical agent repeats uninformative work, spends the means needed to finish, or gives a consequential unresolved question too … | `references/SYSE.51.md` |
| useful material or means exist but are not usable by a person or technical agent at the next step: a worksheet hides its carry row, a source … | `references/SYSE.52.md` |

## Publication units

Non-pattern sections of the framework, reproduced as reference cards:

- `references/SYSE.Reference.md` — Architectural Reference
- `references/SYSE.Application.md` — Worked cases / cross-pattern applications
- `references/SYSE.Sources.md` — Source arguments and refresh

## Navigation rule

Start from the working difficulty, not file order. Follow each card's `Governing patterns` line and frontmatter `dependencies` when a needed result is missing.

## Single surface

`references/` is the canonical surface. `SKILL.md` is routing-only; there is no monolith to read. `INDEX.md` is reference-only.

## Lookup rules

- **Index first, then "no".** Check `references/INDEX.md` before searching. If an id is not listed there, the pattern does not exist — answer "no" and do not open files.
- **Read once.** Do not reopen a card you have already read.
