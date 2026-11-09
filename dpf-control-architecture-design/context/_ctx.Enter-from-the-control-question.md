---
id: "_ctx.Enter-from-the-control-question"
title: Enter from the control question
---

# _ctx.Enter-from-the-control-question: Enter from the control question

---

## Enter from the control question

| Your working difficulty | Obtain first | Direct entry |
| --- | --- | --- |
| A useful observation arrives after the action deadline, or different channels reveal different parts | An observation and memory arrangement, its error bound and the actions it permits; or a precise information limitation | [CAD.5](#cad5---choose-observations-and-internal-state-for-control) |
| One calculation cannot use the needed horizon, information and execution time together | Competing decompositions and the couplings each would remove | [CAD.1](#cad1---derive-a-control-decomposition-from-the-whole-problem) |
| Planner and feedback code use a “reference” with different timing or meaning | The actual exchange and its derived error dynamics | [CAD.2](#cad2---construct-the-planning-and-feedback-interface) |
| A stable controller cannot follow the requested command within state or actuator limits | A jointly admissible command/error domain with continuation, or a specific incompatibility | [CAD.3](#cad3---construct-a-jointly-admissible-command-domain) |
| A more accurate model, faster planner or extra sensor competes for limited resources | A comparison of complete feasible arrangements and the conditions of their realization | [CAD.4](#cad4---co-design-and-realize-the-whole-control-architecture) |

An engineer can use CAD.5 without introducing a planner or multiple layers. An engineer with a qualified lower loop can retain it and change command admission. If a current complete observation and a simple controller already meet the task, they remain a serious stopping alternative. Read the [Architectural Reference](#control-architecture-design-architectural-reference) when several results must fit together or a change reopens their conditions.

The intended reader can work with state-space models, feedback laws, bounded sets and elementary optimization. A reader who lacks those means needs instruction or a qualified control-engineering contributor. The examples are mathematical constructions. Before relying on a physical installation, establish its model, uncertainty and execution premises.
