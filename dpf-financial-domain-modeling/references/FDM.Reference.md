---
id: FDM.Reference
title: "FDM.Reference:1 - The working problem"
---

# FDM.Reference: FDM.Reference:1 - The working problem

> **Problem frame:** Financial work connects institutional relations with resources, records and possible future events. A borrower can have an obligation before a reporting system displays it. A displayed receivable can be disputed or already discharged.
> **First move:** A founder-group account, legal-entity account and portfolio-risk account can all be useful. They answer different questions.

---

## FDM.Reference:1 - The working problem

Financial work connects institutional relations with resources, records and possible future events. A borrower can have an obligation before a reporting system displays it. A displayed receivable can be disputed or already discharged. Money in a related company's account can be relevant to an exposure analysis while remaining unavailable for the borrower's next payment.

The language helps the practitioner recover these relations for a particular use. It does not attempt to replace every financial discipline. Its branch is financial domain modeling: establish the financial subjects, meanings, event conditions and effect claims that a decision, service or connected model needs. The resulting account can be a small table, a diagram or a software model; the carrier does not determine whether its claims are warranted.

Consider a loan with an advance of 100 and one contractual payment of 105 on day 30. A scoring method, its implemented calculator and one produced score are distinct. An applicable decision arrangement can use the score; an agreement can create rights and obligations under its actual formation conditions; funding can make proceeds available; later performance can satisfy only part of what is due. Following those differences explains what a score might contribute and where that contribution could fail.

## FDM.Reference:2 - How the methods connect

FDM.1 recovers a financial position and distinguishes it from its descriptions. FDM.2 chooses the parties and grouping needed by the question. Either can provide an already sufficient answer. A lender explaining which entity owes an amount does not have to model an entire service.

FDM.3 uses adequate parties and terms to derive contractual events. A schedule describes what those terms require under their conditions. Scenario assumptions can produce an expected or conditional flow account; actual occurrences produce a performance account. FDM.4 establishes the effect of an actual event or action and can return a remaining obligation, a discrepancy or an unresolved institutional question.

To obtain the event model, use FDM.1:4.2 for the operative terms and any interpretation that changes the answer. FDM.3:4.2–4.3 then connects each condition to its consequence, constructs the needed state and dates, and derives the amount and next state. Its partial-payment and guarantee cases show how to adapt that construction. A settled fixed payment can still use the short two-row account in FDM.3:5.1.

FDM.5 follows a service output through its use to the participant's intended financial result. It requests a position or effect model when that connection is unclear. Conversely, an accurately modeled financial change can raise the question of whose result it serves. These connections select the next needed result; they do not require all five methods for every use.

There is also a connection within the modeler's present work. While interpreting a payment under contractual terms, the modeler can be deriving a remaining obligation and thereby constructing an account of the borrower's position. Use [FPF B.1.5.EW — Recover How Constituent Actions Enact Encompassing Work][EW] when it is unclear how the present operation performs the encompassing work or which capability is missing. FDM.4:5.2 shows why correct subtraction can leave that work undone. A banking transfer being modeled is a separate occurrence, even when the modeler observes it while working.

## FDM.Reference:3 - Connect models by the financial question

Suppose a lending model stores “loan amount = 100” for the principal, while a payment model requires the amount payable at maturity. Equal-looking field names do not establish an adequate correspondence.

FDM.1 and FDM.2 identify the same lender, borrower and contract. FDM.3 supplies the terms: principal 100, contractual maturity payment 105 in the stated currency on day 30. [SIE.4][SIE] can now establish a qualified correspondence: the principal field supplies the principal input; the maturity amount follows from the applicable terms. Replacing the maturity value by 100 would lose the contractual difference of 5.

[SIE.5][SIE] preserves the relevant party and contract identities. [SIE.6][SIE] combines the statements with their meanings, currency and time. [SIE.3][SIE] asks whether the available models are sufficient for the receiving question and directs a necessary extension. The financial distinction and the general integration method have separate contributions.

For this constructed example, assume that the advance of 100 has actually occurred and is adequately established, creating the obligation to pay 105 on day 30 under the supplied terms.

| Receiving question | Financial statement needed | Meaning that a connection must preserve |
| --- | --- | --- |
| How much was advanced? | Principal advance of 100 under the supplied terms. | The amount advanced. |
| What is contractually due at maturity? | Payment of 105 on day 30. | The contractual amount and event conditions. |
| What was actually paid? | An adequately established payment of 60. | The actual occurrence, with its relevant dates. |
| What remains due after that payment? | 45 under the supplied application rule, with no further fees or interest. | The effect of payment on the obligation. |

FDM.4 supplies the answers about the actual advance, payment and remaining obligation; it does not rewrite the original contractual schedule as if only 60 had been due. A reporting or risk model can retain both the schedule and the observed outcome with their distinct meanings. The connection is complete when it answers the intended question adequately, including any material unresolved premise.

[FIBO][FIBO] supplies a reusable account of financial concepts and their relationships. [ACTUS][ACTUS] supplies a different contribution: logic relating contract terms to scheduled contractual events. A system may need either or both. The example above explains their possible roles; implementing a particular correspondence requires inspecting the chosen definitions, terms, encoding and results.

## FDM.Reference:4 - Parties, resources and several useful structures

A founder-group account, legal-entity account and portfolio-risk account can all be useful. They answer different questions. A common founder can matter to correlated exposures, governance or expected support; the relation alone does not identify another entity as the debtor or make its funds available.

Keep each grouping's criterion and use explicit. Before summing balances, preserve the parties, dates, currencies, restrictions and any relation needed for the intended aggregate. A single organizational tree can be adequate for one report and inadequate for another question. [SIE.5 through SIE.6][SIE] supply unresolved identity and composition work.

The same discipline applies within a loan. The lender's right, the borrower's duty, a bank-account record, usable proceeds and equipment acquired with those proceeds are different subjects. Their relationships explain the financial service.

## FDM.Reference:5 - Practical gain, cost and evidence

The first gain is a smaller, better defined question. A payment report may need only a corrected party reference or a distinction between due and paid. A service design may need to locate who actually uses a score. A disputed obligation may require the applicable institutional rule and evidence of the event it recognizes.

A detailed model costs time to build and maintain. Begin with an adequate existing account and deepen it where a plausible alternative changes interpretation or action. A qualified model, demonstrated non-change or precisely located unknown can be the first useful result.

Recognition and assurance have different jobs. A score presented as a benefit or an aggregate presented as available cash is a reason to examine the account. An actual financial-effect claim needs adequate support for the parties, applicable terms, occurrence and consequence it asserts. A quantitative benefit claim also needs evidence for its comparison and uncertainty. The numerical cases here are constructed under supplied terms.

## FDM.Reference:6 - Source choices and alternatives

The score-and-loan and group-funding cases join two questions: which financial relation a description concerns, and what using the description can change for a participant. A tool supplier can properly deliver information while another participant makes the decision. An authorized automated arrangement can act without a mandatory intermediate change in a human's expectation. A duty or permission is an actual institutional relation under its applicable conditions, distinguishable from descriptions of it. More client admissions are not by themselves a better outcome: suitability, legitimate refusal, participant objectives and the governing conditions can change that conclusion.

[FPF A.2.8][DUTY], [FPF A.2.8.PER][PER] and [FPF A.2.9][ACT] supply the respective duty, permission and communicative-work distinctions. ADM supplies the applied administrative questions. These sources retain results that a vocabulary-only financial model could erase.

A data dictionary is a good first result when the missing answer is a term's meaning. An event model is needed when terms must determine behavior; a service explanation is needed when the use and contribution remain unclear. Combining them is justified by the receiving question. Reconsider a model when actual terms, institutional conditions, observed behavior or a changed use defeats a relied-on distinction.

## FDM.Reference:7 - Using the connected account correctly

For a connected use, establish that the parties, positions, terms and times agree where the models join; that a conditional event remains conditional; and that the evidence supports the particular use or effect being asserted. Use the relevant pattern's substantive questions for its result. An adequate supplied result can be reused while its conditions hold.

The examples expose three consequential mistakes: an amount field substituted for its financial meaning, a group aggregate substituted for available resources and a service output substituted for the participant's outcome. Recover the missing relation rather than adding another label. When only one such question is unresolved, the other adequate accounts remain usable.

For source qualifications, citation and edition information, see the [Sources and Edition Notes](#financial-domain-modeling-principles-framework-sources-and-edition-notes).

## FDM.Reference:End
