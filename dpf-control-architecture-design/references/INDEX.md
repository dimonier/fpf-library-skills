# CONTROL-ARCHITECTURE-DESIGN-PRINCIPLES-FRAMEWORK — Pattern Index

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| CAD.Reference | **CAD.Reference:1 - What the language helps obtain** | — | — | — |
| CAD.5 | **Choose Observations and Internal State for Control** | Stable | Delayed observation, partial sensing, action history, information state, set estimation. “Which sensors and memory let this controller act within its limits?” “Can any action work with these observations?” | Uses A.3.3.PI and C.32.LCA; the main use is self-contained. CAD.2–CAD.4 are conditional receivers of :4.7. |
| CAD.1 | **Derive a Control Decomposition from the Whole Problem** | Stable | Control decomposition, information, horizon, computational burden. “Should these decisions be separated?” | Uses C.39 and MMP.9; CAD.2 develops the selected exchange; CAD.4 compares whole candidates. |
| CAD.2 | **Construct the Planning and Feedback Interface** | Stable | Reference meaning, state reconstruction, sample-and-hold, reset, tracking dynamics. “What does the lower loop actually receive?” | Uses the selected decomposition and MMP.18; CAD.5:4.7 supplies the estimate-based branch. |
| CAD.3 | **Construct a Jointly Admissible Command Domain** | Stable | Invariant error, input reserve, constraint tightening, continuation. “Which commands can remain feasible?” | Uses CAD.2's connected dynamics; CAD.5:4.7 when state is estimated; returns to CAD.1 or CAD.2 on incompatibility. |
| CAD.4 | **Co-design and Realize the Whole Control Architecture** | Stable | Model order, gains, rates, deadlines, whole-candidate comparison. “Which feasible arrangement should be realized?” | Receives applicable CAD.1–CAD.3 and CAD.5 results; uses MMP.22; supplies the broader SYSE.6 decision. |

## Cross-references
- Full monolith: `CONTROL-ARCHITECTURE-DESIGN-PRINCIPLES-FRAMEWORK.md`
