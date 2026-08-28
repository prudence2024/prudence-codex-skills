# ADE Phase 2.5 Runtime Metrics

Runtime: `phase_2_5_non_production_provider_neutral`
Average term recall: `0.875`

| Query | Term recall | Result count | Elapsed ms | Matched terms |
| --- | ---: | ---: | ---: | --- |
| Q1 | 0.667 | 10 | 4164.58 | prompt, instruction |
| Q2 | 1.0 | 10 | 2684.997 | backup, version, control |
| Q3 | 0.667 | 10 | 2502.033 | security, rls |
| Q4 | 1.0 | 10 | 1949.789 | robots, sitemap, llms, aeo |
| Q5 | 1.0 | 10 | 2383.794 | rate, limiting, abuse |
| Q6 | 1.0 | 10 | 1472.876 | ai, agents, production |
| Q7 | 1.0 | 10 | 1842.491 | supabase, authentication, database |
| Q8 | 0.667 | 10 | 1149.079 | evidence, source |

## Interpretation

The prototype proves the retrieval contract, not production relevance quality. The stable local pseudo-vector provider plus lexical provider reached the Phase 2.5 regression floor, but semantic quality remains a Phase 2.6 production-readiness item because no full-scale embedding migration was performed.
