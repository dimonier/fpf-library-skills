---
id: SIE.Reference
title: "SIE.Reference:1 - Meanings, identifiers, claims, carriers, and world-side referents remain distinct"
---

# SIE.Reference: SIE.Reference:1 - Meanings, identifiers, claims, carriers, and world-side referents remain distinct

> **Problem frame:** | Working object | Question it answers | What it does not establish by itself | | --- | --- | --- | | term or designation | Which sign is used in one source?
> **First move:** The first useful whole is `SemanticIntegrationPackage@Use`. It is a connected, inspectable set of eight results, not necessarily one file and not necessarily RDF or a graph:

---

## SIE.Reference:1 - Meanings, identifiers, claims, carriers, and world-side referents remain distinct

| Working object | Question it answers | What it does not establish by itself |
| --- | --- | --- |
| term or designation | Which sign is used in one source? | one shared concept or referent |
| concept, type, or relation | Which meaning or classification does the source express? | that another source uses the same meaning |
| schema or semantic model | Which structures and constraints can be represented? | truth of the represented claims or fitness for this receiver |
| identifier | Which scheme-specific sign identifies under one issuer's rules? | cross-source identity, master identity, or authoritative value |
| claim | What is asserted with which scope, interval, source, and uncertainty? | agreement, preference, authorization, or action |
| data item or carrier | Where is a representation recorded or transported? | preservation of meaning through extraction or transformation |
| world-side referent | Which entity or occurrence the claim is about | that two descriptions identify it at the same grain and interval |

## SIE.Reference:2 - Source authority and receiving authority remain separate

A source owner can define a scheme or publish a value without authorizing the receiver's decision. A master-data steward can decide an enterprise identity without deciding product release or recall. Systems Engineering can decide configuration and effectivity without owning a cross-source mapping. Data Engineering can operate a pipeline without deciding semantic equivalence. The receiving application or professional practice owns its operational or decision outcome.

SIE makes the semantic premises and losses inspectable, tests them for the named use, and returns unresolved decisions to their direct owners. It does not borrow their authority.

## SIE.Reference:3 - Pattern relations do not prescribe a lifecycle

The patterns have information dependencies, not one mandatory calendar sequence. `SIE.1` and `SIE.2` often expose the first stop. A practitioner may enter `SIE.5` when the use and source inventory already exist, `SIE.8` when a realization choice is current, or `SIE.10` when an existing interface needs validation. Discovery, alignment, mapping, implementation, and testing can iterate.

`SIE.3` supplies a qualified reused or developed model when adequacy is unsettled. `SIE.11` follows a changed semantic premise to the results that actually relied on it; a compatible reference repair can finish directly. `SIE.12` supplies the arrangements needed by actual shared-module users. A known adequate model, an unchanged use, or one local interface can continue without performing those further Methods.

## SIE.Reference:4 - The first whole result

The first useful whole is `SemanticIntegrationPackage@Use`. It is a connected, inspectable set of eight results, not necessarily one file and not necessarily RDF or a graph:

1. use contract;
2. source manifest;
3. correspondence set;
4. cross-source identity disposition when it is load-bearing;
5. source-qualified claim composition;
6. mapping specification;
7. realization and interface;
8. validation account.

The package references any SIE.3 model qualification on which it relies. Preserve identity premises where the answer depends on them; explain their non-use only when it affects interpretation or later reliance. A package may return explicit conflict or non-comparability. Positive validation requires matching evidence for every load-bearing premise of the claimed whole use or contract-permitted subset.

[SIE.13](#sie13---construct-a-semantic-integration-for-a-named-receiving-use) supplies the Method for constructing this whole: derive the needed contributions from the answer, connect their use conditions, obtain the next missing result, and bring the permitted combination into receiving use. The following sections explain the architecture and applications of that Method.

## SIE.Reference:5 - Use the repertoire at the scale of the missing result

The [package anatomy](#siereference13---package-anatomy-and-direct-result-relations) states what must be inspectable when the promised result is a whole semantic interface package. Use the Methods whose results are missing or whose qualifications need reopening. With a supplied use contract and qualified source meanings, [SIE.4](#sie4---judge-cross-source-correspondences-and-their-permitted-uses) can return one warranted correspondence or an incompatibility and stop. With an existing interface and its premises, [SIE.10](#sie10---validate-a-semantic-integration-result-for-its-receiving-use) can identify a failed receiving-use obligation without rebuilding that interface. Reuse an available result when its subject, source editions, use, and conditions still match; reopen the contribution whose premise changed.

Some relations need separate answers even when one practitioner handles them. A correspondence supplies a relation between meanings; [SIE.5](#sie5---resolve-cross-source-identity-without-erasing-identifier-authority) supplies a cross-source identity disposition when the answer depends on the same entity at a particular grain and interval. [SIE.6](#sie6---fuse-source-qualified-claims-without-erasing-conflict) then qualifies the composition of source claims. Identity can hold while claims conflict, and claims can be compared without merging their subjects. [SIE.7](#sie7---specify-semantic-extraction-and-transformation-mappings) specifies executable behavior from those premises; [SIE.8](#sie8---choose-virtual-materialized-or-hybrid-semantic-realization) compares ways of supplying it; [SIE.9](#sie9---connect-a-receiving-use-through-a-semantic-interface) carries the qualified result into the receiver's work. Their results constrain one another, while a defect can return to any supplying pattern.

A bounded interface package needs adequate models, its other load-bearing premises, and the required implementation and validation evidence. The five [applications](#cross-pattern-application) demonstrate interface and shared-module uses. Their differences change the work: AP242/QIF needs configuration and effectivity premises; semiconductor traceability makes identity grain and issuer rules central; an analytic can fail on a unit conversion or hidden default; live provider comparison may need qualified difference and non-comparability instead of a shared value. The shared-equipment commons adds module decisions, dependencies, and semantic change. Each application uses the same repertoire at the scope of its receiving question.

If a required distinction cannot be expressed, SIE.3 reuses, extends, or constructs the needed semantic content. An unresolved source definition still limits the dependent mapping or interface claim. SIE.11 compares changed reliance and obtains the affected domain results; its wider account is conditional on a receiving need. SIE.12 supplies shared-module maintenance and decision arrangements where actual users require them. The source, implementation, and receiving owners retain their respective returns.

Use [SIE.13:4.1–4.4](#sie1341---establish-what-would-let-the-receiver-continue) when the missing contribution is not yet known or the available results still need to be connected into the receiving answer. It retains these local entries and sufficient stops.

## SIE.Reference:6 - Qualify the combined arrangement

Three questions remain distinct. Is each source meaning, correspondence, identity disposition, or composition rule supported? Does that result permit the particular use made of it? Can all relied-on results and their realization satisfy the receiving contract together? A true relation may be too lossy for one transformation. Two individually current sources may concern different effectivity intervals. Several feasible components may exceed a shared access limit. The relevant bodies answer their local questions; the whole-use conclusion also needs these joins and common conditions.

For the combination, bind the same receiving question and the actual subjects, grain, intervals, source and rule versions, accepted losses, authority, and failure branches. Where contributions use shared requests, credentials, storage, time, or operating support, compare their total demand with the applicable conditions, including required trace and recovery behavior. A permission to query does not imply permission to replicate or disclose. Keep a common source or derivation visible when several results rely on it; repeated citations or passing tests of the same premise are not independent support for a different claim. The realization comparison belongs in [SIE.8, Solution](#sie84---solution) and the bounded validation in [SIE.10, Solution](#sie104---solution). [SIE.13:4.2–4.6](#sie1342---derive-the-required-contributions-from-the-answer) constructs the required connections, obtains missing contributions and returns their combined result to the receiving use.

### SIE.Reference:6.1 - A shared request limit changes the provider result

Consider a constructed variation of [APP-SIE-04](#sieapplication4---app-sie-04---high-change-provider-availability-without-a-materialized-graph). The receiving contract allows an explicitly incomplete purchasing answer. Assume that adequate models and the required source, correspondence, identity, and composition premises have been supplied. Provider A still means “on hand”; provider B means “available to promise”; their claims must keep those meanings. Permissions allow live retrieval and the agreed immediate presentation, but prohibit replication.

For this illustration, four calls retrieve A's required rows, four retrieve B's, and three retrieve the common source and rule trace required even for a partial answer. All calls consume one gateway allowance of ten requests in the agreed request window; none is shared or counted twice. Retries also consume the allowance, and the contract accepts neither a copied cache nor deferral to another window for this answer. Each pair of contributions fits: 8, 7, or 7 calls. The complete answer requires at least 11 before retries, so pairwise feasibility does not establish the whole arrangement.

SIE.8 therefore cannot select that arrangement as supplying the complete result. Under the stated incomplete-answer permission, an A-only result with the required trace uses seven calls before retries and can be proposed with B explicitly marked as not retrieved under the request limit. SIE.9 must preserve A's on-hand meaning and the incomplete branch; it must not render B as zero stock or call the response a complete provider comparison. For example, an A source value `on_hand = 12` observed at `T` becomes a receiving row `12 on hand at T`, with its source and rule trace and the branch `B not retrieved`. It supplies no available-to-promise value.

SIE.10 tests the remaining required conditions before any bounded positive validation. If both providers are mandatory, return a stop and the exact missing result: for example, an access-owner decision changing the allowance or an implementation that demonstrably reduces calls while preserving meanings and trace. Omitting provenance is not an equivalent repair.

The quantities are construction assumptions, not measurements of providers. Actual use needs evidence for the gateway condition, call demand, permissions, freshness, behavior under failure, and the receiver's interpretation. Passing source lookups or several pairwise tests cannot supply that evidence for the whole. A changed allowance reopens the affected realization and use validation; an unchanged correspondence can remain usable.

**Constituent actions in ongoing work.** While processing an exchange, resolving a source identifier can constitute part of interpreting a correspondence, within an ongoing integration of the receiving information. If the receiving use changes from present eligibility to eligibility at an earlier date, a lookup that returns only the present subject state is no longer sufficient. The team may have parser and database skills but lack the intermediate meaning or temporal-identity account. Supply that contribution through the relevant SIE Method rather than treating a successful query as a successful integration. FPF B.1.5.EW helps recover the connection; SIE.8 and SIE.10 keep the whole arrangement and its warranted validation in view.

## SIE.Reference:7 - Architectural Rationale

The language is organized around the results that make a receiving use possible. Source recovery, relation truth, bounded identity, claim composition, executable semantics, realization, interface, and validation can fail independently and return to different owners. Keeping their Methods directly accessible permits a useful early stop and replacement of one contribution without inventing a new lifecycle for the entire arrangement.

| Serious alternative | When its contribution is enough | Why SIE keeps a different boundary for the combined use |
| --- | --- | --- |
| Use FPF and the owning engineering, data, MDM, or application practice directly | One exact representation, domain identity, configuration, pipeline, or decision result closes the question. | A recurring cross-source interface question still needs source-qualified correspondences, mappings, interpretation, and receiving-use validation joined together. SIE supplies that remainder and returns the other results to their owners. |
| Treat ontology engineering as the whole practice | The missing result is a model that expresses the required distinctions and questions. | An adequate existing model can support integration without a new ontology. Model construction alone does not supply identity dispositions, claim composition, executable mappings, or a usable interface. SIE.3 supplies that distinct model result. |
| Make a materialized knowledge graph the standard result | Permitted copying, a suitable refresh and correction arrangement, and reproducible queries meet the contract. | A graph is one realization. The live-provider case forbids replication, and useful incompatibility must remain expressible. Conversely, live federation is unsuitable when its access, availability, or repeatability cannot meet the use. |
| Use one canonical enterprise model and master identity | A responsible domain or MDM authority has supplied a bounded common model, identity, or authoritative-value result that the use can rely on. | Integration alone cannot grant that authority or erase local grains, versions, claims, and incompatible meanings. SIE preserves the supplied result's scope and the source identifiers that make correction possible. |
| Collapse the work into one prescribed lifecycle | A local team may use a repeatable plan for a recurring, stable situation. | A direct identity question, realization decision, or validation failure has different inputs and stops. The pattern language preserves those entries and conditional result relations; the local plan remains one use of it. |

The complete repertoire joins model adequacy, semantic interfaces, changed reliance, and commons maintenance through their actual results. Completing a small model or interface question remains useful on its own. A continuing service requires its operational results, and a commons requires the rights and dependencies of its actual users.

### SIE.Reference:7.1 - Source contributions behind the arrangement

The [source-use account](#siesources1---source-use-and-currentness) gives the qualified source cut and its dates. The shared architecture combines contributions that answer different questions; it does not treat a standard or tool family as a complete integration Method.

Terminology and registry practice, including [ISO 704:2022](https://www.iso.org/standard/79077.html) and [ISO/IEC 11179-3:2023](https://www.iso.org/standard/78915.html), makes source objects, concepts, definitions, designations, items, and versions distinguishable. SIE.2 adapts that contribution into the smallest inventory needed by the receiver. This improves on schema inspection plus informal recollection: a mapping can point to the operative definition and edition. It still cannot infer a cross-source relation from a registry entry. FPF's source-local meaning and direct Bridge distinctions supply the separate generic questions used by SIE.2 and SIE.4.

[SKOS](https://www.w3.org/TR/skos-reference/) supplies different correspondence forms; [SSSOM 1.0](https://mapping-commons.github.io/sssom/1.0/spec-model/) makes endpoints, predicates, justification, provenance, and source versions inspectable. [OAEI 2025](https://oaei.ontologymatching.org/2025/results/) contributes task-dependent alignment evidence. In [SIE.4, SoTA-Echoing](#sie411---sota-echoing), SIE.4 uses those contributions to separate candidate generation, direct relation judgment, and a receiving-use qualification. A two-column crosswalk or score can help find a candidate, but the chosen relation, permitted loss, and counterexamples determine whether it can support this transformation. A new endpoint sense or defeating counterexample reopens that row.

[ISO 8000-115:2024](https://www.iso.org/standard/88847.html?browse=tc) contributes identifier ownership, semantics, restrictions, and resolution inputs within its declared scope. [PROV-O](https://www.w3.org/TR/prov-o/) supplies distinctions for derivation, attribution, revision, specialization, and alternate descriptions. SIE.5 and SIE.6 adapt these into two different results: an identity disposition and a source-qualified claim composition. A merged key cannot replace the first, and provenance cannot settle the second's truth or authority. The SEMI and GS1 traceability sources in [SIE.5, SoTA-Echoing](#sie511---sota-echoing) make grain, issuer, and event-time failures concrete; they do not authorize a recall or establish an enterprise master identity.

[R2RML](https://www.w3.org/TR/r2rml/) and [QVT 1.3](https://www.omg.org/spec/QVT/) contribute bounded declarative mapping and transformation forms. The [Ontop line](https://ontop-vkg.org/research/publications.html) demonstrates a virtual realization over mappings. SIE.7 and SIE.8 adapt those contributions into an independently inspectable semantic rule and a choice among whole arrangements. This costs explicit specification and comparison, but it permits an implementation to change while preserving the required behavior. Neither RDF nor MOF nor a graph store is required. Failure of a mapping premise returns to the semantic rule; an implementation discrepancy returns to its implementer.

[SHACL](https://www.w3.org/TR/shacl/) supplies declared graph-constraint tests. [DQV](https://www.w3.org/TR/vocab-dqv/) and the data-quality sources in [SIE.10, SoTA-Echoing](#sie1011---sota-echoing) contribute dimensions, measurements, and process questions. SIE.10 retains their distinct evidence roles and adds the representative receiving-use replay. A passing shape can coexist with the wrong identity or a concealed stale branch. The arrangement therefore uses categorical pass, narrow, unresolved, and stop results under the contract, rather than a compensating overall score. Evidence for implementation and operation remains necessary when the conclusion relies on actual service behavior.

[LOT](https://doi.org/10.1016/j.engappai.2022.104755) contributes ontology requirements, development, publication, and maintenance to SIE.3. Sufficient model reuse remains a completed result. [LOT4KG](https://lot.linkeddata.es/LOT4KG/) distinguishes ontology work from graph construction and relates changes to dependent mappings, constraints, and validation; SIE.11 uses those relationships for graph realizations. [OBO Foundry principles](https://obofoundry.org/principles/fp-000-summary.html) contribute scoped module, term-stability, maintenance, and communication practices to SIE.12, with their community-specific rules qualified in the source account.

Reconsider the affected choice when a simpler qualified contribution supplies the same result, a represented use repeatedly needs a missing Method, or a source or case defeats a relied-on boundary. When the need is a reusable Method repertoire, [FPF C.39.RP](../../FPF-Spec.md#c39rp---organize-a-repertoire-for-method-development) returns inspectable alternatives, source contributions, relations, and gaps for that comparison; the integration-specific question stays in SIE.

## SIE.Reference:8 - Costs, perspectives, and correction

The gain is an answer whose meanings, sources, qualifications, and unresolved branches can survive into receiving work. The cost is source recovery, explicit relation and loss judgments, trace, implementation evidence, and representative tests. Keep that burden proportional to what can change the answer. A single correspondence question does not require a service architecture; a claim of a usable whole interface cannot omit a load-bearing identity or provenance obligation merely to stay cheap.

The source cut reflects the receiver's question and the sources practitioners can inspect. A well-documented schema or a familiar formal vocabulary can receive more attention than an inaccessible local rule. Source experts and receiving users may also differ over which distinctions matter. Make missing access, authority, meanings, and perspectives visible in the contract and inventory instead of treating absence as agreement. The five constructed applications illustrate how to work; their [coverage limits](#siereference17---representative-case-coverage) supply no empirical claim about production performance or effectiveness in other settings.

Correct the result at the point that owns the defect. A hidden default returns to SIE.7; an unsafe interpretation of a partial response to SIE.9; unsupported identity to SIE.5 and the required domain authority; a pipeline discrepancy to Data Engineering. For the AP242/QIF case, [SYSE.13](SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse13---establish-configuration-identity-variants-and-effectivity) supplies the decision-specific configuration basis, including actual subjects and effectivity; SIE consumes those premises and can return a mismatch, but does not decide the engineering configuration. The other [owner boundaries](#siereference16---fpf-neighboring-practice-and-authority-boundaries) remain in force. Preserve unaffected qualified contributions and retest what the correction can change.

## SIE.Reference:9 - Before relying on the whole result

Recognition asks which available pattern can supply the next useful result. Assurance asks what supports the actual reliance. Use the checklists in the selected bodies and inherit their answers only while the subject, content, use, source versions, and relevant conditions match. For a combined package, answer these questions in the account the receiver needs:

- Can the receiver recover the question, answer claims, accepted losses, authority boundary, and useful stop? An early correspondence or inventory result must not be presented as a validated interface.
- Can every load-bearing correspondence, identity disposition, and claim-composition premise be traced through the mapping and interface, with its grain, interval, limits, and unresolved branches?
- Does the [whole arrangement](#siereference6---qualify-the-combined-arrangement) meet shared semantic, access, resource, currentness, provenance, and failure conditions? Which implementation or owner result is still absent?
- Does each evidence item support the claim made from it, and does the representative receiving-use test cover positive, negative, and unlike cases? Several passing layers cannot compensate for a hard stop in another.
- Is a narrow result recognizable as narrow, with excluded or unexamined branches and their consequences visible? In the request-limit example, an A-only answer cannot stand for the complete provider comparison.
- Do a model gap, changed semantic premise, or shared-module decision reach SIE.3, SIE.11, or SIE.12 where needed? Are source, implementation, and receiving decisions returned to their owners, with unresolved dependence made visible?

These questions address the failures in the applications: field-name equivalence, merged identifiers without authority, source claims flattened into one value, healthy transport mistaken for semantic fitness, and missing branches hidden from the receiver. Repair the specific premise or interface, obtain the missing contribution, narrow under the contract, or stop.

## SIE.Reference:10 - Intended use and ordinary non-use

Use this framework when the working result must make separately governed meanings, identities, claims, or representations usable together for a named receiver. Use one pattern or a small cooperating set and stop at the first decision-changing result or blocker.

Do not use SIE for local modeling with no cross-source receiving-use question, physical data movement, pipeline operation, one application's schema design, master-data authority, product configuration or release, generic representation choice, or the receiver's operational decision. Obtain those results from their owning practices. A local mapping inside one source can remain local unless it changes a cross-source semantic result.

## SIE.Reference:11 - PatternID and reader order

`SIE.*` is the Semantic Integration Engineering PatternID namespace. Numbers are stable addresses, not steps or maturity levels. The Table of Contents gives reader order. A dependency names a result needed by one use; it does not require every lower-numbered body to run.

## SIE.Reference:12 - Supplied pattern repertoire

The repertoire supplies `SIE.1`–`SIE.13`. The model, change, commons and whole-construction entries return these domain results:

- `SIE.3 - Construct or Reuse a Semantic Model for a Named Use`: adequate reuse or the semantic development required by a demonstrated gap.
- `SIE.11 - Trace Semantic Change and Revalidate Affected Uses`: direct affected-use results, with a common account when a receiver needs it.
- `SIE.12 - Govern Modular Semantic Commons without Universal Authority`: a working shared-module arrangement for actual users.
- `SIE.13 - Construct a Semantic Integration for a Named Receiving Use`: the connected semantic integration, including acquisition of missing contributions, joint conditions and its bounded receiving result.


A supplied Method guides the work; an inaccessible source, unresolved meaning, missing right, or absent implementation result can still limit a particular use.

## SIE.Reference:13 - Package anatomy and direct result relations

[SIE.13](#sie13---construct-a-semantic-integration-for-a-named-receiving-use) constructs the whole from the required contributions below. The table identifies results to connect or reuse, not a required new deliverable from every pattern.


| Package part | Supplying body or return | Minimum inspectable content |
| --- | --- | --- |
| use contract | `SIE.1` | receiver, use, answer claims, tolerated loss/uncertainty, freshness/latency/quality, authority, representative tests, stop and reopen |
| source manifest | `SIE.2`; SIE.3 qualification when needed | assets, schemes, editions/effectivity, meanings and identifiers used, owners/authority, provenance/access, gaps, and references to required model qualifications |
| correspondence set | `SIE.4` | endpoints, relation or incompatibility, orientation, bounded use, permitted loss, justification/evidence, source versions, counterexamples and unresolved rows |
| cross-source identity disposition | `SIE.5` | load-bearing endpoints, grain and interval, disposition kind, schemes and issuers, evidence, authority boundary, downstream references for the relied-on identity; an explanation of unused identity only when it affects interpretation or later reliance |
| source-qualified claim composition | `SIE.6` | source claims, scope, interval, authority, uncertainty, derivation, relied-on identity premises, comparable/conflicting/non-comparable/unresolved relation, qualified view or explicit conflict |
| mapping specification | `SIE.7` | schemes, accepted semantic inputs, rules, conditions, cardinalities, units/codes, defaults, errors, loss, trace, examples and tests |
| realization and interface | `SIE.8`, `SIE.9` | virtual/materialized/hybrid decision, required implementation result, receiver contract, interpretation, currentness, errors, provenance, access assumptions and return path |
| validation account | `SIE.10` | evidence sufficient for the bounded disposition; every load-bearing layer and required cases for a positive use claim; material unexamined reach, pass/narrow/unresolved/stop, and reopen condition |

`SIE.1 → SIE.2` supplies the use and source cut. `SIE.2 → SIE.3` is conditional. `SIE.2` and any supplied use-fit model feed `SIE.4`–`SIE.6`. `SIE.4` can expose an identity question for `SIE.5` and supplies semantic premises to `SIE.7`. `SIE.5` supplies load-bearing identity premises to `SIE.6`, `SIE.7`, and `SIE.10`. `SIE.6` supplies a qualified composition or explicit conflict branch to `SIE.7` and `SIE.9`. `SIE.7 → SIE.8 → SIE.9 → SIE.10` connects executable semantics to realization, receiver, and bounded validation. SIE.11 revisits only affected reliance, using these dependencies where material. SIE.12 supplies shared-module arrangements when actual users require them. These relations may iterate.

## SIE.Reference:14 - Pattern selection and first returned result

| Working question | Start or return | First result |
| --- | --- | --- |
| How can the required contributions supply the receiving answer together? | `SIE.13` | `SemanticIntegrationPackage@Use`, a permitted partial result, or an exact unresolved question or stop |
| What use and loss boundary govern the integration? | `SIE.1` | `SemanticIntegrationUseContract@Use` |
| What does each source mean and own? | `SIE.2` | `SourceSemanticInventory@Use` |
| Are the available models adequate, or what content must change? | `SIE.3` when adequacy is unsettled | `UseFitSemanticModel@Use` or exact blocker |
| Which endpoints correspond or remain incompatible? | `SIE.4` | `QualifiedCorrespondenceSet@Use` |
| Which identifiers concern the same entity at this grain and interval? | `SIE.5` | `CrossSourceIdentityDisposition@Use` |
| How can governed claims be composed without hiding conflict? | `SIE.6` | `SourceQualifiedClaimFusion@Use` |
| Which executable rules implement the accepted semantics? | `SIE.7` | `ExecutableSemanticMappingSpecification@Use` |
| Should the arrangement be virtual, materialized, or hybrid? | `SIE.8` | `SemanticRealizationDecision@Use` |
| What interface carries the meaning into receiving Work? | `SIE.9` | `ReceivingSemanticInterface@Use` |
| Is the result usable for the named receiver? | `SIE.10` | `SemanticIntegrationValidationAccount@Use` |
| What follows from a changed semantic premise? | `SIE.11` | qualified direct result, scoped gap, or a common affected-use account when needed |
| How should shared semantic modules be maintained? | `SIE.12` for actual commons users | `ModularSemanticCommonsAccount@Community` or exact blocker |

## SIE.Reference:15 - Related modeling and engineering work

Use SIE for the contribution that makes separately governed meanings usable together. The following working questions locate that contribution and the decisions that remain with neighboring practices.

| Working question | SIE contribution | Boundary retained |
| --- | --- | --- |
| Terminology and ontology across source models | `SIE.2` recovers source meanings, `SIE.3` qualifies or develops model content for an integration use, and `SIE.4` supplies correspondences | generic terminology, ontology, formal science, and local modeling remain with their direct owners |
| A model needed for a receiving integration answer | `SIE.2`, `SIE.3`, `SIE.4`, `SIE.7`, and `SIE.10` apply when the model supplies a named semantic-integration result | local model construction and research remain outside SIE |
| Formal apparatus needed by a semantic mapping or validation | exact formal apparatus may become a source, mapping, or validation premise | formal modeling itself is not an SIE lifecycle |
| Connected engineering descriptions and changed lifecycle information | SIE can return a qualified semantic interface, mapping package, identity/claim result, or affected-use result | SYSE keeps engineering descriptions, configuration, release, assurance, and digital-thread decisions; Data Engineering keeps pipeline operation |

## SIE.Reference:16 - FPF, neighboring practice, and authority boundaries

FPF owns generic representation, grounding, evidence, source/currentness, identity, comparison, and assurance distinctions. Method Engineering owns Method identity, qualification, trial, fit, worth, repertoire, variant, introduction, and revision. Systems Engineering owns engineered-System, engineering-description, configuration, integration, release, and assurance decisions. Data Engineering owns extraction execution, pipeline/service construction, orchestration, observability, reliability, and recovery. MDM and domain authorities own master identity, authoritative values, survivorship, and domain truth. Applications and operating or decision owners own authorization, risk acceptance, and actual outcomes.

SIE supplies Methods for use-qualified model content, cross-source meanings and correspondences, identity and claim composition, executable mappings, realization, interfaces, validation, changed semantic reliance, and modular commons. Return every non-SIE result to its owner with the exact dependent action.

## SIE.Reference:17 - Representative case coverage

The five applications are constructed method demonstrations, not evidence of a production integration, product release, recall decision, analytic validity, provider performance, or practical effectiveness.

| Case | What it tests | Boundary for reuse |
| --- | --- | --- |
| AP242/QIF | configuration/effectivity, feature identity, source-qualified composition, mapping, interface, and receiving-use validation | engineering and quality authorities retain release and acceptance; AP242 revision reopens affected premises |
| semiconductor traceability | several identifier schemes, grains, issuers, time, contradiction, and disclosure | MDM/domain and recall authorities retain identity, value, and action |
| quality/provenance | mapping coverage, units, defaults, derivation, currentness, and a representative analytic | Data Engineering and source owners repair their results; quality measures do not decide use alone |
| high-change providers | sufficient model reuse, explicit semantic difference, virtual realization, availability/error branches, changed promise horizon, and non-comparability | providers retain source meanings and permissions; purchasing owns action |
| equipment-classification commons | module boundaries, local correspondences, identification, decision and release rights, semantic change, migration, and notice | contacts communicate; source owners and receiving users retain their respective decisions |

## SIE.Reference:18 - Publication boundary

This publication combines thirteen pattern bodies with the shared reader account. The bodies govern their Methods; the Readme, Architectural Reference, applications, Table of Contents, and boundary account help readers find and combine them.

Use an instructional Guide for sequenced learning and memory formation. Use the Engineering DPF Suite Reference for cross-framework discovery. Neither publication replaces the pattern bodies or supplies a missing SIE result.

For source qualifications, citation and edition information, see the [Sources and Edition Notes](#semantic-integration-engineering-principles-framework-sources-and-edition-notes).

## SIE.Reference:End
