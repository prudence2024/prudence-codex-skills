# Design Toolkit Reference

This file grows over time - new sources get appended here as they're added, each with a one-line note on what it's for and how to invoke it.

## MCP-Connected Tools

- **shadcn MCP**: Installs registry components into compatible projects. Invoke with `npx shadcn add @registry/name`. Reach for it when a React/Tailwind project needs production-ready primitives, sections, or animated UI blocks.
- **@shadcn registry**: Base shadcn primitives. Invoke through shadcn MCP as `npx shadcn add @shadcn/name`. Reach for it for accessible primitives, app UI foundations, forms, dialogs, menus, tables, and consistent component structure.
- **@aceternity registry**: Aceternity UI motion-heavy components. Invoke through shadcn MCP as `npx shadcn add @aceternity/name`. Reach for it for motion-heavy hero sections, 3D cards, glowing effects, and landing-page spectacle.
- **@magicui registry**: Magic UI animated components. Invoke through shadcn MCP as `npx shadcn add @magicui/name`. Reach for it for micro-interactions, marquees, animated text, and polished motion details.
- **@animate-ui registry**: Animate UI transition primitives. Invoke through shadcn MCP as `npx shadcn add @animate-ui/name`. Reach for it for clean hover states, transitions, and motion primitives inside app UIs.
- **@motion-primitives registry**: Motion Primitives copy-paste motion components. Invoke through shadcn MCP as `npx shadcn add @motion-primitives/name`. Reach for it for general-purpose React motion patterns without inventing animation plumbing.
- **@cult-ui registry**: Cult UI AI-product patterns. Invoke through shadcn MCP as `npx shadcn add @cult-ui/name`. Reach for it for AI SaaS surfaces, chat/productivity flows, and modern product UI patterns.
- **Mobbin MCP**: Pulls real app screens, flows, and UI patterns by app or category. Invoke when available through the configured MCP tool. Reach for it before building app flows, dashboards, onboarding, settings, checkout, booking, or other common product experiences.
- **AIDesigner MCP**: Clones or style-matches a supplied URL into Tailwind UI. Invoke with a user-provided URL such as an mdx.so project page, Uiverse component page, or public site. Reach for it when the user asks for a specific visual style or provides a reference URL.
- **21st.dev Magic MCP**: Generates new UI components from natural language, styled to match the project. Invoke when available through the configured MCP tool. Reach for it when a custom component is needed and no existing local or registry component fits.

## Manual Reference Sites

- **Uiverse.io**: Free copy-paste HTML, CSS, and Tailwind UI elements such as buttons, loaders, checkboxes, and cards. Browse or copy by hand, or use AIDesigner cloning when appropriate. Reach for it for small standalone interaction ideas.
- **ReactBits**: Animated React components, text effects, and backgrounds. Browse and adapt manually. Reach for it when a React project needs a memorable animated detail, text treatment, or background effect.
- **Codrops**: Tutorials on original interaction patterns. Browse and adapt manually. Reach for it to avoid generic AI-site visuals and to learn distinctive interaction patterns.

## MDX Studio Aesthetic Reference

Treat these as a technique library inspired by source-verified MDX client-site patterns from prevvi.com, eatnaked.co, ai-robots.apps.mdxpreview.xyz, uptown.ae, arturos.com.ve, towerdoors.com.au, and fedorgorst.com. Adapt them to the brand and content; do not use them as a fixed template.

- **Percentage-counter preloader**: A load sequence counting from 0% to 100%. Invoke as a custom loader component. Reach for it when the site benefits from a cinematic reveal or high-production first impression.
- **Ambient background audio**: Optional sensory layer. Invoke only with explicit user intent and visible controls. Reach for it for immersive brand-forward or experiential sites.
- **Astro View Transitions API**: Native page transitions in Astro projects. Invoke with Astro's view-transition support. Reach for it when the project is Astro and page-to-page continuity matters.
- **Multi-row infinite marquees**: Seamless looping rows using duplicated DOM content. Invoke with CSS animation or a motion library. Reach for it for text bands, logo grids, testimonials, press strips, or partner walls.
- **Embedded content video**: Real video placed inside content sections, not only hero backgrounds. Invoke with video elements or embeds. Reach for it when video explains product, process, venue, food, hospitality, robotics, or craft.
- **Floating/parallax decorative clusters**: Layered elements positioned around primary CTAs. Invoke with CSS transforms, scroll transforms, or Motion/GSAP. Reach for it when brand assets or product motifs can frame action areas.
- **Sequential feature storytelling**: Step-by-step sections connected by visual lines. Invoke with structured content blocks and connecting line elements. Reach for it for processes, itineraries, timelines, setup flows, or service journeys.
- **Animated stepped stat counters**: Step reveals such as `1/3` to `2/3` to `3/3`. Invoke with stateful counters or timeline animation. Reach for it when statistics should feel progressive rather than static.
- **Expandable explain-more cards**: Progressive disclosure cards for extra detail. Invoke with accordion, disclosure, or expandable card components. Reach for it when details matter but should not overload the first scan.
- **Consistent hero scroll cue**: Text prompt, icon, or animated mouse indicator. Invoke as a small hero affordance. Reach for it when the first viewport needs a clear cue that more content follows.
- **Interactive mascot/chatbot widget**: Character or helper widget for brand-forward consumer sites. Invoke with a floating widget or stateful interaction. Reach for it when the brand supports a playful guide or assistant.
- **Before/after or comparison cards**: Interactive comparison for naturally paired content. Invoke with slider, toggle, or two-state card. Reach for it for transformations, upgrades, recipes, interiors, performance, or service outcomes.

## Animation Libraries

- **Motion**: React animation and gesture library formerly known as Framer Motion. Invoke by adding Motion to compatible React projects. Reach for it for general-purpose component animation, gestures, presence transitions, and UI feedback.
- **GSAP**: Timeline and scroll-trigger animation library. Invoke by adding GSAP and ScrollTrigger where appropriate. Reach for it for choreographed sequences, scroll-driven storytelling, and precise timelines.
- **Rive**: Interactive vector animation with state machines. Invoke with Rive runtime and `.riv` assets. Reach for it for mascots, icons, loaders, and interactive brand animation.
- **Lottie / LottieFiles**: Lightweight JSON playback for After Effects exports. Invoke with a Lottie player and JSON asset. Reach for it when the animation is already available as Lottie JSON or needs simple playback.
- **Spline**: Embeddable 3D scenes and objects. Invoke with Spline embed/runtime when appropriate. Reach for it for mdx.so-style interactive 3D hero or product visuals.

## Design QA

- **DesignMeter.ai**: External design scoring workflow. After building, describe the page back to the user with layout, palette, typography, and signature element so the user can screenshot it and run it through DesignMeter.ai. If the score is low, revisit spacing, hierarchy, contrast, and visual weight before calling the design done.

## Not Currently Included

- **UI UX Pro Max**: Design-intelligence tool with style, palette, font-pairing database and search script. Leave it out for now because of reported billing or subscription issues on the paid tier. Flag this if the user asks about it again.
- **Higgsfield**: AI cinematic video generator for promotional video content, not a code-level component or UI animation tool. Keep it separate from the component and animation toolkit.
