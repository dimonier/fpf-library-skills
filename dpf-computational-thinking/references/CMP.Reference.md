---
id: CMP.Reference
title: "CMP.Reference:1 - Problem frame and the algorithmic difficulty"
---

# CMP.Reference: CMP.Reference:1 - Problem frame and the algorithmic difficulty

> **Problem frame:** Use this language when you need to obtain, understand, analyze or change an effective way of computing. The work can concern a finite answer, a continuing response, a learning rule, or several processes whose interaction matters.
> **First move:** Suppose a finite list contains individually identified options. Each may be chosen at most once. Costs are positive integers and values are nonnegative integers.

---

## CMP.Reference:1 - Problem frame and the algorithmic difficulty

Use this language when you need to obtain, understand, analyze or change an effective way of computing. The work can concern a finite answer, a continuing response, a learning rule, or several processes whose interaction matters. A practitioner may design the way, inspect one proposed by an AI agent, explain its grounds, or change the division of computation among descriptions, implementations and performers. The first difficulty can precede a recognizable algorithm: what should count as an input, an operation, a state or a useful observation is still open.

The domain is algorithmics within computer science. Its connected subject is effective computation: how descriptions and operations generate possible processes, how those processes obtain meaningful results, how computational ways can themselves be obtained and changed, and what limits their use. A repertoire of named algorithms supplies examples and reusable means; it does not replace this subject. The field is also narrower than every question about computers or human thought. A physical mechanism, an organizational responsibility and a subject model need their own explanations when the computational account depends on them.

### CMP.Reference:1.1 - A description specifies a family of possible processes

Distinguish a computational description from an execution. A description gives rules for operations, choices, state change and interaction under a computational model. An execution is one process admitted by those rules with particular inputs and environmental behavior. The same finite description can admit indefinitely many inputs and executions. It can describe a calculation that returns, a generator that yields further values, or a service that remains available for events. A nondeterministic schedule or random choice can admit several executions even for one input.

This distinction makes an algorithmic guarantee possible and limits it. A guarantee concerns an admitted family, not just the trace that was inspected. One test can expose a counterexample; a general claim needs an argument appropriate to that family. Conversely, a failure outside the admitted conditions does not establish a failure within them, although it may show that the conditions do not serve the actual work. CMP.1 transfers obtainability or a limit only through its justified conversion; CMP.11 derives a resource limit from what every allowed computation must distinguish.

An effective operation is available at a stated level. Comparing two bounded words, evaluating a supplied function, requesting a remote result and choosing a mathematically existing witness are not interchangeable primitives. If a needed operation is missing, its name is a construction obligation. Another algorithm may implement it, a physical system may supply it under qualified conditions, or no suitable means may yet be known. C.29.2 develops that formulation and returns to it when the proposed operations do not obtain the required answer.

The recipient determines the relevant observations. A final number can suffice for one calculation. Another use needs an attaining object, the order of emitted events, an error, an exception, termination, or continued responsiveness. An abstract step can correspond to several implementation steps, but a correspondence that ignores visible intermediate behavior can fail in an interacting context. CMP.12 develops the execution meaning; CMP.14 handles consequential interaction. Keeping those observations explicit prevents a successful value calculation from being mistaken for the required whole behavior.

### CMP.Reference:1.2 - Mathematical, physical and algorithmic grounds cooperate

Mathematical thinking constructs objects, operations and relations, and establishes consequences under assumptions. It includes synthesis and constructive proof, not only checking a finished proposal. A definition or existence proof can nevertheless leave an effective obtaining operation unspecified. MATH.4 and MATH.12 supply constructive arguments; CMP.2 uses such arguments to obtain base cases, recursive questions and a sufficient join. The computational contribution includes whether the stated choices can be carried out and what their unfolding costs.

Physical thinking investigates possible and actual processes, the interactions and conditions that produce them, and the observations that support or challenge an account. It too constructs explanations and arrangements. A device's physical evolution becomes a realization of a computation only through a justified relation among preparation, evolution and interpreted readout. C.29.3 develops this relation. A formal instruction to perform an indivisible update does not establish that a particular device or service supplies it; a fast measured response does not establish all of the algorithm's permitted behaviors.

Algorithmic thinking concentrates on effective organization: which operations obtain the wanted observations, how their composition and interpretation work, which ways can be generated or transformed, and how information and resource conditions constrain the result. Its arguments can be mathematical, and its implementations physical. These are overlapping contributions with different questions, not exclusive professions or three competing standards of truth.

For example, a mathematical account can prove that a composed operation preserves a quantity. The algorithmic account must obtain that operation from available steps, cover its admitted inputs and account for progress and cost. A physical account must establish that the prepared arrangement supplies those steps and observations at the intended scale. A changed arithmetic primitive, communication delay or observable event can invalidate one connection while leaving the other arguments useful. B.5.MPC coordinates the contributions; C.29 connects the modeled result to the subject work that will use it.

### CMP.Reference:1.3 - Build a whole, introduce a level, and generalize deliberately

Decomposition proposes parts whose results might help. Synthesis constructs their connection so that the required whole is obtained. Ask both directions: what does the whole require from each contribution, and what can the available contributions actually produce together? A set of individually correct components can lose a needed distinction at their join or rely on incompatible states, observations or progress conditions. CMP.2 develops this question for recursive answers; CMP.14 for interacting computations; CMP.15 for independently extended forms and operations. These are different constructions, not instances of an automatic rule that good parts make a good whole.

Abstraction establishes a useful level of objects and operations. The level retains distinctions needed by its uses while hiding how those operations are obtained below it. It can introduce a compound unit and new operations rather than merely remove detail. A queue, an expression with binding and a summary of a sequence have different useful operations; none is selected just by counting stored fields. [CMP.16](#cmp16---construct-computational-units-and-operations-for-a-required-whole) develops the joint construction of units, admissible operations and their whole behavior. CMP.10 can then compare stored representations for those operations. CMP.13 has a distinct purpose: a cheaper analysis that soundly approximates the behavior being investigated. An analysis may deliberately admit extra possibilities; a replacement implementation must preserve the observations its users rely on.

Generalization extends the claim to a family of cases on a stated ground. An invariant, structural argument or qualified statistical account can support such an extension; a broader name or another successful example cannot. If a chunk summary combines correctly for every admitted pair, induction can establish its use for every finite assembly. This still leaves out a new observation that the summary discarded. If an interaction argument assumes one writer, adding writers changes a premise rather than simply making the old example larger. CMP.7 develops the separate statistical question of further use of a learned rule.

Levels can be nested: an operation treated as elementary in one algorithm may be a composite algorithm at another level; an interpreter can itself be interpreted. Composition, generalization and abstraction remain different relations. An implementation is not a smaller subtype of its specification, and representing something does not make that thing a part of the representation. Keep the relation that supports the particular inference instead of using one hierarchy for all of them.

### CMP.Reference:1.4 - Descriptions can be computed with, and ways can be obtained

A computational description can be represented as data. An interpreter executes its rules; a translator produces another description; an analyzer obtains a claim about possible executions. These are different results. CMP.12 constructs interpretation and meaning-preserving translation, while CMP.13 constructs a sound approximation for an analysis question. Binding, state, control and the chosen observations determine their connection. Calling a text a program supplies none of those rules by itself.

This enables more than repeated execution. A search can explore descriptions of candidate algorithms, and a learner can obtain a rule from examples or feedback. The outer computation needs an effective candidate representation, ways to propose or change candidates, and a criterion it can actually evaluate. The resulting rule has another use with its own inputs and consequences. CMP.4 supplies justified search exclusions; CMP.6 develops updates from local information; CMP.7 connects the learner, its selected rule and further use. A good update is one contribution to a learner, not a guarantee about every later prediction or action. The Suite Reference's §3.10 develops this connection for learned controllers and changing computational organizations.

Universal execution, approximation, learning and practical accessibility answer different questions. A universal interpreter can simulate the computations expressible in its admitted model; that claim does not supply a solver for every stated problem or a favorable runtime. An approximation theorem can establish that a representation of sufficient quality exists while leaving its size and obtaining procedure unsettled. A learner's useful generalization depends on restrictions and evidence connecting observed and future cases. A physically available arrangement adds its own preparation, accuracy, energy, storage and communication conditions. Do not use any one of these claims as a substitute for the others.

General search and learning can reduce the amount of case-specific behavior that people must prescribe. They still embody choices of representation, feedback, interaction and resources. More computation can improve a result only through a way that can use it; it cannot recover information absent from the available observations or validate an unrelated objective. A failed attempt can therefore call for another algorithm, another representation, a better source of evidence or a changed useful question. It need not call for a larger run of the same method.

### CMP.Reference:1.5 - A computation can be part of a larger computational practice

Reasoning about one algorithm can isolate its input, operations and result. Reasoning about many computations must also explain their dependencies, communication, effects and joint progress. Development by several contributors introduces another question: what independently supplied descriptions and implementations can be combined without leaving a semantic case missing? CMP.14 addresses interacting execution; CMP.15 addresses independent extension. Multiple authors do not necessarily imply concurrent execution, and multiple executing processes do not establish independent development.

People, machines and groups can supply computational contributions when the corresponding operations, interpretation and support are established. A person following a rule, an AI proposing a description, and a machine running that description make different contributions. No general equivalence of their capabilities follows. The preparation needed to learn a method, access a performer or maintain a working arrangement remains part of the receiving practice; a description's availability does not supply it. Core's Method-development and provision methods handle those questions when they matter.

Algorithmics forms a connected discipline because its knowledge constrains its reusable practice and the results of practice can challenge that knowledge's application. An invariant determines permissible composition; a counterexample can expose an inadequate observation or a false preservation claim; measured costs can challenge a cost model; new algorithms can change what is practically obtainable. A method replacement preserves the field's central inquiry when these connections remain, even if the repertoire changes. Adding unrelated computer topics under one title would not supply that connection. Likewise, use of a mathematical or physical result does not by itself make one discipline a constituent of another; an actual larger assembly needs an explanation of what their connection makes possible.

### CMP.Reference:1.6 - Use the grounds to choose and revise a method

Start with elementary preparation: following operations on inputs and retained state, recognizing an observation, and distinguishing one execution from the intended family. Individual methods supply additional constructions. Recursion needs a progress relation and an inductive argument; randomization needs a probability account; a numerical update can need variation and error bounds. Obtain a missing contribution through its full supplier before relying on the result it supports. Familiarity with a method's name is not that preparation.

Follow the actual missing relation. If the answer can be recovered from another solver, CMP.1 can close the need. If joining smaller answers fails, CMP.2 changes what they return. If the available units and operations make the whole awkward or unobtainable, CMP.16 constructs another organization. If repeated work dominates, CMP.3 asks what can be shared; if operations are expensive because of storage, CMP.10 changes the representation. These choices follow from the problem exposed by the common account, not from the order of the Parts.

A resource limit can reopen the answer condition and select approximation or sampling through CMP.8 or CMP.9. A semantic mismatch calls for CMP.12 or the subject interpretation, not merely more computation. A failed shared history calls for CMP.14. A learned rule failing on new cases returns to the conditions of CMP.7; a noisy proposed update can remain unresolved under CMP.6 rather than being declared an improvement. When a required guarantee is impossible in the chosen model, CMP.1 or CMP.11 can justify changing the model, obtaining information or negotiating another result instead of repeatedly searching for the same guarantee.

Bring the local answer back to the whole. Determine whether it supplies the receiving operation under the same meaning, observations and resource conditions. Preserve the constructions whose premises remain valid; revise the affected connection or boundary when they do not. The result can be a complete computation, a useful qualified contribution, or a precise missing operation. Use a known adequate way directly when no further construction, interpretation or assurance would change the work's continuation.

## CMP.Reference:2 - Forces that shape the construction

| Requirement | Choice it creates |
| --- | --- |
| A useful answer | A decision, one witness, every witness, an approximation and a continuing response can require different procedures. |
| Feasible resources | Conversion, preprocessing, memory, communication and output can dominate the apparent main computation. |
| Sufficient retained information | Sharing or summarizing work saves resources while potentially discarding a later-required distinction. |
| A justified conclusion | Small executions help expose a failure; a general guarantee needs an argument covering its admitted inputs and operations. |
| Useful results under uncertainty | A conditional answer, bound or heuristic candidate can be enough; stronger assurance should change the receiving choice enough to repay its cost. |
| Reuse in a changed setting | A different primitive, observation, input promise or interaction can invalidate a formerly correct construction. |

C.29.2 in FPF supplies the computational formulation: what is represented, what answer is required and which operations and resources are available. C.11.DUA helps choose how much additional inquiry or assurance the work warrants. The CMP methods construct the algorithmic contribution needed under that formulation and can expose a reason to revise it. A changed unit, observation or available operation returns to the formulation rather than silently retaining its old answer claim. They do not require a proof or benchmark that cannot change the next useful action.

## CMP.Reference:3 - The methods and their connections

The grounds in §1 explain why these methods belong together. Their connections depend on the result being constructed, not on every method being used. In particular, a change to what counts as an operation can alter a cost bound, an interpretation and a composition argument together. CMP.16 develops that constructive change; the other methods supply the specific obtaining, analysis and interaction contributions it can require.

### CMP.Reference:3.1 - Construct an algorithm

[CMP.1](#cmp1---solve-one-problem-through-another-or-transfer-a-limit-computational-reduction) connects a new computational problem to a solver for another one. Its conversion and answer recovery also determine the direction in which an impossibility or resource result can travel. [CMP.2](#cmp2---derive-a-recursive-procedure-from-a-problem-decomposition) constructs a recursive procedure by choosing smaller problems, sufficient returned information and a reason for progress. [CMP.3](#cmp3---share-and-schedule-repeated-subcomputations) turns repeated subcomputations into a shared dependency structure, choosing evaluation order and what to store or recompute.

[CMP.5](#cmp5---bound-an-optimum-or-recover-a-feasible-candidate-through-a-relaxed-problem) obtains a tractable relaxation and connects its bound or solution back to the original problem. [CMP.4](#cmp4---construct-computational-search-with-justified-exclusions) uses such bounds, or other justified conditions, to exclude search branches without losing the requested result. A feasible candidate can be useful before search finishes; its quality claim depends on the remaining alternatives and available bound.

[CMP.6](#cmp6---derive-an-iterative-computational-update-from-local-information) constructs an admissible iterative change from local information. The neighborhood and progress argument decide what stopping establishes. [CMP.7](#cmp7---construct-a-learner-from-examples-and-feedback) constructs the procedure that selects or updates a rule from examples and feedback. It separates that procedure from the resulting rule and separates successful optimization from what the rule supports on further cases. Search or iterative updating can supply its obtaining operation.

### CMP.Reference:3.2 - Control error and computational cost

[CMP.8](#cmp8---construct-an-approximate-computation-with-controlled-error) turns a permitted approximation into an effective computation with an error and stopping account. Mathematical convergence supplies part of the reasoning; the algorithm still needs usable operations and a finite return condition. [CMP.9](#cmp9---construct-a-randomized-estimator-or-sampling-procedure) constructs sampling and estimation, retaining the target law, dependence and stopping conditions. A random output, a sample distribution and an estimate have different uses.

[CMP.10](#cmp10---choose-a-computational-representation-for-its-access-and-update-operations) derives a data representation from the required access and update operations. It exposes costs moved into conversion, maintenance or output. [CMP.11](#cmp11---derive-a-computational-lower-bound-from-indistinguishable-inputs) proves a lower bound by finding inputs that remain indistinguishable under the allowed observations but require different answers. It constrains all procedures within that model; a changed access operation or tolerated error can reopen the conclusion.

These methods can change the construction in Part A. A prohibitive shared table can motivate scaling, another representation or a weaker answer. A lower bound can redirect the question rather than motivate another attempt at the same impossible guarantee. A randomized construction remains subject to the output conditions the receiving work needs.

### CMP.Reference:3.3 - Interpret, transform and compose computations

[CMP.12](#cmp12---construct-an-interpreter-or-a-meaning-preserving-translation) constructs an evaluator or a translation by specifying expression meaning, binding, primitive operations and control. The preservation relation follows what the receiving computation can observe. [CMP.13](#cmp13---construct-a-computational-abstraction-for-the-property-being-asked) constructs a cheaper abstract computation for a selected property, with operations that justify its conclusions and a way to reconstruct or refine an apparent counterexample. [CMP.14](#cmp14---compose-interacting-computations-through-their-required-observations) constructs the shared-state or communication behavior needed when computations interact, including the assumptions under which progress follows.

[CMP.15](#cmp15---compose-independent-extensions-of-data-variants-and-operations) applies when independently added data variants and operations must work together. It supplies the required combinations, explicit joining implementations, recursive binding and preservation conditions. Use CMP.12 to derive an interpretation that a joining body still needs; use CMP.14 when shared state or changing visible methods introduces interaction. An adequate closed interpreter can remain unchanged when independent extension is unnecessary.

[CMP.16](#cmp16---construct-computational-units-and-operations-for-a-required-whole) constructs units and admissible operations from the required whole behavior. It tests a proposed assembly, changes the information or protocol at a failed join, and connects the resulting abstraction to its implementation. Its result can supply the operations assumed by a recurrence, a representation choice or an interpreter. CMP.13 instead constructs an approximate analysis of a given computation; CMP.14 establishes the joint behavior when the new operations interact. The methods can cooperate without supplying the same result.

The returned operations can themselves become objects of further work: an algorithm can interpret another algorithm's description, a translator can transform it, and an abstract procedure can inspect its possible behavior. Mathematical Thinking supplies constructions of operations and interpretations. CMP adds effective execution and its consequences under the chosen computational model.

These methods do not form a compulsory sequence. A reader with an adequate formulation can enter at a missing bound or representation. A representation failure can return to the recurrence; a semantic failure can return to interpretation; a communication failure can return to composition. Keep the required result and the assumptions of these connections visible when different agents supply the contributions.

### CMP.Reference:3.4 - Constituent actions in ongoing work

Updating a visited set can be part of executing a graph-search algorithm while a route-finding task is under way. Changing the required answer from any route to a route with the fewest edges changes which frontier-selection discipline suffices; a successful visited-set update alone does not establish the stronger result. The practitioner needs to connect the local update, the algorithm's invariant and the route requirement, while retaining its representation and memory conditions. Knowing set operations and the desired route can leave that intermediate algorithmic reasoning missing.

FPF B.1.5.EW helps recover these constituent–whole connections; B.1.5.RS examines a proposed replacement. Examine the connections needed to settle the present question. Performing a method described here can require capability, support and compatible resources for its constituent operations and for the larger work.

## CMP.Reference:4 - Worked connection - One best selection becomes every best selection

Suppose a finite list contains individually identified options. Each may be chosen at most once. Costs are positive integers and values are nonnegative integers. A selection's cost and value are the respective sums for its chosen options; total cost must not exceed capacity W. The first request is the maximum value and one selection achieving it. These are stipulated model conditions; whether they describe an actual investment, experiment or production choice is a separate modeling question.

Use three options: A costs 4 and has value 7; B costs 3 and has value 5; C costs 2 and has value 3. Capacity is 5.

**Construct what a smaller problem must return.** CMP.2 defines R(i,b) as the best value using the first i options with remaining capacity b. The base is R(0,b)=0. If option i costs w_i and has value p_i, its recurrence is:

`R(i,b) = R(i-1,b)` when `w_i > b`;

`R(i,b) = max(R(i-1,b), p_i + R(i-1,b-w_i))` otherwise.

Every selection either excludes or includes option i, so these branches cover its possibilities. Both use a smaller i. Store a choice attaining the maximum when a witness is required. For A, B and C, the final values at capacities 0 through 5 are `0, 0, 3, 5, 7, 8`; recovering the choice at capacity 5 gives B and C.

**Share subproblems and compare cost.** CMP.3 computes each needed pair (i,b) once in dependency order. A full table has (n+1)(W+1) cells and O(nW) updates. This is a count of table operations; arithmetic cost depends on the size of the values. Since W is encoded with about log₂(W+1) bits, this procedure can still be expensive relative to input length. Keeping just two value rows reduces storage, but recovering the selection then requires retained decisions or recomputation. CMP.10 helps compare those operations for the actual workload.

**Use a cheaper bound when it settles the request.** CMP.5 allows fractional choices solely to obtain an upper bound. At capacity 5, take all of A and one third of B: the relaxed value is 26/3. The corresponding fractional optimum follows by considering value per unit cost, or by the bound derived in CMP.4's worked case. Original values are integers, so they are at most 8. The feasible B+C selection reaches 8. CMP.4 can therefore finish the optimality question without searching every remaining branch. When a bound does not settle it, the search retains the unresolved alternatives.

**Change the requested answer and a supplied option.** Add D, costing 4 with value 8, and request every optimal selection. The new final value row is `0, 0, 3, 5, 8, 8`. D and B+C both attain 8. D cannot be combined with another option within capacity; the earlier argument bounds all selections omitting D. The old fractional bound does not cover the changed list: the new relaxation can take D and one quarter of A, giving 39/4. That bound alone leaves the integer value 9 unresolved.

A search for one optimum can discard a branch whose best possible value equals the incumbent. A search for every optimum must retain a branch that may contain a different equal-valued witness. Similarly, a table storing only the minimum cost for each value keeps D at cost 4 for value 8 and can discard B+C at cost 5. Recovering all ties in that compressed table cannot recover a selection already discarded for being heavier.

Return to the original recurrence. After computing R, recover every optimal selection by following each branch whose value equals R(i,b), retaining the distinct choices. At (4,5), both exclusion, R(3,5)=8, and inclusion, 8+R(3,1)=8, qualify. They recover B+C and D. CMP.4 supplies the changed exclusion condition; CMP.3 supplies the retained dependencies or recomputation; CMP.10 exposes what a compressed representation lost. The value calculation survives, while the witness procedure changes. Enumerating all witnesses can require exponential output even if the value table is small.

If the work later permits a near-optimal value, CMP.8 can trade a quantified rounding loss for a smaller computation. That different request does not supply every optimizer of the unrounded problem. Select the answer the work needs before choosing the shortcut.

The same connected method can be used with other finite recurrences and search constructions. Independent additivity and integer capacity belong to this example. A different problem may require different state, recurrence and bounds while preserving the need to connect answer, construction, retained information and cost.

## CMP.Reference:5 - Use checks, assumptions and recurring failures

The worked cases use small inputs and explicit operations so that a reader can reconstruct the method and change a premise. A physical machine can provide different arithmetic, atomicity or memory behavior. An empirical data source can violate the probability or feedback assumptions used by an algorithmic argument. Carry those requirements to the appropriate implementation or subject inquiry when they matter to use.

For a combination of methods, check the following substantive questions:

- Does the original question require a value, a witness, complete enumeration, an approximation or a continuing behavior?
- Can each contribution actually obtain what the next one consumes, under the same input, meaning and resource conditions?
- What is retained or discarded by sharing, compression, relaxation, sampling, learning or translation, and can that change the requested answer?
- Which argument covers correctness and which covers termination or continuing progress? Are their operations and assumptions available in this setting?
- When a condition changes, which dependent conclusion must be revised and which earlier work remains useful?

Use the relevant body's checks where its operation enters; an unchanged supplier need not be rederived. Whole-computation costs can include simultaneously retained tables, repeated conversions or shared communication, even when each local operation is affordable.

| Failure invited by the construction | Practical correction |
| --- | --- |
| Memoization identifies calls by visible arguments while ignoring changing state or effects | Include the consequential context or avoid that reuse. |
| An optimum value is taken to supply every optimal witness | Preserve or reconstruct every required choice; account for output size. |
| Local improvement or training fit is treated as a guarantee about a different target | Recover the actual neighborhood, feedback and performance claim. |
| A stationary sampling law is treated as a finite-run independent sample | Establish the finite-run distribution or use an applicable dependence bound. |
| A translation or composition is checked only by its final value | Include the intermediate observations, failures and progress on which its context relies. |
| A model-specific limit is treated as an unrestricted impossibility | State the access and cost model, error and input promises, then examine which change escapes the bound. |

Being able to repeat a trace is useful preparation but leaves transfer to be tried. Ask the learner or assisting agent to change an input promise, required output or execution rule and recover the affected construction. Human learning, an AI agent's immediate performance and a learned rule's statistical generalization are different capability questions; their assessment should fit the intended work.

## CMP.Reference:6 - Consequences and Architectural Rationale

The repertoire makes a computational contribution discussable before a finished program exists. A practitioner can construct a recurrence, identify a missing return, derive a bound, change a representation or expose a failing interaction. These results support implementation, explanation, reuse and further inquiry. Their cost ranges from tracing a few states to constructing a substantial new algorithm or proof.

The organization follows recurring algorithmic work across branches. A catalogue arranged by familiar algorithms is useful when a reader already recognizes the problem and needs an implementation. A textbook organized by mathematical topics can develop deeper theory. This language serves the choice and construction between those points: what operation is missing, how its result will be obtained, and which downstream use it supports. Its methods are a selected repertoire; a specialized graph, geometric, cryptographic or other algorithm can require additional subject techniques.

Several apparent overlaps are useful distinctions of work. CMP.5 constructs a relaxation and recovery, while CMP.4 decides which search branches its bound can exclude. CMP.3 shares equivalent subcomputations, while CMP.13 deliberately summarizes possibilities for a selected conclusion. CMP.12 preserves the execution meaning needed by a translation, while CMP.14 supplies the interactions needed by the combined computation. Their outputs can be connected without making those methods interchangeable.

Mathematical Thinking supplies objects, operations, arguments and limits; Mathematical Modeling connects a subject question with those constructions. CMP develops effective obtaining procedures and their algorithmic consequences. Physical Thinking and C.29.3 connect required operations to physical interactions, preparation and readout. The computational and physical models must correspond where a claim about execution depends on both. A computational lower bound and a physical performance bound can therefore constrain different aspects of the same proposed system.

Notations and methods of work also matter. An expression can hide binding or evaluation rules that CMP.12 needs to expose. A mathematical model of a working method can use CMP.14 to compare orders and interactions, while the actual organizational roles and responsibilities still require a methodological account. FPF's B.5.MPC coordinates the mathematical, physical and computational contributions; Core's Method-development family develops the corresponding changes to ways of working.

This arrangement permits several routes and several performers. An AI agent can propose code, a specialist can supply a bound and another procedure can check a property. Their contribution remains usable only with the meaning and conditions its receiver needs. A new source or capability can change one construction and the affected connections without replacing the whole language. An unsupported operation becomes a useful next inquiry when resolving it could change what the work can do.

The broad account and the local bodies have different jobs. The account explains why execution meaning, construction, learning, composition and limits constrain one another. A body's complete method obtains a particular contribution. Neither can substitute for the other: a field-level assertion does not provide a missing join, while a set of correct local procedures can leave the receiving whole unavailable. CMP.16 gives one constructive return from a whole requirement to the units and operations that make it possible; it is not a compulsory controller for all uses of this language.

This arrangement preserves ordinary direct use and substantial synthesis. A reader can solve one membership query without studying every branch, or develop a new interacting computational way whose semantic, mathematical and physical dependencies require several full contributions. The explanation should support both grains without turning the easier entry into the boundary of algorithmics.

## CMP.Reference:7 - Shared sources, alternatives and relations

Erickson's [algorithm construction material](https://jeffe.cs.illinois.edu/teaching/algorithms/) and Morin's [Open Data Structures](https://opendatastructures.org/) support the connection between a problem, its representations, a constructed procedure and its argument. The bodies retain explicit conversions, recurrences and operation costs. Direct use of a known algorithm remains preferable when constructing another one adds no needed capability.

The approximation and learning sources cited in CMP.5-.9 connect a deliberately weakened or data-dependent answer to the procedure that obtains it. They also expose limits: a recovered relaxed solution needs feasibility and quality arguments; an optimized training criterion leaves generalization conditions to be established. CMP.8 compares its transparent scaling construction with a stronger recent knapsack scheme. CMP.7 compares historical assessment with adaptive assessment under temporal change. Those comparisons justify reopening the corresponding method when another construction changes cost or supported use.

[SICP's evaluator and compiler construction](https://sicp.sourceacademy.org/chapters/4.1.html) supplies an explicit historical demonstration of programs that interpret and transform programs. CMP.12 combines that construction with current behavior-preservation distinctions. Cousot's [Principles of Abstract Interpretation](https://mitpress.mit.edu/9780262044905/principles-of-abstract-interpretation/) develops computable summaries from the properties they must support; CMP.13 compares direct exploration, coarser abstractions and targeted refinement. These approaches answer different questions: a useful overapproximation can deliberately introduce behaviors that a meaning-preserving translation would have to treat differently.

Lamport's [A Science of Concurrent Programs](https://lamport.azurewebsites.net/tla/science-book.html) and the composition, memory and crash studies discussed in CMP.14 support its separation of observable behavior, permitted interaction and progress. Sequential composition is cheaper when interference is absent. More detailed composition arguments earn their place when shared observations or failures change what the whole computation can do. Each body gives the adopted contribution, serious alternative and conditions that would reopen its selection.

The [Suite Reference (Foundational)](https://github.com/ailev/FPF/blob/main/DPFs/Foundational%20Thinking%20DPF%20Suite/FOUNDATIONAL-THINKING-DPF-SUITE-REFERENCE.md) locates the related publications and explains their shared architecture. C.29.2 supplies computational formulation; C.29.3 physical realization; C.29.1 the transfer between mathematical accounts; C.29 the model-to-subject correspondence. B.5's inquiry methods support the next question when a limit or failure makes the old one insufficient. Notational Engineering supplies methods for constructing expression forms and their interpretations. Use NOT.2 and NOT.3 when those contributions are needed; CMP.12 develops computational execution of the expressions.

Wing's [2008 account of computational thinking](https://www.cs.cmu.edu/~CompThink/papers/Wing08a.pdf) is a historical foundation for relating abstraction, its levels and automation beyond one programming notation. Here that relation is developed through explicit operations, interpretation and conditions of use. [SICP's elementary language account](https://sicp.sourceacademy.org/chapters/1.1.html) and [data-abstraction barriers](https://sicp.sourceacademy.org/chapters/2.1.2.html) give historical constructive foundations: primitive means, combination and named abstractions support changes at different levels. CMP.16 develops a construction problem that needs those connections, while CMP.12 supplies interpretation of descriptions themselves.

Cybenko's [1989 approximation theorem](https://papers.baulab.info/papers/Cybenko-1989.pdf) illustrates a necessary boundary. Its stated approximation conditions and existence result do not provide a training algorithm or a feasible network size; the paper separately identifies constructive and resource questions. Sutton's [2019 historical argument about general search and learning](http://incompleteideas.net/IncIdeas/BitterLesson.html) motivates methods that can exploit additional computation rather than prescribing every domain answer. It is not a theorem that one learner dominates on every data source. CMP.7 keeps the representation, evidence and further-use conditions that a practical learning claim needs.

These foundations do not make the repertoire exhaustive. A specialized algorithm, physical realization or learning result can remain external while supplying a consequential operation. Reopen the affected account when such a result changes an obtainable answer, a justified limit or the useful organization of the computation; do not confuse a historical anchor with a current universal performance claim.

The three Parts group the presentation. The bodies form a repertoire of related Methods, usable individually or in combinations selected for the question. A particular connected use can describe a composite way of working, but membership in this publication alone does not make every method a mandatory step of that work.

## CMP.Reference:End
