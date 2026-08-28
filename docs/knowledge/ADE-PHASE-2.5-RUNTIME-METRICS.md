# ADE Phase 2.5 Runtime Metrics

Runtime: `phase_2_5_non_production_provider_neutral`

Average term recall: `0.875`

| Query | Term recall | Result count | Elapsed ms | Matched terms |
| --- | ---: | ---: | ---: | --- |
| Q1 | 0.667 | 10 | 2152.294 | prompt, instruction |
| Q2 | 1.0 | 10 | 2381.138 | backup, version, control |
| Q3 | 0.667 | 10 | 1877.895 | security, rls |
| Q4 | 1.0 | 10 | 2819.142 | robots, sitemap, llms, aeo |
| Q5 | 1.0 | 10 | 2387.789 | rate, limiting, abuse |
| Q6 | 1.0 | 10 | 2073.514 | ai, agents, production |
| Q7 | 1.0 | 10 | 1867.93 | supabase, authentication, database |
| Q8 | 0.667 | 10 | 1983.486 | evidence, source |

The prototype proves the retrieval contract, not production semantic quality. It uses deterministic hashed token vectors rather than real embeddings.
