# Production foundations reference

Use this reference alongside the security checklist for AI-built applications. Inspect the real repository and deployment configuration; do not accept a generated feature or provider setting as evidence that it works. Report pass, fail, or not verifiable for each relevant control and cite the evidence.

## Backend contracts

- Keep endpoints focused, consistently named, and aligned with the framework's HTTP semantics.
- Validate success and failure paths with realistic requests, including missing fields, wrong types, absent records, dependency failure, and unauthorized access.
- Return appropriate status codes and stable response shapes. Expose only fields the client needs.
- Bound slow work with timeouts and useful failure states; paginate or cap list results and remove unnecessary database calls.
- Trace critical actions in the browser Network panel or an API client instead of testing only through the happy-path UI.

## Database and storage design

- Verify schemas use appropriate types, required/optional rules, foreign keys, and explicit delete behavior.
- Add unique constraints for identities and business keys that must not duplicate.
- Add indexes based on actual search, filter, join, and ordering patterns; verify with representative data rather than assuming test-scale performance.
- Store uploaded blobs in object/file storage and keep controlled references plus metadata in the database.
- Apply schema changes through reviewed, reversible migrations tested away from production.

## Hosting and deployment

- Use preview or staging deployments for meaningful changes before production.
- Keep environment values separated by environment and configured in the hosting platform, not source control.
- Verify build logs, route behavior, custom-domain DNS, valid TLS, redirects, and mixed-content behavior on the deployed URL.
- Maintain a tested rollback path to the previous known-good release and notifications for failed deploys or downtime.
- Never edit production files directly; deploy from version-controlled artifacts.

## Cloud cost controls

- Inventory compute, storage, bandwidth/data transfer, database operations, scheduled work, and paid external API calls.
- Record pricing units, free-tier limits, and likely cost at representative traffic levels such as 1,000 and 100,000 users or requests.
- Check usage at least weekly during early operation; configure budgets, alerts, and provider hard caps where available.
- Use separate development and production credentials, quotas, and budgets so test loops cannot consume production allowance.
- Challenge AI-generated calls that run on every request, page load, keystroke, or loop; debounce, batch, cache, or remove them where behavior permits.

## Version control and delivery discipline

- Create small, meaningful commits with messages that explain the change; make a checkpoint before allowing a large AI rewrite.
- Work in a branch for risky changes, keep a remote copy current, and understand that commit, push, merge, build, and deploy are separate events.
- Run tests, linting, builds, and security checks before merge or production deployment. Inspect failed pipeline and deployment logs instead of retrying unchanged code.
- Keep the lockfile committed and make the deployed revision identifiable and reversible.

## Caching and CDN

- Classify content before caching: public/static content can usually be cached broadly; private, per-user, transactional, or permission-sensitive content requires isolation or `no-store`.
- Give static versioned assets durable cache lifetimes and use content hashes or another cache-busting strategy on deploy.
- Define cache ownership, freshness, invalidation, and behavior when the cache is unavailable. Test that updates become visible when expected.
- Verify CDN and browser caching from response headers and repeat requests, not merely from a provider feature list.
- Optimize image dimensions and formats, lazy-load below-the-fold media, and check font loading and route-level code splitting.

## Capacity and scaling

- Write down expected normal and peak traffic, latency target, and acceptable error rate before selecting scaling settings.
- Establish a baseline, then run a bounded load test with a tool such as k6 or Artillery in a safe non-production environment unless production testing is explicitly authorized.
- Measure response time, error rate, CPU/memory, database connections, and external dependency behavior while load increases.
- Choose vertical or horizontal scaling based on the observed bottleneck. Configure auto-scaling with minimum, maximum, trigger, cooldown, and cost bounds.
- Use dependency-aware health checks, remove unhealthy instances from rotation, and keep horizontally scaled application instances stateless or put session state in a shared store.
- Configure database connection pooling and treat the database as a separate bottleneck; add replicas or other scaling mechanisms only when measurements justify them.

## Review output

- Separate repository-confirmed findings from provider settings that require dashboard access.
- Give each failed control a consequence, evidence, and smallest practical remediation.
- End with the three highest-risk launch blockers, then list lower-priority performance or cost improvements.
