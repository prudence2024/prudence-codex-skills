---
name: session-security
description: Design, implement, or audit secure authenticated-session timeout behavior for web and mobile applications. Use when Codex needs meaningful activity tracking, idle and absolute expiry, a 60-second expiration warning with one-click extension, sustained-focus exceptions, cross-tab coordination, server-side enforcement, or exact workflow and unsaved-state restoration after re-authentication.
---

# Session Security

Treat the server as the authority for expiry and the client as a UX layer. Reuse the project's authentication provider and session primitives; do not invent custom authentication.

## Workflow

1. Identify token lifetime, refresh behavior, idle timeout, absolute maximum lifetime, sensitive routes, and provider constraints.
2. Define meaningful activity: successful form submissions, intentional button actions, authenticated API calls, and page navigation. Do not count mouse movement, timer ticks, passive polling, tab visibility alone, or a background tab.
3. Add a sustained-focus exception for legitimate reading or review work using visible-tab focus plus content engagement signals. Bound and rate-limit this exception; it must not create an unlimited session.
4. Persist the server-confirmed last-activity time and coordinate warning/expiry state across tabs.
5. Show an accessible modal exactly 60 seconds before idle expiry with countdown, “Stay logged in,” and sign-out actions.
6. Extend only after an explicit click and a successful server refresh. Do not close the modal optimistically if extension fails.
7. Before redirecting to re-authentication, capture a safe restoration envelope containing route, parameters, workflow step, scroll/focus context, and permitted unsaved fields.
8. After successful re-authentication, validate the envelope, return to the exact prior state, and clear it after restoration.
9. Apply the checklist and patterns in [references/session-controls.md](references/session-controls.md).

## Guardrails

- Never persist passwords, payment-card data, authentication secrets, one-time codes, or other prohibited sensitive fields in restoration state.
- Encrypt or server-store sensitive drafts; use short expiry, user binding, schema versioning, and integrity checks.
- Enforce idle and absolute expiry server-side even if client JavaScript is disabled or modified.
- Prevent refresh races and replay with one coordinated refresh operation and token rotation where supported.
- Test multiple tabs, offline/online transitions, sleeping devices, clock skew, failed refresh, expired restoration state, back-button behavior, and reduced-motion/screen-reader access.
