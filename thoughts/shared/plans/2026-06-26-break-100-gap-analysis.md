---
date: 2026-06-26
author: "quinnpark (with Claude Code)"
status: draft
research: thoughts/shared/research/2026-06-26-break-100-amateur-gap-analysis.md
tags: [golf, break-100, plan, strokes-gained]
---

# Plan: "Break 100" Stroke-Gap Diagnosis Tool + Report

## Objective

Ship a small, tested script that ingests published strokes-gained-by-handicap
benchmarks (CSV) and outputs, per game category (off-the-tee, approach, short
game, putting), the stroke gap between a ~25-handicap golfer and two targets —
a ~20-handicap "just break 100" tier and a ~15-handicap stretch tier — and
identifies the highest-leverage category. Pair it with a short findings report.

## Non-Goals

- No causal claims. Output is descriptive: gaps between published benchmark
  averages, not the effect of any intervention on the user.
- No personal round tracking or data collection.
- No live API calls or scraping at runtime — benchmark data is a committed,
  source-cited CSV fixture.
- No GUI, web app, or charts library. Plain-text/CSV output is enough.

## Phases

| Phase | Goal | Likely Files | Exit Condition |
|---|---|---|---|
| 1 | Transcribe benchmark data into a cited CSV (Shot Scope tiers: 25/20/15 hcp x 4 categories), one source note per row | `data/benchmarks.csv`, `data/SOURCES.md` | CSV loads; every value has a cited source; tiers + categories complete |
| 2 | `tdd`: write failing tests for the gap calc (per-category gap, biggest-gap pick, two-tier output, bad-input handling) | `tests/test_break100.py` | Tests exist and fail for the right reason (no impl yet) |
| 3 | `implement`: write the script to make tests pass — read CSV, compute `you - target` per category for each tier, rank gaps | `break100.py` | All Phase 2 tests pass |
| 4 | `polish`: clean output formatting, docstrings, README usage, edge cases | `break100.py`, `README` section | `polish` pass done; output readable |
| 5 | Write findings report from the script's output (gap table both tiers, headline leverage category, explicit descriptive caveats) | `thoughts/shared/.../break-100-findings.md` | Report matches script output; caveats present |
| 6 | `review-pr` + human approval | PR / review diff | Human approves; no unresolved review comments |

## Implementation Notes

- **Language:** Python 3 (stdlib `csv` only — no new deps; AGENTS.md says ask
  before adding dependencies).
- **Data shape:** `category,you_25,target_20,target_15,source` so each row
  carries its own citation. Categories: `off_the_tee, approach, short_game,
  putting`. Convention: a *positive* gap = strokes the user could save by
  reaching that target.
- **One source for the headline table** (Shot Scope) to keep category
  definitions consistent; Broadie/Arccos are cross-checks noted in the report,
  not mixed into the CSV.
- **Output:** a small table per target tier plus a one-line "highest-leverage
  category" for each. Keep numbers and labels straight from the CSV so the
  report can be regenerated, not hand-maintained.
- Sequence follows AGENTS.md shipping workflow: `tdd -> implement -> polish ->
  review-pr -> human approval`. Work on a feature branch, not `main`.

## Tests Or Checks

- `python3 -m pytest tests/` (or `python3 -m unittest`) — gap math, ranking,
  two-tier output, malformed/missing-row handling.
- Manual: run `python3 break100.py data/benchmarks.csv` and eyeball the table.
- Data check: every CSV value traces to a citation in `data/SOURCES.md`.

## Rollback Or Recovery

- All work on a feature branch; revert by deleting the branch — `main` and the
  thoughts/ artifacts are untouched.
- Code is self-contained (`break100.py` + `data/` + `tests/`); deleting those
  paths fully removes the tool. No migrations, services, or external state.
