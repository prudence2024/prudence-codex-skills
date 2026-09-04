# ADE Retry And Recovery

Runtime retries are bounded by `RetryPolicy.max_attempts`. Provider unavailability is classified and emitted as structured observability. No infinite retry loop is allowed. Stale or conflicting results are surfaced with warnings and research decisions rather than silently promoted.
