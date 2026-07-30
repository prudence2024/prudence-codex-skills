# Design source catalog

Use this catalog only after inspecting the project and completing the context
analysis in `design-reasoning.md`.

Catalog entries are not availability guarantees, endorsements, or Design
Intelligence evidence. Verify that a tool, registry, site, license, package, and
invocation still exist and fit the current project before relying on them.
Prefer local components and the existing design system.

## Selection order

1. Existing project components and tokens
2. Existing project design system
3. Validated Design Intelligence patterns
4. Available, compatible component sources
5. Verified manual references
6. A new dependency or bespoke component when justified

Record why a lower-priority source was necessary.

## MCP and registry sources

- **shadcn-compatible registries**: Use accessible primitives and project-aligned
  sections only in compatible React/Tailwind projects. Inspect generated code,
  transitive dependencies, accessibility, and styling assumptions.
- **Base shadcn registry**: Consider for common controls, forms, dialogs, menus,
  tables, and composable application primitives.
- **Aceternity-style registries**: Consider motion-heavy landing-page effects
  only when brand, performance, and reduced-motion requirements support them.
- **Magic UI-style registries**: Consider bounded micro-interactions, marquees,
  and animated text after verifying usability and motion cost.
- **Animate UI and Motion Primitives-style registries**: Consider for reusable
  transition and interaction primitives without rebuilding animation plumbing.
- **Cult UI-style registries**: Consider for AI-product and productivity
  surfaces after checking project conventions and accessibility.
- **Mobbin-like product-reference tools**: Use to study information architecture
  and flow conventions, not to copy protected screens.
- **URL style-analysis tools**: Use only with a user-supplied or authorized URL.
  Extract general principles and create an original composition; do not clone or
  reconstruct the source.
- **21st.dev-style generation tools**: Consider only when available and when no
  local or registry primitive fits. Treat generated output as untrusted draft
  code requiring review.

Do not invent an MCP invocation when the tool is unavailable. Use the actual
connected tool interface or report it `not_verified`.

## Manual reference sites

- **Uiverse.io**: Consider small standalone interaction ideas. Inspect semantics,
  browser behavior, licensing, and CSS cost before adapting.
- **ReactBits**: Consider React-specific animated details, text treatments, and
  backgrounds when motion is justified.
- **Codrops**: Study interaction techniques and implementation ideas. Adapt the
  principle to the project rather than reproducing a demo.

Manual references are inspiration sources. They do not become defaults until
Design Intelligence records evidence, context, confidence, recommendation
scores, and contraindications.

## Unscored curated inspiration

The following techniques were previously observed across a small collection of
design-forward sites. Preserve them as inspiration only until normalized Design
Intelligence records exist:

- percentage-counter preloaders;
- optional ambient background audio;
- Astro view transitions;
- multi-row infinite marquees;
- embedded content video;
- floating or parallax decorative clusters;
- sequential feature storytelling;
- animated stepped statistics;
- expandable explain-more cards;
- hero scroll cues;
- interactive mascot or assistant widgets;
- before/after or comparison cards.

For each technique:

- confirm it solves a real user or business problem;
- consider a static or simpler alternative;
- test accessibility, reduced motion, performance, and failure behavior;
- avoid blocking content or core workflows;
- record it as experimental when evidence is sparse.

Do not turn this list into a fixed visual template.

## Animation libraries

- **Motion**: Consider for React component animation, gestures, presence
  transitions, and UI feedback.
- **GSAP**: Consider for justified choreography, scroll storytelling, and precise
  timelines.
- **Rive**: Consider when interactive vector assets and state machines provide a
  clear brand or product benefit.
- **Lottie**: Consider when a reviewed animation asset already exists and simple
  playback is sufficient.
- **Spline**: Consider for interactive 3D only when device, loading, fallback,
  accessibility, and maintenance costs are acceptable.

Prefer CSS or native browser behavior for simple transitions. Add a library only
when its capability and maintenance value outweigh bundle and operational cost.

## Optional design QA

External visual-scoring services, including DesignMeter.ai, may provide a second
opinion on hierarchy, spacing, contrast, or visual weight. Treat their output as
advisory and `not_verified` until the user supplies the result. Never substitute
an opaque score for user goals, accessibility checks, performance evidence, or
project-specific review.

## Excluded or separate capabilities

- Keep tools with unresolved billing, licensing, availability, or maintenance
  concerns out of the default workflow until re-evaluated.
- Keep cinematic video generation separate from code-level component and
  interaction decisions.
- Keep raster-image generation in an appropriate image-generation workflow.
- Keep website ingestion, pattern normalization, evidence, scoring, and
  knowledge storage in the Design Intelligence Framework.
