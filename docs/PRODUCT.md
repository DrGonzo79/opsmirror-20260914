# Product plan

## ICP, JTBD, MVP

ICP: Heads of Support/Operations at 30–150 person subscription commerce or SaaS companies with 500+ monthly refunds, a ticket system, and approval rules that affect margin. JTBD: “When refund policy changes, show me which actual decisions violate it, why, and what a human must verify before the weekly finance review.”

MVP: one versioned refund policy; CSV/API ticket intake; four deterministic checks (approval, evidence, reason, SLA); cited decision queue; verified dispositions; weekly summary. Exclude generic SOP authoring, autonomous enforcement, employee scoring, and opaque compliance claims.

## Data model

`PolicyVersion(id, effective_at, source_uri, checksum)` owns `Rule(code, predicate, severity)`. `Decision(id, occurred_at, actor_ref, amount, evidence_refs)` produces `Finding(rule_id, observed_value, status)`. `Disposition(finding_id, outcome, reviewer, note, timestamp)` distinguishes behavior drift, policy defect, accepted exception, and false positive. Immutable source snapshots and tenant isolation are mandatory before real data.

## Architecture and AI strategy

Today: Next.js static review demo reads shared JSON; FastAPI validates and runs the same explicit domain rules. Production: encrypted object ingestion → schema mapping → deterministic policy evaluator → Postgres evidence ledger → review UI and digest worker. LLM use is constrained to proposing rule drafts and summarizing verified findings; rules require human approval, cite source spans, and execute deterministically. Never use an LLM to silently judge employees.

```text
Policy + ticket export → validation → explicit rules → cited findings → human disposition
       nil/empty/error ↘ named import error + zero-write audit log ↗ weekly summary
```

## Economics and GTM

Sell analyst-led implementation: $1,500 setup + $750/month/workflow. At 20 customers, ~$15k MRR against one ops analyst plus hosting; target >70% contribution margin after mappings stabilize. Expansion: $1,500/month for three workflows, then multi-team enterprise controls. Acquire via 10 personalized “policy drift sample” reports to support operators, Zendesk consultants, and fractional COOs—not broad content marketing.

## Validation, moat, risks

14-day gate: 5 observed audits, 3 real exports, 2 previously unknown high-value gaps, 1 paid pilot, <30 minutes analyst cleanup per 50 tickets. Kill or reframe if exports lack decisive evidence or leaders will not act on findings. Moat is the accumulated tenant-specific map from policy language to verified operational evidence and disposition outcomes—not the LLM or dashboard.

Risks: surveillance optics, incomplete evidence, policy version ambiguity, sensitive customer data, false accusations, connector fragility, and alert fatigue. Mitigate with role-based access, minimization/redaction, explicit confidence and evidence, human verification, immutable versioning, sampling controls, and no worker leaderboard.

## 30 / 60 / 90 days

- **30:** analyst-led CSV audits; five observations; two paid pilots; validate four rules.
- **60:** Zendesk sandbox connector, versioned policy editor, dispositions, weekly digest, deletion controls; 5 paying workflows.
- **90:** multi-policy effective dates, evidence lineage, aggregate drift trends, partner playbook; 10 customers and <15-minute weekly analyst handling.
