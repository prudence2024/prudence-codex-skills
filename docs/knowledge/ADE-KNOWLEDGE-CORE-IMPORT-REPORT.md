# ADE Knowledge Core Import Report

The Phase 2.1 extraction fixture was imported into the Phase 2.2 in-memory validation backend. Records remain `EXTRACTED`; they were not promoted to validated durable knowledge.

```json
{
  "records_processed": 314,
  "records_accepted": 314,
  "records_rejected": 0,
  "duplicates": 2609,
  "conflicts": 157,
  "missing_provenance": 0,
  "malformed_records": 0,
  "unsupported_records": 0,
  "research_candidates": 217,
  "errors": [],
  "backend": "InMemoryKnowledgeRepository",
  "status": "importable_not_promoted",
  "knowledge_status_after_import": "EXTRACTED",
  "semantic_search_backend": "not_implemented",
  "graph_database": "not_implemented",
  "production_memory_ingestion": "not_started"
}
```
