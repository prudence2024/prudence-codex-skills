# AI Assisted Engineering Operational Playbook

Use this playbook when an AI agent plans, implements, reviews, or claims completion of software work.

## Inputs

- User request and acceptance criteria.
- Relevant repository files, tests, schemas, routes, config, and docs.
- Existing project conventions and constraints.
- Tool output: builds, tests, runtime logs, screenshots, API traces, or database checks.
- Related skill outputs from context-engineering, package-intelligence, research-intelligence, or system-breaker.

## Procedure

1. Restate the task as testable claims: feature exists, behavior changes, invariants preserved, regressions avoided.
2. Inspect the repository before planning. Prefer actual files over README claims and previous AI summaries.
3. Select context deliberately: files that own the behavior, tests that cover it, schemas/contracts, config, and prior decisions.
4. Make a small plan that names what changes and what must not change.
5. Implement the smallest robust change using existing patterns.
6. Self-review before testing: compare changed code to requirements, contracts, edge cases, and style.
7. Test the claim proportionately: unit, integration, build, runtime, browser, database, or provider test mode as appropriate.
8. Invoke system-breaker for meaningful fixes, production claims, security/integrity claims, or false-completion risk.
9. Fix failures from evidence, then rerun the failing test and at least one relevant regression check.
10. Report what was verified, what remains untested, and what evidence supports completion.

## Decision Points

- If an API, helper, schema, route, component, env var, or dependency is assumed, verify it exists before using it.
- If a requested implementation conflicts with architecture, stop and report the conflict instead of forcing a patch.
- If tests cannot run, explain why and provide the strongest available alternative evidence.
- If the task would require live mutation, money movement, production data changes, or secret handling, request explicit approval.

## Failure Modes To Break

- Hallucinated APIs, files, imports, CLI flags, env vars, migrations, or package capabilities.
- Fabricated evidence such as claimed tests that were not run.
- Incomplete implementation: UI updated without server behavior, server updated without client states, tests updated without behavior.
- False completion from a passing build only.
- Overengineering: new abstraction, dependency, schema, or service when a local pattern is enough.
- Stale documentation overriding current source.
- Missing tests for edge cases, failure states, and regressions.

## Verification

Use an evidence ladder:

- CODE INSPECTION ONLY: useful but not completion proof.
- AUTOMATED TEST VERIFIED: named tests passed.
- RUNTIME VERIFIED: local app/API/browser behavior observed.
- INTEGRATION VERIFIED: multiple layers exercised together.
- SYSTEM BREAKER VERIFIED: adversarial assumptions tested.

## Outputs

- Task summary.
- Changed files or recommended changes.
- Evidence list with commands/results.
- Assumptions and untested areas.
- Follow-up fixes or owner actions.

## Related Skills

- context-engineering for selecting and compressing task context.
- research-intelligence for current external facts.
- package-intelligence for dependency decisions.
- system-breaker for adversarial verification.
