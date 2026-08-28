# AEO/SEO Integration Prompt
For use with Codex / VS Code, Lovable, Replit, or any AI coding assistant when finalizing a client website.

---

## Prompt

```
You are implementing AI/answer-engine optimization (AEO) and SEO fundamentals on this website before launch. Work through the following, in order, and report what you changed at each step.

### 1. Crawler access audit
- Check /robots.txt. Ensure it does NOT block: GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot, PerplexityBot, Google-Extended, Googlebot, Bingbot.
- Confirm /sitemap.xml exists, is current, and is referenced in robots.txt.
- If this is a client-side-rendered app (React/Vite/etc.), verify the initial HTML response contains real content — not an empty <div id="root">. If it's blank, implement SSR, static prerendering, or a prerender fallback (e.g., prerender.io style) for at least all primary marketing/content pages. AI crawlers that don't execute JavaScript must not see a blank page.

### 2. Schema markup (JSON-LD)
Add JSON-LD structured data directly into page templates (not via a plugin). At minimum:
- `Organization` or `LocalBusiness` on every page (name, logo, address, contact, sameAs social links)
- `WebSite` with `SearchAction` on the homepage
- `Product` schema on any product/service pages (name, description, price, availability)
- `FAQPage` schema on any page with an FAQ section
- `Article` / `BlogPosting` on blog or content pages (headline, author, datePublished, image)
- `BreadcrumbList` if the site has nested navigation

Validate every block with the Schema.org Validator and Google's Rich Results Test before considering it done.

### 3. llms.txt
Create /llms.txt at the site root:
- Plain Markdown, UTF-8, no HTML
- Required H1 with the brand/site name
- Optional blockquote with a one-line description of what the business does
- H2 sections linking to the most important pages (homepage, services/products, about, contact, key content), each with a one-line description
- Use absolute URLs only (https://...)
- Keep the file under 5KB
- Do not treat this as a substitute for steps 1 and 2 — it's a low-cost addition, not the core strategy

### 4. Answer-first content structure
On key pages (home, services, FAQ, product pages), restructure content so it's easy for a model to extract and cite:
- Add or tighten an FAQ section using clear question-style headings with direct, declarative one- or two-sentence answers immediately below each
- Convert any buried comparative or spec information into actual HTML tables or lists, not prose paragraphs
- Ensure each page has one clear, unambiguous H1 stating what the page is about
- Front-load the direct answer/value proposition in the first 1-2 sentences of each major section, before elaboration

### 5. Verification
- curl -I on /llms.txt and /sitemap.xml to confirm 200 status, no redirects
- Confirm robots.txt and llms.txt are both reachable and correctly formatted
- List every file created or modified in this pass
```

---

## Notes for your workflow
- Run this as a final pre-launch pass after the core build is done in Lovable/Bolt/Replit and you've moved into VS Code with Codex for refinement — schema and content structure changes are easiest to get right once the page templates are stable.
- This pairs with your existing visibility-skill.md — consider merging or cross-referencing so future projects pull both automatically.
- llms.txt has no confirmed ranking impact from Google, OpenAI, or Anthropic as of mid-2026 — position it to clients as a low-cost forward-looking addition, not a guaranteed AEO win. The real leverage is steps 1, 2, and 4.
