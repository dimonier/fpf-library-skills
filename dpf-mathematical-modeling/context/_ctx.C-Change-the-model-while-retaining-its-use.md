---
id: "_ctx.C-Change-the-model-while-retaining-its-use"
title: C. Change the model while retaining its use
---

# _ctx.C-Change-the-model-while-retaining-its-use: C. Change the model while retaining its use

---

## C. Change the model while retaining its use

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [MMP.9 - Derive a Reduced Mathematical Model of State Evolution](#mmp9---derive-a-reduced-mathematical-model-of-state-evolution) | Stable | reduction; hidden state; closure; memory; approximation; error; sufficient bound. What contribution is left by eliminated detail, and which replacement preserves the consequence needed? | A.3.3.TR for evolution; C.29.1 for preserved structure; MMP.11 for a replacement family; B.5.RR for affected revision. |
| 2 | [MMP.17 - Construct a Surrogate for Selected Model Responses](#mmp17---construct-a-surrogate-for-selected-model-responses) | Stable | surrogate; selected response; input region; approximation; correction; tail; refinement. Which cheaper construction can supply the model response the next operation actually needs? | MMP.11 for retained structure; CMP.7 and CMP.6 for learning and updates; MMP.14 for consequential mismatch; MMP.18 for coupled use. |
| 3 | [MMP.18 - Couple Models with Compatible Exchanges and Scales](#mmp18---couple-models-with-compatible-exchanges-and-scales) | Stable | coupling; interface; scale; conservation; closure; shared uncertainty; double counting. How can component models exchange quantities and information without changing the required joint answer? | A.3.3.TR and MMP.10 for joint conditions; MATH.18 for retained consequences; MMP.9 and MMP.17 for missing contributions; CMP.8 and CMP.14 for interacting computation. |
| 4 | [MMP.20 - Obtain a Computable Continuation When Physical Constraints Change](#mmp20---obtain-a-computable-continuation-when-physical-constraints-change) | Stable | multimode DAE; changing constraints; consistent initialization; hot restart; mode-change array; impulse; event. How can a composed physical model continue when its active equations change? | MMP.18 for a joint model; A.3.3.TR for events and continuation; C.29.2 for effective computation; CMP.8 for numerical approximation; subject laws for the transition. |
