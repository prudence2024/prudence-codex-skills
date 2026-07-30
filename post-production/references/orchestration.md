# Post Production orchestration

## Single ownership and provenance

Assign each control one primary specialist owner. Cross-domain dependencies may
have contributors, but the final domain decision stays with its owner. Preserve
skill ID, version, decision ID, timestamp, environment, project revision,
evidence, limitations, risks, checks not run, and handoff.

Post Production may reject a result that lacks evidence or conflicts with scope,
but it does not rewrite the specialist's conclusion. Return the issue, record
the resolution, and preserve both the conflict and outcome.

## Shared Context

Read project facts, goals, constraints, decisions, artifacts, risks,
uncertainties, and prior runs. Write deployment identity, audit applicability,
coordination decisions, specialist links, aggregate findings, readiness
calculation, changed artifacts, validation evidence, risks, uncertainty, and
handoffs. Do not flatten specialist records into unattributed prose.

## Evidence states

Keep repository inspection, local execution, production build, preview,
deployed artifact, live response, provider dashboard, external delivery, field
measurement, and owner approval distinct. A successful local build is not a
deployment. A provider configuration is not delivery. Lab data is not field
data.

## Readiness

Define relevant controls before scoring. Publish status-to-value mapping,
category weights, exclusions, denominator, timestamp, environments, and missing
evidence. Do not score N/A controls. Unverified controls must not receive
completed credit. If coverage or evidence is inadequate, report `Not enough
evidence`.

## Sequencing

Order work by safety and dependency: preserve state, establish deployment truth,
fix critical correctness or security blockers, resolve shared infrastructure,
apply domain changes, build, validate preview, deploy only when authorized, then
verify live and provider outcomes.

## Extensions

Future specialist skills and evidence collectors must return versioned,
schema-validated records with bounded scope and provenance. Adding a new domain
must declare its owner, conflicts, dependencies, validation states, readiness
mapping, and report section.
