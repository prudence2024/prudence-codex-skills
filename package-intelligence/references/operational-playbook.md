# Package Intelligence Operational Playbook

Use this playbook before adopting, replacing, or trusting a package, SDK, component library, or tool.

## Inputs

- Need or capability gap.
- Current project stack, runtime, framework, package manager, and constraints.
- Candidate packages and existing in-repo alternatives.
- Research findings, official docs, registry metadata, security/license data, and build/test output.

## Procedure

1. Define the need in one sentence and the minimum capability required.
2. Check existing code and dependencies first. Do not install a package for a capability already present.
3. Consider native platform/framework solutions before third-party dependencies.
4. Identify candidates from official ecosystem docs, maintained registries, and project-compatible examples.
5. For each candidate, inspect maintenance: recent release, issue health, maintainer activity, deprecation notices, bus factor, and ecosystem adoption.
6. Check compatibility: framework version, React/Next/Vite/server/client constraints, ESM/CJS, TypeScript, browser/Node support, SSR/hydration, peer dependencies.
7. Check security and supply chain risk: advisories, install scripts, transitive size, permissions, and package authenticity.
8. Check license and commercial fit.
9. Check performance: bundle size, runtime cost, tree-shaking, WebGL/audio/device cost, and initialization overhead.
10. Check documentation quality and examples against the current version.
11. Decide: adopt, defer, reject, or use native/local solution.
12. If adopted, install with approval where needed, import minimally, build, run tests, and verify representative runtime behavior.
13. Record rollback strategy.

## Example Decision Patterns

- Framer Motion: choose when React interaction state, layout transitions, or gesture orchestration justify the dependency. Prefer CSS for simple hover/fade transitions.
- Three.js: choose for imperative 3D or custom WebGL control. Use React Three Fiber/Drei when the app is React and declarative scene composition helps.
- shadcn/ui: choose when the project accepts copied component source and Tailwind/Radix patterns. Do not treat it as a runtime dependency like a normal component library.
- 21st.dev: evaluate as a design/component source, not automatically as production dependency; verify licensing, provenance, and fit with the local design system.

## Decision Points

- If the package is only nice-to-have, avoid adding it.
- If maintenance or license is unclear, reject or ask owner.
- If the dependency touches auth, payments, secrets, file uploads, or production infrastructure, involve security.
- If current docs are needed, use research-intelligence first.

## Failure Modes To Break

- Installing based on popularity alone.
- Ignoring peer dependency or SSR incompatibility.
- Adding a large library for trivial behavior.
- Trusting examples for older major versions.
- Claiming adoption without build/runtime verification.

## Verification

Minimum adoption proof:

```text
DECISION:
CANDIDATES CONSIDERED:
WHY THIS / WHY NOT OTHERS:
VERSION:
LICENSE:
SECURITY CHECK:
COMPATIBILITY CHECK:
INSTALL RESULT:
BUILD/TEST RESULT:
RUNTIME CHECK:
ROLLBACK:
```

## Related Skills

- research-intelligence for current package facts.
- ai-assisted-engineering for implementation.
- system-breaker for verification of high-risk adoption.
- motion-interaction and three-d-web for domain-specific packages.
