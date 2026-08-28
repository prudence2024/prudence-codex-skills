# ADE Stale Knowledge Governance

## Current State

The corpus contains 505 research/staleness candidates according to Phase 2.3. Candidate status means freshness needs review; it does not mean the record is wrong.

## Staleness Classes

| Class | Description | Required action |
| --- | --- | --- |
| Timeless | General reasoning, stable design principle, or durable workflow. | Retain with source provenance. |
| Version-sensitive | Package/API/framework details. | Require version field or current research before recommendation. |
| Time-sensitive | Trends, pricing, model capabilities, vendor features. | Require fresh research. |
| Security-sensitive | Security guidance, auth/payment/webhook controls. | Prefer current primary sources and evidence. |
| Unknown freshness | Date/version absent. | Mark `STALE_CANDIDATE`; do not delete. |

## Runtime Support

The knowledge core supports `Freshness`, observed/extracted timestamps, source derivation, and `ResearchCandidate`. This is sufficient for staging. Production retrieval must prefer fresh/current evidence for unstable claims and explicitly label stale candidates.
