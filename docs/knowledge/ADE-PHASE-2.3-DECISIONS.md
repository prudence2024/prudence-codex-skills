# ADE Phase 2.3 Decisions

| ID | Decision | Reason | Status |
| --- | --- | --- | --- |
| D-2.3-001 | Treat the 40-source corpus as staging only. | Imported does not mean trusted. | Accepted |
| D-2.3-002 | Add explicit prompt representation. | Prompt-like records must not become facts or procedures accidentally. | Implemented |
| D-2.3-003 | Add access scope to knowledge items. | Project, private, restricted, and global knowledge need separate retrieval boundaries. | Implemented |
| D-2.3-004 | Reject AI-inferred objective facts without validation. | AI reasoning must remain distinguishable from source evidence. | Implemented |
| D-2.3-005 | Hide archived/superseded knowledge by default. | Source revocation needs safe default retrieval behavior. | Implemented |
| D-2.3-006 | Defer Graphiti, Hermes, crawler, production DB, and new skills. | The work order forbids production infrastructure in this phase. | Accepted |
| D-2.3-007 | Require future technology choices to pass governance tests. | Popularity is not evidence of fit. | Accepted |
