---
id: "_ctx.Practical-entries"
title: Practical entries
---

# _ctx.Practical-entries: Practical entries

---

## Practical entries

To construct a semantic integration from several contributions, use [SIE.13](#sie13---construct-a-semantic-integration-for-a-named-receiving-use): receiving need → required meanings and contributions → valid connections and joint conditions → next missing result → supplied receiving answer → affected return after change. Reuse adequate results and finish a sufficient local question directly; this connection is not a requirement to execute the full repertoire. The [worked construction](#sie135---archetypal-grounding) explains why these moves produce a usable whole.


Start from the query, decision, or operation that needs a cross-source answer. The constructed connections below show how meanings, identity, executable rules, and receiving use constrain one another. Reuse supplied results when their use and conditions still match; open the [Table of Contents](#table-of-contents) for another question or the [pattern-selection guide](#siereference14---pattern-selection-and-first-returned-result) for a missing result.

The [Architectural Reference](#semantic-integration-engineering-principles-framework-architectural-reference) explains the repertoire and its [architectural rationale](#siereference7---architectural-rationale). You can ask an assisting agent: “Explain this and give me your comments in the language of my work, without framework jargon.”

### SIE-INSPECTION - Connect inspection evidence to the configured product

- **Situation:** Product-definition and inspection sources are accessible, but a quality engineer cannot tell which inspection result concerns the feature in the configuration being reviewed.
- **Question:** How can the receiving query return applicable evidence and expose the branches it cannot establish?
- **First useful result or blocker:** The required answer for a named feature, configuration, and effectivity, with the permitted incomplete branches; or the missing configuration or acceptance decision that prevents bounding that answer.
- **Start with:** [SIE.1](#sie1---bound-the-receiving-use-and-semantic-contract) when the receiving question is unsettled; [SIE.10](#sie10---validate-a-semantic-integration-result-for-its-receiving-use) when an existing result already fails that question.
- **Stop or return:** Stop a dependent branch on unresolved feature identity or configuration. Return a source-definition gap to its owner, a transformation defect to SIE.7, and the release or inspection-acceptance decision to the engineering or quality authority.

In [APP-SIE-01](#sieapplication1---app-sie-01---ap242-and-qif-product-lifecycle-query), the engineer asks for the QIF plan and result concerning feature `F` in released revision/configuration `R` at effectivity `E`. SIE.1 makes those inputs and the acceptable answer branches explicit. [SIE.2](#sie2---recover-and-qualify-source-semantics-and-authority) then supplies the source editions, local definitions, identifier schemes, and authority needed to interpret them. If the available model cannot distinguish a planned inspection from an observation of that configured feature, [SIE.3](#sie3---construct-or-reuse-a-semantic-model-for-a-named-use) develops that missing distinction and tests it against those cases. An adequate existing model can be reused.

Those meanings allow [SIE.4](#sie4---judge-cross-source-correspondences-and-their-permitted-uses) to state a directed relation: inspection characteristic `C-17` concerns product feature `F-17` under the plan and configuration. [SIE.5](#sie5---resolve-cross-source-identity-without-erasing-identifier-authority) qualifies the feature endpoint at the required grain and effectivity. The relation permits navigation between the records; it does not make a characteristic identical to a product feature. A shared label without the supporting plan and effectivity remains an unmatched candidate. [SIE.6](#sie6---fuse-source-qualified-claims-without-erasing-conflict) uses these premises to combine definition, plan, and observation claims while retaining their sources and any conflict.

[SIE.7](#sie7---specify-semantic-extraction-and-transformation-mappings) turns the accepted relations into selection and transformation rules. The rules select the supplied released configuration, preserve both source identifiers, and expose an unknown unit or unmatched feature. [SIE.8](#sie8---choose-virtual-materialized-or-hybrid-semantic-realization) uses those required behaviours when comparing ways to supply the result; [SIE.9](#sie9---connect-a-receiving-use-through-a-semantic-interface) makes their meanings, timestamps, provenance, and failure branches available in the engineer's query.

The constructed application permits a qualified row set with unresolved local-extension and unknown-unit branches shown separately. SIE.10 can support that narrower answer only with matching evidence for all premises on which it relies, including the engineer's interpretation. A different question can finish much earlier: if a conversion returns 1 millimetre from an input of 1 metre where 1000 millimetres is required, that case establishes the mapping failure and returns it to SIE.7; unrelated layers remain unexamined. When the released configuration changes, [SIE.11](#sie11---trace-semantic-change-and-revalidate-affected-uses) follows the changed applicability through the relied-on identity, mapping, and receiving tests. The query supplies evidence; the responsible authorities still decide release and acceptance.

### SIE-PROVIDERS - Compare live availability under semantic and access limits

- **Situation:** Two provider APIs both expose an availability number, but their quantities and copying permissions differ from what a purchasing comparison assumes.
- **Question:** Which qualified answer can the interface supply within the receiving and access conditions?
- **First useful result or blocker:** Separately attributed quantities with the conditions needed for comparison, or a semantic or access limit that defeats the proposed answer.
- **Start with:** [SIE.2](#sie2---recover-and-qualify-source-semantics-and-authority) and [SIE.6](#sie6---fuse-source-qualified-claims-without-erasing-conflict) for unsettled meanings and comparison; [SIE.8](#sie8---choose-virtual-materialized-or-hybrid-semantic-realization) when those premises are supplied and realization is the remaining question.
- **Stop or return:** Exclude prohibited copying. Return an infeasible complete answer for a permitted narrower result or an access-owner decision. Reopen the affected meaning and interface when a provider changes the quantity it reports.

In the constructed provider case of [APP-SIE-04](#sieapplication4---app-sie-04---high-change-provider-availability-without-a-materialized-graph) and SIE.6, Provider A reports 12 on hand and Provider B reports 9 available to promise. SIE.2 recovers the reservation and horizon rules behind the quantities. [SIE.3](#sie3---construct-or-reuse-a-semantic-model-for-a-named-use) can reuse a model that keeps both measures, providers, units, times, and horizons distinct. [SIE.4](#sie4---judge-cross-source-correspondences-and-their-permitted-uses) supplies the qualified product-family relation. SIE.6 retains separate provider claims: the numbers do not support a common “21 available” total. For the question “Who can supply 8 now?”, A's reservation check and B's promise horizon must also support the receiving use.

Both providers prohibit replication. That prohibition is sufficient for SIE.8 to reject a copied availability store. If the question asks which remaining arrangement to use, compare query-time retrieval and any permitted hybrid with their latency, provenance, failure behaviour, and common resource demands. Develop only serious remaining alternatives. Obtain further evidence when its possible contribution to the choice justifies the burden and displaced work.

The [shared-request example](#siereference61---a-shared-request-limit-changes-the-provider-result) assumes four calls for A, four for B, and three for the required common trace, all under one ten-call allowance. The complete answer needs eleven calls before retries. With permission for an incomplete answer, A plus the trace needs seven: [SIE.9](#sie9---connect-a-receiving-use-through-a-semantic-interface) can expose “12 on hand at T” and “B not retrieved”, retaining the source and rule trace. B has not reported zero. SIE.10 still checks the other conditions needed for that narrower use; if both providers are mandatory, the result is a stop until the allowance or call demand is changed on supported grounds.

Suppose B keeps the same JSON field but changes its promise horizon. [SIE.11](#sie11---trace-semantic-change-and-revalidate-affected-uses) compares the meanings and finds the uses that consume them. An “available now” view returns to claim composition, mapping, interface, and receiving-use validation; a future-planning view may accept the new horizon after checking its own conditions. Product descriptions whose meanings are independent of that quantity can keep their earlier qualification. An inaccessible consumer interpretation remains unresolved. Purchasing decides how to act on the qualified or incomplete answer.

### SIE-COMMONS - Govern shared semantic modules

- **Situation:** Several organizations use a shared classification, and a proposed improvement would change which objects belong to one of its classes.
- **Question:** How can the shared model evolve while each consumer can still identify the meaning its work needs?
- **First useful result or blocker:** The proposed distinction and the users whose questions depend on it, or an unresolved definition or decision right that prevents the change.
- **Start with:** [SIE.12](#sie12---govern-modular-semantic-commons-without-universal-authority), with [SIE.3](#sie3---construct-or-reuse-a-semantic-model-for-a-named-use) for changed model content and [SIE.11](#sie11---trace-semantic-change-and-revalidate-affected-uses) for actual consumer reliance.
- **Stop or return:** Keep incompatible criteria in scoped modules when their users need them. A pair needing only one interface can complete that agreement; shared-module governance is useful when independently maintained modules and users create that further need.

In [APP-SIE-05](#sieapplication5---app-sie-05---a-modular-equipment-classification-commons), two manufacturers and a service partner share equipment classes. A proposal replaces “equipment with a replaceable drive” with “equipment serviced through a replaceable drive module”. Equipment X has only a separately replaceable drive; Y also supports drive-module replacement. These cases expose the changed classification: X belongs to the earlier class but not the proposed one, while Y belongs to both.

SIE.3 uses those cases to make the meanings distinguishable. Under the constructed SIE.12 agreement, the authorized maintainers keep `equip:DriveReplaceable` for the earlier meaning and introduce `equip:DriveModuleServiceable` for the new one. Both definitions and their editions remain recoverable. Source owners continue to supply the product descriptions on which membership depends.

SIE.11 follows each consumer's question. The service partner adopts the new class for module-replacement planning, so [SIE.4](#sie4---judge-cross-source-correspondences-and-their-permitted-uses) revisits its correspondences and the query uses the revised relation. [SIE.10](#sie10---validate-a-semantic-integration-result-for-its-receiving-use) checks the integration premises, including the result that admits Y and excludes X. Manufacturer A still needs its spare-drive query under the earlier meaning and can retain matching evidence. The release supplies the access, dependencies, migration information, and notice those uses need. These two completed outcomes leave other consumers' migration to be established where it matters.
