# SEO Crawlability Playbook — Fix Client-Rendered SPAs for Google

**Purpose:** Diagnose and fix the "empty shell" crawlability problem in a client-rendered React SPA.

**The core problem:** A pure client-side-rendered (CSR) React + Vite SPA serves an empty
`<div id="root"></div>` shell for every URL. Content and per-route meta tags are injected by
JavaScript after load. Non-JS crawlers and link-preview bots (WhatsApp, LinkedIn, Facebook, X, Slack)
run no JS, so every shared link shows the same generic title/description/image.

**Next.js and TanStack Start projects are usually fine** — both SSR by default. For those, this is a
hygiene check, not a rebuild (see Phase 1B).

## Phase 0 — Diagnose

```bash
SITE="https://www.example.com"
INNER="$SITE/some-inner-page"

curl -s -A "Googlebot/2.1 (+http://www.google.com/bot.html)" "$SITE"  > /tmp/home.html
curl -s -A "Googlebot/2.1 (+http://www.google.com/bot.html)" "$INNER" > /tmp/inner.html

grep -o '<div id="root">[^<]*</div>' /tmp/home.html

[ "$(md5 -q /tmp/home.html)" = "$(md5 -q /tmp/inner.html)" ] \
  && echo "IDENTICAL SHELL — needs prerendering" || echo "Distinct HTML — likely OK"

grep -o '<title>[^<]*</title>' /tmp/home.html /tmp/inner.html

for f in /tmp/home.html /tmp/inner.html; do
  echo "$f: $(sed 's/<[^>]*>//g' "$f" | tr -s ' \n' ' ' | wc -w) words"; done
```

**Verdict:** Empty `<div id="root">` + identical HTML across routes + same generic `<title>` →
HAS THE PROBLEM. Distinct per-route HTML with real content/titles → already fixed or SSR framework.

## Phase 1A — Vite branch: build-time prerendering

(Full reference implementation — routes manifest, renderRoute/injectIntoTemplate, prerender.mjs
build script — omitted here since ICT is on TanStack Start, not plain Vite CSR. Consult this section
only if a future project is a plain Vite React SPA without built-in SSR.)

Key gotcha worth keeping regardless of framework: **env-dependent module-load throws can fail a build
on Vercel** (e.g. a Supabase client that throws if a URL env var is undefined at import time). Any
prerender/SSR step that imports such a module needs a safe fallback value so import-time code never
throws just because an env var isn't visible in that render context.

## Phase 1B — Next.js / SSR-framework branch: hygiene check (usually no rebuild)

Frameworks that SSR by default (Next.js App Router, **TanStack Start**) normally do not have the
empty-shell problem. Verify and fix only what's missing:

- [ ] Phase 0 curl already shows distinct per-route HTML with real content — if so, no rendering work needed
- [ ] Each route sets a UNIQUE title + description + canonical + Open Graph via the framework's
      server-side head/meta API (not injected only client-side)
- [ ] Dynamic routes (product pages, blog posts) render their real content server-side, not just after
      a client-side data fetch
- [ ] `sitemap.xml` and `robots.txt` exist, are current, and reference each other
- [ ] Watch for any component accidentally opting out of server rendering — that pushes rendering
      client-side and can strip SSR'd metadata
- [ ] Structured data (JSON-LD) rendered server-side in the page output, not injected by client JS

## Phase 2 — Shared SEO hygiene (any stack)

- [ ] `robots.txt`: allow public pages, block admin/account/dashboard/API/dev paths, reference the
      absolute sitemap URL
- [ ] `sitemap.xml`: lists all public canonical URLs, generated from the same route/product source as
      the rest of the app so it cannot drift out of sync
- [ ] `llms.txt`: AI-crawler policy + concise accurate business summary — mirror the allow/disallow
      intent of `robots.txt`
- [ ] Canonical tag on every page (absolute URL, self-referencing)
- [ ] Open Graph + Twitter card per page — verify a shared link preview differs per page
- [ ] One `<h1>` per page, meaningful heading hierarchy
- [ ] JSON-LD appropriate to page type (Organization/LocalBusiness on home, Product on product pages,
      BreadcrumbList on inner pages)

## Phase 3 — Verify (evidence before claiming done)

- [ ] Build succeeds; inner routes produce real server-rendered content, not an empty shell
- [ ] Re-run Phase 0 curls against the built/deployed output — two different routes return DIFFERENT
      HTML with DIFFERENT titles, and visible word count is substantial, not ~20
- [ ] Paste an inner URL into a link-preview tool (or share it on WhatsApp) — preview shows that
      page's own title/description/image, not the homepage's
- [ ] Google Search Console → URL Inspection → "View Crawled Page" shows real content, once the site
      is live and verified there
- [ ] No `<title>`/canonical duplicated across distinct pages
