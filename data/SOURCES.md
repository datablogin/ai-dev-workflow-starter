# Benchmark Data Sources

Provenance for every value in `benchmarks.csv`. Plan requires each value to
trace to a cited source (see
`thoughts/shared/plans/2026-06-26-break-100-gap-analysis.md`, Phase 1 exit
condition, and the scorecard's data-traceability gate).

## What the numbers are

Strokes-gained **per round, measured against the PGA Tour baseline (0.0)**,
broken down into the four standard categories. All values are negative because
every amateur loses strokes to the tour. Because every tier is measured against
the *same* tour baseline, the tier-to-tier difference is a valid estimate of the
strokes a golfer could save by improving from one tier to the next — which is
exactly the gap this project computes.

Tiers used:
- `you_25`  — 25-handicap golfer (the user, shoots ~100)
- `target_20` — 20-handicap "just break 100" target
- `target_15` — 15-handicap stretch target

## Source

### `golfity-broadie-2026`

- **Table:** "Strokes Gained Benchmarks for Every Handicap Level," Golfity.
  <https://golfity.com/blog/strokes-gained-benchmarks-for-every-handicap/>
- **Attribution:** Golfity presents the table as derived from Mark Broadie's
  strokes-gained research (*Every Shot Counts*), measured vs PGA Tour baseline.
- **Cross-check:** The 15- and 20-handicap rows match a second, independent
  Golfity article to the decimal:
  <https://golfity.com/blog/strokes-gained-for-15-20-handicappers/>
  (15-hcp: OTT -2.7 / APP -6.0 / ARG -2.0 / PUTT -1.5;
   20-hcp: OTT -3.4 / APP -7.5 / ARG -2.5 / PUTT -1.8).

Full published table (for traceability; rows used in the CSV are 25/20/15):

| Handicap | Off the Tee | Approach | Around Green | Putting | Total |
|----------|-------------|----------|--------------|---------|-------|
| Scratch  | -0.8 | -1.5 | -0.5 | -0.4 | -3.2 |
| 5        | -1.4 | -3.0 | -1.0 | -0.8 | -6.2 |
| 10       | -2.0 | -4.5 | -1.5 | -1.2 | -9.2 |
| 15       | -2.7 | -6.0 | -2.0 | -1.5 | -12.2 |
| 20       | -3.4 | -7.5 | -2.5 | -1.8 | -15.2 |
| 25       | -4.2 | -9.0 | -3.0 | -2.2 | -18.4 |
| 30       | -5.0 | -10.5 | -3.5 | -2.5 | -21.5 |

## Provenance caveat (read before trusting precision)

- The pivot research named **Shot Scope** as the intended primary source. Shot
  Scope's exact per-category numbers are published only in a binary ebook PDF
  that could not be machine-extracted this session, so the concrete headline
  table here comes from the Golfity/Broadie source instead. This keeps the table
  internally consistent (single source, single baseline) per the plan's
  "one source for the headline table" rule.
- These are **population averages by handicap, not the user's own measured
  game.** Treat the output as a strong prior about where a typical 25-handicap
  loses strokes — not a measurement of this golfer. (Descriptive, not causal.)
- `short_game` in the CSV == "Around the Green" in the source table.

## How to update

If better data is obtained (e.g. transcribed Shot Scope tables, or the user's
own tracked rounds), replace the values in `benchmarks.csv`, add a new source ID
section here, and update the `source` column. Keep one source per headline table
to avoid mixing inconsistent category definitions or baselines.
