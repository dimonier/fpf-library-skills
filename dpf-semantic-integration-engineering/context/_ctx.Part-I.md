---
id: "_ctx.Part-I"
title: "Part I - Semantic Integration Engineering Methods"
---

# _ctx.Part-I: Part I - Semantic Integration Engineering Methods

---

## Part I - Semantic Integration Engineering Methods

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [SIE.1 - Bound the Receiving Use and Semantic Contract](#sie1---bound-the-receiving-use-and-semantic-contract) | Stable | What exact receiving use, semantic loss boundary, authority, and validation obligation govern this integration? | FPF C.37; C.39.RQ; direct receiver and source-owner results |
| 2 | [SIE.2 - Recover and Qualify Source Semantics and Authority](#sie2---recover-and-qualify-source-semantics-and-authority) | Stable | What does each load-bearing source mean, under which edition, effectivity, authority, and access conditions? | SIE.1 or equivalent contract; FPF F.0.1, F.0.2; direct source owners |
| 3 | [SIE.3 - Construct or Reuse a Semantic Model for a Named Use](#sie3---construct-or-reuse-a-semantic-model-for-a-named-use) | Stable | Does an available model answer the receiving questions, or what semantic extension is needed? | SIE.1 or equivalent use; relevant SIE.2 source meanings; domain participants |
| 4 | [SIE.4 - Judge Cross-Source Correspondences and Their Permitted Uses](#sie4---judge-cross-source-correspondences-and-their-permitted-uses) | Stable | Which exact endpoint relation, difference, or incompatibility is warranted and usable here? | SIE.2; supplied SIE.3 result when required; FPF F.9 |
| 5 | [SIE.5 - Resolve Cross-Source Identity without Erasing Identifier Authority](#sie5---resolve-cross-source-identity-without-erasing-identifier-authority) | Stable | Do these source endpoints concern the same entity at the required grain and interval, or another relation? | SIE.2; conditional SIE.4; direct MDM/domain authority inputs |
| 6 | [SIE.6 - Fuse Source-Qualified Claims without Erasing Conflict](#sie6---fuse-source-qualified-claims-without-erasing-conflict) | Stable | How can source claims be composed while preserving scope, authority, uncertainty, conflict, and non-comparability? | SIE.2, SIE.4; SIE.5 when identity is load-bearing; FPF C.2.1, A.10 |
| 7 | [SIE.7 - Specify Semantic Extraction and Transformation Mappings](#sie7---specify-semantic-extraction-and-transformation-mappings) | Stable | Which executable rules preserve the accepted correspondences, identities, claim branches, and losses? | SIE.2, SIE.4; conditional SIE.5 and SIE.6; FPF A.6.3.RT |
| 8 | [SIE.8 - Choose Virtual, Materialized, or Hybrid Semantic Realization](#sie8---choose-virtual-materialized-or-hybrid-semantic-realization) | Stable | Which available realization can meet the semantic, freshness, access, provenance, recovery, and combined resource conditions? | SIE.1, SIE.7; direct Data Engineering, platform, provider, and protection results |
| 9 | [SIE.9 - Connect a Receiving Use through a Semantic Interface](#sie9---connect-a-receiving-use-through-a-semantic-interface) | Stable | What smallest interface carries the required meanings, branches, provenance, and return paths into receiving Work? | SIE.1, SIE.7, SIE.8; conditional SIE.4-SIE.6 results |
| 10 | [SIE.10 - Validate a Semantic Integration Result for Its Receiving Use](#sie10---validate-a-semantic-integration-result-for-its-receiving-use) | Stable | What does the evidence settle about the named receiving use, and which claimed premises still need validation? | SIE.1 or equivalent use; relevant SIE.2-SIE.9 results; direct domain and receiver acceptance criteria |
| 11 | [SIE.11 - Trace Semantic Change and Revalidate Affected Uses](#sie11---trace-semantic-change-and-revalidate-affected-uses) | Stable | Which receiving results depend on the changed semantic premise, and what can now continue? | Changed relied-on premise; relevant SIE.2-SIE.10 results; FPF A.10.1 when discovery is needed |
| 12 | [SIE.12 - Govern Modular Semantic Commons without Universal Authority](#sie12---govern-modular-semantic-commons-without-universal-authority) | Stable | How can actual users maintain and rely on shared semantic modules and their changes? | Actual shared-module uses; SIE.3, SIE.4, and SIE.11 when their results are needed |
| 13 | [SIE.13 - Construct a Semantic Integration for a Named Receiving Use](#sie13---construct-a-semantic-integration-for-a-named-receiving-use) | Stable | How do we obtain and connect the required contributions, choose the next missing result, and supply an answer that works under their joint conditions? | Receiving need and available results; SIE.1–SIE.11 where their contributions are needed; SIE.12 for actual commons work |
