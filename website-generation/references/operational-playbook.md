# Website Generation Operational Playbook

Use this playbook to build or audit a website from a brief, references, or existing implementation. Do not use it to build an autonomous website generator.

## Inputs

- User brief, audience, business goal, content, brand constraints, and required workflows.
- Authorized references, screenshots, existing site/app code, assets, and design system.
- Framework, hosting, accessibility, performance, SEO, and deployment constraints.

## Procedure

1. Clarify the primary user jobs and the first screen. Build the actual useful experience, not a marketing shell, unless a landing page is explicitly requested.
2. Analyze references by decomposing principles: information hierarchy, layout rhythm, interaction patterns, density, typography scale, spacing, color roles, and content strategy.
3. Respect authorization. Extract reusable principles; do not clone protected expression, proprietary assets, copy, or exact layout unless the user owns or is authorized to recreate them.
4. Define information architecture: routes, sections, navigation, content hierarchy, and repeated item types.
5. Define design system choices: tokens, components, states, icons, images/media, responsiveness, and accessibility requirements.
6. Implement using existing project patterns and components before inventing new abstractions.
7. Verify responsive behavior on mobile, tablet, desktop, and wide desktop. Text must not overflow or overlap.
8. Verify accessibility: semantic controls, labels, focus, keyboard navigation, contrast, reduced motion, and alt text.
9. Perform visual QA with screenshots when possible. Check layout, spacing, image rendering, canvas/media, and state changes.
10. Check performance: payload, images, lazy loading, layout shift, animation cost, and critical route speed.
11. Invoke system-breaker for significant launch, production, payment, auth, admin, or safety claims.
12. Report final evidence and untested areas.

## Decision Points

- Use real or generated visual assets for websites/games/tools where visuals are part of the experience.
- Use website-specific visual language; do not apply one generic card-heavy landing pattern everywhere.
- Hand off SEO/discoverability to visibility, production readiness to post-production/security, and package adoption to package-intelligence.
- Do not add broad CMS/generator architecture unless explicitly requested.

## Failure Modes To Break

- Reference copied too literally without authorization.
- First screen fails to show the actual product/place/person/tool.
- Mobile text overflow, clipped controls, or overlapping content.
- Decorative visuals hide missing functionality.
- Accessibility and reduced-motion ignored.
- Performance harmed by oversized media or animation.
- Claims of visual quality without runtime/screenshot evidence.

## Verification

```text
BRIEF SUMMARY:
REFERENCE PRINCIPLES:
AUTHORIZATION BOUNDARY:
INFORMATION ARCHITECTURE:
COMPONENTS:
RESPONSIVE QA:
ACCESSIBILITY QA:
VISUAL QA:
PERFORMANCE QA:
SYSTEM BREAKER CHECKS:
EVIDENCE:
```

## Related Skills

- design-toolkit for design system and UI quality.
- motion-interaction for purposeful animation.
- three-d-web for 3D scenes.
- visibility for SEO and AI discoverability.
- security/post-production for launch readiness.
- system-breaker for adversarial verification.
