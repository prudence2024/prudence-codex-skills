# System Breaker Attack Playbook

Use this reference for meaningful adversarial testing. Apply only the sections relevant to the user's system, environment, authorization, and risk.

## Trust Model

Never trust the client. Treat browser-provided values as untrusted, including IDs, email, role, price, subtotal, delivery fee, discount, coupon, quantity, inventory, status, redirect URL, payment status, checkout attempt ID, file metadata, content type, filenames, and Admin visibility state.

UI hiding is not authorization. Client validation is not server validation. Client payment success is not payment verification. UUID unpredictability is defense-in-depth, not authorization.

## Authentication And RBAC

Test unauthenticated direct route access, direct server/API access, expired sessions, logout then browser-back, stale sessions, inactive Admins, missing roles, missing `role_id`, deleted roles, disabled permissions, deep links, concurrent Admins, multiple accounts on separate devices, unauthorized Clerk accounts, and malformed identity mappings.

For every protected operation, test owner/Admin, restricted staff, inactive staff, normal authenticated user, and unauthenticated user. Attempt both UI navigation and direct server/API/server function access. PASS requires server-side rejection for unauthorized access.

## IDOR

Manipulate order IDs, customer IDs, product IDs, receipt IDs, review IDs, payment IDs, checkout attempt IDs, Admin IDs, invitation IDs, resource slugs, and any tenant/account scoped identifier. Verify one user cannot read or modify another user's resource by changing an identifier.

## Input And Output Handling

Use harmless probes: empty, missing, null, undefined, whitespace-only, very long input, Unicode, emoji, apostrophes, hyphens, HTML-like text, SQL-like text, negative numbers, very large numbers, scientific notation, duplicate data, leading/trailing spaces, `test'`, `<b>TEST</b>`, and `<script>TEST</script>`.

Do not label HTML-looking input as XSS merely because it contains markup. Trace the output sink and verify context-specific encoding or sanitization for React JSX, HTML email, PDF/HTML templates, metadata, Telegram, logs, Admin UI, receipts, and structured data.

## File Uploads

Test wrong extension, renamed executable, incorrect MIME, oversized file, tiny file, corrupted file, duplicate filename, unexpected dimensions, and unsupported image format. Never rely solely on the browser-supplied MIME type.

## Database And Migrations

Test duplicate inserts, constraint violations, concurrent writes, stale updates, missing foreign keys, race conditions, partial failure, migration drift, code migration not applied to the live database, manually applied migration not in migration history, unexpected NULL values, and deleted related records.

Migration verification should move through: migration history -> dry-run -> safety classification -> apply -> live verification -> regression. Never assume migration files equal live schema.

## Payments And Commerce

Payment systems must be tested adversarially. Test double-click Pay, two tabs, duplicate initialization, retry after timeout, callback twice, webhook twice, callback plus webhook race, refresh during callback, cancelled payment, failed payment, stale callback, late webhook, order already paid, changed cart, changed coupon, changed delivery fee, inventory becoming unavailable, and coupon quota consumed elsewhere.

Never trust browser payment status. Provider verification or validated webhook state must be authoritative.

Prove exactly-once business effects: one paid transition, one inventory decrement, one coupon consumption, one receipt, and one fulfilment event. A condition preventing negative stock is not automatically proof of payment idempotency.

## Concurrency

Whenever an operation can be triggered twice, test it twice simultaneously. Examples: checkout initialization, account invitation, product creation, coupon use, inventory update, receipt generation, email send, payment finalization, and testimonial moderation.

Look for SELECT-then-INSERT and SELECT-then-UPDATE races. Prefer database constraints, transactions, compare-and-swap, unique idempotency keys, or other server-enforced concurrency guarantees.

## Network And Runtime Failure

Test offline, intermittent connection, slow connection, request timeout, duplicate retry, browser refresh, navigation during request, connection restored, and provider unavailable. Application state must recover cleanly, and network failure must not become false business success.

## Third-Party Dependencies

Safely simulate or inspect failure handling for providers such as Clerk, Supabase, Paystack, Cloudinary, Resend, Brevo, Telegram, Sentry, uptime providers, and external APIs.

Classify each dependency as critical or best-effort. Core business actions must not silently succeed when required critical dependencies fail. Non-critical notification failures should not necessarily break the core business operation.

## Secrets

Search read-only across tracked source, Git history, generated client bundles, server bundles, documentation, environment examples, logs, and source maps where available. Look for API secrets, service-role keys, Clerk secrets, Paystack secrets, Telegram tokens, email-provider secrets, Cloudinary secrets, database passwords, JWT/session data, and LLM credentials.

Never print a discovered secret value. Report only secret type, location, current or historical exposure, and remediation required. Do not automatically rewrite Git history or rotate credentials.

## Availability

Verify public homepage response, health endpoint response, database dependency detection, distinguishable third-party degradation, cron heartbeat monitoring, and uptime alerting. Do not expose sensitive internals in public health responses.

## Performance

Treat extreme slowness as a failure condition. Test cold cache, warm cache, desktop, mobile, slow network, large result sets, and many Admin records. Measure actual TTFB, FCP, LCP, request count, server function count, database latency, image payload, and JavaScript payload. Do not report "feels faster" as evidence.

## SEO And Discoverability

Verify runtime `/robots.txt`, `/sitemap.xml`, and `/llms.txt`; file existence is not enough. Check HTTP status, content type, production domain, actual URL count, dynamic products, dynamic blog posts, categories, CMS pages, and private route exclusion.

Try to prove content expected to be discoverable is missing.

## Configuration

Test missing environment variables, malformed values, stale values, Admin setting changes during active user flows, cached settings not invalidated, and client attempts to override server configuration. Business-critical configuration must have server-side validation. If no authoritative business rule exists, return `OWNER DECISION REQUIRED`.

## Severity

Use `BLOCKER`, `CRITICAL`, `HIGH`, `MEDIUM`, and `LOW`.

- `BLOCKER`: prevents required operation or safe deployment.
- `CRITICAL`: likely severe compromise, payment/data breach, or unrestricted privilege escalation.
- `HIGH`: significant security, financial, authorization, or integrity defect.
- `MEDIUM`: important reliability/security issue with limited impact or exploitability.
- `LOW`: hardening, minor UX, operational, or defense-in-depth issue.

Do not inflate severity merely to make an audit appear important.

## Finding Format

Every finding should contain:

```text
ID:
Severity:
Area:
Assumption:
Attack:
Expected:
Actual:
Evidence:
Reproduction:
Root Cause:
Fix:
Regression Test:
Verification Status:
```

## Stop Conditions

Stop and request owner approval when required work involves destructive database change, data deletion, production credential rotation, real refund, real payment, changing legal text, changing business policy, customer-data retention changes, major architecture replacement, uncontrolled third-party changes, denial-of-service traffic, brute force, or testing systems the user does not own.

Otherwise continue through: find -> fix -> regression -> verify.

## Final Output Shape

For full audits, return:

```text
SYSTEM BREAKER STATUS

ATTACK SURFACE:
ATTACKS EXECUTED:
RUNTIME TESTS:
SAFE-MODE TESTS:
BLOCKED TESTS:

BLOCKERS:
CRITICAL:
HIGH:
MEDIUM:
LOW:

FIXES:
REGRESSIONS:

DATABASE:
AUTH/RBAC:
PAYMENTS:
INPUTS:
FILES:
NETWORK:
THIRD PARTIES:
SECRETS:
AVAILABILITY:
PERFORMANCE:
DISCOVERABILITY:

CODE INSPECTION ONLY:
RUNTIME VERIFIED:
OWNER ACTIONS:

OVERALL: PASS / CONDITIONAL PASS / FAIL
```

The objective is not to prove that the application works. The objective is to try to prove that it does not work safely, and only issue PASS when those attempts fail with evidence.

## Phase 1.6 Additional Coverage

Use this section when the system under test includes user-facing UI, APIs, webhooks, rate limits, inventory, or production observability.

### Frontend, UI, And Accessibility

Test the same workflow on narrow mobile, mobile landscape, tablet, desktop, wide desktop, and browser zoom where practical. Exercise loading, empty, error, disabled, optimistic, retry, offline, and stale-data states. Keyboard navigation must reach every interactive control in a logical order, visible focus must remain obvious, dialogs must trap and restore focus, form controls must have accessible names, and destructive actions must have clear confirmation or recovery.

Treat UI polish as evidence only after runtime inspection or screenshot review. Source inspection alone is `CODE INSPECTION ONLY`.

### Backend And Application Logic

For every meaningful business rule, identify the authoritative server path and test whether the client can bypass it. Cover direct API/server-action calls, malformed payloads, missing fields, wrong types, stale IDs, privilege changes during request execution, and concurrent state changes. Important rules must fail closed on the server.

### API Failure Matrix

For each critical endpoint or server action, verify safe handling for relevant statuses: 400, 401, 403, 404, 409, 422, 429, 500, 502, 503, and timeout. A safe response should avoid stack traces, secret leakage, false success, duplicate business effects, and unrecoverable UI state.

### Rate Limiting And Abuse Resistance

Inspect or test bounded repeated attempts for login, checkout initialization, coupon validation, contact forms, reviews/testimonials, file uploads, password or invitation flows, webhooks, search, and Admin mutations. Use safe local or staging volumes only. PASS requires a server-side control, not merely a disabled button.

### Webhooks And External Callbacks

For each webhook or callback, test missing signature, malformed signature, replay, duplicate delivery, out-of-order delivery, stale event, event for unknown resource, provider timeout, handler timeout, and partial database failure. Provider signatures and server-side verification are authoritative; browser redirects are not.

### Inventory Reservation And Release

When inventory exists, test reservation creation, expiration, payment success, payment failure, abandoned checkout, duplicate payment finalization, webhook/callback race, concurrent carts for last unit, manual Admin stock change during checkout, and refund/cancellation behavior. Evidence should prove no negative stock, no double decrement, and no permanently stuck reservation unless business rules explicitly allow it.

### Observability And Operational Evidence

Check whether failures produce useful logs, metrics, traces, alerts, or audit records without logging secrets, payment secrets, session tokens, full card data, or sensitive personal data. A production-readiness PASS needs enough observability for an owner to detect and diagnose failures after deployment.

### Frontend/Backend/API Coverage Table

For substantial audits, include this compact coverage table:

```text
SURFACE:          [frontend / backend / API / database / webhook / provider / observability]
ASSUMPTION:       [what must hold]
BREAK TEST:       [safe test or inspection]
EVIDENCE:         [runtime/test/code/log/db/provider]
RESULT:           [PASS / FAIL / NOT TESTED]
NEXT ACTION:      [fix, retest, owner action, or none]
```
