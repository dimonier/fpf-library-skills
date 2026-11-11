# OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK — Pattern Index

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| OPS.Reference | **OPS.Reference:1 - Start from a difficulty in continuing operation** | — | — | — |
| OPS.23 | **Connect Operational Reasoning — The Operational Mantra** | Stable | — | OPS.1; relevant OPS.3–OPS.22; FPF A.1.STM |
| OPS.1 | **Identify the Operating System, Commitments, and Flow Units** | Stable | — | FPF A.1.SCR, A.6.REL, C.2.1, A.10 |
| OPS.2 | **Select Work-Management Views and Coordination Methods** | Stable | — | OPS.1; FPF A.22, C.29; conditional C.30.LCA, B.2.5, C.27.TA |
| OPS.3 | **Distinguish Operating Subjects, Cases, Queues, Resources, and Records** | Stable | — | OPS.1, OPS.2; FPF A.6.REL, C.2.1; conditional B.2.5 |
| OPS.4 | **Keep Current Operating State Recoverable Across Participants** | Stable | — | OPS.2, OPS.3; FPF C.2.1, A.10, A.15.8; conditional C.30.LCA |
| OPS.5 | **Admit Work and Limit Starts** | Stable | — | OPS.2, OPS.3, OPS.4; FPF C.11, A.10 |
| OPS.6 | **Continue Cases and Handle Exceptions** | Stable | — | OPS.5; FPF A.15.7, C.11, A.10 |
| OPS.7 | **Manage Aging, Urgency, and Service Commitments** | Stable | — | OPS.6 evidence; FPF C.27.TA; conditional C.27, C.11 |
| OPS.8 | **Coordinate Queues and Buffers** | Stable | — | OPS.3, OPS.4; conditional OPS.9–OPS.11; FPF C.16, A.22, E.18 |
| OPS.8.1 | **Choose Work-Release Rules When Earlier Work Can Return** | Stable | — | OPS.8, OPS.5; conditional OPS.10.1 and OPS.10.2, OPS.15.1, MMP.8 and MMP.8.SD |
| OPS.8.2 | **Use Protective Capacity While Keeping It Available** | Stable | — | OPS.8; conditional OPS.10.1 and OPS.10.2, OPS.12, C.40.OI and C.40.DC, HCD.2, C.39.MF and A.3.1.WT |
| OPS.9 | **Diagnose and Treat the Current Operating Constraint** | Stable | — | OPS.3, OPS.4; conditional OPS.8, OPS.10, OPS.11; FPF C.16, C.28, C.11.CRC |
| OPS.10 | **Qualify Operating Capacity Under Variability** | Stable | — | OPS.3, OPS.4; conditional OPS.8, OPS.9, OPS.11; FPF C.16, C.27.TA, C.11.CRC |
| OPS.10.1 | **Construct and Compare Operating Capacity Models** | Stable | — | OPS.10, OPS.11.1, OPS.15.1; conditional OPS.10.2, MMP.7 and MMP.13, CMP.9; FPF C.29, C.11.CRC |
| OPS.10.2 | **Construct and Revise a Feasible Deadline Schedule** | Stable | How can a schedule meet the deadline with precedence, shared resources and calendar gaps | OPS.10, OPS.11.1, OPS.15.1; conditional OPS.10.1, OPS.7 and OPS.8, MMP.10, CMP.4 and CMP.5; FPF C.29 |
| OPS.11 | **Coordinate Interacting Operating Structures** | Stable | — | OPS.3, OPS.4; conditional OPS.8–OPS.10; FPF A.22, E.18.NET, C.11.CRC |
| OPS.11.1 | **Construct and Reconcile Operating Models Across Scales** | Stable | — | OPS.11, OPS.19; conditional OPS.15.1, MMP.10 and MMP.18; FPF A.22.CGUS, E.18.3, C.29 |
| OPS.12 | **Protect Human Conditions in Operating Decisions** | Stable | — | OPS.3; conditional OPS.10, OPS.13–OPS.15; FPF C.16, A.10, A.11.OP |
| OPS.13 | **Align Commitments, Resources, and Service Outcomes** | Stable | — | conditional OPS.10, OPS.12, OPS.14, OPS.15, OPS.18; FPF A.10, C.16 |
| OPS.14 | **Relate Throughput, Cash, and Operating Consequences** | Stable | — | conditional OPS.10, OPS.12, OPS.13, OPS.15; FPF C.16, A.10, A.11.OP |
| OPS.15 | **Build a Decision-Specific Operating Account** | Stable | — | OPS.3; conditional OPS.4, OPS.12–OPS.14, OPS.18; FPF C.16, A.10, E.13, A.11.OP |
| OPS.15.1 | **Derive Operating Quantities from Events** | Stable | — | OPS.15; conditional OPS.11.1; FPF C.16, C.29; MMP.7 for an observation model |
| OPS.16 | **Decide Whether and How to Change an Operating Method** | Stable | What does bounded evidence support: adopting, revising or branching an admitted operating Method, retaining or revising a candidate account, testing Method identity, stopping | OPS.15, OPS.17 and OPS.18; applicable OPS.10–OPS.13, OPS.19; conditional OPS.11.1, OCE.11; A.3.1.WT, A.3.1.CC, A.3.1.FT, C.11.MV, A.3.1.MV and A.3.1.MI; FPF A.3.1.MR, A.3.1, A.3.2, A.15.1, A.15.2, A.10, C.16 |
| OPS.17 | **Compare and Refresh Operations Methods** | Stable | — | A.3.1.MV; conditional OPS.5–OPS.15, OPS.18, OPS.22, KCAE.MEMORY, KCAE.CHANGE, KCAE.EVAL, CB.14, A.3.1.WT, A.3.1.FT, C.11.MV; FPF A.3.1, A.3.2, C.16, G.5, A.11.OP |
| OPS.18 | **Control Operating Quality and Reliability** | Stable | — | conditional OPS.12–OPS.15, OPS.17; FPF C.16, A.10, A.11.OP |
| OPS.19 | **Reconcile Simultaneous Operating Work Across Cases and Scales** | Stable | — | OPS.1, OPS.3; conditional OPS.11, OPS.12, OPS.15, OPS.17; FPF C.32.MWA, C.11 |
| OPS.20 | **Deliberately Continue and Change Operations Culture** | Stable | — | OPS.16, OPS.17, OPS.19; FPF C.36; C.36.MC |
| OPS.21 | **Choose Operating Aims, Targets and Comparisons** | Stable | — | conditional OPS.1, OPS.10, OPS.13, OPS.15, OPS.19, STR.5 and STR.8, MA.1, MA.2, MA.5 and MA.6, OCE.10 |
| OPS.22 | **Interpret Operating Performance and Decide the Response** | Stable | — | conditional OPS.13, OPS.15, OPS.19, OPS.21, MA.7 and MA.9, OCE.10; HCD.11 and CGOV.13 for distinct receiving questions |
| OPS.Application | **OPS.Application:1 - APP-OPS-01 — PumpWorks continuing control-service operation** | — | — | — |
| OPS.Sources | **OPS.Sources:1 - Bibliographic returns for shared sources** | — | — | — |

## Cross-references
- Full monolith: `OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md`
