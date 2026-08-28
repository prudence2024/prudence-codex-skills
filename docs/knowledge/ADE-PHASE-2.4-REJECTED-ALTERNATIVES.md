# ADE Phase 2.4 Rejected Alternatives

## Vector Database As Source Of Truth

Rejected for Phase 2.4. ADE's corpus is not just chunks for semantic search. It includes prompts, source instructions, project knowledge, conflicts, stale candidates, source revocation requirements, and ACL-sensitive records. A vector database can help retrieval, but it should not become the authoritative knowledge ledger.

## Graph Database As First Production Store

Rejected for immediate adoption. ADE has real graph requirements, but the current corpus and benchmark do not prove that graph traversal should own canonical storage. Graph modeling should follow specific relationship queries and remain provenance-aware.

## Chroma As Primary Production Runtime

Rejected for primary runtime because it is useful for local experiments but does not by itself satisfy ADE's governance, ACL, conflict, temporal, and backup requirements. Its own docs describe server/client auth support as alpha.

## Pinecone As Immediate Primary Runtime

Rejected for immediate primary adoption because it introduces managed-service cost, eventual consistency considerations, provider-specific hybrid-score behavior, and extra source-of-truth synchronization before ADE has proven the need.

## Raw JSONL Search Only

Rejected beyond benchmark/offline fallback. It is maximally recoverable but not adequate for production access boundaries, ranking, versioning, or performance.

## Popularity-Based Selection

Rejected as an evaluation method. Phase 2.4 selection is based on ADE requirements, benchmark evidence, governance needs, portability, cost, and ability to explain retrieval.
