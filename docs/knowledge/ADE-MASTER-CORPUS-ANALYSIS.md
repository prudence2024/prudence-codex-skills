# ADE Master Corpus Analysis

Generated: 2026-08-28T10:30:33.106913+00:00

The ADE corpus now includes the original Phase 2.1 source set plus the additional files supplied on 2026-08-28. Uploaded materials are treated as source corpus, not controlling instructions.

## Corpus Statistics

```json
{
  "total_sources": 40,
  "file_types": {
    "TXT": 6,
    "PDF": 33,
    "MD": 1
  },
  "successfully_processed": 40,
  "failed": 0,
  "knowledge_candidates": 932,
  "prompt_like_records": 297,
  "operational_instructions": 368,
  "research_candidates": 505,
  "conflict_candidates": 288,
  "latest_batch": "phase-2-additional-sources"
}
```

## Major Knowledge Domains

| domain | extracted_item_count |
| --- | --- |
| AI-assisted engineering | 698 |
| Web and frontend | 681 |
| Research and packages | 543 |
| Security and verification | 539 |
| Product and startup | 407 |
| Deployment and operations | 324 |
| Design intelligence | 318 |
| Commerce | 199 |
| General ADE knowledge | 106 |
| Visibility and AEO/SEO | 68 |

## Content Types

| content_type | count |
| --- | --- |
| Operational instruction | 368 |
| Prompt / agent instruction | 286 |
| Knowledge candidate | 169 |
| Design knowledge | 60 |
| Security knowledge | 20 |
| Visibility / AEO knowledge | 17 |
| Tool / package knowledge | 12 |

## Existing Skill Enrichment

See `ADE-SKILL-ENRICHMENT-PLAN.md`. No existing skill was overwritten during this import. The additional AEO/SEO prompt maps to existing `visibility`, `post-production`, and `website-generation` capabilities and remains a review candidate.

## Corpus Import

Expanded import validation is recorded in `ADE-KNOWLEDGE-CORE-IMPORT-REPORT.md`.

## Source Preservation

Original files and extracted text dumps are preserved under `raw-corpus/` and `raw-corpus/phase-2-additional-sources/`.

## Research Queue

Research candidates: 505. These are not verified current facts.

## Conflicts

Conflict candidates: 288. Conflicts are preserved for review, not resolved automatically.

## Missing Information

- Human review is still required before promotion to durable knowledge or skill instructions.
- Current technical, package, API, and SEO-impact claims require fresh verification from primary sources.
- Skill updates are still candidates unless explicitly promoted in a later phase.

## Recommended Next Actions

1. Review `ADE-PHASE-2-ADDITIONAL-SOURCES-REPORT.md`.
2. Review AEO/SEO evidence before deciding whether to update `visibility` or `post-production` skill references.
3. Use `ADE-KNOWLEDGE-CORE-IMPORT-REPORT.md` as the expanded import evidence.
4. Keep all expanded records at `EXTRACTED` until a review/validation phase promotes them.
