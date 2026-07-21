---
name: post-production
description: Coordinate a complete evidence-based post-production audit and hardening pass for websites and web applications across SEO, AI discoverability, accessibility, performance, Core Web Vitals, security, metadata, structured data, analytics, monitoring, deployment, progressive enhancement, mobile behavior, crawlability, indexability, and code quality. Use before launch, after a major release, when reviewing Lighthouse/PageSpeed/Search Console/Bing findings, when comparing a live deployment with a repository revision, or when the user requests a production-readiness score and prioritized remediation report.
---

# Post Production

Audit the real project and deployed environment before claiming production readiness. Coordinate the existing specialist skills instead of duplicating their detailed guidance.

## Reference routing

- Read [references/audit-matrix.md](references/audit-matrix.md) for the complete cross-discipline checklist and result statuses.
- Use `$visibility` for SEO, AI crawlability, metadata, schema, indexing, local SEO, analytics, and social-preview work.
- Use `$design-toolkit` for accessibility, responsive behavior, progressive enhancement, forms, browser diagnostics, and frontend performance.
- Use `$security` for secrets, APIs, headers, CSP, cookies, dependencies, rate limiting, data access, and infrastructure controls.
- Use `$incident-response` for error tracking, logs, alerts, uptime, health checks, rollback, backups, runbooks, and recovery drills.
- Use `$legal-business` when the site collects personal data, takes reservations or payments, or publishes legal policies.
- Use `$session-security` only when authenticated sessions exist.
- Use `$support-triage` when the request begins with a user-reported production failure or deployment discrepancy.

## Workflow

1. Establish scope and deployment truth.
   - Read project instructions and inspect the stack, routes, integrations, data stores, auth, payments, forms, hosting, Git branches, and deployment configuration.
   - Record the current worktree state before editing. Preserve unrelated changes.
   - Identify the exact deployed revision when possible. Compare live asset hashes, build identifiers, or distinctive markup with the repository; a pushed commit is not proof of deployment.

2. Produce the baseline report before changes.
   - Inventory what already exists and do not duplicate it.
   - Classify each relevant control as `[x] Completed`, `[-] Partial`, `[ ] Not Started`, `N/A`, or `Unverified`.
   - Rank findings as Critical, High, Medium, or Low and give evidence plus user impact.
   - Never invent a score. Derive scores from explicit completed/relevant checks or report tool scores with their source, URL, mode, timestamp, and limitations.

3. Run proportionate checks.
   - Build, test, type-check, lint, and audit dependencies using the project's real commands.
   - Inspect initial server HTML, metadata, links, status codes, redirects, structured data, robots, sitemap, llms.txt, manifests, headers, and browser console/network behavior.
   - Test representative phone, tablet, and desktop layouts plus keyboard-only operation.
   - Run Lighthouse/PageSpeed against a production build or deployed URL. Distinguish lab results from field data and local results from live results.
   - Mark provider-dashboard controls such as billing alerts, uptime notifications, Search Console ownership, and rollback history `Unverified` until direct evidence exists.

4. Apply authorized fixes.
   - Prefer framework-native and existing-project patterns.
   - Keep changes small, reversible, and tied to confirmed findings.
   - Preserve working functionality and user data. Do not add a provider, tracker, cookie, or paid service without confirming configuration and privacy impact.
   - Do not run intrusive security scans, load tests, destructive recovery tests, or production fault injection without explicit authorization and safe bounds.

5. Verify after changes.
   - Re-run affected checks and the production build.
   - Check the preview deployment before production when available.
   - Verify the live environment separately after deployment; a successful local build or preview is not production evidence.
   - Confirm fixes using concrete output, not code inspection alone.

6. Deliver the final report.
   - Lead with the executive outcome and the three largest remaining risks.
   - Include measured SEO, accessibility, performance, security, AI-discoverability, and Core Web Vitals results where evidence supports them.
   - List Critical, High, Medium, and Low findings; changes applied; remaining owner actions; commands/checks run; and checks that could not be completed.
   - End with the status checklist from the audit matrix and provide a concise GitHub commit message whenever project files changed.

## Guardrails

- Do not promise or optimize solely for a Lighthouse score of 100. Prioritize user harm, conformance, Core Web Vitals, and repeatable evidence.
- Do not add schema types merely because they are listed. Add only types supported by visible, truthful page content and working features; never fabricate reviews, ratings, prices, or SearchAction behavior.
- Treat `llms.txt`, `humans.txt`, and similar conventions accurately: useful where applicable, but not guaranteed ranking signals.
- Distinguish application behavior from hosting-provider preview or authentication injection when diagnosing CSP, manifest, console, or indexing issues.
- Keep preview/staging URLs out of search indexes and canonicalize public content to the production domain.
