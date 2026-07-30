---
name: visibility
description: SEO, local SEO, AI-crawlability, structured data, sitemap/robots/llms.txt, social preview, analytics, and indexing workflow for websites. Use when Codex needs to audit or implement website visibility improvements, optimize hotels/restaurants/physical businesses for local search and Google Business Profile readiness, fix client-rendered SPA crawlability issues, add schema code, generate or verify sitemap.xml/robots.txt/llms.txt, improve Open Graph/Twitter metadata, validate SSR/prerendered HTML, configure GA4/search-console workflows, or prepare a site for Google Search Console, Bing Webmaster Tools, AI assistants, and link previews.
---

# Visibility

Own SEO, discoverability, indexing, structured data, metadata, social previews,
crawlability, search performance, and web visibility. Start from truthful project
facts and deployment evidence, then implement only the visibility controls the
project needs.

Consume applicable `$design-toolkit` decisions and validation results. Do not
repeat design reasoning, component selection, visual hierarchy, interaction,
accessibility implementation, or general frontend-performance planning.

## Reference routing

- Read
  [references/visibility-reasoning.md](references/visibility-reasoning.md) for
  responsibility boundaries, Shared Context use, evidence levels, alternatives,
  decisions, and Design Toolkit consumption.
- Read
  [references/visibility-skill-source.md](references/visibility-skill-source.md)
  for the scoped execution checklist and stack-aware workflow.
- Read
  [references/reference-seo-crawlability-playbook.md](references/reference-seo-crawlability-playbook.md)
  when diagnosing SSR, prerendering, empty-shell SPAs, route HTML, or per-route
  metadata visibility.
- Read
  [references/reference-seo-how-to.md](references/reference-seo-how-to.md) when
  implementing metadata, structured data, robots, sitemaps, analytics,
  `llms.txt`, content guidance, or monitoring workflows.

Treat overlapping accessibility and performance material in legacy references as
visibility requirements or measurements. Use Design Toolkit for design decisions
and frontend implementation strategy.

## Workflow

1. Read and validate Shared Context. If none exists, create an in-memory envelope
   and report that it was not persisted.
2. Inspect project instructions, stack, routes, rendering, content sources,
   deployment, locales, public/private boundaries, analytics, search
   configuration, and current visibility assets.
3. Consume relevant Design Toolkit decisions and artifacts. Preserve approved
   design intent; record unresolved design dependencies instead of redesigning.
4. Establish business facts, target markets, audience search intent, public
   content, visibility objectives, current indexing state, and evidence gaps.
5. Verify crawlability like a bot using initial response HTML, status codes,
   canonical URLs, internal links, robots directives, and representative routes.
6. Evaluate metadata, structured data, sitemap, robots, `llms.txt`, social
   previews, local visibility, analytics, indexing workflows, and search
   performance only where applicable.
7. Compare credible implementation alternatives and record why the selected
   approach fits the real stack, content model, deployment, and maintenance
   constraints.
8. Before implementation, record the selected strategy, alternatives, rejection
   reasons, risks, trade-offs, truthfulness constraints, and remaining
   uncertainty.
9. Implement only authorized, framework-native changes. Derive visibility data
   from real content and routes; never invent business facts, ratings, reviews,
   prices, availability, or working search behavior.
10. Validate local or preview output, then validate the deployed environment
    separately when available. Distinguish configuration, readiness,
    registration, indexing, and measured search performance.
11. Update only declared Shared Context fields and produce the standardized
    report.
12. Handoff design/accessibility/frontend-performance work to `$design-toolkit`,
    security-policy decisions to `$security`, and account-owner actions to the
    user or named operator.

## Required decision record

For every material visibility decision, explain:

- why the selected strategy was chosen;
- which alternatives were considered and why they were rejected;
- which Design Toolkit decisions or constraints were consumed;
- truthfulness and content-source requirements;
- crawlability, indexing, metadata, schema, social, and search-performance
  implications;
- risks and trade-offs;
- remaining uncertainties;
- validation evidence and checks not run;
- owner-only actions and specialist handoffs.

Use `schemas/visibility-decision.json` for machine-readable decision artifacts.

## Evidence rules

- Treat source code as implementation evidence, not proof of deployment,
  indexing, analytics receipt, rich-result eligibility, or ranking.
- Record exact URL, environment, revision, timestamp, tool, mode, and limitation
  for live or laboratory measurements.
- Mark provider dashboards, ownership, registrations, and external results
  `not_verified` until direct evidence exists.
- Treat Search Console, Bing, analytics, PageSpeed, and social-debugger results as
  provider evidence tied to the inspected property and time.
- Do not promise rankings, indexing dates, rich results, traffic, or Core Web
  Vitals outcomes.

## Guardrails

- Preserve the original meaning and information architecture of approved Design
  Toolkit decisions unless a visibility defect requires a documented handoff.
- Do not add schema types unsupported by visible, truthful content and working
  features.
- Do not let `robots.txt`, `llms.txt`, meta tags, or schema contradict actual
  access rules or business practices.
- Keep private, preview, staging, account, admin, and sensitive routes out of
  public indexes.
- Do not expose secrets, analytics credentials, verification tokens, or private
  URLs in Shared Context or reports.
- Do not treat `llms.txt`, `humans.txt`, agentic audits, or other emerging
  conventions as guaranteed ranking signals.
- Do not change CSP or broader security policy without `$security`; state the
  required visibility endpoint and hand off the policy decision.
- Do not redesign interfaces, choose components, or duplicate Design Toolkit
  validation.
