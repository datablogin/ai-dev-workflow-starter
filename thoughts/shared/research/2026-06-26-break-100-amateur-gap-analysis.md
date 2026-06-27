---
date: 2026-06-26
author: "quinnpark (with Claude Code)"
status: draft
supersedes: thoughts/shared/research/2026-06-26-golf-course-design-scores.md
tags: [golf, break-100, amateur-improvement, strokes-gained, feasibility]
---

# Research: "Break 100" Amateur Stroke-Gap Diagnosis

## Question

For an amateur who shoots ~100 (roughly a 25-30 handicap), which part of the
game — off-the-tee, approach, short game (around the green), or putting —
accounts for the biggest stroke gap versus the benchmark needed to *break 100*,
and is therefore the highest-leverage place to practice?

Deliberately **descriptive / diagnostic, not causal**. We are comparing
published benchmark averages across skill levels, not estimating the effect of
an intervention on one golfer. That honest scoping is itself a repo lesson:
don't claim causation the data can't support (carried over from the superseded
pro-score research).

## Context

- Audience pivot: the deliverable must help *the user's* game, not pros.
  See pivot handoff `thoughts/shared/handoffs/2026-06-26-golf-project-pivot.md`.
- No self-experiments and no personal data collection. We rely entirely on
  **published, aggregated** strokes-gained-by-handicap benchmarks.
- **Target tiers (decided with user):** report the gap against TWO references —
  - `T1` ~20-handicap "just break 100" (the lowest handicap that reliably
    shoots under 100), and
  - `T2` ~15-handicap stretch target.
  Showing both separates near-term from longer-term leverage.
- **Deliverable (decided with user):** a small script that ingests benchmark
  tables (CSV) and outputs per-category gaps, plus a written findings report.
  This intentionally exercises the repo's `tdd -> implement -> polish ->
  review-pr` shipping workflow.

## Candidate Data Sources

| Source | Provides | Access / Notes | Confidence |
|---|---|---|---|
| **Shot Scope** (350M+ shot DB) | Strokes-gained benchmarks for 6 tiers: scratch, 5, 10, 15, 20, 25 hcp, split by driving / approach / around-green / putting | **Free**, published in blog + a strokes-gained ebook PDF. Tiers bracket our user (25) and both targets (20, 15) almost exactly. **Primary source.** | High |
| Mark Broadie, *Every Shot Counts* | Strokes-gained methodology + amateur benchmark tables by skill (80/90/100 golfer) | Book (paid). Full amateur hole-out tables not all printed; methodology is the canonical reference. Use as **cross-check**. | Medium |
| Arccos Golf | Strokes gained in 5 categories vs a database of users at similar handicap | App-internal comparison; aggregate stats appear in press/blog rather than a clean downloadable table. **Secondary cross-check.** | Medium |
| USGA scoring-distribution data | Score distributions / handicap context to define "break 100" | Public; useful for framing the target, not for category splits. | Medium |

## Findings

| Finding | Evidence | Confidence |
|---|---|---|
| The exact data the project needs **exists and is free** | Shot Scope publishes strokes-gained benchmarks for scratch/5/10/15/20/25 hcp, split by the four standard categories, from a 350M+ shot database | High |
| The benchmark tiers line up with our design | User ~25 hcp; targets at 20 and 15 hcp are all distinct published Shot Scope tiers — direct subtraction gives the per-category gaps | High |
| **The old project bottleneck is gone** | Prior research's hardest sub-task was hand-collecting course-design features; the amateur pivot needs none of that | High |
| Approach play is the likely headline gap | Shot Scope + Broadie both report the largest losses (and widening gap with handicap) come from approach / shots outside 100 yds (~2/3 of skill-level scoring differences) | Medium |
| Method is simple + verifiable | Gap = `your_tier - target_tier` per category; a tiny script + unit tests fully covers it | High |

## Risks

- **Benchmark population != the user.** Shot Scope tiers are averages over many
  golfers at a handicap, not this golfer. The output is "where a typical
  25-hcp loses strokes vs a typical 20/15-hcp," a strong prior, not a
  measurement of the user's own game. State this plainly in the report.
- **Category definitions must match across sources.** "Short game / around the
  green" vs "wedges inside 100" are not identical cuts. If we mix Shot Scope and
  Broadie numbers we can double-count or mislabel. Mitigation: use **one source
  (Shot Scope) for the headline table**; others are cross-checks only.
- **Exact PDF numbers not yet transcribed.** The ebook PDF is binary; values
  weren't machine-extracted this session. Transcribing the table by hand into a
  CSV is a small, explicit implementation task (with the source cited per row).
- **Descriptive-not-causal must stay loud.** Easy to slide into "fix approach
  and you'll break 100." We can say "closing the approach gap is the largest
  available stroke saving," not "this will cause you to break 100."

## Open Questions (resolved this session unless noted)

- Which dataset is accessible? -> **Resolved: Shot Scope, free, primary.**
- Define "break 100" precisely? -> **Resolved: two tiers, 20-hcp and 15-hcp.**
- Output format? -> **Resolved: small script (CSV in, gaps out) + report.**
- (Open, for implementation) Exact per-category benchmark values to transcribe
  into the CSV, with a cited source for each cell.

## Recommendation

Proceed to `plan`. The feasibility question is settled: free, well-structured
benchmark data exists at exactly the granularity the design needs, and the
method is a transparent per-category subtraction that a small tested script
handles cleanly. Keep the framing strictly descriptive. Next artifacts: a
phased plan and a scorecard, then the `tdd -> implement -> polish` shipping
loop for the script.
