# ADE Production Readiness Design

Before production deployment, ADE must have:

- tested PostgreSQL migrations and rollback plan;
- source integrity verification for every preserved source and extracted item;
- backup, restore, and point-in-time recovery drills;
- ACL and project membership enforcement before retrieval providers run;
- secret scanning for source, extracted text, logs, and generated artifacts;
- observability for retrieval latency, empty results, low confidence, stale results, conflict surfacing, and provider failures;
- embedding versioning and reindexing controls;
- source revocation propagation to structured rows, full-text index, vector index, graph index, caches, and context packets;
- knowledge deletion and retention policy;
- audit logs for promotions, source changes, conflict resolution, and Hermes-submitted observations;
- failure recovery for index rebuilds, partial ingestion, provider outage, and rollback.

No production infrastructure is deployed by the consolidated Phase 2 work order.
