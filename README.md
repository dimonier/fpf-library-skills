# FPF Library — Agent Skills

**Methods for solving difficult problems, expanding what you can do, and continuing development** — packaged as portable agent skills.

This repository repackages the [First Principles Framework (FPF) Library](https://github.com/ailev/FPF) by [Anatoly Levenchuk](https://github.com/ailev) into the standard **agent-skill** format (`SKILL.md` + `assets/` + `references/` + `context/`). Each top-level folder is a self-contained skill that an AI coding agent loads on demand.

> This is an independent repackaging for agent use. It is not an official FPF publication and is not endorsed by Anatoly Levenchuk. The framework text is his, under CC BY 4.0; the packaging and tooling are reproduced here under their own terms (see [NOTICE.md](NOTICE.md)).

## What's inside

| | |
|---|---|
| `fpf-core` | The complete FPF Core (400+ patterns) — canonical monolith in `assets/`, decomposed per-pattern references, reader-help context cards. Root of the dependency chain. |
| `dpf-*` (40 skills) | Domain Principle Frameworks: 36 subject frameworks + 4 Suite References, in the same source-faithful shape. |
| `fpf-library-sync` | Maintenance tooling that rebuilds the skills (both `fpf-core` and the `dpf-*` fleet) from the canonical library. |

Every content skill reads the same way: **bring a situation, find the pattern, apply it, check the result** — never read a whole framework cover-to-cover.

## Skill index

### Core

| Skill | DocID | Covers |
|---|---|---|
| [`fpf-core`](fpf-core/SKILL.md) | FPF | Transdisciplinary concepts and methods: methodological work, architecture, decision and development. |

### Engineering Suite

| Skill | DocID | Framework |
|---|---|---|
| [`dpf-systems-engineering`](dpf-systems-engineering/SKILL.md) | SYSE | Defining the system, designing, realizing, integrating, qualifying and changing it. |
| [`dpf-semantic-integration-engineering`](dpf-semantic-integration-engineering/SKILL.md) | SIE | Making separately governed meanings usable together. |
| [`dpf-control-architecture-design`](dpf-control-architecture-design/SKILL.md) | CAD | Choosing observations and memory; planning-and-feedback arrangements. |
| [`dpf-maintenance-engineering-and-management`](dpf-maintenance-engineering-and-management/SKILL.md) | MNT | Maintenance policy, interventions, restoring functioning, return to use. |
| [`dpf-knowledge-corpus-access-engineering`](dpf-knowledge-corpus-access-engineering/SKILL.md) | KCAE | Finding, reading and using documentary knowledge with provenance. |
| [`dpf-engineering-reference`](dpf-engineering-reference/SKILL.md) | — | Engineering Suite Architectural Reference. |

### Management Suite

| Skill | DocID | Framework |
|---|---|---|
| [`dpf-strategy`](dpf-strategy/SKILL.md) | STR | Worthwhile direction; options, capabilities, investments, business models. |
| [`dpf-goal-construction-and-regulation`](dpf-goal-construction-and-regulation/SKILL.md) | GOALS | Goals and achievement evidence; complete OKR/CFR. |
| [`dpf-operations-management`](dpf-operations-management/SKILL.md) | OPS | Operating arrangements; work, provision, service and improvement. |
| [`dpf-marketing`](dpf-marketing/SKILL.md) | MKT | Customer inquiry, offers, acquisition, distribution and use. |
| [`dpf-corporate-governance`](dpf-corporate-governance/SKILL.md) | CGOV | Corporate powers, decisions, controls and accountability. |
| [`dpf-corporate-finance`](dpf-corporate-finance/SKILL.md) | FIN | Financial parties, positions, rights, obligations, events and flows. |
| [`dpf-management-accounting`](dpf-management-accounting/SKILL.md) | MA | Costs, capacity, economic consequences; forecasting. |
| [`dpf-leadership`](dpf-leadership/SKILL.md) | LDR | Directing personal action; joint direction and responsibility. |
| [`dpf-human-resource-management`](dpf-human-resource-management/SKILL.md) | HRM | Workforce conditions, assessment, reward, voice, protection. |
| [`dpf-community-management`](dpf-community-management/SKILL.md) | CB | Participation, relationships, shared practices, contributions. |
| [`dpf-customization-and-productization-management`](dpf-customization-and-productization-management/SKILL.md) | CUST | Client differences while developing repeatable offerings. |
| [`dpf-engineering-asset-management`](dpf-engineering-asset-management/SKILL.md) | EAM | Use, renewal, replacement and other asset changes over time. |
| [`dpf-organization-administration`](dpf-organization-administration/SKILL.md) | ADM | Requests, permissions, obligations, provision, records. |
| [`dpf-organization-change-engineering`](dpf-organization-change-engineering/SKILL.md) | OCE | Organizational changes to contributions, roles, authority, interfaces. |
| [`dpf-management-reference`](dpf-management-reference/SKILL.md) | — | Management Suite Architectural Reference. |

### Foundational Thinking Suite

| Skill | DocID | Framework |
|---|---|---|
| [`dpf-mathematical-modeling`](dpf-mathematical-modeling/SKILL.md) | MMP | Relating a subject question to mathematics; infer, predict, compare interventions. |
| [`dpf-mathematical-thinking`](dpf-mathematical-thinking/SKILL.md) | MATH | Mathematical objects, operations and alternatives. |
| [`dpf-physical-thinking`](dpf-physical-thinking/SKILL.md) | PHY | Constructing and testing physical accounts. |
| [`dpf-notational-engineering`](dpf-notational-engineering/SKILL.md) | NOT | Expressions, interpretations and transformations. |
| [`dpf-computational-thinking`](dpf-computational-thinking/SKILL.md) | CMP | Algorithms within correctness, resource and interaction conditions. |
| [`dpf-foundational-thinking-reference`](dpf-foundational-thinking-reference/SKILL.md) | — | Foundational Thinking Suite Architectural Reference. |

### Human Capability Engineering Suite

| Skill | DocID | Framework |
|---|---|---|
| [`dpf-human-capability-development`](dpf-human-capability-development/SKILL.md) | HCD | Capability demand, programmes, learning products, feedback, transfer, retention. |
| [`dpf-somatic-movement-modeling`](dpf-somatic-movement-modeling/SKILL.md) | SOM | Bodily experience, regulated effort, coordinated movement. |
| [`dpf-human-capability-engineering-reference`](dpf-human-capability-engineering-reference/SKILL.md) | — | Human Capability Engineering Suite Architectural Reference. |

### Further domain frameworks

| Skill | DocID | Framework |
|---|---|---|
| [`dpf-decision-design`](dpf-decision-design/SKILL.md) | PSDA | Decision problems, alternatives, consequences and uncertainty. |
| [`dpf-explanation-design`](dpf-explanation-design/SKILL.md) | EXD | Explanations, worked examples and dialogues. |
| [`dpf-narrativization-and-narrative-studies`](dpf-narrativization-and-narrative-studies/SKILL.md) | NSTD | Followable narratives; working and fictional accounts. |
| [`dpf-research-method-practice`](dpf-research-method-practice/SKILL.md) | RMP | Framing research, evidence, synthesis, warranted contribution. |
| [`dpf-implementation-facilitation`](dpf-implementation-facilitation/SKILL.md) | IS | Putting evidence-informed practice to use under local conditions. |
| [`dpf-defense-and-transmission-modeling`](dpf-defense-and-transmission-modeling/SKILL.md) | DTM | How practices persist and spread; protective action. |
| [`dpf-economic-reasoning-and-coordination`](dpf-economic-reasoning-and-coordination/SKILL.md) | ECO | Exchange, commitments, incentives, shared resources, coordination. |
| [`dpf-embodied-rhythmics`](dpf-embodied-rhythmics/SKILL.md) | RHY | Rhythmic relations; sound, movement, reference, layers. |
| [`dpf-music-and-dance-practice-engineering`](dpf-music-and-dance-practice-engineering/SKILL.md) | MDPE | Music and dance practices; tools, environments, styles. |
| [`dpf-financial-domain-modeling`](dpf-financial-domain-modeling/SKILL.md) | FDM | Financial parties, positions, rights, obligations, events and flows. |

### Tooling

| Skill | Role |
|---|---|
| [`fpf-library-sync`](fpf-library-sync/SKILL.md) | Rebuilds `fpf-core` from `FPF-Spec.md` and builds / refreshes the `dpf-*` skills from the FPF Library `DPFs/**` monoliths. |

## Repository layout

```
skills/
├── fpf-core/                  # Core skill (root of the dependency chain)
│   ├── SKILL.md               # routing + entry-table + reading discipline
│   ├── LICENSE                # CC BY 4.0 (full text)
│   ├── NOTICE.md              # source / packaging / third-party split
│   ├── assets/FPF-Spec.md     # canonical monolith, verbatim
│   ├── references/*.md        # one file per pattern (400+)
│   └── context/               # entry cards + USING-FPF instruction
├── dpf-*/                     # 40 domain skills, same shape
└── fpf-library-sync/          # MIT tooling (scripts/) — builds fpf-core + dpf-*
```

Each DPF skill holds `assets/<MONOLITH>.md` (the framework source), `references/<PID>.md`
(source-faithful per-pattern decomposition), `context/` (reader help), `SKILL.md`
(routing), `LICENSE` and `NOTICE.md`.

## Installing / using

Copy the skills you need into your agent's skills directory, or point the agent at this
repo directly. Examples:

- **Claude Code** — `.claude/skills/<name>/`
- **OpenCode** — `skills/<name>/`
- Any agent that follows the `SKILL.md` convention.

`fpf-core` is the root; the `dpf-*` skills link back to it. Load `fpf-core` first when
you need the governing patterns, then the relevant `dpf-*` for the domain mechanism.

## Building from source

To regenerate the skills from the canonical library:

```bash
# fpf-core, from FPF-Spec.md:
python fpf-library-sync/scripts/sync_fpf_core.py            # full sync
python fpf-library-sync/scripts/sync_fpf_core.py --check    # check only

# DPF skills, from DPFs/**:
python fpf-library-sync/scripts/sync_library.py --validate
python fpf-library-sync/scripts/sync_library.py --dry-run
python fpf-library-sync/scripts/sync_library.py     # full build
```

Requires Python 3.10+ (and `git` in PATH for the `fpf-core` path). See the tool's `SKILL.md`.

## Status

The skills are a **source-faithful decomposition**: pattern bodies are reproduced from
the current FPF Library working edition and are not independently re-validated beyond the
source's own status markers. The library is an "eternal alpha" — continuously revised.
When a specific pattern's identity matters, cite the publication, edition and complete
PatternID, and check the upstream repository for the latest edition.

## License and attribution

- **FPF framework text** (`assets/`, pattern bodies in `references/` and `context/`) —
  © Anatoly Levenchuk, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). See
  [LICENSE](LICENSE) and each skill's `NOTICE.md` for the exact change notes.
- **Packaging and routing** (`SKILL.md` dispatcher text, `description`, `INDEX.md`, this
  README) — © Dmitry Ulanov, CC BY 4.0.
- **Tooling** (`fpf-library-sync/` scripts) — © Dmitry Ulanov,
  [MIT](https://opensource.org/licenses/MIT).
- **Third-party material** quoted inside the framework text remains with its own rights
  holders.

Full split: [NOTICE.md](NOTICE.md).

## Credits

- [Anatoly Levenchuk](https://github.com/ailev) — First Principles Framework, FPF Library.
- Dmitry Ulanov — agent-skill packaging and maintenance tooling.