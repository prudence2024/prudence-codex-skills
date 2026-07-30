# Visibility reasoning and responsibility boundary

Use this reference for material visibility decisions and for any work that
intersects Design Toolkit or Security ownership.

## Contents

1. Visibility context
2. Design Toolkit consumption
3. Visibility evidence levels
4. Strategy alternatives
5. Decision requirements
6. Domain responsibilities
7. Shared Context integration
8. Extension points and handoffs

## Visibility context

Establish:

- truthful business identity, offerings, locations, markets, and contact facts;
- target audiences, languages, regions, and likely search intent;
- public content and routes intended for discovery;
- private, account, administrative, preview, staging, and sensitive boundaries;
- framework, rendering model, content source, deployment, and canonical property;
- content ownership, publishing cadence, update events, and maintenance ability;
- current metadata, structured data, sitemap, robots, social-preview, analytics,
  and search-platform state;
- measured search evidence and unresolved uncertainty.

Do not infer business facts from a competitor, reference site, placeholder,
schema example, or model memory.

## Design Toolkit consumption

Read applicable `design-toolkit` decisions from Shared Context or supplied
artifacts. Consume:

- approved content hierarchy and information architecture;
- component and design-system constraints;
- brand and audience decisions;
- accessibility findings;
- responsive and frontend-performance constraints;
- media, interaction, and conversion decisions;
- remaining design uncertainty.

Visibility may identify that a design decision harms crawlability,
discoverability, metadata exposure, semantic content, link behavior, or measured
search performance. Record the evidence and hand the decision back to Design
Toolkit. Do not independently redesign the interface.

Examples:

- Specify that navigation destinations need crawlable anchors; let Design
  Toolkit decide their visual and interaction treatment.
- Specify required server-visible headings and product facts; let Design Toolkit
  decide composition and hierarchy within semantic constraints.
- Report LCP or layout-shift evidence that affects search performance; let Design
  Toolkit own general frontend optimization and presentation trade-offs.
- Specify image and page metadata requirements; consume the approved brand and
  media decisions rather than selecting a new visual direction.

If no Design Toolkit output exists, complete visibility-only work and create a
handoff for material design decisions. Do not make an implicit substitute design
decision.

## Visibility evidence levels

Keep these states separate:

1. **Implemented** — source or configuration contains the control.
2. **Built** — the project successfully produces an artifact.
3. **Deployed** — the target environment serves the artifact.
4. **Reachable** — the intended public URL returns the expected status and
   content.
5. **Registered** — a provider property or submission is confirmed.
6. **Received** — analytics, indexing, or notification provider receipt is
   confirmed.
7. **Indexed** — a search provider reports or demonstrates indexing.
8. **Measured** — field or provider data supports a performance or visibility
   outcome.

Never collapse these into “done.” Record environment, URL, revision, timestamp,
tool, and limitations.

Use `not_verified` for provider dashboards, ownership, live deployment,
indexing, analytics receipt, share previews, or measurements without direct
evidence.

## Strategy alternatives

Compare credible options for the real stack:

- existing framework metadata and server-rendering APIs;
- static generation or prerendering;
- SSR or hybrid rendering;
- dynamic server routes for sitemaps or structured content;
- build-time generation from trusted content data;
- manual owner actions versus safe automation;
- no change when current behavior is already correct.

Evaluate:

- initial HTML and crawler behavior;
- canonical and route correctness;
- content freshness and source-of-truth drift;
- hosting and deployment constraints;
- maintenance and operational ownership;
- privacy and security boundaries;
- compatibility with Design Toolkit decisions;
- provider support and audience relevance;
- reversibility and failure behavior.

Do not prescribe a rendering rebuild merely because a framework supports one.
Diagnose the actual response first.

## Decision requirements

Every material visibility decision must state:

1. the selected strategy and why it fits;
2. alternatives considered and specific rejection reasons;
3. Design Toolkit decisions consumed;
4. truthful data sources and drift controls;
5. affected visibility domains;
6. implementation, deployment, provider, and measurement evidence;
7. risks and mitigations;
8. trade-offs;
9. remaining uncertainties;
10. validation evidence and checks not run;
11. owner actions and specialist handoffs.

Validate machine-readable decisions against
`schemas/visibility-decision.json`.

## Domain responsibilities

### SEO and discoverability

- Align public content, search intent, internal links, headings, and route
  semantics without inventing claims or redesigning presentation.
- Distinguish technical discoverability from content strategy and ranking
  promises.

### Crawlability

- Inspect initial response HTML, status codes, redirects, canonical URLs,
  directives, link graphs, rendering, and route variants.
- Detect empty shells, accidental client-only content, soft 404s, loops, orphan
  pages, and conflicting canonical signals.

### Indexing

- Manage truthful index directives, canonicalization, sitemaps, IndexNow or
  provider submission readiness, and public/private boundaries.
- Treat registration and indexing as external states requiring evidence.

### Structured data

- Select types supported by visible content and working features.
- Derive changing facts from maintained data sources.
- Never fabricate ratings, reviews, offers, prices, availability, events, search
  actions, or organizational claims.

### Metadata and social previews

- Require unique, truthful per-route titles, descriptions, canonical URLs, Open
  Graph fields, and platform metadata where appropriate.
- Consume approved Design Toolkit brand and image artifacts.
- Verify server-visible tags and actual preview tools when available.

### Search performance

- Record lab and field data separately.
- Track search-facing rendering, response, Core Web Vitals, and content-access
  evidence.
- Handoff general frontend-performance diagnosis and design trade-offs to Design
  Toolkit.

### Web and AI visibility

- Keep robots, `llms.txt`, markdown mirrors, structured data, and public content
  mutually consistent.
- Represent emerging conventions accurately and avoid guaranteed-ranking claims.

## Shared Context integration

Read project identity, goals, constraints, facts, assumptions, uncertainty,
decisions, artifacts, risks, and prior runs. Bind code and live observations to
the inspected revision and environment.

Write attributable:

- observed crawl, route, metadata, schema, social, analytics, provider, and
  performance facts;
- uncertainty about deployment, ownership, indexing, receipt, or measurement;
- approved visibility decisions;
- generated or changed artifacts;
- risks;
- validation runs;
- handoffs.

Do not store credentials, verification tokens, unpublished URLs, raw analytics
identifiers when sensitive, or unnecessary personal data.

## Extension points and handoffs

Future adapters may implement framework metadata, search engines, indexing
providers, analytics, local search, schema rules, crawlers, preview validators,
or search-performance metrics. Each adapter must declare inputs, outputs,
provider/version scope, evidence semantics, rate and credential handling,
validation, failure behavior, and context access.

Adapters remain advisory or operational components under Visibility. Visibility
retains final domain reasoning and unified reporting.

Handoff:

- design, components, accessibility implementation, responsive behavior, visual
  hierarchy, interaction, and general frontend performance to `$design-toolkit`;
- CSP, headers, secrets, authorization, privacy controls, and broader security
  policy to `$security`;
- account verification, business listings, provider ownership, review
  collection, and other credentialed owner actions to the user or named
  operator.

