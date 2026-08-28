# ADE Knowledge Runtime Requirements

## Phase 2.3 Requirements Matrix

| Requirement | Priority | Why | Test |
| --- | --- | --- | --- |
| Structured storage | Must | Preserve typed records, provenance, access scope, status, and relationships. | Insert/query all 932 staging items without field loss. |
| Full-text search | Must | Prompts and instructions need lexical traceability. | Query exact source phrases and recover source IDs. |
| Semantic retrieval | Should | User queries will not always match source wording. | Retrieve relevant lower-lexical items with explanation. |
| Embeddings | Should | Needed for scalable semantic retrieval. | Rebuild embeddings from source records and revoke by source. |
| Graph storage | Should | Conflicts, decisions, tools, projects, and sources form relationships. | Explain source-to-claim-to-decision paths. |
| Metadata filtering | Must | Access scope, project, freshness, type, and source quality are governance boundaries. | Restricted/project records never leak into global retrieval. |
| Versioning | Must | Technical guidance and decisions change over time. | Store multiple versions without overwriting. |
| Temporal queries | Should | Stale and current claims must be separable. | Ask what was believed at a date and retrieve matching records. |
| Provenance | Must | ADE must answer where knowledge came from. | Trace every retrieved item to source record/location. |
| Access control | Must before production | Corpus can include private/startup/restricted information. | Unauthorized global query returns no restricted records. |
| Deletion/revocation | Must before production | Source removal must remove direct and future indexed derivatives. | Archive source and verify default retrieval omission. |
| Conflict representation | Must | 288 conflict candidates require explicit status. | Return conflict status with contested claims. |
| Explainability | Must | Recommendations must distinguish evidence from inference. | Retrieval answer includes why, source, freshness, and confidence. |

## Technology Evaluation Rule

Do not choose a database, vector store, graph engine, crawler, or memory layer in Phase 2.3. Future choices must satisfy the matrix above and pass adversarial corpus tests.
