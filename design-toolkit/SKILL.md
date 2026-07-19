---
name: design-toolkit
description: Frontend design, implementation, and animation toolkit for polished web apps, landing pages, dashboards, and interactive UI. Use when Codex needs to choose component libraries or design references, plan responsive and accessible components, improve forms and frontend performance, select animation techniques, or run post-build UI quality checks.
---

# Design Toolkit

Use this skill to decide where to pull frontend UI patterns, components, references, and animation techniques from before building. Treat it as the sourcing layer: it says what tools and references to reach for. Pair it with any existing `frontend-design.md` or project design instructions for how to think through layout, audience, hierarchy, brand, accessibility, and implementation quality.

## Workflow

1. Read `references/toolkit.md` when the task involves frontend UI sourcing, animation choices, landing-page polish, component inspiration, or a request for a more premium visual feel.
2. Read `references/frontend-foundations.md` when building or auditing components, responsive behavior, accessibility, forms, browser behavior, or frontend performance.
3. Inspect the existing project stack and design system before invoking new libraries or copying patterns.
4. Choose the smallest useful source: prefer existing project components first, then MCP-connected tools, then manual reference sites, then animation libraries.
5. Adapt references to the project's content, brand, and audience. Do not copy every technique into every page.
6. Verify the result at representative phone, tablet, and desktop sizes and with keyboard navigation. Include evidence for any quality claim.
7. After implementation, describe the resulting layout, palette, typography, and signature interaction so the user can run a screenshot through DesignMeter.ai if they want objective design QA.

## Guardrails

- Do not add paid, unavailable, or unconfigured MCP dependencies without checking local availability.
- Use shadcn-style registry components when they fit the existing stack; avoid forcing them into non-React or non-Tailwind projects.
- Use Mobbin or manual references to inform UX structure, not to clone protected product screens wholesale.
- Use AIDesigner-style cloning only when the user supplies a URL or explicitly wants style matching.
- Keep animation purposeful: support hierarchy, feedback, pacing, storytelling, or brand feel.
- Respect performance and accessibility. Avoid motion that blocks content, breaks reduced-motion expectations, or hides core workflows.
- Treat generated UI as a first draft. Check real behavior, error states, and device layouts before calling it complete.

## Reference

- `references/toolkit.md`: itemized MCP tools, manual reference sites, MDX studio patterns, animation libraries, design QA, and excluded tools.
- `references/frontend-foundations.md`: component structure, responsive and accessibility checks, form resilience, browser diagnostics, and frontend performance verification.
