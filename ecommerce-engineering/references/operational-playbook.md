# E-Commerce Engineering Operational Playbook

Use this playbook for checkout, payments, orders, inventory, coupons, CMS/admin commerce, webhooks, and transaction integrity.

## Inputs

- Product/catalog/cart/order/payment requirements.
- Server routes/actions, database schema, payment provider docs, webhook handlers, inventory model, coupon rules, and admin permissions.
- Test credentials or provider test mode when payment execution is required.
- Existing security, system-breaker, incident-response, database/schema evidence, and payment-provider test-mode outputs where available.

## Core Rules

- Browser prices, totals, discounts, delivery fees, inventory, and payment success are untrusted.
- Server-calculated amounts and provider verification/webhooks are authoritative.
- Payment finalization must be idempotent.
- Authorization and customer isolation are server responsibilities.
- Do not run real payments/refunds or destructive production operations without explicit approval.

## Checkout Procedure

1. Validate cart items server-side: product exists, active/published, purchasable, quantity allowed, stock available, price current.
2. Calculate subtotal, discount, delivery/tax/fees, and total on the server.
3. Validate coupon server-side: active, time window, minimum spend, usage limits, customer eligibility, product/category applicability.
4. Create a checkout attempt/order draft with stable ID, amount snapshot, customer, cart lines, and idempotency key.
5. Initialize payment using the server amount only.
6. Handle user cancellation, timeout, retry, duplicate initialization, and abandoned checkout.
7. Verify payment by provider API or validated webhook before marking paid.

## Webhook Procedure

1. Verify provider signature using the correct secret and raw body.
2. Reject missing/malformed signatures safely.
3. Check event type, provider reference, amount, currency, status, and target order/attempt.
4. Enforce idempotency with unique event/reference records or transactional guards.
5. Handle duplicate, delayed, out-of-order, replayed, unknown-resource, failed, and partial-failure events.
6. Ensure exactly-once business effects: one paid transition, one inventory decrement/reservation conversion, one coupon consumption, one receipt/fulfilment trigger.
7. Log operational evidence without secrets or full sensitive payment data.

## Order State Machine

Recommended states:

```text
DRAFT -> PAYMENT_PENDING -> PAID -> FULFILMENT_PENDING -> FULFILLED
      -> PAYMENT_FAILED
      -> ABANDONED
      -> CANCELLED
      -> REFUNDED / PARTIALLY_REFUNDED
```

Rules:

- State transitions must be server-authorized.
- Invalid backward transitions should fail safely.
- Duplicate callbacks/webhooks must leave state unchanged after first success.
- Failed operations must not create paid orders or double fulfilment.

## Inventory Procedure

1. Decide model: check-at-payment, reservation, or manual stock only.
2. For reservations, create expiry and release behavior for abandoned/failed checkout.
3. Test concurrent purchase of the last unit.
4. Prevent negative stock with database constraints or transactional compare-and-swap.
5. Verify duplicate payment finalization does not double decrement.
6. Define cancellation/refund restock rules explicitly.

## Security And Authorization

Test:

- Unauthenticated order access.
- Customer A accessing Customer B order/receipt.
- Price/coupon/cart manipulation in requests.
- Admin-only product/order/coupon/media mutations.
- Inactive/restricted admin roles.
- Direct API access bypassing UI visibility.
- Upload/media permissions for product CMS.

## CMS Procedure

- Validate roles for create, update, delete, publish, unpublish, price edit, stock edit, coupon edit, refund action, and media deletion.
- Require confirmation or recovery for destructive operations.
- Preserve audit records for price, stock, coupon, order, and refund changes.
- Avoid publishing incomplete products with missing price, stock policy, images, or required metadata.

## Failure Modes To Break

- Client changes price/quantity/discount and server trusts it.
- Browser success page marks order paid without provider verification.
- Duplicate webhook creates duplicate receipt or decrements stock twice.
- Delayed webhook revives cancelled/abandoned checkout incorrectly.
- Coupon quota race allows overuse.
- Inventory race oversells last item.
- IDOR exposes another customer order.
- Admin UI hides action but server allows it.

## Verification

```text
CHECKOUT SERVER TOTAL:
PAYMENT INIT:
PAYMENT VERIFY:
WEBHOOK SIGNATURE:
WEBHOOK IDEMPOTENCY:
ORDER STATE:
INVENTORY:
COUPONS:
AUTHORIZATION:
CMS:
REGRESSION TESTS:
EVIDENCE:
UNTESTED AREAS:
```

## Related Skills

- Use this playbook's checkout, webhook, inventory, and idempotency procedures for commerce-specific checks; these are local capabilities, not separate top-level skills.
- security for auth, secrets, APIs, uploads, and headers.
- system-breaker for adversarial verification, regression evidence, and safe failure testing.
- incident-response for monitoring and payment failure operations.
