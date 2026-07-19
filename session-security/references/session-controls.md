# Session control reference

## Activity classification

Count only intentional, relevant events:

- successful or server-accepted form submission;
- meaningful button/menu action;
- authenticated user-initiated API request;
- client-side or full page navigation;
- explicit save, edit, upload, approve, or workflow transition.

Never count pointer movement, scrolling by itself, focus without engagement, passive refresh, analytics calls, background sync, or an open background tab.

## Sustained-focus exception

For document reading, review, dashboards, or training content, accept bounded evidence such as:

- tab is visible and window focused;
- document section or media position advances over time;
- keyboard-based reading/navigation occurs;
- an explicit “Continue reading” acknowledgement appears at a reasonable interval.

Throttle proof updates and retain an absolute session lifetime. Do not use webcam, invasive biometrics, or continuous behavioral surveillance.

## Expiry modal

- Open at 60 seconds remaining based on server-derived expiry.
- Use `role="alertdialog"`, a clear title, countdown text, and keyboard focus management.
- Provide “Stay logged in” as the primary action and “Sign out now” as the secondary action.
- Announce material countdown changes without speaking every second.
- If refresh fails, preserve state and explain that re-authentication is required.
- Synchronize the result to other tabs using `BroadcastChannel` or a storage event.

## Restoration envelope

```text
version, user_id, created_at, expires_at
route, route_params, query
workflow_id, workflow_step
draft_schema, allowed_draft_fields
scroll_position, focus_target
return_nonce, integrity_proof
```

Allowlist fields per form. Prefer server-side encrypted draft storage for customer, health, financial, legal, or other sensitive data. Validate the destination route and user identity to prevent open redirects or cross-account restoration.

## Verification checklist

- Server rejects expired sessions.
- Warning starts at 60 seconds and handles clock skew.
- Explicit extension succeeds and rotates/refreshes safely.
- Passive events do not extend idle time.
- Sustained-focus proof is bounded and expires absolutely.
- All tabs agree on extended or expired state.
- Exact route, draft, and workflow step return after re-authentication.
- Restoration cannot cross users, outlive its TTL, or include prohibited data.
