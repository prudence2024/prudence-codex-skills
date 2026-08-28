# 3D Web Operational Playbook

Use this playbook for Three.js, React Three Fiber, Drei, WebGL scenes, or deciding not to use 3D.

## Inputs

- Product goal and why 3D is proposed.
- Existing frontend stack and package constraints.
- Target devices, browsers, performance budget, accessibility needs, and fallback requirements.
- Assets, models, textures, environment maps, and licensing/provenance.

## Procedure

1. Ask whether 3D adds user value: inspection, spatial understanding, product experience, simulation, game interaction, or brand moment.
2. Decide not to use 3D if a static image/video/CSS interaction communicates as well, if essential content would become inaccessible, or if performance budget is too tight.
3. Choose architecture: Three.js imperative scene, React Three Fiber component scene, Drei helpers, or non-3D alternative.
4. Validate package choices with package-intelligence if new dependencies are needed.
5. Define scene structure: canvas ownership, camera, controls, lights, objects, materials, animation loop, resize handling, and cleanup.
6. Optimize assets: file size, texture resolution, compression, lazy loading, and fallback placeholders.
7. Design interactions: pointer, touch, keyboard alternative, hover/focus states, and disabled/reduced-motion states.
8. Add progressive fallback for no WebGL, low-power devices, errors, and reduced motion.
9. Verify runtime: nonblank canvas, correct framing, responsive sizing, interaction, animation, no console errors, and acceptable performance.
10. Capture screenshot or pixel evidence for important scenes.

## Decision Points

- Full-bleed/unframed scenes are appropriate for immersive hero or product scenes.
- Framed canvas is acceptable for editors, dashboards, or contained tools.
- Essential information must exist outside the canvas or have an accessible equivalent.
- Avoid 3D when it would create a decorative loading/performance burden.

## Failure Modes To Break

- Blank canvas due to asset, camera, light, or renderer failure.
- Object clipped on mobile or wide screens.
- Controls unusable on touch devices.
- Render loop continues after unmount.
- Hydration/client-only errors.
- Missing fallback when WebGL fails.
- Unlicensed or oversized assets.

## Verification

```text
VALUE DECISION:
PACKAGE DECISION:
SCENE ARCHITECTURE:
ASSET CHECK:
MOBILE CHECK:
DESKTOP CHECK:
ACCESSIBILITY/FALLBACK:
PERFORMANCE:
SCREENSHOT/PIXEL EVIDENCE:
```

## Related Skills

- package-intelligence for Three.js/R3F/Drei adoption.
- motion-interaction for animation behavior.
- website-generation or design-toolkit for page fit.
- system-breaker for runtime failure testing.
