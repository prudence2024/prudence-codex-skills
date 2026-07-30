# Security reasoning and integration

## Context and evidence

Start from Shared Context when supplied. Record provenance for facts and preserve
conflicting evidence as uncertainty. Treat source inspection, local execution,
deployment configuration, provider settings, live responses, exercised controls,
and monitored outcomes as different evidence levels.

Never print secret values. Redact identifiers and sensitive data unless they are
strictly necessary and authorized.

## Risk and alternatives

Describe the asset, actor, trust boundary, threat event, preconditions, existing
controls, likelihood, impact, and evidence strength. Distinguish a confirmed
vulnerability from a missing control, risky pattern, hardening opportunity, or
unverified provider state.

For each material control, compare at least one credible alternative. Explain why
the selected approach fits the current stack and constraints, why alternatives
were rejected, operational costs, compatibility impact, rollback, residual risk,
and remaining uncertainty.

## Shared Context

Read project facts, goals, constraints, assumptions, uncertainties, decisions,
artifacts, risks, and prior skill runs. Write only attributable facts, decisions,
artifacts, risks, uncertainties, validation results, skill-run summaries, and
handoffs. Do not overwrite another skill's decision silently; record a conflict
and return it to the owning skill.

## Boundary handoffs

- Give Session Security authentication constraints, cookie and token requirements,
  server-enforcement expectations, and threat evidence.
- Give Incident Response alerting, logging, recovery, breach-readiness, or active
  incident findings. Do not operate incident command here.
- Give Legal Business verified data flows, processors, retention, security
  controls, and unresolved compliance facts. Do not make legal conclusions here.
- Give Design Toolkit security requirements for forms, errors, authentication,
  sensitive actions, and recovery interfaces.
- Give Visibility bounded requirements for CSP, public endpoints, redirects, and
  headers without selecting search strategy.

## Extension contract

Future scanners and provider adapters accept bounded targets and authorization,
then return tool identity and version, environment, timestamp, evidence,
limitations, and redacted findings. Their results are advisory. Security retains
final risk classification and reporting ownership.

## Reporting

Lead with the three highest-risk launch blockers. For every finding include
status, severity, consequence, evidence, smallest practical remediation,
validation state, owner, and residual uncertainty. List commands run, artifacts
changed, checks not run, risks, context changes, and handoff.
