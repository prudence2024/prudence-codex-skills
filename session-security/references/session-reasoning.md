# Session Security reasoning and integration

## State-machine contract

Model explicit states for active, warning, extending, expired,
reauthenticating, restoring, signed-out, and failure. Define each transition's
trigger, server evidence, side effects, persistence, broadcast behavior, retry
policy, and terminal outcome. The server clock and server-confirmed expiry remain
authoritative.

## Shared Context

Read project facts, constraints, assumptions, uncertainties, decisions,
artifacts, risks, and prior runs. Consume Security decisions for authentication,
tokens, cookies, authorization, and threat constraints. Consume Design Toolkit
decisions for modal, focus, motion, and interaction behavior. Record conflicts
instead of overwriting either owner.

Write attributable policy facts, decisions, artifacts, test evidence, risks,
uncertainties, and handoffs. Never persist restoration payload contents in Shared
Context.

## Evidence

Keep code presence, local build behavior, server enforcement, multi-tab behavior,
device sleep behavior, accessibility behavior, deployed behavior, and monitored
outcomes distinct. A client countdown does not prove server expiry. A refresh
handler does not prove rotation, race safety, or cross-tab consistency.

## Alternatives and privacy

Compare timeout and restoration strategies against threat exposure, user effort,
provider capability, accessibility, implementation complexity, privacy,
maintainability, and failure behavior. Reject passive surveillance and unlimited
sustained-focus extensions.

## Extensions and handoffs

Provider, platform, transport, storage, and test adapters return versioned,
bounded evidence and limitations. They do not replace Session Security's final
policy decision. Hand authentication weaknesses to Security, UI conflicts to
Design Toolkit, and abuse or outage readiness to Incident Response.
