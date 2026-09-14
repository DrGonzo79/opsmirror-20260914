# CEO Review

**Mode:** Scope reduction for a one-day public prototype  
**Status:** Done with explicit production concerns

## Nuclear challenge

The original “company source of truth” premise is too broad and competes with every knowledge platform. The user outcome is earlier detection of costly operational exceptions, not better docs. The narrow refund-decision wedge is more direct, measurable, and sellable.

Current state → this prototype → 12-month ideal: manual SOP spot-checks → explainable refund evidence queue → continuous, version-aware process assurance with verified feedback loops.

## Alternatives and decision

Minimal analyst report (fastest), review workbench (chosen), and continuous process graph (ideal) were compared. The workbench earns its extra scope because verification dispositions create learning data; live connectors and generalized AI were deferred.

## Eleven-section review

1. **Architecture:** Keep rules deterministic and policy-versioned; frontend/backend duplication is acceptable only for demo fixtures. Production needs a shared generated rule contract.
2. **Errors:** Name validation, mapping, timeout, version-conflict, and delivery failures; never produce a silent partial report.
3. **Security:** Ticket text is confidential; require tenant isolation, redaction, RBAC, retention, and access logs before real use.
4. **Data/interaction edges:** Cover nil/empty imports, bad types, huge amounts, encoding, duplicates, double-submit, stale filters, and navigation during import. Prototype prevents invalid/oversized amounts and empty API batches.
5. **Code quality:** Four stable gap codes beat a premature rule DSL. Extract a shared contract before adding a second workflow.
6. **Tests:** Cover happy path, all four gaps, validation, fixture result, human verification, new decision, and mobile overflow. Connector and policy-version tests are deferred until those systems exist.
7. **Observability:** Track import health, mapping coverage, drift rate, verification latency, false positives, connector lag, and digest delivery; never log raw text.
8. **Database/state:** Prototype state is explicitly ephemeral. Production requires immutable policy versions, unique source decision IDs, idempotent imports, and append-only dispositions.
9. **API:** `/audit` is bounded to 500 decisions and returns stable codes. Add authentication, tenant scope, idempotency, async status, and versioning before exposure.
10. **Performance:** Synchronous evaluation is fine at 500 rows. Queue batches and partition evidence at 10×/100×; models must not sit in the critical evaluation path.
11. **UX:** Evidence precedes judgment; demo labels, loading/error/empty states, responsive layout, keyboard-focusable native controls, and human verification are required. Avoid employee leaderboards.

## Accepted / deferred / excluded

Accepted: one refund policy, explicit rules, fictional fixtures, filters, cited gaps, manual add, verification, tested API. Deferred: authenticated ingestion, connectors, persistence, model-assisted rule drafting, alerts. Excluded: autonomous enforcement, employee scoring, generic knowledge search, paid APIs, and claims of live backend deployment.
