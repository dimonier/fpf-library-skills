---
id: "_ctx.Practical-entries"
title: Practical entries
---

# _ctx.Practical-entries: Practical entries

---

## Practical entries

A mathematical result often becomes an input to further work: a construction supplies the objects for a proof, a failed implication changes the question, and a changed rule requires an argument that its useful properties survive. The patterns in this language help make and connect those contributions.

The two worked connections below start at different places. The first turns a working difficulty into a mathematical question and returns the answer to its subject. The second changes a rule so that independently obtained results can be combined, proves the new rule and revisits it when the requested answer changes. Enter with the results already available; a settled contribution need not be reconstructed.

Use the Table of Contents to find other questions and the actual pattern titles. Each body states its prerequisites, method, examples and limits. A construction can serve mathematics itself or describe another subject; FPF C.29 helps establish what its result says about that subject.

You can ask an assisting agent: “Explain this and comment on my proposal without FPF jargon; use the language of my work.”

### MP-FRAME - Find the mathematical contribution in an unfamiliar problem

- **Situation:** Something in the work is unexplained or fails, and you do not yet know whether another observation, a new model, a mathematical construction or a different computation is needed.
- **Question:** What must become distinguishable or possible for the next answer to be useful?
- **First useful result or blocker:** A mathematical task with a stated use. For example, a cart's travel log gives total distance, but that total cannot tell whether the cart returned to its start. Identify the position question first. With straight-line motion and known displacements, a sequence of signed displacements supplies an account that can answer it. MATH.1 constructs the sequences and their composition; MATH.5 derives the accumulated displacement from the elementary displacements. A sensor report must first be interpreted as the movement it measures.
- **Start with:** FPF B.5.FM. State the working question, identify the participants and relations that may change its answer, and build a small account that yields a consequence. If an unfamiliar theory supplies the account, B.5.TU helps construct its application. B.5.MPC connects the physical, mathematical and computational contributions when the difficulty lies between them. Their bodies are in the FPF publication linked above. If the problem is deciding what an object must let you form or recover, use MATH.16. If it is deciding which distinctions can be forgotten, use MATH.2. If an implication is doubtful, use MATH.6. The question determines the construction; an available formula may settle only part of it. C.29 supplies the interpretation through which a mathematical result answers the original question. C.29.2/.3 develop a needed procedure and its execution.
- **Stop or return:** After the question changes, test whether the summary still determines the answer. If two runs have the same final position but differ in a requested visit, recover the information that separates them. MATH.2 helps locate the failed identification; B.5.QD develops the next useful question. For a working method changed by the result, B.1.5.CM helps describe the proposed operations and their relations; A.3.1.CC checks the claims in that account and its description. The Architectural Reference's worked use follows these choices in detail.

### MP-COMBINE-RESULTS - Change a rule so that separately obtained results can be combined

- **Situation:** A rule works for one input, but splitting the work or combining its results changes the answer.
- **Question:** What must each contribution retain, how should contributions combine, and why will the result still answer the original question?
- **First useful result or blocker:** A composable summary with a stated use. For an arithmetic mean of finitely many real values, return each group's sum and count; add these pairs and divide the total sum by the total count.
- **Start with:** [MATH.23](#math23---develop-a-conjecture-by-changing-a-construction) to develop the question; [MATH.2](#math2---treat-objects-as-the-same-while-preserving-operations-quotient) to choose compatible identification; [MATH.17](#math17---construct-mathematical-spaces-of-operations-and-operations-on-them) to work on the combining operation; [MATH.19](#math19---construct-a-proof-through-intermediate-claims) for the argument.
- **Stop or return:** Use the proved rule within its assumptions. A new statistic, allowed transformation or arithmetic implementation can invalidate a retained-information or proof step; return to that step.

#### Worked connection for MP-COMBINE-RESULTS


**1. Recover the failure and intended result.** Averaging the means of [0] and [2,4] gives 1.5, while the mean of the combined list is 2. MATH.23 turns this difference into a question: which summary recovers the mean of every nonempty combined finite list, for every partition into nonempty groups? The result is a claim and its range of cases for the identification step.

**2. Decide what may be forgotten.** MATH.2 tests identification against the operations still needed. Equal means are insufficient: [0] and [0,0] both have mean 0, but adjoining [2] gives means 1 and 2/3. Instead identify lists with equal sum and count. Concatenation respects that identification because both components add. Empty lists can have summary (0,0); division is defined only after the combined count is positive.

**3. Make the rule itself available for work.** Combine (s,n) and (t,m) as (s+t,n+m). MATH.17 asks whether the operation stays within the chosen space and which laws the use needs. The pair summarizes an input; the binary operation is another mathematical object, which can be compared with a replacement. Associativity permits regrouping; commutativity permits reordering. These laws become premises needed by the proof.

**4. Connect the local calculation to all allowed combinations.** MATH.19 separates two claims: summarizing a concatenation equals combining its summaries, and extracting s/n at positive n returns the list's arithmetic mean. The first follows from addition of sums and lengths. Repeated combination follows by induction over the finite grouping, using [MATH.4](#math4---construct-a-witness-by-induction) if that induction needs construction. The argument thus covers every stated partition.

**5. Use the result with its conditions.** Contributors can now return pairs to combine. FPF C.29 connects the mathematics to actual records: which values belong to the population and whether any are duplicated remain subject questions. Real addition supplies the laws above; floating-point regrouping needs its numerical account when rounding can change the use.

**6. Develop the next question.** If the answer becomes a median, sum and count no longer suffice: [0,0,6] and [0,3,3] share both but have medians 0 and 3. Return to step 2 and use MATH.23 to construct the new question. A quantile method or a different summary can supply the next contribution.
