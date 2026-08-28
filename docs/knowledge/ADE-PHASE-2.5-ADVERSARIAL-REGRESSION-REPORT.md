# ADE Phase 2.5 Adversarial Regression Report

## Status

SYSTEM BREAKER STATUS: CONDITIONAL PASS

## Attacks Executed

| Attack | Test | Evidence | Result |
| --- | --- | --- | --- |
| Missing provenance in context packet | `test_runtime_returns_explainable_context_packet_with_provenance` | Automated test verifies source ID, source location, original text reference, provider, warning. | PASS |
| Project/restricted leakage | `test_access_boundaries_prevent_global_project_and_restricted_leakage` | Runtime filters candidates by principal scopes and project before retrieval. | PASS |
| Stale knowledge returned by default | `test_stale_and_temporal_filters_are_enforced_before_retrieval` | Stale item is hidden unless explicitly requested. | PASS |
| Temporal mismatch | `test_stale_and_temporal_filters_are_enforced_before_retrieval` | Future-valid item excluded from `as_of=2023` query. | PASS |
| Conflict hidden from retrieval | `test_conflicting_sources_are_preserved_in_explanation` | Conflict ID appears in explainable result. | PASS |
| AI inference treated as fact | `test_ai_inference_stays_labeled_and_cannot_be_fact` | Core model rejects AI-derived fact; runtime warns on AI inference. | PASS |
| Duplicate collapsed silently | `test_duplicate_information_is_not_silently_collapsed` | Duplicate record exists and both items remain retrievable. | PASS |
| Revoked source still retrieved | `test_source_revocation_removes_items_from_default_retrieval` | Archived source item disappears from default retrieval. | PASS |
| Benchmark not measurable | `test_phase_2_5_runtime_metrics_against_existing_corpus` | Corpus-backed average term recall is checked against stable floor. | PASS |

## Findings

### P2.5-001 - MEDIUM - Retrieval relevance is not production-grade

Assumption: the local vector prototype can approximate semantic retrieval well enough for production quality.  
Attack: benchmark real ADE queries against the 932-item corpus.  
Expected: measurable recall and known weak spots.  
Actual: average term recall is `0.875`; three queries returned partial term recall.  
Root cause: prototype uses stable hashed token vectors, not real embeddings or a trained reranker.  
Fix: Phase 2.6 should test real embeddings and a reranker behind the same provider-neutral interface.  
Verification status: AUTOMATED TEST VERIFIED for current baseline; production semantic quality NOT VERIFIED.

### P2.5-002 - MEDIUM - Prototype latency is too high for production

Assumption: the local runtime proves production performance.  
Attack: run corpus-backed retrieval metrics.  
Actual: per-query runtime is measured in roughly 1.1s to 4.2s in the generated metrics artifact.  
Root cause: full corpus import and scan happen in-process; no persistent index exists.  
Fix: production PostgreSQL FTS/vector indexes, incremental indexing, and caching.  
Verification status: RUNTIME MEASURED; production performance NOT VERIFIED.

## Overall

CONDITIONAL PASS. The contract is proven, but true semantic retrieval quality and production latency require Phase 2.6 work.
