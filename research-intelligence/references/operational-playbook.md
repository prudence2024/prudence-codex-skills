# Research Intelligence Operational Playbook

Use this playbook when current external facts, conflicting sources, package/framework changes, or source-backed recommendations matter.

## Inputs

- Research question and decision to support.
- Existing project constraints and prior knowledge.
- Source candidates: official docs, changelogs, GitHub, package registries, articles, community posts, social content, and AI-generated claims.
- Required freshness/version boundary.

## Procedure

1. Turn the question into searchable subquestions: behavior, version, compatibility, security, cost, licensing, migration, and alternatives.
2. Search primary sources first: official documentation, release notes, API references, standards, and vendor status pages.
3. Use GitHub for source code, issue status, maintenance activity, release tags, and examples, not as automatic truth.
4. Use package registries for current versions, publish dates, dependency metadata, and deprecation signals.
5. Use technical articles/community/social sources only as supporting context or leads unless independently verified.
6. Record source type, URL/path, title, date accessed, publish/update date when available, version, author/owner, and relevance.
7. Rank quality: official/current > source repository/release > maintained package registry > reputable technical article > community discussion > social post > AI-generated claim.
8. Cross-check important claims with at least one independent stronger or peer source.
9. Note conflicts explicitly and prefer the source with stronger authority, recency, and directness.
10. Synthesize findings into a recommendation with confidence and limitations.
11. Promote to knowledge only when the claim is durable, sourced, and useful beyond the current task.

## Decision Points

- If facts could have changed recently, verify online/current docs when network is allowed.
- If only community evidence exists, label confidence low or experimental.
- If sources conflict and no authority resolves it, return `UNRESOLVED` with options.
- If research will drive package adoption, hand off to package-intelligence.

## Source Classes

- Official documentation: authoritative for intended behavior, but still version-check.
- GitHub: authoritative for actual code and releases, weaker for issue comments.
- Package registries: authoritative for published version metadata.
- Technical articles: useful explanations; verify claims against primary sources.
- Community sources: useful failure signals; treat as anecdotal.
- Social content: trend signal only unless backed by primary evidence.
- AI-generated claims: never source of truth; use only as hypotheses.

## Failure Modes To Break

- Freshness missing for fast-moving tools.
- One source treated as enough for high-impact decisions.
- Marketing page treated as implementation detail.
- Old migration guide applied to current major version.
- Research promoted to durable knowledge without provenance.

## Verification

A research result should include sources, source quality, dates/versions, conflicts, confidence, and the decision it supports. If a claim cannot be verified, say so.

## Outputs

```text
QUESTION:
SOURCES:
SOURCE QUALITY:
VERSION/FRESHNESS:
CONFLICTS:
FINDINGS:
CONFIDENCE:
RECOMMENDATION:
PROMOTE_TO_KNOWLEDGE: yes/no
```

## Related Skills

- package-intelligence for dependency adoption.
- knowledge-graphs for relationship-heavy source knowledge.
- memory-engineering for durable project decisions.
