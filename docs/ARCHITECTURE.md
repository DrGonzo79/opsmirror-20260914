# Architecture

## Prototype

```text
data/policy.json ─┐
                  ├─ Next.js deterministic inspector ─ interactive static export
data/tickets.json ┤
                  └─ FastAPI /audit ─ validated findings JSON
```

The fixture contract is intentionally explicit and shared. GitHub Pages hosts only the static frontend. FastAPI remains locally runnable/tested source.

## API contract

`POST /audit` accepts one validated policy and 1–500 tickets. It returns counts plus findings with stable gap codes. Pydantic returns 422 for empty batches, invalid money, overlong identifiers, and invalid SLA values. Production additions: authenticated tenant context, idempotency key, policy checksum, import status resource, structured audit log, timeouts, and rate limits.

## Failure and observability map

- Empty/malformed export → `422 validation_error`; UI names the field; no partial audit.
- Unknown columns → `mapping_required`; quarantine import; mapping task counter increments.
- Policy parse uncertainty → `rule_review_required`; no active rule until approved.
- Connector timeout → `source_timeout`; retain cursor, retry with jitter, alert after three attempts.
- Stale policy/decision conflict → `policy_version_conflict`; rerun against effective version.
- Digest failure → `delivery_failed`; findings remain visible; retry and page on sustained failure.

Production metrics: import success/latency, mapped-field coverage, findings per 100 decisions, verification latency, false-positive disposition rate, stale-policy age, connector lag, and digest delivery. Alerts need runbooks and tenant-safe trace IDs.

## Security and scale

Treat tickets as confidential customer data: encrypt in transit/at rest, isolate tenants, redact free text by default, short retention, audit access, SSO/RBAC, signed connector webhooks, dependency scanning, and export/delete controls. At 10×, batch rules and queue imports. At 100×, partition decisions by tenant/month and precompute aggregates; never put raw ticket text in logs or model prompts by default.
