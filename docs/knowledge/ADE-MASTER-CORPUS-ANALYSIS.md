# ADE Master Corpus Analysis

Generated: 2026-08-28T00:33:36.455904+00:00

The uploaded zip was processed as a source corpus. Its contents are not treated as instructions that override system, developer, repository, security, or user work-order boundaries.

## Corpus Statistics

```json
{
  "total_files": 6,
  "file_types": {
    "TXT": 5,
    "PDF": 1
  },
  "total_sources": 6,
  "successfully_processed": 6,
  "failed": 0,
  "duplicates": 0,
  "conflicts": 157,
  "prompts": 148,
  "instructions": 123,
  "skill_candidates": 4,
  "knowledge_candidates": 314,
  "research_candidates": 217
}
```

## Major Knowledge Domains

| domain | extracted_item_count |
| --- | --- |
| Web and frontend | 291 |
| AI-assisted engineering | 286 |
| Security and verification | 246 |
| Research and packages | 225 |
| Product and startup | 207 |
| Deployment and operations | 161 |
| Design intelligence | 152 |
| Commerce | 101 |
| General ADE knowledge | 19 |

## Existing Skill Enrichment

See `ADE-SKILL-ENRICHMENT-PLAN.md`. No Phase 1 skill was overwritten.

## New Skill Candidates

See `ADE-SKILL-CANDIDATES.md`. Candidates are review items only.

## Development Systems

See `ADE-DEVELOPMENT-SYSTEMS.md`.

## Application Blueprints

See `ADE-APPLICATION-BLUEPRINTS.md`.

## Design Intelligence

Design-related extracted items: 21. Review `ADE-EXTRACTED-ITEMS.jsonl` for source sections tagged `Design knowledge`.

## Security Knowledge

Security-related extracted items: 2. Candidate enrichments route primarily to `system-breaker` and security review, without weakening safety boundaries.

## Startup/Product Knowledge

Startup/product extracted items: 0. These are confidential project knowledge candidates and are not promoted to production memory.

## Research Queue

Research candidates: 217. See `ADE-RESEARCH-QUEUE.md`.

## Conflicts

Conflict review candidates: 157. See `ADE-SOURCE-CONFLICTS.md`.

## Outdated Candidates

Potential stale candidates are marked `STALE_CANDIDATE` in `ADE-EXTRACTED-ITEMS.jsonl`.

## Missing Information

- Human review is still required to normalize raw extracted items into approved durable knowledge.
- Current package/API/tool claims require fresh research before recommendation.
- Direct source-vs-source contradiction resolution is not complete in this first pass.

## Recommended Next Actions

1. Review `ADE-EXTRACTION-MANIFEST.md` for per-source completeness.
2. Review `ADE-PROMPT-INVENTORY.md` and decide which prompts are safe to promote as reusable templates.
3. Review `ADE-SKILL-ENRICHMENT-PLAN.md` before modifying any Phase 1 skill.
4. Use `ADE-RESEARCH-QUEUE.md` to verify stale/current claims against primary sources.
5. Normalize approved items from `ADE-EXTRACTED-ITEMS.jsonl` into retrievable ADE knowledge only after review.
