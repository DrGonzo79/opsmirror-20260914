# OpsMirror

OpsMirror is a runnable vertical-slice prototype for comparing a written refund SOP with actual support decisions. It turns explicit policy rules into explainable gaps, then gives an operations lead a human verification workflow.

**Public demo:** https://drgonzo79.github.io/opsmirror-20260914/

All demo organizations, tickets, agents, and outcomes are fictional. Browser analysis is deterministic and runs locally. No data is uploaded. The Python API is tested source and is **not publicly deployed**.

## Run

```bash
npm ci
npm run dev
```

In another terminal:

```bash
cd api
uv sync --locked
uv run uvicorn main:app --reload
```

## Verify

```bash
npm run typecheck
npm run test:e2e
npm run build
cd api && uv run pytest
npm audit --audit-level=high
```

## What works

- Run an explainable refund decision audit against shared fictional fixtures.
- Change the manager approval threshold and see the result update.
- Filter aligned/drifted decisions and inspect cited gaps.
- Add and validate a fictional decision; mark findings human-verified.
- POST up to 500 decisions to the FastAPI `/audit` domain operation.

See `docs/PRODUCT.md`, `docs/ARCHITECTURE.md`, and `docs/BUILD_PROMPTS.md` for the commercial plan and next phases.
