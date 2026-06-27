---
date: 2026-06-26
author: "quinnpark (with Claude Code)"
status: active
tags: [golf, handoff, project-pivot, amateur-improvement]
---

# Handoff: Golf Project Pivot — "Break 100" Gap Analysis

## Purpose of this note

Carry the project cleanly into a fresh Claude Code session. Read this first,
then read the research artifact it references. Everything you need is on disk —
no chat history required.

## Where the project started

Original idea: find *causal* relationships between **course design** and
**pro tournament scores**. First `shape-work` research artifact:
`thoughts/shared/research/2026-06-26-golf-course-design-scores.md`.

Key lesson that artifact surfaced: observational golf data rarely *proves*
causation, and pro data is irrelevant to the user's own game.

## What changed (the pivot)

1. **Audience = the user**, an amateur who shoots in the 100s
   (roughly a 25–30 handicap). The project must help *their* game.
2. **No self-experiments and no personal data collection.** The user cannot
   track their own rounds or randomize their own play. Earlier self-experiment
   idea is OFF the table.
3. **Use existing / published data instead.**

## New project direction

**"Break 100": a stroke-gap diagnosis using published amateur benchmark data.**

Core question:
> For a golfer shooting ~100, which part of the game (off-the-tee, approach,
> short game, putting, penalties) accounts for the biggest gap versus the level
> needed to break 100 — and where is the highest-leverage place to improve?

Method: compare published **strokes-gained-by-handicap** benchmarks for a
~100-shooter against the benchmark for bogey golf (~break 100 / ~18 handicap).
The category with the largest gap is the highest-leverage practice target.

This is **descriptive / diagnostic, NOT causal** — and that honest scoping is
itself a repo lesson (verification bias: don't claim causation we can't defend).

## Candidate data sources (verify access in next session)

- Mark Broadie, *Every Shot Counts* — strokes-gained benchmark tables by skill.
- Arccos Golf — published aggregate amateur stats by handicap.
- Shot Scope — published "amateur vs better golfer" data by handicap.
- USGA handicap / scoring-distribution data.
- Any public Kaggle amateur golf dataset as a cross-check.

## Where we are in the repo workflow

```
research (pro version) ✅  →  [NEEDS REVISION for amateur pivot]  →  plan  →  scorecard  →  ...
```

The existing research artifact is **about pros and is now partly outdated.**

## Next steps for the new session

1. Open Claude Code in `~/Projects/ai-dev-workflow-starter`.
2. Say: "Read thoughts/shared/handoffs/ and thoughts/shared/research/, then
   continue the Break 100 project."
3. Revise (or supersede) the research artifact for the amateur direction:
   confirm which benchmark data is actually accessible.
4. Then move to the `plan` skill: phase the gap-analysis work.
5. Decide deliverable format: a written findings report, a simple spreadsheet,
   or a small script that ingests benchmark tables and outputs the gaps.

## Open questions to resolve next session

- Which benchmark dataset is realistically accessible (free vs. paid)?
- Define "break 100" target precisely (e.g., scoring avg < 100, or a target
  handicap)?
- Output format: report, spreadsheet, or a small tool (the latter would also
  exercise the repo's `tdd → implement → polish` shipping workflow)?
