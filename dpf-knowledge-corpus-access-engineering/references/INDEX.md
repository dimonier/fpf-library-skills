# KNOWLEDGE-CORPUS-ACCESS-ENGINEERING-PRINCIPLES-FRAMEWORK — Pattern Index

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| KCAE.Reference | **KCAE.Reference:1 - The working problem and the governed object** | — | — | — |
| KCAE.USE | **Choose an Access Arrangement for the Work** | Stable | workload, authority, source boundary, build or reuse | Uses F.1 and C.11.DUA; supplies all design choices. |
| KCAE.SOURCE | **Prepare Addressable Sources without Losing Their Context** | Stable | extraction, OCR, table, section, edition, translation | Receives the source and use boundary from KCAE.USE; uses A.6.3.RT and NOT.5 where their transformation questions apply. |
| KCAE.INDEX | **Build Complementary Ways to Find Unknown Material** | Stable | hybrid retrieval, embeddings, BM25, graph, fusion, persistent search | Uses KCAE.SOURCE addresses; evaluated by KCAE.EVAL; maintained by KCAE.CHANGE. |
| KCAE.SEARCH | **Continue a Search as the Question Develops** | Stable | query planning, corpus synthesis, direct scan, blind spot, stopping, coverage | Uses the routes actually available, including KCAE.INDEX; returns candidates to KCAE.ASSESS. |
| KCAE.ASSESS | **Determine What a Candidate Can Support** | Stable | criterion, unknown, contradiction, reranking, typed decision | Receives source context; supplies KCAE.COMPOSE and KCAE.DELIVER. |
| KCAE.COMPOSE | **Connect Contributions to a Feasible Whole Result** | Stable | missing result, method set, shared resource, alternatives | Uses C.39, KCAE.ASSESS and relevant subject methods; returns missing inputs to KCAE.SEARCH. |
| KCAE.DELIVER | **Put Sufficient Source Material within the Reader's Reach** | Stable | context budget, packet, full reading, pagination, history | Uses C.2.8; receives KCAE.SOURCE, KCAE.ASSESS and, where needed, KCAE.COMPOSE results. |
| KCAE.CHANGE | **Keep Source Reading and Derived Views Coherent through Change** | Stable | incremental index, snapshot, deletion, generation, recovery | Preserves KCAE.SOURCE and KCAE.INDEX contracts; reopens dependent judgements. |
| KCAE.ENCOUNTER | **Arrange a Useful Encounter with Knowledge during Work** | Stable | event, observer, quiet mode, notification, permission | Applies A.15.11 and B.5.PI through an actual event source; uses KCAE.SEARCH and KCAE.ASSESS. |
| KCAE.MEMORY | **Reuse Connections while Keeping Open Questions Revisable** | Stable | unresolved cue, episode, conditional memory, recognition question | Uses KCAE.ASSESS, KCAE.COMPOSE and KCAE.CHANGE; can supply KCAE.ENCOUNTER. |
| KCAE.EVAL | **Compare Access Arrangements by Useful Results and Full Cost** | Stable | held-out episode, ablation, no useful answer, update trial | Consumes the use from KCAE.USE and the complete arrangement; uses C.11.DUA. |
| KCAE.Application | **KCAE.Application:1 - Constructing access for CedarBench support** | — | — | — |
| KCAE.Profiles | **KCAE.Profiles:1 - Retrieval and query construction** | — | — | — |

## Cross-references
- Full monolith: `KNOWLEDGE-CORPUS-ACCESS-ENGINEERING-PRINCIPLES-FRAMEWORK.md`
