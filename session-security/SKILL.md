---
name: session-security
description: Design, implement, or audit secure authenticated-session timeout behavior for web and mobile applications. Use when Codex needs meaningful activity tracking, idle and absolute expiry, a 60-second expiration warning with one-click extension, sustained-focus exceptions, cross-tab coordination, server-side enforcement, or exact workflow and unsaved-state restoration after re-authentication.
---

# Session Security

## Purpose and boundaries

Design, implement, or audit server-enforced session timeout behavior with a
clear client state machine and safe restoration. Reuse the project's
authentication provider and session primitives.

- Session Security owns meaningful activity, idle and absolute expiry, warning
  timing, explicit extension, sustained-focus exceptions, cross-tab
  coordination, reauthentication return, and restoration envelopes.
- `$security` owns authentication architecture, token and cookie controls,
  authorization, threat assessment, and general API security. Consume its
  constraints; do not invent a new auth system.
- `$design-toolkit` owns modal, focus, responsive, and interaction design.
  Supply required states and accessibility behavior rather than duplicating
  interface reasoning.
- `$incident-response` owns operational response to session abuse or auth
  outages; hand off monitoring and incident findings.

## References

- Read [session-controls.md](references/session-controls.md) for activity,
  sustained-focus, warning, restoration, and verification details.
- Read [session-reasoning.md](references/session-reasoning.md) for state-machine,
  Shared Context, evidence, reporting, and handoff rules.

## Workflow

1. Validate supplied Shared Context or create an in-memory envelope. Record the
   auth provider, token lifetimes, server session semantics, sensitive routes,
   client platforms, workflow state, data sensitivity, and uncertainty.
2. Consume applicable Security and Design Toolkit decisions. Record conflicts
   rather than silently replacing them.
3. Define a state machine for active, warning, extending, expired,
   reauthenticating, restoring, signed-out, and failure states.
4. Define meaningful activity. Count intentional, relevant actions; do not count
   pointer movement, timer ticks, passive polling, tab visibility alone, or
   background activity.
5. Define bounded sustained-focus evidence for legitimate reading or review.
   Retain an absolute maximum lifetime and avoid invasive surveillance.
6. Persist server-confirmed activity and expiry. Coordinate warnings, refresh,
   expiry, and sign-out across tabs or application instances.
7. Show an accessible warning exactly 60 seconds before idle expiry. Extend only
   after an explicit action and successful server refresh; never close the
   warning optimistically.
8. Capture an allowlisted, user-bound, integrity-protected, short-lived
   restoration envelope before reauthentication. Exclude prohibited data.
9. Validate the return target and user, restore the exact permitted workflow
   state, then clear or invalidate the envelope.
10. Test server rejection, clock skew, multiple tabs, refresh races, offline and
    sleeping devices, absolute expiry, failed refresh, expired or cross-user
    restoration, back navigation, screen readers, keyboard access, and reduced
    motion.
11. Record the decision, update Shared Context, produce the standardized report,
    and hand off security, design, or operational follow-up.

## Decision and reporting contract

For every material decision, explain:

- selected policy and implementation, plus why;
- credible alternatives, rejection reasons, and trade-offs;
- Security and Design Toolkit constraints consumed;
- state transitions, server authority, restoration data, and privacy limits;
- risks, failure behavior, validation evidence, owner actions, and uncertainty;
- Shared Context changes and handoffs.

Validate structured decisions against `schemas/session-security-decision.json`.
Use the common report and Shared Context schemas for run output.

## Guardrails

- Never persist passwords, payment-card data, authentication secrets, one-time
  codes, or other prohibited fields in restoration state.
- Encrypt or server-store sensitive drafts; bind them to the user, expire them,
  version their schema, and protect integrity.
- Enforce idle and absolute expiry server-side even when client code is disabled
  or modified.
- Coordinate one refresh operation and use provider-supported token rotation to
  prevent refresh races and replay.
- Do not claim exact restoration, cross-tab consistency, or server enforcement
  without exercising the relevant path.
