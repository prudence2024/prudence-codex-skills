# Visibility Skill

A reusable skill for making any web project actually findable and correctly
represented — by search engines, by AI crawlers/assistants, and by link previews
(WhatsApp/social shares). Paste this into any project (as `VISIBILITY-SKILL.md`,
or fold into `AGENTS.md`/`.cursorrules`) alongside the two reference documents
`reference-seo-how-to.md` and `reference-seo-crawlability-playbook.md` — this file
is the scoped checklist to execute; those two are the background/full code.

Fill in `[BUSINESS NAME]`, `[DOMAIN]`, `[CITY]`, `[SERVICE/PRODUCT TYPE]` etc. per
project — everything else in this file applies unchanged.

---

## Step 0 — Identify the stack first (this changes what applies)

Before doing anything else, determine which category the project falls into:

- **A) SSR-by-default framework** (Next.js App Router, TanStack Start, Remix,
  SvelteKit, Nuxt) — the "empty shell" crawlability problem in the reference
  playbook usually does not apply. Treat everything below as a **hygiene check**:
  verify it's actually working correctly, don't assume a rebuild is needed.
- **B) Client-rendered SPA with no SSR** (plain Vite + React/Vue with no
  prerendering step) — the empty-shell problem is real here. Follow Phase 1A of
  `reference-seo-crawlability-playbook.md` (build-time prerendering) before the
  rest of this checklist will actually matter — an unindexed/undifferentiated page
  can't be helped by good meta tags if the crawler never sees real content in the
  first place.
- **C) Static site generator** (Astro, Hugo, plain static export) — already
  produces real per-route HTML by nature. Skip straight to the hygiene items below.

Confirm with the Phase 0 diagnostic curl commands in the playbook — don't guess
based on the framework name alone; verify.

---

## 1. Schema.org structured data

Pick the schema type that matches the actual business, don't default to generic
`Organization` if a more specific type fits:
- Physical/local business (shop, restaurant, clinic, etc.) → `LocalBusiness` or a
  more specific subtype (`Store`, `Restaurant`, `ElectronicsStore`, etc.) with a real
  `PostalAddress`
- E-commerce product → `Product` schema on every product page (name, image,
  description, `offers` with price/currency/availability)
- Content/blog → `Article` schema per post
- SaaS/service business with no physical location → `Organization`, omit the
  address fields

Pull values from live data (the actual product/content database), never hardcode —
hardcoded structured data drifts from reality the first time a price or listing
changes. See `reference-seo-how-to.md` §2 for full JSON-LD templates.

## 2. llms.txt — tell AI assistants about the business

One per project, at `/public/llms.txt` (or the framework's equivalent public root).
Write it for a model summarizing the business to a user — factual, no marketing
fluff. Template:

```txt
# [BUSINESS NAME] — AI Guidelines
> One-line summary of what the site is and who it's for.

## About
A short, factual paragraph: what the business does, who runs it, what makes it
genuinely useful. Written for a model that will summarize this to a user.

## Key Pages
- / — Homepage
- /about — About
- /contact — Contact
[Add every genuinely public page type — product listings, service pages, blog, etc.]

## Key Facts
- What's offered, pricing model if relevant, who it's for
- Location, if a physical/local business
- Anything the business specifically wants an AI assistant to state accurately

## Contact
- Website: https://[DOMAIN]/contact
```

Mirror the allow/disallow intent of `robots.txt` so the two files never contradict
each other.

## 3. Markdown mirrors — clean AI-readable page content

For key pages (home, main listing/catalog pages, individual product/service/article
pages, about, contact), serve a plain-text/markdown version alongside the HTML page
— e.g. `/products/[slug].md` returning just the name, price/details, and description
as clean markdown, no nav/header/footer/scripts. This lets an AI assistant or a
crawler with no JS/CSS rendering read the actual content directly. Cheap to build:
it's the same data already powering the real page, output as text instead of
markup.

## 4. sitemap.xml — dynamic, generated from real data

Never hand-write this for any project with more than a handful of static pages —
generate it from the live data source (CMS, database, content collection) at build
time or via a route that queries it directly, so every real page is included and it
cannot silently drift out of date. Format reference: `reference-seo-how-to.md` §5.

## 5. robots.txt

Allow public routes, block admin/account/dashboard/API/dev paths, reference the
absolute sitemap URL. Template: `reference-seo-how-to.md` §4 — adapt the specific
allowed/blocked paths to the actual project's route structure, don't ship the
generic example paths unchanged.

## 6. IndexNow — instant search engine notification

Bing, Yandex, and other IndexNow-participating engines support near-instant crawl
requests instead of waiting for their next scheduled crawl:
- Generate an IndexNow API key (a random string), host it at `/[key].txt`
  containing just the key
- On every content create/update/publish, call:
  `https://api.indexnow.org/indexnow?url=[changed-url]&key=[key]&keyLocation=https://[DOMAIN]/[key].txt`
- Wire this into the actual publish/save action server-side — not a manual step for
  whoever owns the content, it should fire automatically

Most valuable for any project where content/inventory/pricing changes frequently —
less critical for a mostly-static marketing site that rarely updates.

## 7. Page load speed

**Core Web Vitals must pass** — LCP < 2.5s, INP < 200ms, CLS < 0.1 — since Google
uses these as a ranking signal, not just a UX nicety. Verify with PageSpeed
Insights/Lighthouse after major feature additions, not only once at the end.
Standard techniques: lazy-loaded images below the fold, code-split routes,
compressed/responsive images, CDN, browser caching.

## 8. Open Graph tags — title, image, description, per page

Every page needs its own `og:title`, `og:description`, and `og:image` — this is
what makes a WhatsApp/social share of a specific page show that page's own content,
not a generic homepage logo. Use the SEO component pattern in
`reference-seo-how-to.md` §3, adapted to the actual framework's head/meta API.

## 9. Page titles — locally relevant, not just keyword-stuffed

Pick the pattern based on the business type — don't force a local-SEO pattern onto
a business with no physical location, and don't skip it for one that has one:

- **Local/physical business:** `{Item/Service} in {City} | {Business Name}` —
  e.g. `Laptops in Ikeja, Lagos | ICT Integrated Solutions`. This is what surfaces
  the business for "[service] near me"-style searches, not just generic
  product-name searches where it competes nationally/globally.
- **Non-local business (SaaS, national/global brand, content site):**
  `{Item/Topic} | {Business Name}` — no city, keyword-focused.

Every page needs a unique title following whichever pattern applies — not just the
homepage.

## 10. Server-side rendering — verify, don't assume

A framework supporting SSR isn't the same as every page actually using it
correctly. Confirm per the Step 0 stack category: no route accidentally opts into
client-only rendering, dynamic content renders in the initial server response, not
only after a client-side fetch completes.

## 11. Self-verification — act as a search engine crawler

Verify like a crawler would, not just visually in a browser:

```bash
SITE="[actual domain once live, or localhost during dev]"
curl -s -A "Googlebot/2.1 (+http://www.google.com/bot.html)" "$SITE/[a real inner page]" > /tmp/inner.html
curl -s -A "Googlebot/2.1 (+http://www.google.com/bot.html)" "$SITE/" > /tmp/home.html

# Two different pages must return different titles and real content, not an empty shell
grep -o '<title>[^<]*</title>' /tmp/home.html /tmp/inner.html
sed 's/<[^>]*>//g' /tmp/inner.html | tr -s ' \n' ' ' | wc -w
```

If titles are identical across pages, or word count is near-zero, something is
rendering client-only when it shouldn't be — go back to item 10 before continuing.

## 12. Ranking checklist — run through before calling this done

- [ ] Structured data validates with no errors (Google's Rich Results Test)
- [ ] `sitemap.xml` and `robots.txt` reference each other and are both reachable
- [ ] `llms.txt` reflects real, current business information — no placeholder text
      left in
- [ ] Every page has a unique title following the correct pattern for the business
      type (item 9)
- [ ] Every page has unique OG title/description/image — verified with an actual
      link share preview test, not just a code read-through
- [ ] IndexNow fires automatically on publish, if implemented — verified with a
      real test publish
- [ ] Core Web Vitals pass on a representative content page and a listing/index page
- [ ] Self-verification curl test (item 11) shows distinct, real content per page
- [ ] Once live: submit the site in Google Search Console and Bing Webmaster Tools
      — a manual, one-time owner action, not something an AI coding tool can do

---

*Once the domain is live and Search Console/Bing Webmaster Tools are set up, this
becomes an ongoing-monitoring skill rather than a one-time build — see
`reference-seo-how-to.md` §"Monitoring and Tools" for the recurring workflow.*
