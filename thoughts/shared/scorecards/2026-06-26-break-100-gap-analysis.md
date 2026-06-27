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
  Mitigation: single source (Shot Scope) for the headline CSV.
- Sign/direction confusion in the gap (who minus whom). Mitigation: explicit
  convention (positive = strokes saveable) plus a unit test asserting it.

## Final Result

| Field | Result |
|---|---|
| Delivered artifact or PR | <pending> |
| Checks | <pending> |
| Remaining risks | <pending> |
| Human approval | pending |
