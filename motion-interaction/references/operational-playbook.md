# Motion Interaction Operational Playbook

Use this playbook when adding, reviewing, or debugging web motion.

## Inputs

- User goal and interface workflow.
- Existing design system, component framework, CSS, and motion libraries.
- Target devices, performance constraints, reduced-motion requirements, and accessibility expectations.
- Screenshots or runtime behavior when available.

## Procedure

1. Define the job of motion: feedback, continuity, hierarchy, spatial orientation, delight, or state change.
2. Decide whether animation is useful. If it does not improve comprehension, feedback, or perceived quality, skip it.
3. Choose technique:
   - CSS transitions/animations for simple state changes.
   - Framer Motion for React state-driven choreography, layout transitions, gestures, and page transitions.
   - Web Animations API for imperative browser-native sequences.
   - Avoid JavaScript animation for simple hover/focus effects.
4. Design timing and easing to match task importance. Keep operational UI restrained.
5. Include reduced-motion behavior from the start.
6. Verify keyboard, focus, scroll, and screen-reader behavior are not harmed.
7. Test mobile, low-power devices where practical, zoom, and viewport changes.
8. Watch for layout shift, hydration mismatch, jank, repaint storms, and scroll hijacking.
9. Keep animations cancelable or resilient when state changes quickly.
10. Report evidence and limitations.

## Decision Points

- Use micro-interactions for direct feedback: button press, save state, drag/drop, disclosure.
- Use page transitions only if they preserve orientation and do not delay navigation.
- Use scroll interaction sparingly; never hide critical content behind fragile scroll timing.
- Prefer no animation for high-risk, time-sensitive, or accessibility-sensitive flows unless it clarifies state.

## Failure Modes To Break

- Motion that hides loading or failure states.
- Reduced-motion ignored.
- Focus jumps after animated route/dialog changes.
- Layout shifts caused by animated dimensions.
- Heavy animation blocking input or hurting mobile performance.
- Animation library added without package-intelligence when CSS would suffice.

## Verification

Check:

- Reduced motion enabled.
- Keyboard-only workflow.
- Mobile viewport.
- Fast repeated interactions.
- Route/dialog enter and exit.
- Performance trace or visual inspection for jank when risk is material.

## Outputs

```text
MOTION PURPOSE:
TECHNIQUE:
REDUCED MOTION:
ACCESSIBILITY CHECKS:
PERFORMANCE CHECKS:
FAILURE STATES:
EVIDENCE:
```

## Related Skills

- design-toolkit for visual design fit.
- package-intelligence for Framer Motion or animation library adoption.
- system-breaker for failure-state verification.
