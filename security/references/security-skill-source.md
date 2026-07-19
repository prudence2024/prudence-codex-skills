# Security Skill

A reusable, project-agnostic security skill — paste as `SECURITY-SKILL.md` (or fold
into `AGENTS.md`/`.cursorrules`) at the start of any project. Re-run the checklist at
the end before every launch, not just once. This supersedes the earlier
`security-first-vibe-coding-rules.md` — same foundation, with dependency scanning,
monitoring/observability, backup/recovery, CI/CD gates, and full form-validation code
folded in as their own proper sections instead of scattered bullets.

**How to use this:** paste the whole thing as project-level instructions at the start
of any new build. When a project needs something this file doesn't cover, add it here
— this file is meant to grow, not stay static.

---

## 1. Secrets & Environment Variables

- All API keys, tokens, database URLs, and service credentials live in `.env` files
  only — never hardcoded, not even "temporarily for testing."
- `.env`, `.env.local`, and `.env.*.local` must always be in `.gitignore`.
- Frontend code never contains a raw secret value. In frameworks with a public
  variable prefix (`NEXT_PUBLIC_`, `VITE_`), only genuinely public values belong
  there — never a secret key, even one that "seems low-risk."
- If a key is intentionally public-safe (e.g. a Stripe/Paystack publishable key),
  comment clearly that it's meant to be exposed, so nobody later assumes it's a leak.
- Generate a `.env.example` with all required variable names and empty values.
- Backend-only secrets are read via `process.env.VAR_NAME` and never echoed back in
  an API response.
- Rotate any secret that ever touched a public repo, a shared screen, or an AI chat
  transcript, even briefly.

## 2. Authentication & Session Security

- Never roll your own authentication — use a proven provider (Supabase Auth,
  NextAuth.js, Clerk, Auth0, Passport.js, lucia-auth).
- Passwords: **Argon2id** hashing (preferred over bcrypt where available), never
  plain text.
- JWTs: strong secret (32+ chars, from env), short expiry (15 min–1 hour), refresh
  tokens with rotation. Refresh tokens live in httpOnly, secure, SameSite cookies —
  **never in `localStorage`**, where any injected script can read them.
- Admin/sensitive routes: server-side authorization check on every request, never a
  client-side-only check (a hidden button or disabled UI element is not a security
  control — it's cosmetic).
- Implement account lockout/backoff after repeated failed logins, backed by an
  actual login-attempt log (see §11) — a lockout *rule* with nothing recording
  attempts isn't enforceable.
- Support 2FA/OTP as a hardening option, especially for admin accounts.
- Authentication answers "who is this." Authorization answers "what are they allowed
  to do." Every request verifies both.
- No table/collection gets a blanket "allow all to authenticated" policy — scope
  access explicitly in the policy/function itself, never by trusting the frontend to
  only ask for the right rows.

## 3. Input Validation & Injection Prevention

- Validate every input server-side against an explicit schema (Zod/Pydantic/Joi) —
  client-side validation is UX only, never security.
- **Never build queries with string concatenation.** Use an ORM or parameterized
  queries every time, even for "simple" queries.
- **Mass assignment:** save only the exact fields a form expects — never the raw
  submitted object — or someone can sneak in a field like `"role": "admin"`.
- **Stored XSS:** any user-submitted text that later gets displayed again — a
  contact message in an admin panel, a review, a comment — renders as plain text,
  never raw HTML. No `dangerouslySetInnerHTML`/`v-html` on user content without
  sanitizing first. No `eval()` or `new Function()` on dynamic content.
- **CSV/formula injection:** escape any exported field starting with `=`, `+`, `-`,
  or `@` before it can be opened in Excel/Sheets.
- **Spam/bot flooding:** pair rate limiting with a honeypot field on public forms.

### Form validation reference implementation (Zod + XSS sanitization)

Full defence-in-depth pattern for any form: frontend Zod validation → XSS
sanitization → server-side re-validation (never trust the client) → CORS-restricted
API endpoint. Install: `npm install zod xss`.

**`lib/validation.ts`** — schema per form, reusable helpers for error extraction:

```typescript
import { z } from 'zod'

// Adapt phone validation to the actual target region/format per project —
// this is illustrative, not universal.
const validatePhone = (phone: string): boolean => {
  const digits = phone.replace(/\D/g, '')
  return digits.length >= 10 && digits.length <= 15
}

export const contactFormSchema = z.object({
  name: z.string()
    .min(2, 'Name must be at least 2 characters')
    .max(100, 'Name must be less than 100 characters')
    .regex(/^[a-zA-Z\s\-'\.]+$/, 'Name can only contain letters, spaces, hyphens, apostrophes and dots'),
  email: z.string()
    .email('Please enter a valid email address')
    .max(254, 'Email must be less than 254 characters')
    .toLowerCase(),
  phone: z.string()
    .min(10, 'Phone number must be at least 10 digits')
    .max(20, 'Phone number must be less than 20 characters')
    .refine(validatePhone, 'Please enter a valid phone number'),
  message: z.string()
    .min(10, 'Message must be at least 10 characters')
    .max(2000, 'Message must be less than 2000 characters'),
  agreedToTerms: z.boolean()
    .refine(val => val === true, 'You must agree to the terms and privacy policy'),
})
export type ContactFormData = z.infer<typeof contactFormSchema>

export const newsletterSchema = z.object({
  email: z.string().email('Please enter a valid email address').max(254).toLowerCase(),
})

// ── Common patterns worth reusing ──
// Optional field with empty-string fallback:
//   comments: z.string().max(2000).optional().or(z.literal(''))
// Enum validation:
//   category: z.enum(['electronics', 'accessories'], { message: 'Invalid category' })
// Numeric bounds:
//   quantity: z.number().int().min(1).max(100)
// Conditional validation (optional field, validated only if present):
//   phone: z.string().max(20).refine((val) => !val || validatePhone(val), 'Invalid phone').optional().or(z.literal(''))

export const getFieldErrors = (error: z.ZodError): Record<string, string> => {
  const errors: Record<string, string> = {}
  error.issues.forEach((err) => {
    const path = err.path.join('.')
    if (!errors[path]) errors[path] = err.message
  })
  return errors
}
```

**`lib/sanitize.ts`** — strip malicious content before it's ever stored:

```typescript
import xss, { IFilterXSSOptions } from 'xss'

const xssOptions: IFilterXSSOptions = {
  whiteList: {},
  stripIgnoreTag: true,
  stripIgnoreTagBody: ['script', 'style'],
}

export const sanitize = (input: string): string => {
  if (!input || typeof input !== 'string') return ''
  return xss(input.trim(), xssOptions)
}

export const sanitizeObject = <T extends Record<string, unknown>>(obj: T): T => {
  const sanitized: Record<string, unknown> = {}
  for (const [key, value] of Object.entries(obj)) {
    if (typeof value === 'string') sanitized[key] = sanitize(value)
    else if (Array.isArray(value)) sanitized[key] = value.map((v) => typeof v === 'string' ? sanitize(v) : v)
    else if (value !== null && typeof value === 'object') sanitized[key] = sanitizeObject(value as Record<string, unknown>)
    else sanitized[key] = value
  }
  return sanitized as T
}

export const sanitizeEmail = (email: string): string => (email || '').trim().toLowerCase()
export const sanitizePhone = (phone: string): string => (phone || '').replace(/[^\d\s\+\-]/g, '').trim()
```

**Server-side re-validation is mandatory** — the frontend schema is UX, this is the
actual security boundary. Example API handler pattern (adapt to the actual
framework — Next.js App Router shown):

```typescript
// app/api/contact/route.ts
import { NextRequest, NextResponse } from 'next/server'
import { contactFormSchema, getFieldErrors } from '@/lib/validation'
import { sanitize, sanitizeEmail, sanitizePhone } from '@/lib/sanitize'
import { z } from 'zod'

const ALLOWED_ORIGINS = ['https://yourdomain.com', 'https://www.yourdomain.com', 'http://localhost:3000']

export async function POST(request: NextRequest) {
  const origin = request.headers.get('origin') || ''
  const isAllowedOrigin = ALLOWED_ORIGINS.includes(origin)

  try {
    const body = await request.json()
    const result = contactFormSchema.safeParse(body)
    if (!result.success) {
      return NextResponse.json(
        { success: false, error: 'Validation failed', errors: getFieldErrors(result.error) },
        { status: 400, headers: isAllowedOrigin ? { 'Access-Control-Allow-Origin': origin } : {} }
      )
    }

    const clean = {
      name: sanitize(result.data.name),
      email: sanitizeEmail(result.data.email),
      phone: sanitizePhone(result.data.phone),
      message: sanitize(result.data.message),
    }

    // Process clean data — save, email, etc. Never the raw unsanitized body.

    return NextResponse.json({ success: true }, { status: 200,
      headers: isAllowedOrigin ? { 'Access-Control-Allow-Origin': origin } : {} })
  } catch (error) {
    console.error('Form API error:', error) // log full detail server-side only
    if (error instanceof z.ZodError) {
      return NextResponse.json({ success: false, error: 'Validation failed', errors: getFieldErrors(error) }, { status: 400 })
    }
    return NextResponse.json({ success: false, error: 'Something went wrong. Please try again.' }, { status: 500 }) // generic to client
  }
}

export async function OPTIONS() {
  return new NextResponse(null, { status: 200, headers: {
    'Access-Control-Allow-Methods': 'POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
  }})
}
```

For a serverless/edge-function context (Supabase Edge Functions, Vercel Functions),
the same three-part pattern applies — validate, sanitize, explicit CORS allowlist —
just adapted to that platform's request/response shape.

**Validation rules quick reference**

| Field type | Rule of thumb |
|---|---|
| Name | 2–100 chars, letters/spaces/hyphens/apostrophes only |
| Email | Valid format, max 254 chars, lowercase before storing |
| Phone | Region-appropriate format check, don't over-constrain internationally |
| Message/comment | Reasonable min/max length (e.g. 10–2000 chars) |
| Dropdown/select | `z.enum()` of allowed values, never freeform for a fixed set |
| Checkbox (required agreement) | Boolean + `.refine(val => val === true, ...)` |
| Multi-select | `z.array()` with `.min(1)` if at least one selection is required |

## 4. Database Security

- Enable row-level security (or equivalent) on every table from the start, with
  explicit, minimal policies — no table left on default "allow all."
- Least privilege at the database-user level too — the credential your app connects
  with should only have the permissions it actually needs.
- Sensitive writes (payments, order status, role changes) only happen from trusted
  server-side code (service-role key/edge function), never directly from the client.
- Don't return raw database errors to the client — they leak schema information.
- Every list/query endpoint has an explicit page-size limit.
- Any webhook verifies its signature before acting, and is idempotent.

## 5. Rate Limiting

Every public-facing endpoint needs rate limiting — especially auth, form
submissions, AI completions, file uploads, and anything expensive to run.

Reasonable defaults (adjust per app):
- Auth endpoints (login, register, password reset): **5 requests / 15 minutes / IP**
- General API: **60 requests / minute / IP**
- AI/LLM proxy endpoints: **10 requests / minute / user**
- File uploads: **5 requests / minute / IP**

Return `429 Too Many Requests` with a `Retry-After` header — never fail silently.

Libraries by stack: `express-rate-limit` (Node/Express) · Next.js middleware with
`lru-cache` or Upstash Redis (Edge/Vercel) · `slowapi` (FastAPI) · `Flask-Limiter`
(Flask).

## 6. CORS & HTTP Security Headers

- Never use a wildcard (`*`) CORS origin in production on anything touching real
  data — whitelist exact origins (see the `ALLOWED_ORIGINS` pattern in §3).
- Restrict allowed HTTP methods to what each endpoint actually needs.
- Set on every deployment: `Content-Security-Policy`, `Strict-Transport-Security`,
  `X-Content-Type-Options: nosniff`, `X-Frame-Options: DENY`,
  `Referrer-Policy: strict-origin-when-cross-origin`.
- Remove the `X-Powered-By` header.
- Session tokens live in secure, httpOnly, SameSite cookies — never `localStorage`.

## 7. File Upload Security

- Validate file type by MIME type *and* actual content, not just the extension.
- Set strict size limits per upload type.
- Rename every uploaded file to a generated UUID — never keep the original filename.
- Store uploads outside the web root or in a cloud bucket, never with executable
  permissions.
- Scan for malware if the upload is public-facing or handles sensitive content.
- Only persist the file reference to the database after the upload is confirmed
  complete — an interrupted upload should never leave a broken reference behind.

## 8. Observability & Monitoring

- **Error tracking:** wrap the app in a global error boundary/middleware that
  catches unhandled errors, logs full detail to a real error-tracking service
  (Sentry or equivalent), and returns a clean generic message to the user — never a
  raw stack trace.
- **Structured server-side logging:** log with context (timestamp, user ID if
  available, route, sanitized input) to a logging service (not just console output
  nobody reads).
- **Uptime monitoring:** an external uptime check (Better Stack or equivalent) that
  alerts if the app goes down — you want to find out before a customer tells you.
- **Product/usage analytics** (PostHog or equivalent) is not itself a security
  control, but pairs with the above for spotting abnormal usage patterns (a sudden
  spike in a specific endpoint's traffic is often the first visible sign of abuse).
- Distinguish 4xx (client error) from 5xx (server error) — don't collapse
  validation failures into a generic 500.
- Define basic SLOs (service-level objectives) for critical paths (checkout, auth)
  so "is this degraded" has an actual threshold, not a gut feeling.

## 9. Dependency & Vulnerability Management

- Run an audit (`npm audit`, `pip-audit`, `cargo audit`) after installing anything,
  fix high/critical findings before shipping.
- Before accepting any AI-suggested package, confirm it actually exists on the real
  registry with a real publish history — AI tools occasionally invent a plausible
  package name that doesn't exist, and attackers register those names and wait
  ("slopsquatting").
- Avoid packages with no updates in 2+ years for anything security-relevant.
- Commit the lockfile, pin versions in production — the same lockfile across
  dev/staging/prod prevents "works on my machine" version drift becoming a security
  gap.
- **Monthly dependency/security audit** as a standing calendar reminder, not a
  one-time launch task.
- **Automate security scanning in CI** so a vulnerable dependency fails the build,
  not just an occasional manual check.
- For anything public-facing and significant: periodically run **OWASP ZAP**
  against the domain and **Burp Suite** against the API as active security testing,
  not just passive dependency scanning.

## 10. Backup & Disaster Recovery

- Automated backups, with three things explicitly decided, not assumed: **frequency**
  (how often), **location** (cross-region or off-site — a backup stored next to the
  thing it's backing up doesn't survive the failure that takes out both), and
  **actually testing the restore** — a backup nobody has ever restored from is a
  backup you don't actually have.
- Point-in-time recovery where the platform supports it, for undoing a bad
  migration or accidental data change without losing everything since the last
  snapshot.
- **Write an incident/data-breach response plan before you need one** — who gets
  notified, how the incident gets verified, how affected users get communicated
  with. Deciding this during an actual incident is how bad decisions get made under
  pressure.

## 11. Session & Login Logging

- Every login attempt — successful or failed — gets recorded (email/identifier
  attempted, success/failure, IP, user agent, timestamp). This is what makes
  "account lockout after repeated failures" (§2) actually enforceable.
- Lockout logic reads this log: e.g. 5+ failed attempts for the same identifier in
  15 minutes blocks further attempts with a clear message.
- Log inserts happen server-side (never a client-writable table with an open
  policy) so the log can't be flooded or tampered with by the same attacker it's
  meant to catch.
- Restrict read access to admin/owner roles only.

## 12. CI/CD & Code Review Discipline

- Automated CI/CD pipeline — tests and security scanning run on every push, not
  manually before a release when it's convenient.
- PR/merge gates: a minimum test-coverage threshold, no merge while critical issues
  are open, a coding-standards/lint check.
- Explicit standing instruction to any AI coding tool: never modify payment logic
  or run data-deleting operations against production without an explicit,
  human-confirmed step — these are exactly the operations where an AI's confident
  wrong guess costs the most.

## 13. Network Resilience & Partial Failure Handling

Bad or intermittent network is a routine condition to design for, not an edge case.

- **Idempotency on every write that costs money or creates a record.** The client
  generates a unique key (UUID) once per attempt and sends it with every retry —
  the backend checks "does a record already exist for this key" before creating a
  new one. This is what makes a duplicate tap or a retried request produce one
  record, not two.
- **Never trust a client-side redirect alone to confirm a payment succeeded** — a
  webhook (server-to-server) is the source of truth; the client-facing page should
  also verify directly rather than assuming success from the URL it landed on.
- **Decouple side effects from the core transaction** — a failure in a
  notification/email/webhook call must never roll back or block the primary action
  that already succeeded.
- **No-cache on transactional pages** (`Cache-Control: no-store`) with a
  check-and-redirect if the underlying record is already complete — stops a
  browser back-button from re-submitting a payment that already went through.
- **Persist in-progress form/cart state locally** (never sensitive payment
  details) so a dropped connection doesn't erase what someone already typed.
- **Apply updates in intended order, not arrival order** — guard rapid repeated
  actions on a laggy connection with a version/sequence check or debounce.
- **Reconcile on reconnect rather than replaying a queue** — refetch current state
  with one clean request instead of firing off every queued action.
- **Distinguish "slow" from "failed"** with sensible timeouts and a "still
  processing" state, rather than silently retrying or silently giving up.
- **Caching under failure:** decide explicitly who/what invalidates a cache and
  when, what happens on stale permissions/stale inventory, and what the app does if
  the cache itself becomes unavailable — "the cache never fails" is not a plan.

## 14. If This App Uses AI/LLM Features

- Never send raw user input straight to an LLM without sanitizing it first — this
  is how prompt injection happens.
- Route all LLM calls through your own backend — the API key stays server-side.
- Set a `max_tokens` limit on every LLM call, log token usage per user.
- Implement per-user/per-session token budgets if usage would otherwise be
  expensive and uncapped.
- Validate and sanitize LLM output before rendering it in the UI — generated
  content can itself contain HTML/script that becomes an XSS vector if rendered raw.

## 15. The Rule That Catches the Most, Regardless of Stack

- If AI-generated output includes a comment like *"for simplicity, we'll skip
  validation here"*, *"in production you'd want to add auth"*, or *"this is a
  placeholder, replace before launch"* — that's the AI telling you the code is
  incomplete. Don't ship it; ask it to finish the job with the same rigor as
  everything else.
- Review AI-generated code the way you'd review a pull request from someone new to
  production systems: assume it looks clean and check anyway.
- Explicitly ban prompts like "skip authentication for now" or "ignore security
  checks to save time" — you'll get code exactly as insecure as requested.

---

## Before You Launch — Checklist

- [ ] `.env` not committed to git; `.env.example` exists with empty values
- [ ] Every table/collection has explicit RLS/access policies — none on default-allow
- [ ] Every form and API payload is schema-validated *and* sanitized server-side
- [ ] Form submissions save only the exact expected fields, never the raw payload
- [ ] User-submitted content never renders as raw HTML anywhere, including admin views
- [ ] Any CSV/spreadsheet export escapes fields starting with `=`, `+`, `-`, `@`
- [ ] Every public endpoint has a rate limit and returns 429 + Retry-After when hit
- [ ] Payment/webhook endpoints verify signatures and are idempotent
- [ ] CORS restricted to known origins, no wildcard
- [ ] Security headers configured (CSP, HSTS, X-Frame-Options, X-Content-Type-Options, Referrer-Policy)
- [ ] File uploads validated by content, size-capped, renamed to UUID, stored outside web root
- [ ] Errors return generic messages to the client; real detail goes to server-side logs/error tracking
- [ ] Dependencies audited, lockfile committed, monthly audit scheduled, CI scanning active
- [ ] OWASP ZAP / Burp Suite pass done on anything significant and public-facing
- [ ] Backup frequency + location decided, and a restore has actually been tested
- [ ] A written incident/breach response plan exists
- [ ] Login attempts are logged, and lockout is actually enforced from that log
- [ ] Every money-moving or record-creating action uses an idempotency key
- [ ] Tested as a *second* user: can User A see or modify User B's data by guessing
      or editing a URL/ID?
- [ ] Billing alerts set on every paid service
- [ ] Launched to a small audience first, not announced everywhere on day one

---

*This is a living checklist, not a substitute for an actual security review on
anything handling real money or personal data. For anything beyond a small store or
side project, pair this with a human review before going live.*
