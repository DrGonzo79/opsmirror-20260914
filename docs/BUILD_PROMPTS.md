# Phased build prompts

1. **Pilot ingestion:** Add authenticated CSV imports with tenant-scoped encrypted storage, schema mapping, duplicate detection, import status, deletion, and tests for malformed/empty/oversized files. Preserve stable gap codes.
2. **Policy versions:** Build an effective-dated policy editor whose rules cite source spans, require human approval, and re-run decisions idempotently. Add conflict and rollback tests.
3. **Review ledger:** Persist findings and append-only dispositions (behavior drift, policy defect, accepted exception, false positive). Add RBAC, audit logs, accessibility, and reviewer-latency metrics.
4. **Connector + digest:** Add a Zendesk sandbox connector with cursor recovery, rate limits, retry/jitter, lag monitoring, and a weekly digest whose delivery failure never hides findings.
5. **Constrained AI:** Propose rule drafts and summaries from redacted text; require citations and approval, evaluate precision/recall on verified dispositions, and keep deterministic execution authoritative.
