---
id: "_ctx.Part-C"
title: "Part C - Interpret, transform and compose computations"
---

# _ctx.Part-C: Part C - Interpret, transform and compose computations

---

## Part C - Interpret, transform and compose computations

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [CMP.12 - Construct an Interpreter or a Meaning-Preserving Translation](#cmp12---construct-an-interpreter-or-a-meaning-preserving-translation) | Stable | interpreter; compiler; semantics; binding; environment; control; observable behavior. How does an expression execute, and what must its translation preserve? | MATH.5/.17/.18 for expression composition and interpretation; C.29.3 when realizing the primitives. |
| 2 | [CMP.13 - Construct a Computational Abstraction for the Property Being Asked](#cmp13---construct-a-computational-abstraction-for-the-property-being-asked) | Stable | abstract interpretation; reachable states; sound approximation; fixed point; refinement. Which cheaper computation supports this property, and can its counterexample occur? | MATH.2/.18 for identification and interpretation; CMP.3/.4 for scheduling and exploration. |
| 3 | [CMP.14 - Compose Interacting Computations through Their Required Observations](#cmp14---compose-interacting-computations-through-their-required-observations) | Stable | concurrent algorithm; shared state; protocol; atomicity; interference; progress. Which interactions preserve the required whole behavior? | CMP.3/.10/.12 for dependencies, representation and semantics; C.29.3 for implementation assumptions. |
| 4 | [CMP.15 - Compose Independent Extensions of Data Variants and Operations](#cmp15---compose-independent-extensions-of-data-variants-and-operations) | Stable | expression problem; independent extension; data variants; operations; open recursion; joining implementation; dispatch; separate compilation. How can separately added forms and operations work together without changing old modules? | CMP.12 for interpretation; CMP.14 when interactions change observations; NOT.2 and NOT.3 for new expression structure and meaning. |
| 5 | [CMP.16 - Construct Computational Units and Operations for a Required Whole](#cmp16---construct-computational-units-and-operations-for-a-required-whole) | Stable | computational abstraction; units and operations; constructors; invariant; closure; refinement; composition. How can the units and allowed operations be changed together so that the required whole can be obtained and justified? | C.29.2 for the computational question; MATH.17/.18 for composition and interpretation; CMP.2/.10/.12/.14 for recursive construction, storage, execution meaning and interaction. |
