# Frontend foundations reference

Use this checklist after choosing the visual direction and again after
implementation. Report every relevant item as `pass`, `fail`, `partial`,
`not_applicable`, or `not_verified`, with a file, screen, browser observation, or
test result.

## Structure, maintainability, and consistency

- Split repeated or independently testable UI into focused components instead of
  generating an entire page as one block.
- Follow the project's folder structure and naming conventions; introduce a new
  convention only when the current one is genuinely missing.
- Reuse shared tokens and primitives for color, typography, spacing, controls,
  and states.
- Explain intentional exceptions to the design system and keep them bounded.
- Prefer the simplest state and component model that supports the required
  behavior.
- Keep server-only work and secrets out of browser bundles. Load only the client
  code needed for the current route or interaction.
- Record new dependencies, ownership, upgrade cost, and why existing primitives
  were insufficient.

## Responsive and device verification

- Check representative phone, tablet, and desktop widths, including a narrow
  phone near 375px.
- Verify wrapping, overflow, touch-target size, sticky/fixed elements, menus,
  dialogs, tables, and orientation changes.
- Use browser emulation for quick iteration, then test critical flows on at least
  one real phone when available.
- Do not claim mobile readiness from a desktop screenshot alone.

## Accessibility

- Use buttons for actions, links for navigation, ordered heading structure,
  useful image alternatives, and associated form labels.
- Traverse the full critical flow with a keyboard. Confirm visible focus, logical
  order, usable dialogs, and no keyboard traps.
- Check text and control contrast, zoom/reflow, touch targets, and reduced-motion
  behavior where relevant.
- Verify errors are announced or associated with affected fields and do not
  depend on color alone.
- Prefer native semantics. Add ARIA only when it expresses behavior native HTML
  cannot provide.

## Forms and failure states

- Test empty, invalid, unusually long, and special-character input.
- Show specific errors, focus the first invalid field when appropriate, and
  preserve safe input after a rejected or failed submission.
- Provide bounded loading, success, empty, offline, timeout, and retry states;
  never leave an indefinite spinner as the only response.
- Prevent repeated clicks or delayed responses from creating duplicate actions.
- Keep conversion interactions clear and voluntary; do not use misleading
  hierarchy, obstructive consent, or hidden costs.

## Frontend performance

- Serve responsive images at appropriate dimensions and prefer modern formats
  such as WebP or AVIF.
- Lazy-load below-the-fold media, but do not lazy-load the likely largest
  above-the-fold element.
- Verify static assets use durable cache headers plus content-hashed filenames
  or another cache-busting mechanism.
- Load fonts without blocking rendering where possible, for example with preload
  where justified and `font-display: swap`.
- Check route-level code splitting and remove avoidable client-side work or
  oversized dependencies.
- Inspect bundle composition, unused JavaScript/CSS, dead exports, hydration
  cost, long tasks, tree shaking, continuous animation, and avoidable third-party
  execution before adding micro-optimizations.
- Use Lighthouse and the browser Network and Performance panels as evidence.
  Prioritize real bottlenecks rather than chasing a score in isolation.

## Progressive enhancement

- Keep critical information and navigation readable when JavaScript, animation,
  web fonts, media, analytics, or a third-party dependency fails.
- Prefer real links, buttons, labels, and native form behavior as the baseline,
  then enhance with client-side interaction.
- Do not let preloaders, reveal animations, carousels, or hydration hide initial
  content from users, assistive technology, or performance tooling.
- Verify that failure of a non-essential integration does not block the primary
  page or form workflow.

## Browser diagnostics

- Inspect console errors and warnings, failed requests, response status codes,
  payload size, caching behavior, and mixed content.
- Trace at least one critical user action from the interface through its network
  request and visible result.
- Distinguish application defects from preview-provider or browser-extension
  injection.
- End the review with the three highest-impact fixes, ordered by user harm,
  business impact, and effort.
