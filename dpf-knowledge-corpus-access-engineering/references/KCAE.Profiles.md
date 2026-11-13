---
id: KCAE.Profiles
title: "KCAE.Profiles:1 - Retrieval and query construction"
---

# KCAE.Profiles: KCAE.Profiles:1 - Retrieval and query construction

> **Problem frame:** These profiles are replaceable implementations of the methods, not successive generations every installation must adopt. Select from the receiving workload and test the complete arrangement.

---

## KCAE.Profiles:1 - Retrieval and query construction

These profiles are replaceable implementations of the methods, not successive generations every installation must adopt. Select from the receiving workload and test the complete arrangement. A name such as RAG, agentic search or knowledge graph does not specify source authority, reading sufficiency or update semantics.

### KCAE.Profiles:1.1 - Exact, lexical and semantic units

**Exact and lexical retrieval.** Retain a resolver for named addresses and an inverted index for original terms. BM25 is a credible term-ranking choice: its weighting accounts for term occurrence, frequency and document length. Its tuning belongs to development data and the chosen retrieval unit. An exact technical identifier may deserve a separate lane because stemming or dense similarity can weaken its distinction. Lexical retrieval can work very well when the question and source share vocabulary; it can miss a useful paraphrase or another language. The algorithmic supplier is the historical [BM25 treatment in Introduction to Information Retrieval](https://nlp.stanford.edu/IR-book/html/htmledition/okapi-bm25-a-non-binary-model-1.html).

**Dense retrieval over original units.** Encode source units with a selected document encoder, encode the question compatibly, and retrieve nearby vectors under the model's similarity convention. Store source identity and context with each vector. An approximate nearest-neighbour index trades search work against agreement with exact vector neighbours; this agreement is not semantic recall. [HNSW](https://arxiv.org/abs/1603.09320) is an established historical algorithmic option, not a guarantee about the useful passages in a new corpus. Test multilingual queries, rare identifiers, conditions and negation. Keep a source route outside the embedding view.

**Late interaction.** The original [ColBERT](https://arxiv.org/abs/2004.12832) contribution represents a document and query with token-level embeddings and postpones fine-grained interaction until retrieval. It offers a richer matching alternative to a single vector per unit, with different storage and query costs. Its 2020 evaluation is historical evidence for that construction, not a current ranking of all retrieval models. Apply KCAE.SOURCE and KCAE.CHANGE to its larger representation just as to a simpler index.

### KCAE.Profiles:1.2 - Query variants and contextual representations

Question reformulation can expose aliases, translations and the result a method must provide. In [HyDE](https://aclanthology.org/2023.acl-long.99/), a generated hypothetical document supplies text to encode for retrieval. That 2023 mechanism can bridge vocabulary without making the generated document evidence. Keep the original question, reject invented case facts, and test whether expansion helps the receiving population rather than only increasing pool size.

[Contextual Retrieval](https://www.anthropic.com/engineering/contextual-retrieval) attaches generated document context to chunks before embedding and lexical indexing, then combines retrieval and reranking. Its 2024 account supplies a useful context-preservation construction and reported provider experiments. Here it is a historical comparator: the prefix can make an otherwise ambiguous chunk findable, but it is derived text and has context dependencies to refresh. It cannot replace the source reading or warrant transfer of the reported gains.

For fusion, [Cormack, Clarke and Buettcher's Reciprocal Rank Fusion](https://cormack.uwaterloo.ca/cormack/cormacksigir09-rrf.pdf) supplies the rank-based mechanism used in KCAE.INDEX:4.4. It avoids requiring comparable raw score magnitudes. The original constant and results belong to the original experiment. Choose pool depths and fusion behavior with the actual candidate population, and retain source-return and permission checks after fusion.

### KCAE.Profiles:1.3 - Structural and multiscale retrieval

Explicit section containment, definitions and references are useful low-cost structure. A generated graph or hierarchy adds inferred relations and its own loss. Use those relations to propose material, then inspect the source support appropriate to the question.

[GraphRAG §2.6](https://arxiv.org/html/2404.16130v1) selects a community level, shuffles its summaries into bounded contexts, produces intermediate answers, then combines them within a final context budget after helpfulness-based filtering. Its direct source-text map/reduce comparator is also a serious alternative. Prepared communities can amortize repeated broad questions, while preparation, updating and successive compression add burden and loss. The reported answer comparisons do not establish completeness of every summary or resulting answer.

[RAPTOR](https://arxiv.org/html/2401.18059v1) recursively clusters and summarizes material. Its query construction offers both traversal with pruning at successive levels and collapsed-tree retrieval across all levels. The latter can recover a useful node without requiring a successful top-down path, but a selected cross-level set is still not the whole source population. Preserve underlying membership when parent, child or overlapping summaries contribute to one answer. These 2024 sources supply implementable alternatives; KCAE.SEARCH:4.6 supplies the population and aggregation conditions for using their output in a bounded synthesis.

[LazyGraphRAG](https://www.microsoft.com/en-us/research/blog/lazygraphrag-setting-a-new-standard-for-quality-and-cost/) builds noun-phrase co-occurrence communities without advance LLM summaries. At query time it develops subqueries, explores communities through relevance testing, groups relevant source chunks, extracts claims and reduces selected claims to an answer. A relevance-test budget bounds exploration. This shifts preparation toward query-time work and is a serious comparator where advance summary cost is hard to amortize. Its selected claims and stopping condition still need an honest coverage account; deferred interpretation does not eliminate selection loss. The provider's bounded experiments do not transfer their quality/cost ratios to another corpus.

### KCAE.Profiles:1.4 - Direct semantic inspection and long-context reading

A direct original-block pass is useful when the question needs distinctions outside prepared selectors, or when the corpus is small enough that preparation would not pay. Enumerate blocks from the source inventory, supply the bounded state and criterion, retain plausible and unresolved blocks, and inspect their reading closures. The TypeSafe [semantic-find cookbook](https://docs.typesafe.ai/cookbooks/semantic_find) demonstrates addressed clause selection over a supplied document with a separate adequacy question. Its Jev 1.12 example is a bounded mechanism, not evidence of exhaustive semantic search in an arbitrarily large corpus.

Long-context reading can supply another direct profile, especially for a small stable dossier or repeated cached use. The [Gemini long-context documentation](https://ai.google.dev/gemini-api/docs/long-context) treats caching as a cost option and warns that multiple-item retrieval performance can vary. Compare actual model/version behavior and full lifecycle cost. A large accepted input window neither ensures every relevant relation is recovered nor makes a changed source cache current. Even when the dossier fits, use KCAE.DELIVER if the recipient still lacks material, context or access needed for the intended contribution.

## KCAE.Profiles:2 - Typed assessors and generative readers

### KCAE.Profiles:2.1 - A bounded Jev role

The TypeSafe interface takes a state and typed questions. It can fill a screening or classification role when inputs, meanings and subsequent operations are controlled. It does not replace source acquisition, explanation, deterministic calculation or final domain judgement. [Model documentation](https://docs.typesafe.ai/models) describes English as the primary language and calls for testing other languages. Text-only inputs require an adequate prior transformation of a diagram or table. Treat version, limits, prices and availability as implementation inputs to verify at use, not durable properties of this framework.

The [Jev 1.13 jaggedness account](https://docs.typesafe.ai/model-jaggedness/jev-1.13) identifies sensitivities including negation, indirection, mathematical content, long irrelevant state and adversarial instructions. Give the assessor a focused state and explicit criterion, test the forms your cases use, and calculate exact arithmetic in code after semantic facts are obtained. A typed shape reduces parsing ambiguity; it is not an accuracy certificate. Keep retrieved instructions as untrusted source content, not a change to the assessor's authority.

Use a generative reader when the task needs an explanation, missing-condition recovery, query construction or a new connection that the fixed questions cannot express. Use an appropriate specialist when interpretation or authority depends on that profession. Combine roles only when the receiving result and total cost justify them.

### KCAE.Profiles:2.2 - What the cookbooks contribute, and what must change

The [skill-suggestion cookbook](https://docs.typesafe.ai/cookbooks/skill_suggestion) supplies progressive selection: short descriptions for a wide ranking, fuller descriptions plus instruction openings for the shortlisted Choice, and full descriptions for per-candidate fits. Its Jev 1.12 demonstration uses synthetic requests. The inspected code gates on the maximum fits score, then returns the Choice winner; these can refer to different candidates. This is a static example defect, not a measured failure rate or a general vendor claim. KCAE.ASSESS:4.4 binds adequacy to the returned candidate. Method-library use also replaces the example's action-oriented screen with the required contribution, including explanations, and reads complete necessary instructions before reliance.

The [feature-discovery cookbook](https://docs.typesafe.ai/cookbooks/autoresearch_feature_discovery) proposes natural-language questions, obtains numeric features, uses supervised-model errors to revise them and assesses held-out data. It demonstrates this on a bounded tasting-note prediction problem. KCAE.MEMORY adapts the error-to-question loop for recognition aids, while requiring actual permitted episodes and a separate test population when the intended recognition claim needs that evidence. The adaptation is a proposed domain construction, not evidence that the cookbook already solves open-ended method noticing.

### KCAE.Profiles:2.3 - Comparative evidence beyond the output type

The 2026 [early empirical audit of typed decision models](https://arxiv.org/html/2609.32160v1) warns that interface specialization and comparison conditions can be confused with intrinsic accuracy gains. [Typed decision coherence beyond calibration](https://arxiv.org/html/2609.33209v1) separates logical consistency among answers from probability calibration. These are bounded, early studies, useful as failure and comparison evidence rather than a final vendor ranking.

Accordingly, compare the actual typed and generative alternatives with matched evidence and required output. Test ranking, adequacy thresholds, calibration and any logical relationships separately. A model that selects the best available option can still need a distinct all-options-inadequate outcome. No scalar combines source authority, completeness, capability and permission into an automatic licence to act.

## KCAE.Profiles:3 - Packages, tools, dynamic loading and storage

### KCAE.Profiles:3.1 - Put the appropriate work at preparation and query time

A skill can carry a usable entry and the procedure for obtaining deeper sources. A tool service can expose search and edition-aware reading. A package can pin and distribute content and dependencies. A local reader can keep sensitive source material within a permitted environment. These contributions can be combined. Their exact contract must state identity, allowed data flow, completeness, freshness and failure behavior; the form's name supplies none of those guarantees.

[Anthropic's context-engineering account](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) describes lightweight identifiers and runtime source loading, including combinations of prepared retrieval and exploration. This is a current implementation comparator for the preparation/query split. It highlights why additional exploration has a cost. KCAE uses the mechanism where the runtime supplies it and tests the actual reader result instead of treating dynamic loading as inherently superior.

**VibeVM is a concrete package/runtime alternative.** Its [project README](https://github.com/vibevm/vibevm/blob/main/README.md) distinguishes resolved package identities, materialized content and computed agent boot material. The [boot-lane manual](https://github.com/vibevm/vibevm/blob/main/vibevm/vibepacks/org.vibevm.core/vibevm-docs/v1.0.0/vibevm/vibespecs/model/boot-lane.xml) describes a priority text plus an index of static or dynamic contributions, consumer-selected inclusion and conditional loading. It also directs citations back to authored sources rather than generated boot positions. That supplies a practical deferred-reading profile. Qualify the package/version and host behavior used; the documentation is not an observed deployment of this corpus. Dynamic inclusion is neither a guarantee that an unknown useful method will be noticed nor a substitute for complete source reading. It can coexist with semantic search, an exact reader and a separately authorized observer.

The engineering question is therefore not “packages or RAG?” A package can distribute an exact source and entry, a service can search it, an assessor can qualify candidates and a host can load the selected material. Another installation can use direct local files and no service. Compare the operations, source returns and costs of those actual arrangements.

### KCAE.Profiles:3.2 - Storage guarantees belong to their real scope

[SQLite's isolation documentation](https://www.sqlite.org/isolation.html) supports reasoning about committed database transactions and snapshots within its database. It does not transact a separate vector provider or object store. Use it for the atomic catalogue or local state only when the selected mode and operations provide the required behavior.

The [OpenAI retrieval documentation](https://developers.openai.com/api/docs/guides/retrieval) describes asynchronous file ingestion and eventually consistent removal. A service using that interface must wait for actual readiness and handle stale removal results. Do not infer complete deletion or cross-store consistency from a successful request submission. This is one provider-specific contract to place inside KCAE.CHANGE, not a universal ban on remote retrieval.

[CodeNib v2](https://arxiv.org/html/2607.25431v2), especially its boundaries and update experiments, distinguishes a useful multi-view code corpus from a transaction over a mutable workspace. Its incremental/fresh comparisons expose variation and incomplete equivalence despite completed updates. Adopt persistence/reload and changed-case checks; do not claim that its code-corpus results validate a support or method library. The general engineering requirement is to test the source/view relation the receiving use relies on.

A software observer can obtain idempotency support from a runtime library where its persistence and execution assumptions hold. The [AWS Powertools idempotency documentation](https://docs.aws.amazon.com/powertools/python/latest/utilities/idempotency/), especially “Concurrent identical in-flight requests” and “Lambda request timeout,” distinguishes in-progress and completed records, rejects concurrent processing and allows another attempt after the in-progress timeout. This is a concrete comparator for KCAE.ENCOUNTER:4.3, not a required SDK. Its stored-result behavior does not settle an external effect performed before completion, or transfer Lambda's timeout semantics to another worker environment. Obtain those properties from the actual receiver and runtime.

## KCAE.Profiles:End
