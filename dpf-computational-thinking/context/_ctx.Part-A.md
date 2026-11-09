---
id: "_ctx.Part-A"
title: "Part A - Construct an algorithm"
---

# _ctx.Part-A: Part A - Construct an algorithm

---

## Part A - Construct an algorithm

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [CMP.1 - Solve One Problem through Another or Transfer a Limit (Computational Reduction)](#cmp1---solve-one-problem-through-another-or-transfer-a-limit-computational-reduction) | Stable | reduction; solver reuse; input conversion; answer recovery; computability; complexity. Can this problem be solved through another one, and in which direction does a limit transfer? | C.29.2 for the required answer and computational model; MATH.17/.18 for composition and interpretation. |
| 2 | [CMP.2 - Derive a Recursive Procedure from a Problem Decomposition](#cmp2---derive-a-recursive-procedure-from-a-problem-decomposition) | Stable | recursion; decomposition; induction; sufficient return; termination. What must smaller problems return so that their answers construct the required whole? | MATH.4/.12 for inductive or extracted constructions; C.29.2 for the computational formulation. |
| 3 | [CMP.3 - Share and Schedule Repeated Subcomputations](#cmp3---share-and-schedule-repeated-subcomputations) | Stable | memoization; dynamic programming; sharing; dependency order; effects; storage; recomputation. Which repeated subcomputations can share an answer, in what order, and what should be retained or recomputed within the memory limit? | CMP.2 for the recurrence; CMP.10 for representation and operation costs. |
| 4 | [CMP.4 - Construct Computational Search with Justified Exclusions](#cmp4---construct-computational-search-with-justified-exclusions) | Stable | search; branch and bound; pruning; witness; completeness; interruption. Which alternatives can be excluded while preserving the requested answer? | MATH.20 for bounds; CMP.5 for relaxation; MMP.10 for a subject constraint formulation when needed. |
| 5 | [CMP.5 - Bound an Optimum or Recover a Feasible Candidate through a Relaxed Problem](#cmp5---bound-an-optimum-or-recover-a-feasible-candidate-through-a-relaxed-problem) | Stable | relaxation; feasible recovery; upper and lower bounds; approximation. How can an easier problem improve or bound an answer to the original problem? | MATH.20 for comparison; CMP.4 for bounded search; CMP.8 for controlled approximation. |
| 6 | [CMP.6 - Derive an Iterative Computational Update from Local Information](#cmp6---derive-an-iterative-computational-update-from-local-information) | Stable | local search; iterative update; neighborhood; step choice; noisy feedback; stopping. What does an admissible local change improve, and what follows on stopping? | MATH.10/.20/.21 for variation, bounds or convergence; CMP.7 for learning that needs an update. |
| 7 | [CMP.7 - Construct a Learner from Examples and Feedback](#cmp7---construct-a-learner-from-examples-and-feedback) | Stable | learning algorithm; rule class; inductive restriction; feedback; training fit; generalization. Which rule should examples select, and what supports its further use? | CMP.4/.6 for selection or updating; MMP.7 for a modeled data source; C.11.DUA for consequential additional inquiry. |
