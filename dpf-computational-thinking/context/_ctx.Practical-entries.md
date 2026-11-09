---
id: "_ctx.Practical-entries"
title: Practical entries
---

# _ctx.Practical-entries: Practical entries

---

## Practical entries

Bring a need to obtain something, distinguish alternatives, maintain a response or change the way work is done. The computational question is how available operations could produce the required observations across the intended cases. The operations, representation and organization may themselves need to be invented. A mathematical description of the desired answer, a working device and one successful execution each leave different questions open.

Think of a computational description as a way of specifying a family of possible processes. Inputs, retained state, primitive operations and interactions determine which processes can occur; an interpretation says what their observations mean. The description can then be implemented, analyzed, transformed or supplied as data to another computation. This view includes numerical and symbolic work, search and learning, and ongoing interaction. It lets you change the way a result is obtained instead of only executing an existing recipe faster.

If the computational question is not yet clear, use FPF C.29.2 to connect the receiving need to represented information, required observations, available operations and resources. Then follow the difficulty that the formulation exposes. An adequate known algorithm can finish the inquiry. A missing way to assemble useful operations may need [CMP.16](#cmp16---construct-computational-units-and-operations-for-a-required-whole); a missing argument or an unavailable physical operation may need a different supplier. CMP.Reference:1 explains these grounds and their consequences before the method-family map in :3.

The examples below show how one method's result makes another method usable, including where to branch or return when a condition changes. Use the Table of Contents and the patterns' own `Use this when` and `Problem frame` for other questions. Open only the contributions the question needs; a sufficient existing answer does not require a new analysis.

For inexpensive direct help, [CMP.10 - Choose a Computational Representation for Its Access and Update Operations](#cmp10---choose-a-computational-representation-for-its-access-and-update-operations) can settle how to make one membership query in an existing unsorted list: a scan may suffice, with no new index to build. Many later queries or a different update workload can change that choice.

You can ask an assisting agent: “Explain this and give me your comments in the language of my work, without framework jargon.” Ask it to follow an input through the proposed operations, retain the assumptions needed by the next method, and explain what the result permits.

### CP-DESCRIPTION-TO-BEHAVIOR - A notification rule becomes an ongoing service

- **Situation:** You want messages from a named sender to trigger an immediate notification, while other messages wait for a later digest. A rule can be stated, but that statement does not yet define the behavior of the service.
- **Question:** What information and operations make the rule executable, and which changes require another computational organization?
- **First useful result or blocker:** An executable rule connected to its message and notification operations, with explicit conditions on identity, repetition and timeliness, or the unavailable information or operation that prevents that behavior.
- **Start with:** C.29.2 for the computational question. Use [CMP.16](#cmp16---construct-computational-units-and-operations-for-a-required-whole) if the units and operations still need construction; use [CMP.12](#cmp12---construct-an-interpreter-or-a-meaning-preserving-translation) when a rule description needs interpretation. A known adequate implementation can be used directly.
- **Stop or return:** Stop when the required behavior is available with adequate grounds. A different source of messages, required observation or failure condition reopens its dependent construction, rather than automatically requiring every method below.

Start with an admitted event containing a sender identifier, message identifier and content. Suppose sender identity is supplied reliably, events arrive once in order, and a notification operation is available. An interpreter can read a description such as `If(SenderIs(Vasya), Notify, AddToDigest)`: test the supplied identifier and perform the selected action. CMP.12 derives the meaning of those constructors and their composition. Defining the description as data also permits a later tool to translate or analyze rules. It does not make arbitrary natural-language instructions unambiguous.

The word *immediate* introduces a further obligation. Decide whether the receiver needs an eventual response, a bound after receipt, or a bound after the message was sent. The last bound also depends on message transport. An interpreter that selects the correct action does not establish any of these timing guarantees by itself. C.29.3 connects computational operations to an actual executor and readout; the receiving work supplies the useful deadline and the consequences of missing it.

Now the transport may repeat a message. Re-executing `Notify` can duplicate an external effect, even if rule evaluation is a pure function. A message identifier and retained delivery state can support a changed operation, but recording before or after sending leaves different crash cases. CMP.14 develops the interaction and failure conditions; the Readme's retry case below shows why a repeated logical request needs a different argument from a cached function result. CMP.10 helps select storage only after the required identity and retention conditions are known. Deleting delivery state after an arbitrary interval cannot preserve a promise covering later repetitions.

If messages must instead be classified by urgency inferred from content, the known sender test no longer supplies the decision rule. CMP.7 constructs the learner, its candidate rule family, feedback and conditions of further use; CMP.4 or CMP.6 can supply its search or update. Better training fit does not establish the future error rate, and classifier quality does not establish delivery behavior. A change to inference can therefore preserve the notification protocol while reopening the evidence for classification.

This one use can involve an interpreted description, learned behavior and an interacting realization without making all three compulsory. Their connection follows from what the service must do and what its environment supplies. The full methods explain the respective constructions; this entry shows why changing a condition selects a different one.

### CP-INDEPENDENT-EXTENSIONS - A new data form and a new operation must work together

- **Situation:** One contributor adds a data variant while another adds an operation; their separate extensions leave the joint case undefined.
- **Question:** Who supplies the missing behavior, how is it selected, and which old uses remain unchanged?
- **First useful result or blocker:** A composition covering the required pairs, with an explicit joining implementation, or a named unsupported or conflicting pair.
- **Start with:** [CMP.15 - Compose Independent Extensions of Data Variants and Operations](#cmp15---compose-independent-extensions-of-data-variants-and-operations). Use CMP.12 when the interpretation itself still needs construction; use CMP.14 when shared state or changes during execution affect the result.
- **Stop or return:** Keep a sufficient closed design when independent extension adds no useful freedom. A new required pair, changed meaning or changed dispatch rule reopens the affected composition.

For example, one extension supplies lexical `Let` and its evaluation, while another supplies free-variable analysis for the old arithmetic forms. Combining the modules leaves `FreeVariables(Let)` to be written. The bound name is removed from the body's free names, but not from the value expression's free names. CMP.15:5 derives this joining rule and shows both an executable assembly and a typed alternative. Successful registration alone cannot establish that meaning.

### CP-TRANSLATION-SCOPE - A translation works on test inputs; which executions does it preserve?

- **Situation:** Expressions have been translated to a machine with different arithmetic, and a few successful tests do not settle the permitted input range.
- **Question:** Under which input conditions does the translated program preserve the required result?
- **First useful result or blocker:** A source-to-target correspondence with an established input condition, or a concrete mismatch or unresolved condition preventing that claim.
- **Start with:** [CMP.12 - Construct an Interpreter or a Meaning-Preserving Translation](#cmp12---construct-an-interpreter-or-a-meaning-preserving-translation). If the correspondence depends on a property of possible executions, use [CMP.13 - Construct a Computational Abstraction for the Property Being Asked](#cmp13---construct-a-computational-abstraction-for-the-property-being-asked) to obtain that premise.
- **Stop or return:** Use a sufficient correspondence on its established scope. Changed inputs or machine operations reopen the affected premise. An abstract warning alone is not a demonstrated failing execution.

For example, the source computes `(x + 1) * (x - 2)` with unbounded integers. The target uses unsigned 8-bit arithmetic, wrapping modulo 256. CMP.12 specifies evaluation and translation: evaluate each operand in order, pop the right operand before the left, and append the expression's result without changing an existing stack prefix. At `x = 5`, both executions produce 18. That test does not establish correspondence for other inputs.

Suppose the allowed integers satisfy `2 <= x <= 16`. CMP.13 can compute ranges at the expression's intermediate steps: `x + 1` lies in `[3,17]`, `x - 2` in `[0,14]`, and their product in `[0,238]`. These ranges cover every source execution under the stated input condition. No arithmetic intermediate overflows the target range. This discharges the arithmetic premise of CMP.12's correspondence argument; it does not replace the argument about operand order and preservation of the stack.

Now allow `x = 17`. The source returns 270 and the target 14. The changed range calculation warns that wrapping is possible; this concrete execution establishes an actual mismatch. Return to CMP.12 to choose wider arithmetic, retain a justified input restriction, or explicitly change the intended arithmetic. Do not “repair” the analyzer by removing a real input. For a different abstract warning, CMP.13 checks the proposed execution against the original computation. If reconstruction establishes that a lost distinction produced an impossible path, refine that distinction; failure to resolve a path is not proof that it is impossible.

The same connection can supply a premise about control, binding, errors or effects, but it needs an abstraction for that property and the actual execution rules. A range argument establishes none of those other properties by itself. The direct patterns give those constructions beyond this arithmetic example.

### CP-ANSWER-UNDER-LIMITS - Obtain the answer the work needs within available resources

- **Situation:** A finite selection problem is expensive; changing from one best selection to every best selection can invalidate a shortcut.
- **Question:** How can construction, sharing, bounds and retained information preserve the answer now required?
- **First useful result or blocker:** An answer-producing procedure with justified exclusions and sufficient reconstruction information, or the specific resource limit it cannot meet.
- **Start with:** [CMP.2](#cmp2---derive-a-recursive-procedure-from-a-problem-decomposition), then [CMP.3](#cmp3---share-and-schedule-repeated-subcomputations) when subproblems repeat. A useful bound from [CMP.5](#cmp5---bound-an-optimum-or-recover-a-feasible-candidate-through-a-relaxed-problem) can justify exclusions in [CMP.4](#cmp4---construct-computational-search-with-justified-exclusions).
- **Stop or return:** Stop at the answer sufficient for the work. Changed data, completeness or permitted error reopen the choices that depended on them; a faster value computation need not retain every witness.

First specify whether the result is a value, one selection attaining it, all such selections, or an allowed approximation. [CMP.2 - Derive a Recursive Procedure from a Problem Decomposition](#cmp2---derive-a-recursive-procedure-from-a-problem-decomposition) constructs subproblems with enough returned information to assemble that answer. [CMP.3 - Share and Schedule Repeated Subcomputations](#cmp3---share-and-schedule-repeated-subcomputations) uses their identity and dependencies to decide what can be computed once, when it is needed, and what must remain available for reconstruction.

CMP.Reference:4 supplies a small connected case. Each distinct item may be selected at most once; costs and values add, and capacity is 5.

| Item | Cost | Value |
| --- | ---: | ---: |
| A | 4 | 7 |
| B | 3 | 5 |
| C | 2 | 3 |

Let `R(i,b)` be the best value using the first `i` items within capacity `b`. CMP.2 separates exclusion of the next item from its feasible inclusion. CMP.3 shares each resulting `(i,b)` subproblem. The final values for capacities 0 through 5 are `0, 0, 3, 5, 7, 8`; B+C attains 8. Keeping only two rows can save value-storage, but recovering a selection still needs choices or justified recomputation. CMP.10 chooses a representation for those actual accesses and retained distinctions. The table uses order `nW` updates for `n` items and integer capacity `W`; that is not a polynomial bound in the number of bits encoding `W`.

If exploring alternatives remains expensive, [CMP.5 - Bound an Optimum or Recover a Feasible Candidate through a Relaxed Problem](#cmp5---bound-an-optimum-or-recover-a-feasible-candidate-through-a-relaxed-problem) permits fractional items to obtain an upper bound. A plus one third of B gives the fractional optimum `26/3`. Since original values are integers, they cannot exceed 8. B+C reaches 8, so the optimum is already settled. [CMP.4 - Construct Computational Search with Justified Exclusions](#cmp4---construct-computational-search-with-justified-exclusions) consumes such a bound to exclude alternatives; it does not treat an arbitrary relaxed candidate as an upper bound.

Now add D with cost 4 and value 8, and request **every** optimal selection. Both D and B+C must survive. The old bound concerned a different item set: D plus one quarter of A gives the new fractional optimum `39/4`, so its integer upper bound is 9 and does not alone settle optimality. The updated recurrence gives optimum 8. At its final state both the exclude-D and include-D branches attain 8; following both recovers the two selections.

The output change also changes pruning: for one optimum, an upper bound `U <= L`, where `L` is an attained value, excludes a branch that cannot improve it. For all optima, equality can hide another required selection, so this exclusion needs `U < L`. Storing only the cheapest selection for each value would keep D and discard B+C; following ties later cannot restore information already lost. Return to the recurrence and retain the required choices and item identities. Listing all answers can itself require much more work than computing their common value.

If a near-optimal answer would actually suffice, [CMP.8 - Construct an Approximate Computation with Controlled Error](#cmp8---construct-an-approximate-computation-with-controlled-error) changes the permitted error and construction; it does not answer the request for all exact optima. If the disputed question is what *any* algorithm must spend, [CMP.11 - Derive a Computational Lower Bound from Indistinguishable Inputs](#cmp11---derive-a-computational-lower-bound-from-indistinguishable-inputs) requires a stated access and cost model. One slow implementation establishes no such limit. Other selection problems need their own sufficient subproblems and valid bounds; the item table is an example of the joins, not their scope.

### CP-RETRY-AND-RECOVER - Share calculations without merging requests or repeating their effects

- **Situation:** Requests repeat expensive calculations, replies can be lost, and a restart can erase some remembered results.
- **Question:** Which work may be shared while each logical request still has its required effect and reply?
- **First useful result or blocker:** Distinct reuse and request identities, a retention rule and a composed procedure, or the missing atomic operation or delivery condition.
- **Start with:** [CMP.14](#cmp14---compose-interacting-computations-through-their-required-observations) for required observations; [CMP.3](#cmp3---share-and-schedule-repeated-subcomputations) for reusable calculations; [CMP.10](#cmp10---choose-a-computational-representation-for-its-access-and-update-operations) for retained records. Return their results to CMP.14's interaction argument.
- **Stop or return:** Keep a sufficient existing procedure. Changed effects, record retention or failure conditions reopen the affected claim. At-most-once effects alone promise neither a reply nor a deadline.

Suppose a request runs a deterministic calculation `f(x)` and adds its result to a shared counter and returns the counter value immediately after that addition. For the input in this example, `f(x) = 5`, and the counter starts at 0. [CMP.14 - Compose Interacting Computations through Their Required Observations](#cmp14---compose-interacting-computations-through-their-required-observations) first distinguishes the intended observations: two independently intended requests must add twice; a retransmission of one request must not add again. A lost reply does not show whether the first addition occurred.

CMP.3 supplies a different distinction. A pure calculation of `f(x)` may be shared when its inputs and governing version make its returned result interchangeable. That reuse does not identify two independently intended additions. Give a logical request its own identifier `k`, reused only by its attempts, and keep its payload consistent. Two requests with the same `x` may reuse the calculated 5 while still adding 10 in total. If the calculation is cheap, there is no need to cache it.

These two identities determine what CMP.10 must represent: a cache for calculation results, when worthwhile, and a separate map from completed request identifiers to their payloads and returned results. Discarding a pure calculation's cache entry only causes recomputation under the same conditions. Discarding a request's completion record while an old attempt can still arrive can repeat an effect. The records' retention rules cannot be borrowed from one another merely because both look like tables.

CMP.14 uses those records in the actual interaction. After obtaining the amount, the receiver must atomically either find `k` completed and recover its original reply, or add the amount and record that reply as `k`'s completed result. Sending the reply may follow. For one request the counter becomes 5; loss of its reply followed by a retry returns the stored 5 without another addition. A genuinely new request adds another 5 and receives 10. A later retry of the first request still receives its original 5. An efficient lookup table by itself supplies no atomicity for this composite operation.

Now let a restart preserve the counter but lose completed-request records. Retrying the first request can raise 5 to 10: calculation reuse may remain correct while the composed effect is wrong. Return to CMP.14's failure model and CMP.10's retention choice. Effect and completion result must survive together if that guarantee is required. Persisting an identifier in one place and performing an external service's effect elsewhere does not close the crash interval between them; the missing operation or external guarantee remains a blocker.

Finally, keep the response question separate. Avoiding repeated effects does not require eventual message delivery. Eventual response does: it needs adequate retry, delivery, processing and retained-state conditions for both request and reply. Those conditions still provide no fixed deadline. Reopen only the affected assumption when it changes. The same separation applies to shared calculations, updates and message protocols beyond this counter example; the direct methods determine their actual identity, atomicity, storage and progress requirements.
