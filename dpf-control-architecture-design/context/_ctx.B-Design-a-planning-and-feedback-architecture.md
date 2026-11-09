---
id: "_ctx.B-Design-a-planning-and-feedback-architecture"
title: "B. Design a planning-and-feedback architecture"
---

# _ctx.B-Design-a-planning-and-feedback-architecture: B. Design a planning-and-feedback architecture

---

## B. Design a planning-and-feedback architecture

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| --- | --- | --- | --- | --- |
| B.1 | [CAD.1 - Derive a Control Decomposition from the Whole Problem](#cad1---derive-a-control-decomposition-from-the-whole-problem) | Stable | Control decomposition; information; horizon; computational burden. “Should these decisions be separated?” | Uses C.39 and MMP.9; CAD.2 develops the selected exchange; CAD.4 compares whole candidates. |
| B.2 | [CAD.2 - Construct the Planning and Feedback Interface](#cad2---construct-the-planning-and-feedback-interface) | Stable | Reference meaning; state reconstruction; sample-and-hold; reset; tracking dynamics. “What does the lower loop actually receive?” | Uses the selected decomposition and MMP.18; CAD.5:4.7 supplies the estimate-based branch. |
| B.3 | [CAD.3 - Construct a Jointly Admissible Command Domain](#cad3---construct-a-jointly-admissible-command-domain) | Stable | Invariant error; input reserve; constraint tightening; continuation. “Which commands can remain feasible?” | Uses CAD.2's connected dynamics; CAD.5:4.7 when state is estimated; returns to CAD.1 or CAD.2 on incompatibility. |
| B.4 | [CAD.4 - Co-design and Realize the Whole Control Architecture](#cad4---co-design-and-realize-the-whole-control-architecture) | Stable | Model order; gains; rates; deadlines; whole-candidate comparison. “Which feasible arrangement should be realized?” | Receives applicable CAD.1–CAD.3 and CAD.5 results; uses MMP.22; supplies the broader SYSE.6 decision. |
