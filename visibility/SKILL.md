---
name: visibility
description: SEO, local SEO, AI-crawlability, structured data, sitemap/robots/llms.txt, social preview, analytics, and indexing workflow for websites. Use when Codex needs to audit or implement website visibility improvements, optimize hotels/restaurants/physical businesses for local search and Google Business Profile readiness, fix client-rendered SPA crawlability issues, add schema code, generate or verify sitemap.xml/robots.txt/llms.txt, improve Open Graph/Twitter metadata, validate SSR/prerendered HTML, configure GA4/search-console workflows, or prepare a site for Google Search Console, Bing Webmaster Tools, AI assistants, and link previews.
---

# Visibility

## Overview

Use this skill to make a website findable and accurately represented by search engines, AI crawlers/assistants, and social/link-preview bots. Start with the current stack and crawlability evidence, then implement only the visibility pieces the project actually needs.

## Reference Routing

- Read `references/visibility-skill-source.md` for the scoped execution checklist and project workflow.
- Read `references/reference-seo-crawlability-playbook.md` when diagnosing SSR/prerendering, empty-shell SPAs, route HTML, or per-route metadata visibility.
- Read `references/reference-seo-how-to.md` when implementing concrete SEO assets: meta tags, Schema.org JSON-LD, robots.txt, sitemap.xml, GA4/CSP notes, llms.txt, content guidance, and monitoring workflows.

## Workflow

1. Identify the stack before editing.
   - SSR-by-default frameworks such as TanStack Start, Next.js App Router, Remix, SvelteKit, and Nuxt usually need a hygiene check, not a rendering rebuild.
   - Plain client-rendered Vite/React/Vue SPAs need empty-shell diagnostics and usually prerendering or SSR.
   - Static site generators usually go directly to metadata, schema, sitemap, robots, and content checks.

2. Verify crawlability like a bot.
   - Use curl with a Googlebot user agent against home and at least one inner route.
   - Confirm the returned HTML has real content, distinct titles, canonical URLs, and per-route metadata.
   - Do not claim SSR/prerendering is fixed based only on browser appearance.

3. Implement core technical visibility.
   - Unique page title, description, canonical, Open Graph, and Twitter card per public route.
   - One meaningful H1 per page and sensible heading hierarchy.
   - Crawlable anchor links for internal navigation.
   - Structured data rendered server-side where possible.
   - `robots.txt` and `sitemap.xml` generated from real route/content data.
   - `llms.txt` with factual business summary, key pages, key facts, contact, and AI crawler guidance aligned with robots.txt.
   - Crawl the internal link graph to find broken links, orphan pages, excessive crawl depth, redirect chains or loops, soft 404s, duplicate URL variants, and canonical conflicts.
   - Validate useful 404 behavior, pagination and breadcrumbs where applicable, the web app manifest and icon set, and RSS/Atom for sites with regularly published content.

4. Choose schema by page and business type.
   - Local physical business: `LocalBusiness` or a specific subtype with real address and contact fields.
   - Hotel/lodging: include `Hotel`, `LodgingBusiness`, `Offer`, and room/service data where appropriate.
   - Product pages: `Product` with image, description, offers, price/currency/availability when real data exists.
   - Blog/content: `Article` or `BlogPosting`.
   - Add `Restaurant`, `Event`, `Course`, `FAQPage`, `BreadcrumbList`, `SearchAction`, `Review`, `AggregateRating`, `VideoObject`, or `ImageObject` only when the visible content and working feature genuinely support that type.
   - Avoid fake ratings, fake reviews, stale prices, or hardcoded facts that can drift from source data.

5. Handle local SEO for hotels, restaurants, and physical businesses.
   - Recommend creating and verifying a Google Business Profile as an owner action.
   - Keep NAP data (Name, Address, Phone) consistent across the website, schema, Google Business Profile, social profiles, and directories.
   - Encourage genuine customer reviews; never fabricate ratings, reviews, or review schema.
   - Add high-quality, current photos regularly, especially rooms, food, exterior, interior, amenities, team, and guest spaces.
   - Choose accurate primary and secondary Google Business Profile categories for the actual business type.
   - Add all real services, amenities, booking options, business hours, and special hours.
   - Keep business hours, phone numbers, address, website URL, and booking/contact links current.
   - List the business on trusted local and industry directories such as Google Maps, Bing Places, Apple Business Connect, TripAdvisor, hotel/travel directories, local chambers, and relevant regional listings.
   - Treat Google Business Profile setup, directory accounts, review collection, and live listing verification as owner-side tasks unless credentials/account access are explicitly provided.

6. Support AI and social previews.
   - Add or update `llms.txt`.
   - Consider markdown mirrors for important pages when useful.
   - Verify social previews with actual share/debug tools or by inspecting server-rendered OG tags.
   - Treat `humans.txt` as optional attribution, `/.well-known/security.txt` as a maintained security-contact convention, and `browserconfig.xml` as platform-specific metadata rather than universal SEO requirements.

7. Optimize speed and mobile usability.
   - Compress local images into modern formats such as WebP/AVIF while preserving original fallbacks.
   - Serve responsive image sizes with explicit `sizes`, `loading`, `decoding`, and high priority only for above-the-fold LCP media.
   - Compress videos into mobile-friendly variants, use `preload="none"` or on-demand loading for non-critical videos, and keep poster images lightweight.
   - Avoid autoplaying heavy video on mobile unless it is muted, inline, and clearly beneficial to the first viewport.
   - Add lightweight loading, skeleton, or preloader states for slow networks without blocking usable content longer than necessary.
   - Check mobile tap targets, horizontal overflow, layout shift, and reduced-motion behavior before calling the experience seamless.
   - Re-run build and, when live, verify Core Web Vitals/PageSpeed on the homepage and at least one media-heavy inner page.

8. Validate before calling done.
   - Build passes.
   - Home and inner route curl outputs are distinct and contentful.
   - `robots.txt`, `sitemap.xml`, and `llms.txt` are reachable at root paths.
   - JSON-LD is valid for the page type.
   - No placeholders remain in visibility assets.
   - If live, use Google Search Console URL Inspection and Bing Webmaster Tools/IndexNow where relevant.
   - Verify configured analytics providers in the browser Network panel, including duplicate events, consent behavior, and CSP-blocked collection endpoints; do not claim dashboard receipt from script presence alone.
   - Separate readiness from verified registration/indexing for Google, Bing/Yahoo, DuckDuckGo, Brave, Yandex, and Baidu, and recommend only engines relevant to the site's audience.

9. Validate agent accessibility and ARIA.
   - Run standard accessibility checks and inspect the rendered browser accessibility tree. Review PageSpeed Agentic Browsing findings separately when available; this evolving audit category is not a direct SEO ranking factor.
   - Prefer native HTML semantics. Search rendered markup for invalid or misleading role overrides, confirm roles are permitted and appropriate, and verify every `aria-labelledby` and `aria-describedby` reference resolves to a real, unique ID.
   - Use `aria-modal` only with a genuine `dialog`, `alertdialog`, or correct native modal implementation. Treat consent and preference banners as non-modal unless they block background interaction and implement focus entry, containment, dismissal, and restoration.
   - Do not add unnecessary ARIA to chase a score. Verify Preview or Production output, then rerun Lighthouse/PageSpeed after deployment; a local source change does not prove the live result is fixed.

   Final verification:

   - [ ] No inappropriate role overrides on semantic HTML elements.
   - [ ] All ARIA references resolve to real, unique elements.
   - [ ] Non-modal banners do not claim dialog/modal semantics.
   - [ ] Real modal dialogs implement focus entry, focus containment, dismissal, and focus restoration.
   - [ ] PageSpeed Agentic Browsing findings reviewed when available.
   - [ ] Accessibility tree inspected in browser developer tools.
   - [ ] Fix verified on the deployed Preview or live URL.

## Output Expectations

When auditing, report findings by severity with file/line references where local code is available. When implementing, keep changes aligned to the framework's official head/meta APIs and existing route/data patterns. Mention which checks were run, which could not be run, and any owner-only tasks such as Search Console verification.
