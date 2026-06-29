---
date: 2026-06-26
author: "quinnpark (with Claude Code)"
status: draft
plan: thoughts/shared/plans/2026-06-26-break-100-gap-analysis.md
tags: [golf, break-100, scorecard]
---

# Scorecard: "Break 100" Stroke-Gap Diagnosis Tool + Report

## Primary Outcome

| Metric | Target | Measurement |
|---|---|---|
| Highest-leverage category identified | One named category per target tier (20-hcp, 15-hcp), backed by the data | Script output + report section |
| Per-category gaps computed | All 4 categories x 2 tiers = 8 gap values, each derived from cited benchmarks | `break100.py` output table |
| Data traceability | 100% of CSV values have a cited source | `data/SOURCES.md` vs `data/benchmarks.csv` |

## Delivery Gates

| Gate | Required Result | Evidence |
|---|---|---|
| Tests/checks | All unit tests pass (gap math, ranking, two-tier, bad input) | `python3 -m pytest tests/` output |
| Review | `review-pr` complete, no unresolved comments | PR review thread |
| Privacy/security | No secrets, no personal round data; only published aggregates committed | Diff review of `data/` |

## Acceptance Criteria

- [ ] Script reads `data/benchmarks.csv` and prints per-category gaps for both
      the 20-hcp and 15-hcp targets.
- [ ] Script names the highest-leverage category for each tier.
- [ ] Every benchmark value cites its source in `data/SOURCES.md`.
- [ ] Findings report regenerable from script output (numbers not hand-typed).
- [ ] Report states plainly the result is **descriptive, not causal**, and that
      benchmarks are population averages, not the user's own game.
- [ ] Tests cover gap math, biggest-gap selection, and malformed input.

## Scope Guardrails

- Must not change: the superseded pro-score research artifact (kept as history).
- Must not touch: `main` directly — feature branch only.
- Must not add: runtime network calls, scraping, or new dependencies beyond
  Python stdlib (ask first per AGENTS.md).
- Must not claim: causation, or that closing a gap *will* make the user break 100.

## Regression Risks

- Mixing category definitions across sources -> miscomputed/mislabeled gaps.
  Mitigation: single source for the headline CSV (Golfity/Broadie table vs Tour
  baseline; Shot Scope's exact numbers were not machine-extractable this
  session — see data/SOURCES.md).
- Sign/direction confusion in the gap (who minus whom). Mitigation: explicit
  convention (positive = strokes saveable) plus a unit test asserting it.

## Final Result

| Field | Result |
|---|---|
| Delivered artifact or PR | Local only (no PR by choice). Branch `break-100-gap-analysis`: `break100.py`, `data/benchmarks.csv`, `data/SOURCES.md`, `tests/test_break100.py`, findings report `thoughts/shared/research/2026-06-28-break-100-findings.md`. 6 commits, `main` untouched. |
| Checks | All 11 unit tests pass (`python3 -m unittest discover -s tests`). Tool runs: `python3 break100.py data/benchmarks.csv`. `/simplify` (4-angle) applied, no behavior change. |
| Remaining risks | Headline data is Golfity/Broadie, not Shot Scope as originally intended (documented update path in data/SOURCES.md). Benchmarks are population averages, not the user's own game (descriptive, not causal). |
| Human approval | Pending — local review only; user chose not to push/open a PR. |
