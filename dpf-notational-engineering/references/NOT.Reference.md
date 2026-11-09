---
id: NOT.Reference
title: "NOT.Reference:1 - Problem frame and the work of designing a notation"
---

# NOT.Reference: NOT.Reference:1 - Problem frame and the work of designing a notation

> **Problem frame:** Use this language when an expression's conventions need to be constructed or changed so that people or computational agents can work with it.
> **First move:** A group uses a simple rule, `r(q,b) = q + q + b`, over real numbers. Here q is one supplied input value and b is a shared parameter. The immediate work is to obtain values, inspect dependence on b and change that parameter.

---

## NOT.Reference:1 - Problem frame and the work of designing a notation

Use this language when an expression's conventions need to be constructed or changed so that people or computational agents can work with it. The work may involve mathematical reasoning, a model, an algorithm, a diagram of a method, a movement score or another structured expression. Its subject supplies the distinctions and correct consequences; notational engineering supplies ways to make those distinctions expressible and usable.

A reader can recognize all the signs and still be unable to compose them, recover a dependency or perform the next transformation. Two displays can look consistent while referring to different objects. An abbreviated instruction can rely on preparation that its new reader lacks. These difficulties become especially visible when descriptions pass between specialists, people and AI agents.

Begin with one operation and an expression on which it matters. You need enough subject knowledge to say what a correct result would be, or access to someone who can supply that contribution. The individual methods then expose their additional prerequisites: rules for binding names, an interpretation, an allowed transformation, a temporal reference or a performer's available operations. Knowing a particular branch of mathematics, physics, programming or music is required only for a use that needs it.

Keep a sufficient notation when its conventions already serve the work. A.6.3.RT.OE in FPF helps construct an expression around a needed operation under available conventions. This DPF becomes useful when the conventions themselves leave a consequential distinction, interpretation or manipulation unsupported. Repair a mistaken subject account at its source; notation design can make that mistake visible without supplying the subject's answer.

## NOT.Reference:2 - Forces that shape the choice

| Requirement | Choice it creates |
| --- | --- |
| Express the needed distinctions | More detail can support one inference while obscuring another. |
| Make a frequent operation easy | A form convenient for lookup can make revision or composition expensive. |
| Preserve meaning during change | A compact rewrite can hide binding, side conditions or an observable intermediate result. |
| Retain complementary strengths | Several forms can aid different operations while adding correspondence and update work. |
| Fit the reader's preparation | A familiar shorthand can depend on acquired skills or an interpreter unavailable to the next reader. |
| Fit the medium | A persistent inscription, a sound and a gesture make different inspection and replay operations available. |

A notation's quality is relative to the work, reader and access conditions. C.2.8 characterizes the structure a reader can recover from a publication under stated resources and preparation. Use that common account when comparing expressions; the number of symbols or successful recognition of their names does not by itself measure useful understanding. C.11.DUA helps decide when an additional comparison can change the choice enough to warrant its cost.

## NOT.Reference:3 - The methods and their connections

### NOT.Reference:3.1 - Design what can be expressed and done

[NOT.1](#not1---choose-the-distinctions-and-operations-a-notation-must-support) derives a design requirement from the operation and from cases that need different treatment. [NOT.2](#not2---define-expression-rules-for-recoverable-binding-and-composition) constructs formation, grouping, scope and reference rules. [NOT.3](#not3---give-expressions-an-operative-interpretation) gives the resulting expressions a meaning and a route by which a prepared reader obtains a consequence. These contributions connect what the work needs, what can be written and what the reader can do with it.

[NOT.4](#not4---construct-transformations-of-expressions-that-preserve-their-use) constructs changes to expressions, with their applicability conditions and preserved observations. A mathematical argument may justify a rewrite. A computational procedure may apply it. A surrounding physical or organizational use determines whether the preserved observation is sufficient. The same marks can therefore admit one transformation in a pure calculation and require another treatment when each occurrence performs an interaction.

### NOT.Reference:3.2 - Translate, combine and improve notations

[NOT.5](#not5---translate-between-notations-while-tracking-lost-distinctions) constructs a translation with the receiving question in view. It identifies losses, needed supplements and the limits of returning to the source. [NOT.6](#not6---coordinate-complementary-representations-through-shared-references) keeps several useful forms in joint use: it connects their referents and dependencies, then interprets an edit before propagating its consequences. A derived display value and an independently observed value can require different treatment even when they occupy similar cells.

[NOT.7](#not7---redesign-a-notation-around-the-readers-difficult-operations) locates an actual reading or editing burden, changes the expression or editing arrangement there, and compares both the intended improvement and effort moved elsewhere. [NOT.8](#not8---construct-temporal-or-embodied-notation-with-a-reading-procedure) adds the origins, frames, segmentation and available replay or enactment operations needed when signs unfold in time or bodily action. A temporal score can need the same formation, interpretation, translation and redesign methods as a static diagram.

There is no compulsory eight-stage process. Enter where the difficulty occurs. A translation loss can return to the original design requirement. An inconsistent update can expose a reference problem. A reading difficulty can require teaching a missing operation rather than another symbol. The working reminder for a longer combination is: **Recover the operation; make references and interpretation usable; carry the intended change; retain useful differences; repair the remaining burden.** The relevant bodies supply the conditions under which each continuation is needed.

### NOT.Reference:3.3 - Constituent actions in ongoing work

Defining an operator's binding rule can be part of constructing an expression grammar while a notation for working calculations is being designed. If users must transform an expression without changing its meaning, visually convenient grouping is insufficient: the interpretation of the transformed expression must remain recoverable. Symbol recognition and subject knowledge can both be present while the intermediate ability to follow binding and transformation rules is absent. The notation design must provide those rules and support their use; a successful reading of one expression does not establish the whole notation's suitability.

FPF B.1.5.EW helps recover these constituent–whole connections; B.1.5.RS examines a proposed replacement. Examine the constituent–whole connections that can change the present result. Carrying out a Method described here can require additional capability, available support and compatible resources for its constituent operations or for the larger work it contributes to.

## NOT.Reference:4 - Worked connection - A formula, graph and table must change together

### NOT.Reference:4.1 - Construct the expressions and their interpretation

A group uses a simple rule, `r(q,b) = q + q + b`, over real numbers. Here q is one supplied input value and b is a shared parameter. The immediate work is to obtain values, inspect dependence on b and change that parameter. This stipulated mathematical example supplies its own interpretation; applying it to a price, measurement or other subject would require a separate account of that subject.

NOT.1 makes the operations explicit. A list of output values supports lookup at listed inputs. It does not necessarily support changing the rule or obtaining an answer at an unlisted input. NOT.2 fixes the references: both q occurrences use the same supplied value; b denotes the same parameter throughout this use. Parentheses or graph connections determine which operands each addition consumes.

For an operation graph, connect the input q to both inputs of one addition, then connect its result and b to a second addition. NOT.3 interprets those connections as addition of the supplied real values. With b=1 and q=0, 1 and 2, the outputs are 1, 3 and 5. A reader can obtain them by following the graph without a software implementation.

NOT.4 permits the transformation `q + q + b` to `2*q + b` under that interpretation. The arithmetic identity supplies preservation for every admitted q and b. A shorter inscription may be useful for changing or explaining the rule, but its symbol count does not establish that every reader will find it easier.

### NOT.Reference:4.2 - Translate only as far as the receiving question allows

NOT.5 translates the rule at b=1 into the table `(0,1), (1,3), (2,5)`. Lookup at those three inputs survives. The table alone does not determine the value at q=3: both `2*q + 1` and `2*q + 1 + q*(q-1)*(q-2)` agree on its rows, but give 7 and 13 respectively at q=3.

If the receiving work needs the general rule, retain that rule or a sufficient construction of it alongside the table. If it only needs the three listed values, the table can suffice. There is no reason to demand recovery of discarded distinctions that cannot affect the requested use.

### NOT.Reference:4.3 - Interpret an edit before propagating it

Now a participant asks that the output at q=1 become 4 while the coefficient 2 remains fixed. NOT.6 treats this as a constraint on the rule, not as an isolated replacement of a displayed cell. It gives `2*1 + b = 4`, hence b=2. The graph receives the new parameter; the table becomes `(0,2), (1,4), (2,6)`. Its former values were derived outputs, so they are recalculated.

If another participant also requires the old output at q=0 to remain 1, that requirement gives b=1. It conflicts with b=2 under the retained rule. The useful result is the conflicting pair of requirements and the assumption on which it depends. Silently choosing one edit would conceal the decision that the group must make.

An independent measurement record is different again. If its row says that an observed output was 3, a parameter change does not change that past observation. Keep the record and updated prediction separately so that the difference can inform the subject inquiry. Correspondence between representations does not license overwriting every similarly named value.

### NOT.Reference:4.4 - Change the operation and revisit the affected construction

Suppose a later description replaces each occurrence of q with a fresh sensor read. This changes the operation assumed in :4.1. If consecutive reads return 4 and 5 while b=1, `read() + read() + b` returns 10; `2*read() + b` using the first reading returns 9. The former rewrite is still correct for a single supplied q, but it cannot be transferred to this new interpretation merely by replacing the printed name.

NOT.3 restores what an occurrence now does; NOT.4 reopens the transformation's condition. If the intended operation is to take one sample and reuse it, explicitly bind that sample once. If two observations are required, retain them. CMP.12 provides the algorithmic interpretation when implementing those instructions. The physical measurement method supplies what each read obtains and under which conditions.

Finally, NOT.7 can compare the group’s editing arrangements. A single named b avoids separately editing every derived row, while a table remains useful for direct lookup. Keeping both requires the correspondence already constructed in NOT.6. The comparison is about the actual operations, not a declaration that formulas or tables are universally better.

The connected result is a usable rule, its complementary expressions and an account of what the change affects. An adequate answer may be the new table, the conflict, or the need for a different reading operation. This combination also applies to other expression families: the arithmetic and sensor supply the worked conditions, while the transferable work is to recover references, interpretation, loss and intended change.

## NOT.Reference:5 - Conditions of use, checks and recurring failures

When a combined use needs checking, ask whether its participants can recover the same subject references, whether each operation has the inputs and interpretation it consumes, and whether a change reaches every dependent expression that matters. Keep independent observations, intended constraints and derived values distinguishable. An unchanged source can retain its previous interpretation; a new receiving question can make a formerly harmless loss important.

Three failures illustrated above need different repairs. More explicit syntax repairs ambiguous grouping or binding. A restored interpretation repairs an unknown operation. A translation supplement repairs a discarded distinction. Repeating a correct legend will not necessarily repair any of them. Use the method that changes the difficulty actually observed.

Prepared readers can fill gaps without noticing. A worked use by such a reader supports that use under its preparation and access conditions. Human learning, performance by an AI agent and reliable machine execution need their own applicable evidence. To assess understanding, ask for an actual consequence and a meaningful change; do not infer general capability from recognition of labels or fluent repetition of the example. EXD and HCD supply explanation and learning methods when those are the missing contributions.

Temporal and embodied uses require further care. Recover the reference that determines when or where a sign applies. A pause may be a specified rest or an observation gap; turning a body changes the room direction of body-right. NOT.8 carries these distinctions through decoding and keeps a correctly interpreted instruction separate from the capability to enact it. Its rhythmic and movement cases offer different ways to test that general method.

Additional assurance should serve the next use. A small construction and its changed-condition case can settle a local design choice. A claim about faster human learning or broad usability requires more than that construction. Seek the corresponding evidence when that stronger claim matters; retain the useful bounded result meanwhile.

## NOT.Reference:6 - Consequences and Architectural Rationale

This repertoire makes the expression and its interpretation available for deliberate work. Practitioners can expose a tacit step, preserve a useful rewrite, return from a lossy summary, coordinate complementary forms or redesign an expensive operation. They can hand a named contribution to another person or computational agent without assuming that the receiving agent reconstructs the same conventions unaided.

The organization follows operations across media. A catalogue organized by mathematical symbols, programming languages, diagrams, music and dance is valuable for finding established conventions. It would repeat several design problems here while hiding their common structure. Conversely, imposing one universal notation would sacrifice distinctions or useful operations of particular practices. The selected methods support reuse of existing notations and construction of differences where the receiving work needs them.

Formation, interpretation and transformation have distinct results. A well-formed expression can still lack an interpretation; an interpreted expression can lack an effective evaluation algorithm; a valid result can be expressed in a form that makes its revision difficult. Keeping those questions separate lets their methods connect without crediting syntax for a mathematical proof, a computational construction or a performer's preparation.

Translation and coordination also differ. A one-way translation may deliberately discard information irrelevant to its receiver. Continued joint use needs correspondence and an update policy, sometimes retaining several noninterchangeable accounts. Redesign then asks whether the resulting reading and editing operations justify their combined burden. NOT.8 specializes these operations where temporal or embodied carriers change the references and access conditions; it does not make every notation a performance score.

The two Parts group this presentation. They do not prescribe an order of work or imply that all eight methods are parts of every project. A narrower mathematical, programming or performance profile can reuse several bodies and add the rules peculiar to its practice. Such a profile must state which new operation or distinction it adds. The present language provides no complete grammar for every subject and no general theory of perception or learning.

## NOT.Reference:7 - Shared sources, alternatives and refresh

The bodies preserve their adopted contributions and limits. Several source lines also explain the arrangement of the language as a whole.

| Source line | Contribution and comparison |
| --- | --- |
| Blackwell and Green's [Cognitive Dimensions account](https://www.cl.cam.ac.uk/~afb21/publications/BlackwellGreen-CDsChapter.pdf), especially activities and notation/environment distinctions | This historical framework makes the actual operation and design trade-offs discussable. NOT.1 and NOT.7 connect those observations to a construction and a comparison. A list of desirable dimensions alone does not decide a redesign. |
| [NotaScope](https://ieeevis.b-cdn.net/vis_2023/pdfs/v-full-1328.pdf) and the [2024 Programming User Experience method](https://ppig.org/files/2024-PPIG-35th-brazauskas.pdf) | Matched expression galleries and structured expert observations can expose design differences. The bodies retain the limits of metrics and the small expert study; they do not turn either into a universal measure of understanding. |
| Formal expression, binding and graphical-reasoning sources in NOT.2–.4, including Macbeth, Dutilh Novaes and Piedeleu/Zanasi | Their contributions make the permitted manipulations and the reader's reasoning operations explicit. The synthesis allows syntax and spatial arrangement to support reasoning while requiring the actual interpretation and applicable rule. A resemblance between drawings alone supplies neither. |
| [Bidirectional programming](https://janis-voigtlaender.eu/papers/ThreeComplementaryApproachesToBidirectionalProgramming.pdf) and [partial states](https://link.springer.com/chapter/10.1007/978-3-032-22723-2_2) | These constructions expose information loss, retained complements and different meanings of an update. NOT.5–.6 adapt those questions to coordinated representations; automatic two-way copying is inadequate when a target edit is ambiguous or conflicts with a retained condition. |
| Ainsworth's [DeFT account](https://www.inf.ufpr.br/alexd/REPRESENTACOES_EXTERNAS/Ainsworth_2006.pdf) and the [recent meta-analysis of multiple representations](https://link.springer.com/article/10.1007/s10648-024-09958-y) | Complementary forms can constrain interpretation and support different operations, but coordination and preparation cost matter. These contributions support a conditional choice of several forms, not an assertion that adding forms always improves learning. |
| Solkattu, Takadimi, movement-notation and auditory-notation sources compared in NOT.8 | Different conventions reveal the importance of temporal reference, segmentation and the distinction between a score and its realization. The synthesis keeps their differences rather than assigning one meaning to every syllable, gesture or silence. |

Current rewriting and binding research can improve how expressions are transformed; bidirectional methods can change which updates are recoverable; empirical studies can revise the assumed burden for particular readers and media. Reopen the affected method when such a contribution changes its construction or supported use. A newer source or more familiar convention alone does not establish a better choice.

## NOT.Reference:8 - Relations to other frameworks

[Mathematical Thinking (MATH)](https://github.com/ailev/FPF/blob/main/DPFs/Foundational%20Thinking%20DPF%20Suite/MATHEMATICAL-PRACTICE-DPF.md) supplies objects, compositions, arguments and interpretations used when the represented construction is mathematical. [Computational Thinking (CMP)](https://github.com/ailev/FPF/blob/main/DPFs/Foundational%20Thinking%20DPF%20Suite/COMPUTATIONAL-THINKING-DPF.md) supplies effective procedures, including interpreters and translations. NOT designs the expression conventions those methods can consume; it does not substitute a mathematical meaning for an algorithm that obtains its consequence.

[Mathematical Modeling (MMP)](https://github.com/ailev/FPF/blob/main/DPFs/Foundational%20Thinking%20DPF%20Suite/MATHEMATICAL-MODELING-PRACTICE-DPF.md), [Physical Thinking (PHY)](https://github.com/ailev/FPF/blob/main/DPFs/Foundational%20Thinking%20DPF%20Suite/PHYSICAL-THINKING-DPF.md) and FPF C.29 connect a subject with mathematical constructions and interpreted observations. B.5.MPC coordinates mathematical, physical and computational contributions when they are jointly needed. NOT.5–.6 help express those correspondences while keeping the related objects and claims distinguishable.

In FPF Core, C.37.MP relates the claims needed when different uses of a working method require complementary descriptions. Explanation Design (EXD) develops explanations; Human Capability Development (HCD), in the Human Capability Engineering Suite, develops and assesses human capabilities. They remain external contributions, used when the work needs that result. A notation repair can help any of them, while an operation missing from the method or from the reader's preparation needs the corresponding method or learning contribution.

The [Suite Reference (Foundational)](https://github.com/ailev/FPF/blob/main/DPFs/Foundational%20Thinking%20DPF%20Suite/FOUNDATIONAL-THINKING-DPF-SUITE-REFERENCE.md) locates the publications and their shared architecture. Use the cited body's operative rules when its question arises. If an available edition changes those rules or no longer supplies the result your use needs, revisit that dependency rather than assuming that the shared PatternID guarantees compatibility.

## NOT.Reference:End
