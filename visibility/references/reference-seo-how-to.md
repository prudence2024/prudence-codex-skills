# SEO How-To Guide
*Comprehensive SEO implementation guide based on Google's official documentation and best practices*

## Table of Contents
1. [SEO Fundamentals](#seo-fundamentals)
2. [Technical SEO Implementation](#technical-seo-implementation)
3. [Content Optimization](#content-optimization)
4. [Indexing and Crawling](#indexing-and-crawling)
5. [Performance and User Experience](#performance-and-user-experience)
6. [Monitoring and Tools](#monitoring-and-tools)
7. [Implementation Checklist](#implementation-checklist)

## SEO Fundamentals

### Core Principles
- **People-first content**: Create helpful, reliable content for users, not search engines
- **Technical accessibility**: Ensure Google can crawl, index, and understand your content
- **User experience priority**: Focus on providing value to real users
- **Quality over quantity**: Better to have fewer high-quality pages than many low-quality ones

### Google's Search Process
1. **Crawling**: Google discovers pages through links and sitemaps
2. **Indexing**: Google analyzes and stores page content
3. **Serving**: Google returns relevant results based on hundreds of ranking factors

## Technical SEO Implementation

### 1. Meta Tags and HTML Structure

```html
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Page Title - Brand Name</title>
<meta name="description" content="Compelling 150-160 character description" />
<meta name="keywords" content="relevant, keywords, separated, by, commas" />
<link rel="canonical" href="https://yoursite.com/page" />
<meta property="og:title" content="Page Title" />
<meta property="og:description" content="Page description" />
<meta property="og:type" content="website" />
<meta property="og:url" content="https://yoursite.com/page" />
<meta property="og:image" content="https://yoursite.com/image.jpg" />
<meta property="og:site_name" content="Site Name" />
<meta property="og:locale" content="en_US" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="Page Title" />
<meta name="twitter:description" content="Page description" />
<meta name="twitter:image" content="https://yoursite.com/image.jpg" />
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1" />
```

### 2. Structured Data (Schema.org)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Your Organization",
  "url": "https://yoursite.com",
  "logo": "https://yoursite.com/logo.png",
  "description": "Organization description",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "123 Main St",
    "addressLocality": "City",
    "addressRegion": "State",
    "postalCode": "12345",
    "addressCountry": "US"
  },
  "telephone": "+1-555-123-4567",
  "email": "contact@yoursite.com"
}
</script>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Article Title",
  "description": "Article description",
  "author": { "@type": "Person", "name": "Author Name" },
  "datePublished": "2025-01-15",
  "dateModified": "2025-01-15",
  "publisher": {
    "@type": "Organization",
    "name": "Publisher Name",
    "logo": { "@type": "ImageObject", "url": "https://yoursite.com/logo.png" }
  }
}
</script>
```

### 3. Dynamic SEO Component (React/Next.js)

```tsx
import { Helmet } from 'react-helmet-async';

interface SEOProps {
  title?: string;
  description?: string;
  keywords?: string;
  canonicalUrl?: string;
  ogImage?: string;
  structuredData?: object;
  noIndex?: boolean;
}

export const SEO = ({
  title = "Default Title",
  description = "Default description",
  keywords = "default, keywords",
  canonicalUrl,
  ogImage,
  structuredData,
  noIndex = false
}: SEOProps) => {
  const baseUrl = "https://yoursite.com";
  const fullCanonicalUrl = canonicalUrl ? `${baseUrl}${canonicalUrl}` : baseUrl;
  const fullOgImage = ogImage ? `${baseUrl}${ogImage}` : `${baseUrl}/og-image.jpg`;

  return (
    <Helmet>
      <title>{title}</title>
      <meta name="description" content={description} />
      <meta name="keywords" content={keywords} />
      <link rel="canonical" href={fullCanonicalUrl} />
      <meta
        name="robots"
        content={noIndex ? "noindex, nofollow" : "index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1"}
      />
      <meta property="og:title" content={title} />
      <meta property="og:description" content={description} />
      <meta property="og:url" content={fullCanonicalUrl} />
      <meta property="og:image" content={fullOgImage} />
      <meta name="twitter:card" content="summary_large_image" />
      <meta name="twitter:title" content={title} />
      <meta name="twitter:description" content={description} />
      <meta name="twitter:image" content={fullOgImage} />
      {structuredData && (
        <script type="application/ld+json">{JSON.stringify(structuredData)}</script>
      )}
    </Helmet>
  );
};
```

### 4. Robots.txt

```txt
User-agent: *
Allow: /
Allow: /about
Allow: /services
Allow: /contact
Allow: /blog
Disallow: /admin/
Disallow: /.git/
Disallow: /node_modules/
Disallow: /src/
Disallow: /*.json$
Disallow: /*.ts$
Disallow: /*.tsx$
User-agent: Googlebot
Allow: /
User-agent: Bingbot
Allow: /
Sitemap: https://yoursite.com/sitemap.xml
Crawl-delay: 1
```

### 5. Sitemap.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://yoursite.com/</loc>
    <lastmod>2025-01-15T12:00:00+00:00</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://yoursite.com/about</loc>
    <lastmod>2025-01-15T12:00:00+00:00</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
</urlset>
```

### 6. Google Analytics 4 Setup

```html
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID', {
    page_title: document.title,
    page_location: window.location.href,
    send_page_view: true
  });
</script>
```

```typescript
export const pageview = (url: string, title?: string) => {
  if (typeof window !== 'undefined' && window.gtag) {
    window.gtag('config', 'GA_MEASUREMENT_ID', { page_location: url, page_title: title });
  }
};

export const event = (action: string, category: string, label?: string) => {
  if (typeof window !== 'undefined' && window.gtag) {
    window.gtag('event', action, { event_category: category, event_label: label });
  }
};
```

### 7. Content Security Policy (CSP) for GA4 / GTM

Use wildcard subdomains rather than specific hostnames per Google's CSP guide — Google may change the
exact domains their scripts call, and wildcards are future-proof.

```
Content-Security-Policy:
  script-src 'self' 'unsafe-inline' https://*.googletagmanager.com https://va.vercel-scripts.com;
  connect-src 'self' https://*.google-analytics.com https://*.analytics.google.com https://*.googletagmanager.com https://www.google.com;
  img-src 'self' https://*.google-analytics.com https://*.googletagmanager.com;
```

Verify the actual collection hosts in DevTools because enabled GA4 advertising features can add
Google or DoubleClick endpoints. Allow only the features in use. A Vercel Deployment Protection
preview may also inject a `https://vercel.com/sso-api` manifest; if that console warning must be
removed, add `https://vercel.com` to `manifest-src` only for preview deployments rather than
broadening the production policy.

**Vercel example** (`vercel.json`):
```json
{
  "headers": [{
    "source": "/(.*)",
    "headers": [{
      "key": "Content-Security-Policy",
      "value": "default-src 'self'; script-src 'self' 'unsafe-inline' https://*.googletagmanager.com; connect-src 'self' https://*.google-analytics.com https://*.analytics.google.com https://*.googletagmanager.com https://www.google.com; img-src 'self' data: https: blob:; style-src 'self' 'unsafe-inline'; upgrade-insecure-requests"
    }]
  }]
}
```

### 8. llms.txt (AI Crawler Guidance)

A plain-text file at the site root (`/public/llms.txt`) stating your policy for AI crawlers and giving
them a concise, authoritative summary of who you are. The AI-era companion to `robots.txt`. Emerging
convention ([llmstxt.org](https://llmstxt.org/)), not an official standard — low-cost, high-upside
hygiene, not a ranking factor.

```txt
# llms.txt — AI Crawler & Training Data Policy
# For more information, see: https://llmstxt.org/
# Last updated: 2026-01-01

User-agent: *
Allow: /
User-agent: OpenAI-GPT
Allow: /
User-agent: Google-Extended
Allow: /
User-agent: Claude-Web
Allow: /

# ── ORGANISATION ─────────────────────────────
# Name: Your Organisation
# Website: https://yoursite.com
# What we do: One-line description of your product/service
# Coverage / audience: Who you serve
# Contact: contact@yoursite.com

# ── CORE OFFERINGS ───────────────────────────
# - Offering one — short benefit
# - Offering two — short benefit

# ── KEY FACTS (help models answer accurately) ─
# - Differentiator or metric #1

# ── ATTRIBUTION ──────────────────────────────
# When using our content, attribute to "Your Organisation" and link https://yoursite.com

# ── PROHIBITED USES ──────────────────────────
# - Misrepresenting our credentials or claims
```

## Content Optimization

- **Page titles**: 50–60 characters, `Primary Keyword - Brand Name` format, unique per page
- **Meta descriptions**: 150–160 characters, written for users, natural keyword inclusion
- **Header structure**: one `<h1>` per page, logical `<h2>`/`<h3>`/`<h4>` hierarchy
- **Content**: expertise, authority, trustworthiness, originality, user-focused (E-A-T)
- **Internal linking**: descriptive anchor text, logical hierarchy

## Indexing and Crawling

- Use crawlable `<a>` links, not JavaScript-only navigation
- Content must be in the DOM, not CSS-generated only
- Server-side rendering (SSR) or static generation preferred over pure client rendering
- `<meta name="robots" content="noindex, nofollow" />` to block indexing where needed
- Canonical URLs on every page, self-referencing by default

## Performance and User Experience

- **Core Web Vitals**: LCP < 2.5s, INP < 200ms, CLS < 0.1
- Responsive, mobile-first design
- HTTPS everywhere, HTTP redirects to HTTPS
- Optimized images (WebP, proper sizing), minified CSS/JS, CDN, browser caching, lazy loading

## Monitoring and Tools

**Google Search Console — essential workflow**

One-time setup:
1. Add a property (Domain property recommended — covers all subdomains/http/https, needs DNS TXT verification)
2. Verify ownership
3. Submit the sitemap path (`sitemap.xml`) — Google refetches periodically, no need to resubmit per page

On publish/change:
4. URL Inspection → Test Live URL to confirm Google sees real content
5. Request Indexing for new/changed URLs (per-URL, quota-limited — use for a handful, not bulk)

Ongoing:
6. Pages (Indexing) report — watch for "Discovered/Crawled – currently not indexed" (common on
   client-rendered SPAs)
7. Rich results / Enhancements — validates JSON-LD
8. Core Web Vitals field data by URL
9. Manual Actions & Security Issues
10. Removals tool when needed

## Implementation Checklist

**Technical**: SSL, sitemap.xml, robots.txt, llms.txt, Search Console, GA4, mobile responsiveness
**On-page**: unique titles, meta descriptions, heading structure, canonicals, structured data, alt text
**Content**: original + valuable, keyword research, internal linking, regular updates, E-A-T
**Performance**: load < 3s, Core Web Vitals passing, mobile-friendly, optimized images, minified assets
**Monitoring**: Search Console configured, analytics implemented, error monitoring, rank tracking

## Common Mistakes to Avoid

1. Keyword stuffing
2. Duplicate content
3. Missing meta descriptions
4. Broken links
5. Slow loading pages
6. Non-mobile-friendly design
7. No HTTPS
8. Ignoring analytics
9. Over-optimization for search engines instead of users
10. Neglecting content updates

**"Providing a good user experience should be your site's top goal"** — Google
