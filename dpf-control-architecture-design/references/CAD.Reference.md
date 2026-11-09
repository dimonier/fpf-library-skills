---
id: CAD.Reference
title: "CAD.Reference:1 - What the language helps obtain"
---

# CAD.Reference: CAD.Reference:1 - What the language helps obtain

> **Problem frame:** A controller acts on information that can be partial, old or costly to obtain. Its chosen action must affect the plant before another decision is due, fit the available actuation and leave an acceptable continuation.
> **First move:** This branch applies when separate planning and feedback decisions are worth considering. Its exact-state construction remains useful when the state is actually available.

---

## CAD.Reference:1 - What the language helps obtain

A controller acts on information that can be partial, old or costly to obtain. Its chosen action must affect the plant before another decision is due, fit the available actuation and leave an acceptable continuation. When planning and feedback are separated, their different models and time scales add another coupling: an attractive nominal command may be impossible for the lower loop to realize.

The useful result is a control architecture whose information, command meanings, error allowances and execution conditions are mutually consistent for the required task. The result may instead be a reasoned rejection: no tested realization fits, a sufficient enclosure is too coarse, or indistinguishable states make the required action impossible. These conclusions call for different next work.

There are two directly useful branches. CAD.5 constructs the information available to a specified controller. CAD.1–CAD.4 develop a planning-and-feedback arrangement when separation has a useful reason. Their quantitative results connect where an estimate, command or timing claim is actually used. The language does not require every design to use both branches.

Its recurring tensions are concrete. A precise delayed sensor leaves recent disturbances unknown. A larger model can reduce modeling error while missing the deadline. A gain that reduces tracking error can consume more input authority. Conservative sets can protect a guarantee while excluding a useful design. All of these must be judged against the same task; a smaller isolated error measure is not automatically a better control result.

FPF C.43 supplies the common Method for connecting observation, choice and action in ongoing control. Apply it when the available assessment, alternatives and execution conditions still need to become one coherent continuation; an adequate architecture can remain unchanged. CAD specializes the engineering construction of the information, command and timing relations. Its state sets, error bounds and feasible commands give quantitative answers under declared models; they do not by themselves settle the legitimacy of a goal, the economics of competing resource uses or a developing subject's next worthwhile problem. Conversely, a common control mantra does not replace these calculations. A changed information delay returns to CAD.5 and its dependent bounds; an unavailable correction can reopen CAD.3 or the architecture choice; a changed goal first changes the task against which those results are used.

FPF C.43:4.5.1 also supplies the common construction of required temporal relations without imposing a periodic schedule. CAD.2 makes that construction executable through event ordering, behavior between updates and reset rules; CAD.5 preserves sample phase, information age and observation gaps, and CAD.4 qualifies the shared implementation schedule. An action can vary its timing while another required contribution continues, provided their joint resource and dynamic conditions still hold. Changing one of these relations reopens the dependent calculation; equal update frequencies alone do not preserve it.

## CAD.Reference:2 - The objects and independently useful contributions

The plant, sensors, actuators and controller computers are systems. A dynamical model is a mathematical description of selected behavior. A feedback law prescribes how to choose an input; an implementation performs that calculation and applies an actual input. A design Method constructs or assesses an arrangement; one run of that Method is design work. The framework describes Methods and their relations. A model or feedback-law revision can change the required computation without requiring a different physical plant; changing a processor can change timing without changing the law.

In CAD.5, a *channel* is a realizable observation alternative with a measurement meaning, uncertainty, sample times, arrival conditions and resource demands. An *information state* retains what is needed to update the compatible possibilities and choose the next action. It can be a history, a sufficient recursive state or a conservative set representation; it is not necessarily another sensor or a physical control layer. The estimate \(\hat x\), the true model state \(x\), estimation error \(\eta=x-\hat x\), nominal state \(z\) and tracking error \(e=x-Pz\) have different meanings.

In CAD.1–CAD.4, *planner*, *tracker* and *layer* identify contributions in a selected control organization. They do not automatically identify processor boundaries, physical parts or system-role assignments. Different functions can share a processor; one function can be distributed. Their order is not a ranking of people.

| Recurring design question | What its Method constructs | Why the result can be needed independently |
| --- | --- | --- |
| Information sufficient for action | CAD.5: channel/timing alternatives, sufficient memory and update, estimation uncertainty and admissible action or impossibility | A single controller may need better observations without a different decomposition. |
| Useful separation of decisions | CAD.1: alternative decompositions, reasons for each split and exposed losses | A timing or horizon problem can change the split while sensing remains adequate. |
| Meaning and behavior of an exchange | CAD.2: reconstruction, command, hold/interpolation/reset rules and error dynamics | A communication or reference representation can change without replacing either controller. |
| Feasible command and continuation | CAD.3: compatible error and command sets, state/input margins and continuation conditions | A larger demand can exceed a previously useful domain while the architecture remains unchanged. |
| Realizable whole choice | CAD.4: feasible configurations, comparison under common demands, execution and revision conditions | A processor, solver or scheduling change can alter the preferred realization. |

These are connected problem families with independent uses. CAD.4 constructs the comparison of whole layered candidates; CAD.5:4.8 compares information arrangements. This Reference explains the quantities shared by those Methods and the conditions under which their results can be combined.

## CAD.Reference:3 - Information, tracking and execution must describe the same loop

### CAD.Reference:3.1 - How information changes a command margin

CAD.5 constructs compatible state histories from the measurements actually available before the action. Past inputs must be the inputs actually applied; a planned input or a measured value treated as current can produce a different information set. A run-wide bound \(V_\eta\) must cover startup and every allowed delivery mode, not only a favorable observation window.

When the interface is

$$
u=K(\hat x-Pz)+Qz+Rv,
$$

CAD.5:4.7 derives the estimate-based version of CAD.2's tracking equation:

$$
e^+=Fe+Hz+Gv+w-BK\eta.
$$

CAD.3 therefore receives the effective forcing \(W\oplus(-BK)V_\eta\). For every admitted nominal state and command, its state and input tests become

$$
\{Pz\}\oplus E\subseteq X,\qquad
\{Qz+Rv\}\oplus KE\oplus(-K)V_\eta\subseteq U.
$$

The separate set sums are sufficient enclosures, not assertions that tracking and estimation errors are independent. A tighter joint representation may recover a useful design that these separate margins reject. A failure of a sufficient enclosure is consequently different from CAD.5's indistinguishability proof that no action can meet the demand.

This is a two-way design connection. A tighter required command domain can require fresher observations. A sensor or estimator change can enlarge \(V_\eta\), shrink the usable command domain and invalidate a nominal performance claim. CAD.4 includes the cost of obtaining and updating that information. If a larger planner delays the estimator or communication, the old age bound is no longer a premise of the same realization. Reuse an unaffected result, but return the changed timing to CAD.5 and the resulting error to CAD.3.

### CAD.Reference:3.2 - A complete joint design and a changed delay

Consider the constructed scalar plant

$$
x_{k+1}=x_k+u_k+w_k,\qquad |w_k|\le .005,
$$

with \(|x|\le .65\), \(|u|\le .06\), initial \(x_0=z_0=0\), and a requested nominal motion satisfying \(|z|\le .5\), \(|z_{k+1}-z_k|\le .04\). The required tracking bound is \(|x-z|\le .11\), including intervals in which the nominal command uses the full rate \(.04\). The lower law is \(u=-.5(\hat x-z)\). Assume its update is completed every fast tick. The planner needs two fast ticks to calculate a new segment and supplies one every four ticks. Each calculation starts at least two ticks before its segment takes effect, and each new segment starts at the preceding segment's terminal nominal state. Hold \(z=0\) until the first segment is available. These timing and joining conditions are premises to establish for an actual realization.

A complete scalar sensor has error radius \(.005\) and gives the controller a sample at most two ticks old. CAD.5 propagates that sample through the actual intervening inputs, giving

$$
|\eta|\le r=.005+2(.005)=.015.
$$

Known \(x_0\) gives a startup radius at most \(.01\) before the first two-tick-old sample is usable. Thus the uniform radius \(.015\) covers startup as well. A current complete observation would need less memory and give a smaller radius; the delayed sensor is considered here because it is an available realization, not because delay is desirable.

CAD.2 models the timed segment by \(d_k=z_{k+1}-z_k\), so

$$
e_{k+1}=.5e_k-d_k+w_k+.5\eta_k.
$$

CAD.3 obtains the invariant radius

$$
E=\frac{.04+.005+.5(.015)}{1-.5}=.105.
$$

The initial error is inside it. The input bound is \(.5(E+r)=.06\); the state bound is \(.5+E=.605\le .65\); the required tracking bound is met. At the end of a nominal motion, holding \(z\) sets \(d=0\), which stays inside the same admitted increment set and preserves the continuation. The conclusion is conditional on the stated sample, plant and timing bounds.

This also explains the decomposition and interface choice. Asking the two-tick planner for a fresh result every tick misses its assumed deadline. Sending a held target that jumps by \(4(.04)=.16\) can fail immediately: from exact initial alignment and zero estimation error, that jump requests input \(.08>.06\). Sending a joined segment at the same four-tick planning rate preserves the requested nominal rate and the bound above. CAD.4 compares this whole realization with a faster planner, another controller or a current sensor, including their actual costs; the input margin alone does not rank them.

Now suppose shared computation increases the maximum observation age to four ticks. CAD.5 gives \(r=.025\); the same construction gives \(E=.115\) and input allowance \(.07\). It no longer establishes the required tracking or input limits. Reducing the allowed increment to \(.03\) gives \(E=.095\) and input allowance \(.06\), but does not satisfy the unchanged request for the full \(.04\) rate. Recovering the old age bound, using a more timely observation, changing the interface or controller, or obtaining a less conservative joint bound are different repairs to compare. This failed sufficient calculation is not a proof that every controller with four-tick-old observations is impossible.

The example crosses the information, exchange, feasibility and implementation questions without inventing a new control law synthesis theorem. It is an application of CAD.5:4.5–4.7, CAD.2's substitution and timing construction, CAD.3's invariance test and CAD.4's whole-candidate comparison. The larger task determines whether a smaller command domain remains useful.

## CAD.Reference:4 - The layered planning-and-feedback branch

This branch applies when separate planning and feedback decisions are worth considering. Its exact-state construction remains useful when the state is actually available. The estimate-based connection is in CAD.5:4.7 and CAD.Reference:3; use it wherever the implemented law acts on an estimate. The following sections develop the reasons, quantities, alternatives and returns within the layered branch.

### CAD.Reference:4.1 - The recurring whole problem

A layered control architecture divides decisions while controlling one connected behavior. The division is useful when it lets different calculations use appropriate information, horizons and execution resources. It becomes harmful when each calculation relies on a behavior that the others do not supply.

The difficult question is therefore not just which operation follows another. It is whether the chosen decomposition, models, command meanings, error bounds, feasible commands and execution arrangement can all be true of the same closed loop. A later result can change an earlier design premise. The four Methods are separately usable because these questions arise independently; their results must still agree wherever one receives another.

**Extended reminder.** A useful control split preserves the whole task by making its lost interactions explicit. The exchanged command and its timing determine the error that the lower behavior must contain; the containment consumes state clearance and actuator authority, so it limits what the upper decision may request. Those limits reshape the useful model, horizon and decomposition, while the resources needed to compute and execute them change timing again. Compare and realize this connected choice under one demand, and return a changed condition to the premise it invalidates.

This reminder names a coupled argument. It does not prescribe four approval stages, prove a bound, or replace the constructions below.

### CAD.Reference:4.2 - Why these four contributions belong together

CAD.1 answers a functional design question: which decisions should become distinct and why? Its result determines which interactions are no longer solved together. A long-horizon optimizer and a fast feedback law are useful only if their separation addresses a real difficulty, such as calculation time or unequal access to information.

CAD.2 answers a modeling and realization question: what behavior does that separation actually produce? It turns a selected command into an exchange with units, time, interpolation, feedback and reset semantics, then derives the joint evolution. This can reveal that a presumed “same reference” is a different signal after implementation. The result constrains the decomposition: an upper model that cannot be related to the lower dynamics under useful conditions is a reason to retain more state, change the command or abandon that split.

CAD.3 answers a feasibility question: which behaviors can be requested without contradicting the conditions of their realization? Error is not merely a quality score. It consumes physical clearance and correction authority. A command envelope that makes the bound large can leave no useful actuation range; a smaller envelope can restore feasibility but prevent the required task. This result therefore constrains both the interface and the original functional choice. It also distinguishes a possible next action from a domain in which operation can continue.

CAD.4 answers a whole engineering choice: which mutually consistent configuration is worth realizing under the actual demand and resources? It compares the outputs of the other Methods, but it also changes their inputs. A different processor, horizon, model order or scheduling arrangement changes what can be computed on time and therefore which error dynamics and command domain are relevant.

The relation is not that every engineer must perform these Methods in this textual order. The relation is that a claim used by another part must be available with the conditions that make it useful. An inherited result can supply it. A changed condition can withdraw it. A missing result can block one architecture while leaving another usable.

### CAD.Reference:4.3 - Connect dynamics, decisions and computation by their actual quantities

The common quantities make the reasoning inspectable. The task sets a demanded progression, cost or reachability condition. A candidate command class S says what the planner may send. The interface yields an error evolution, such as $e^+=Fe+Hz+Gv+w$. S and the mismatch domain bound its forcing. An invariant E bounds the difference between nominal and realized behavior. The inclusions $Pz+E\subseteq X$ and $Qz+Rv+KE\subseteq U$ then restrict S. These are the exact-state formulas. When feedback uses an estimate, CAD.5:4.7 adds estimation error to both the forcing and the input allowance.

These are mutually constraining statements, not independent labels. Enlarging S can enlarge E, which can make the proposed S inadmissible. Reducing E by changing a gain can increase the size of KE and consume more actuator authority. Reducing the planning model can shorten computation while increasing H or the mismatch set. A longer update interval can fit the computation and enlarge the change the tracker must absorb. A bigger model can remove an important residual but leave no time to use the result.

Thus “more accurate”, “faster” and “more robust” are incomplete comparisons until their quantities and costs are named. A more accurate nominal prediction does not imply a smaller implemented error if it arrives late. A smaller tracking error does not imply a better task result if the permitted command range becomes too small. A feasible computation does not imply safe execution if its output is applied at the wrong instant.

The mathematical construction does not eliminate the engineering choice. It makes the choice explicit: accept a smaller envelope, change an interface, spend more computation, use another sensor or actuator, or revise an impossible requirement. SYSE.6 remains the place for that larger system decision.

### CAD.Reference:4.4 - Reuse the external foundations without losing the subject transition

C.39 supplies the reasoning from a needed result back to necessary operations and forward through their joins. Here that reasoning asks whether the result called “a feasible controller” includes a realizable command, its timing and a continued path, rather than stopping at the existence of a feedback gain.

MMP.9 supplies the account of what model reduction removes. CAD.1 and CAD.2 consume that account at a specific control decision: does the missing state create memory or forcing that the planner must retain or the tracker must absorb? Calling the lower loop “fast” does not establish that its omitted dynamics are negligible.

MMP.18 supplies the general construction of compatible exchanges and scales. CAD.2 fills its control-specific content: which signal is held, which state is propagated, what resets, and how a reference change enters the error. A well-typed exchange still needs this behavior.

MMP.22 supplies the transformation from mathematical operations to workable performance. CAD.4 consumes it when choosing what to precompute, what data are available at the deadline, what resource is shared and which result can actually arrive. The computation is part of realizing the selected control behavior; successful algebra alone does not enact it.

C.30.LCA then helps describe the resulting control structure adequately. It can expose an unrepresented latency or lower guarantee. It does not establish the guarantee's truth. Conversely, a valid error calculation does not ensure that a view shows the assumptions needed by the next engineer.

These foundations remain useful outside control engineering. The subject contribution here is their specific connection to control decisions, error dynamics, admissible commands and execution. Neither collection of general references nor a single numerical example supplies that connection by itself.

### CAD.Reference:4.5 - Several legitimate entries and their returns

An engineer replacing a communication interface can start at CAD.2. Preserve the task, qualified model and existing controller law if they remain unchanged. Derive what the new delay or interpolation does to their connection, then return only the affected error and command assumptions to CAD.3. If the new interface cannot support any useful domain, the change reaches CAD.1 or the system architecture decision.

An engineer asked to increase speed can start at CAD.3. Hold the implementation and model fixed while testing the enlarged command class. If correction authority is exhausted, CAD.2 can investigate a continuous segment instead of a larger jump. CAD.4 compares that repair with a changed gain, faster planner or different plant arrangement. The order follows the uncertainty that matters, not a mandatory restart.

An engineer moving the same software onto shared computing hardware starts at CAD.4. A model of independent task execution is no longer the implementation premise. Establish the shared scheduling and communication behavior; if it changes the admitted timing, return that timing to CAD.2. A new hardware name alone does not require every control theorem to be reproved, but an unbounded delay removes the old timing-dependent conclusion.

An engineer with a simple controller already meeting the requirement can stop before any of these expansions. A framework that always recommends more layers has lost its baseline. Conversely, a proven lower law does not justify stopping when the upper layer can issue commands outside its qualified envelope.

#### CAD.Reference:4.5.1 - Keep a qualified loop and govern its commands

When an existing loop already tracks and rejects disturbances adequately, but abrupt or excessive commands violate constraints, command admission can be the remaining problem. [Garone, Di Cairano and Kolmanovsky's survey, §2.1 and §6.1](https://merl.com/publications/docs/TR2016-102.pdf) develops reference and command governors as additions before a stabilized loop. They modify commands using the current closed-loop state and predicted constraint admissibility, rather than merely applying a fixed low-pass filter.

For the basic held-command construction, use a model whose state includes the plant and controller. Obtain a set of state-command pairs from which holding the selected command satisfies the constraints at all claimed future instants. A scalar reference governor selects the largest admitted step along the line from the previous command toward the desired one; a command governor can optimize the command vector. The previous command supplies continuation only under the construction's admissibility and initialization conditions. Scalar search is smaller, while the restricted search direction can sacrifice response.

This is a candidate within the control architecture question, not an opposing field. It can preserve a qualified lower controller and avoid introducing a reduced planning model. Compare its reference distortion, progress and computation with the required task. If filtering makes the requested arrival time unattainable, constraint satisfaction alone has not solved that task. If the lower controller, sensor or timing changes, its governor model and admissible sets must change with it.

Later constructions change different premises: observer-dependent domains in CAD.2–CAD.3, online cost adaptation in CAD.1, and inexact computation or controller switching in CAD.4. Use those developments only with their corresponding models and conditions.

### CAD.Reference:4.6 - Worked joint revision

The running example begins with two different concerns: a planner needs two fast ticks of computation, while an inexpensive feedback law runs every tick. CAD.1 makes the reason for separation explicit. The separation does not yet decide the command: a held target and a timed segment remain alternatives.

CAD.2 derives how their meanings change the error. A held target creates a boundary jump; a joined segment supplies bounded increments at every fast tick. CAD.3 turns that difference into actuator reserve. At the doubled demand, the four-tick held target has a direct violating first input; the joined-segment command has a sufficient input bound of 0.05 under the toy model. Its limited reference interval also has an explicit continuation by holding the reference.

CAD.4 returns the result to the practical choice. The segment design fits the declared computation arrangement but requires a clocked generator, continuity at handover and an admitted initial error. The engineer cannot keep only its attractive input number and omit that realization. If physical actuation is later found to be delayed, the error derivation changes and the bound must be reopened. The reason for separating planning from feedback can remain useful even while that specific realization fails.

During the calculation of an error margin, the immediate mathematical work contributes to constructing a command domain, which contributes to choosing a viable control architecture, which contributes to the engineered system's required behavior. A changed whole requirement alters what counts as a useful local margin. This connection explains why a numerically correct sub-result can still fail to resolve the engineering problem.

### CAD.Reference:4.7 - Recognition, assurance and the cost of the arrangement

A layered diagram recognizes a candidate organization. A plausible trace recognizes a candidate behavior. Mathematical invariance establishes a conditional property; a real model, disturbance envelope and execution arrangement must support its premises before physical reliance. These are different results, and the full use needs whichever the intended claim actually consumes.

The primary trade-off is between cheaper or more specialized local decisions and the burden of maintaining their coupling. More patterns or more formal interface declarations do not settle that trade-off. The arrangement earns its cost when separate decisions remain useful and their conditions can be made compatible. A direct controller or direct existing Method remains preferable when it already serves the task.

A whole-use inspection therefore asks whether the selected split has a useful reason, whether the derived exchange is the one realized, whether its command/error dependence closes, whether continuation and performance are distinguished, and whether implementation conditions fit. These questions use the full constructions of CAD.1–CAD.4; they are not an alternative checklist proof.

### CAD.Reference:4.8 - Source boundaries, bias and future change

The constructions compared in the patterns answer different quantitative questions. The reader should not assemble their conclusions into a theorem that none states. The cost-elimination branch, sampled linear margins, continuous error-based safety transfer, reference governing and a specific two-layer co-design each retain their own models and qualifications. The direct derivations and explicit returns here make a first use possible without claiming complete coverage of control engineering.

The running linear case makes computations transparent but can bias intuition toward easy matching, full-state access and deterministic timing. Its general lesson is to derive and reconnect the consequences of a split. Its numerical margins, feasible domain and fallback remain local to the stated model.

When a source revises a relied-on condition, reopen that condition and its consumers. When a physical model or execution fact changes, reopen the claims that use it even if no source publication changed. A new paper can improve a method; a failed application can expose a missing family of problems. Either can justify revising the framework's scope, while an unchanged adequate supplier remains available.

## CAD.Reference:5 - What is covered and what must be supplied

The first quantitative use needs a usable plant model, initial conditions, uncertainty sets, candidate channels and delivery conditions, a specified feedback law or finite family, required state/input limits, and a control objective. CAD.5 develops information and action constructions for that class. CAD.1–CAD.4 add planning models, command reconstruction, error sets, joint constraints and execution choices when their assumptions fit.

The methods do not promise arbitrary nonlinear or learned-controller synthesis, identification of an unknown plant, security of a communication channel, or certification of a physical installation. Those are real neighboring tasks: an unsupported disturbance envelope or an unbounded communication delay can defeat a mathematically correct conclusion here. Obtain the missing model or guarantee, restrict the intended use, or retain the negative result. The separate continuous-time branch in CAD.3:4.5 needs its stated derivative, Lipschitz and forward-containment premises; sampled constraints do not establish intersample safety.

A proposed architecture, a mathematically qualified model and a physically qualified implementation support different claims. The practitioner should be able to answer which observation times and executed inputs were used, which error bound holds over the allowed run, which one action works for all compatible states, what preserves continuation, and how computation realizes those conditions. The full patterns supply these tests; the questions here do not replace their derivations.

The examples favor transparent linear calculations and explicitly bounded uncertainties. Exact sets can be expensive and outer sets conservative. A stochastic expected-cost task may justify a different estimator and schedule; CAD.5:11 compares that alternative. An unqualified biological analogy or a component score cannot replace the chosen model and control criterion.

## CAD.Reference:6 - Why one language, with independent uses

The information and layered branches share a control-engineering question: which implemented arrangement can produce the required behavior under the available information, actuation, time and resources? Their shared state, error and timing meanings make a result from one branch usable by the other. Keeping those connections explicit reduces the amount a reader must privately derive when a sensor, command or processor changes.

The language is narrower than systems engineering. SYSE.5 constructs the engineered system's functional organization and bearer alternatives; SYSE.6 decides the broader architecture. A control result is one input to those decisions. Putting all specialist derivations inside their general explanations would not remove the need to learn control modeling or maintain its source conditions. Conversely, a control engineer changing one sensor need not reopen the whole system design when its interfaces and required effects remain satisfied.

Two separate framework accounts could expose the same Methods, but would still need to maintain the common estimation/tracking/input/timing connection. One account with direct entries keeps that connection available while allowing independent change. Quantization can change CAD.5 and the bounds that consume its result without changing a valid decomposition. A new command governor can change CAD.3 or CAD.4 without changing an adequate information state. A common file does not require a common calculation or a fresh pass through every Method.

The gain is an obtainable connected explanation and localized adaptation, not a measured reduction in learning time or engineering cost. The costs remain substantial: modeling, set computation, numerical qualification, physical evidence and the effort to understand the selected branch. A direct existing controller, a suitable external design or a competent provider can be the cheaper sufficient route. Where the complete needed method is already known, use its result rather than recreate it for this framework.

## CAD.Reference:7 - Sources, external suppliers and consequential change

The full source comparisons belong with the affected Methods. CAD.5:11 distinguishes the historical diversity-enabled sweet-spot model, internal prediction and applied-action feedback, bounded-set estimation and stochastic sensor scheduling. DeSS compares complementary components under a task and resource model; IFP concerns a controller's reuse of internal information. Neither establishes the other. The selected bounded-set construction is used because the stated task asks for hard sampled constraints, not because it is universally superior.

CAD.1–CAD.4:11 compare decomposition, reduced-model interfaces, invariant margins, governors, safety filters, inexact computation and switching under their different conditions. A reference governor can preserve a qualified loop; a safety filter changes the applied control law and therefore the error calculation; separate stable switching modes do not establish a common invariant domain. A more recent result matters when it changes the usable construction or comparison, not merely because it has a later date.

| External supplying publication | Contribution used here | Receiving use and return |
| --- | --- | --- |
| [FPF Core](https://github.com/ailev/FPF/blob/main/FPF-Spec.md), C.32.LCA | General construction of complete control-architecture alternatives and their joint conditions | CAD supplies the specialized numerical constructions. A changed general architecture requirement reopens the affected framing, not an unchanged algebraic identity. |
| FPF Core, C.30.LCA | Adequacy of a control-structure view | A view must expose the information, authority, timing and lower guarantees needed for its use. Its adequacy does not prove a control bound. |
| FPF Core, A.3.3.PI | Retaining information needed by future prediction and update | CAD.5 constructs a particular sufficient internal state and explains what a reduction must preserve. |
| FPF Core, C.39 and C.32 | Construction of useful connected ways and whole architecture alternatives | CAD.1 and CAD.4 use those general operations with control-specific models, alternatives and constraints. |
| [Systems Engineering DPF](https://github.com/ailev/FPF/blob/main/DPFs/Engineering%20DPF%20Suite/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md), SYSE.5 and SYSE.6 | Functional organization, bearer alternatives and the system architecture decision | CAD results can supply that wider work. Control feasibility neither chooses every system bearer nor settles the whole project. |
| [Mathematical Modeling DPF](https://github.com/ailev/FPF/blob/main/DPFs/Foundational%20Thinking%20DPF%20Suite/MATHEMATICAL-MODELING-PRACTICE-DPF.md), MMP.9, MMP.18 and MMP.22 | Model reduction, compatible coupled models, and transformation of mathematical operations into workable performance | CAD.1–CAD.4 provide the control-specific receiving operations. A changed model exchange or computational realization reopens the error or deadline premise that uses it. |

These remain external contributions. Core does not require this DPF for its own applications. Select an obtainable edition of a supplying publication and the exact relied-on content before applying it; a locator or title alone is not that content. If a relied-on premise changes, revisit its receiving use. If only the carrier or publication date changes, inspect compatibility rather than assuming either breakage or preservation.

For the domain construction, a changed plant, measurement model, uncertainty, command objective, admitted switching, timing or resource arrangement reopens the dependent calculation. A source correction reopens the particular claim imported from it. Unchanged information, interface or model results remain usable under their original conditions.

## CAD.Reference:8 - Names and continuing references

This is the **23 October 2026** edition of **Control Architecture Design Principles Framework (CAD)**, a constituent of the Engineering DPF Suite in FPF Library. Cite the framework and edition together with the full PatternID and section needed for the particular claim or calculation.

*Control architecture design* here means designing the organization of observations, retained information, control decisions, exchanges and execution for the engineered dynamical behavior stated in CAD.Reference:1–2. It does not mean that every controller needs layers. **CAD** is a local reference code for this named framework in FPF Library, not the general engineering abbreviation for computer-aided design.

Each complete Method has one body below. This Reference explains the framework and its conditional connections.

## CAD.Reference:End
