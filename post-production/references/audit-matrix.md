# Post-production audit matrix

Use only relevant controls. Mark every item with evidence as `[x] Completed`, `[-] Partial`, `[ ] Not Started`, `N/A`, or `Unverified`.

## Repository and deployment identity

- Framework, rendering mode, package manager, routes, public assets, APIs, forms, auth, storage, payments, analytics, and hosting are inventoried.
- Current branch, commit, remote tracking branch, dirty files, production branch, and deployed revision are distinguished.
- Local, preview/staging, and production checks are labeled separately.
- Build, test, type-check, lint, dependency audit, and CI status are recorded.

## SEO and crawl graph

- Unique titles, descriptions, canonical URLs, robots directives, H1s, semantic landmarks, heading order, image alternatives, and descriptive anchors.
- Internal links resolve without broken targets; orphan pages and excessive crawl depth are identified.
- Redirect chains, loops, incorrect HTTP status codes, soft 404s, duplicate URLs/content, trailing-slash/query variants, and canonical conflicts are checked.
- Pagination and breadcrumbs are implemented only where the information architecture needs them.
- XML sitemap contains indexable canonical routes, excludes redirects/errors/private URLs, validates, and agrees with robots.txt.
- A useful 404 page returns the correct 404 status.
- RSS/Atom exists when regularly published content and feed users justify it.

## AI discovery and structured data

- Server-rendered semantic content is readable without depending on client interaction.
- `llms.txt` is factual, current, reachable, and aligned with robots policy; markdown mirrors are considered for important content.
- JSON-LD matches visible page content and validates.
- Select only applicable types: Organization, WebSite, Person, Article/BlogPosting, Product, Service, SoftwareApplication, BreadcrumbList, FAQPage, LocalBusiness, Hotel, Restaurant, Event, Course, Review/AggregateRating, SearchAction, VideoObject, and ImageObject.
- FAQ, reviews, ratings, prices, events, and site-search actions are never invented or marked up when the visible feature/data does not exist.

## Accessibility and progressive enhancement

- Landmarks, accessible names, labels, errors, buttons versus links, navigation, skip link, heading sequence, and alternatives are correct.
- Keyboard order, visible focus, dialogs, menus, carousel duplicates, hidden focusable elements, and traps are tested.
- Text/control contrast, touch targets, zoom, reduced motion, screen-reader announcements, and color-independent meaning are checked.
- Critical content remains readable when JavaScript, animation, web fonts, media, analytics, or a third-party dependency fails.
- Forms preserve safe input and provide bounded loading, timeout, retry, offline, error, and success states.

## Performance and Core Web Vitals

- LCP, INP, CLS, FCP, and TTFB are measured in the appropriate lab/field context.
- LCP media is discoverable, correctly prioritized, not lazy-loaded, and not hidden behind a blocking preloader.
- Images use suitable dimensions, responsive sources, modern formats, explicit dimensions, and below-fold lazy loading.
- Fonts avoid render blocking; resource hints are justified rather than added indiscriminately.
- JavaScript/CSS bundles, route splitting, tree shaking, unused code, long tasks, hydration work, critical CSS, compression, caching, and CDN delivery are inspected.
- Static assets use durable caching and content hashes; HTML/private/transactional responses use safe freshness rules.
- Code-split clients handle deployment-version skew with the framework or bundler's native dynamic-import/preload failure hook, at most one guarded automatic reload, and a useful fallback if recovery fails; broad error matching and reload loops are avoided.
- HTML revalidates or uses `no-cache`, content-hashed JS/CSS remains immutable, and navigation from an old tab across a new preview deployment is tested for missing chunks, one-time recovery, and monitoring behavior.

## Security and privacy

- HTTPS redirect, TLS, CSP, HSTS, Permissions-Policy, Referrer-Policy, frame protection, MIME protection, and cross-origin policies are verified on deployed responses.
- CSP console violations are mapped to the exact directive, source, environment, and responsible component; allowlists remain least privilege.
- Cookies use appropriate Secure, HttpOnly, SameSite, scope, and lifetime attributes where cookies exist.
- State-changing endpoints have an applicable CSRF defense; CORS is not mistaken for CSRF protection.
- Secrets, environment separation, client bundle exposure, dependency advisories, input validation, output encoding, rate limits, generic errors, upload controls, auth/authorization, and data policies are checked.
- `/.well-known/security.txt` is considered for public sites with a maintained security contact and expiry date.

## Metadata, manifests, and social sharing

- Open Graph and Twitter/X title, description, image, URL, type, and image dimensions are route-appropriate.
- Favicon set, Apple touch icon, web app manifest, manifest icons/start URL/display/theme colors, and optional `browserconfig.xml` are valid and reachable.
- `humans.txt` is optional and added only when the owner wants public attribution; it is not treated as an SEO requirement.
- Actual share-preview tools or server-rendered tag inspection confirm representative inner pages.

## Analytics and search platforms

- Only configured providers are evaluated: GA4/GTM, Vercel Analytics, Search Console, Bing Webmaster Tools, Microsoft Clarity, Meta Pixel, LinkedIn Insight, or others.
- Scripts load once, page views/events are not duplicated, consent requirements are respected, CSP allows required endpoints, and browser/network evidence confirms delivery.
- Owner registration/readiness is separated for Google, Bing/Yahoo, DuckDuckGo, Brave, Yandex, and Baidu; do not claim submission or indexing without dashboard evidence.
- Local businesses have consistent NAP, truthful LocalBusiness subtype, opening/special hours, map/contact links, directory readiness, and owner-managed review workflows.

## Monitoring, recovery, and foundations

- External uptime checks, liveness/readiness endpoints, error tracking, source maps, structured logs, redaction, severity routing, and tested alerts exist.
- Deploy rollback, backups, restore testing, RTO/RPO, incident ownership, runbooks, and outage communication are verified.
- API contracts, database constraints/indexes/migrations, shared rate limiting, cache invalidation, cost budgets, scaling bounds, and bounded non-production load tests are checked when applicable.

## Code quality and maintainability

- Folder and naming conventions are coherent; repeated logic uses appropriate shared components or utilities.
- Unused files, dependencies, exports, dead code, debug output, stale feature flags, TODO production placeholders, and oversized dependencies are identified before removal.
- Type safety, tests around critical behavior, documentation for non-obvious operations, lockfile consistency, and maintainable framework-native patterns are assessed.

## Reporting template

1. Executive summary and evidence-based readiness score or `Not enough evidence`.
2. Measured category scores with source, URL/environment, timestamp, and limitations.
3. Critical, High, Medium, and Low findings with impact, evidence, and remediation.
4. Changes applied and verification results.
5. Remaining recommendations split into repository work, deployment work, provider-dashboard work, and owner/legal work.
6. Final checklist using the five statuses above.
7. GitHub commit message when files changed.
