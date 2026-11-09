# SEMANTIC-INTEGRATION-ENGINEERING-PRINCIPLES-FRAMEWORK — Pattern Index

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| SIE.Reference | **SIE.Reference:1 - Meanings, identifiers, claims, carriers, and world-side referents remain distinct** | — | — | — |
| SIE.1 | **Bound the Receiving Use and Semantic Contract** | Stable | What exact receiving use, semantic loss boundary, authority, and validation obligation govern this integration | FPF C.37; C.39.RQ; direct receiver and source-owner results |
| SIE.2 | **Recover and Qualify Source Semantics and Authority** | Stable | What does each load-bearing source mean, under which edition, effectivity, authority, and access conditions | SIE.1 or equivalent contract; FPF F.0.1, F.0.2; direct source owners |
| SIE.3 | **Construct or Reuse a Semantic Model for a Named Use** | Stable | Does an available model answer the receiving questions, or what semantic extension is needed | SIE.1 or equivalent use; relevant SIE.2 source meanings; domain participants |
| SIE.4 | **Judge Cross-Source Correspondences and Their Permitted Uses** | Stable | Which exact endpoint relation, difference, or incompatibility is warranted and usable here | SIE.2; supplied SIE.3 result when required; FPF F.9 |
| SIE.5 | **Resolve Cross-Source Identity without Erasing Identifier Authority** | Stable | Do these source endpoints concern the same entity at the required grain and interval, or another relation | SIE.2; conditional SIE.4; direct MDM/domain authority inputs |
| SIE.6 | **Fuse Source-Qualified Claims without Erasing Conflict** | Stable | How can source claims be composed while preserving scope, authority, uncertainty, conflict, and non-comparability | SIE.2, SIE.4; SIE.5 when identity is load-bearing; FPF C.2.1, A.10 |
| SIE.7 | **Specify Semantic Extraction and Transformation Mappings** | Stable | Which executable rules preserve the accepted correspondences, identities, claim branches, and losses | SIE.2, SIE.4; conditional SIE.5 and SIE.6; FPF A.6.3.RT |
| SIE.8 | **Choose Virtual, Materialized, or Hybrid Semantic Realization** | Stable | Which available realization can meet the semantic, freshness, access, provenance, recovery, and combined resource conditions | SIE.1, SIE.7; direct Data Engineering, platform, provider, and protection results |
| SIE.9 | **Connect a Receiving Use through a Semantic Interface** | Stable | What smallest interface carries the required meanings, branches, provenance, and return paths into receiving Work | SIE.1, SIE.7, SIE.8; conditional SIE.4-SIE.6 results |
| SIE.10 | **Validate a Semantic Integration Result for Its Receiving Use** | Stable | What does the evidence settle about the named receiving use, and which claimed premises still need validation | SIE.1 or equivalent use; relevant SIE.2-SIE.9 results; direct domain and receiver acceptance criteria |
| SIE.11 | **Trace Semantic Change and Revalidate Affected Uses** | Stable | Which receiving results depend on the changed semantic premise, and what can now continue | Changed relied-on premise; relevant SIE.2-SIE.10 results; FPF A.10.1 when discovery is needed |
| SIE.12 | **Govern Modular Semantic Commons without Universal Authority** | Stable | How can actual users maintain and rely on shared semantic modules and their changes | Actual shared-module uses; SIE.3, SIE.4, and SIE.11 when their results are needed |
| SIE.13 | **Construct a Semantic Integration for a Named Receiving Use** | Stable | How do we obtain and connect the required contributions, choose the next missing result, and supply an answer that works under their joint conditions | Receiving need and available results; SIE.1–SIE.11 where their contributions are needed; SIE.12 for actual commons work |
| SIE.Application | **SIE.Application:1 - APP-SIE-01 - AP242 and QIF product-lifecycle query** | — | — | — |
| SIE.Sources | **SIE.Sources:1 - Source use and currentness** | — | — | — |

## Cross-references
- Full monolith: `SEMANTIC-INTEGRATION-ENGINEERING-PRINCIPLES-FRAMEWORK.md`
