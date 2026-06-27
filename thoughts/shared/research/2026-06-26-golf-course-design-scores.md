---
date: 2026-06-26
author: "quinnpark (with Claude Code)"
status: superseded
superseded_by: thoughts/shared/research/2026-06-26-break-100-amateur-gap-analysis.md
tags: [golf, causal-inference, course-design, feasibility]
---

> **SUPERSEDED (2026-06-26).** The project pivoted from a causal course-design ->
> pro-score study to an amateur "Break 100" stroke-gap diagnosis. See the pivot
> handoff `thoughts/shared/handoffs/2026-06-26-golf-project-pivot.md` and the
> replacement research artifact
> `thoughts/shared/research/2026-06-26-break-100-amateur-gap-analysis.md`.
> Kept on disk intentionally: the "correlation != causation" lesson below still
> informs the new (deliberately descriptive, non-causal) scoping.

# Research: Causal Effect of Course Design on Golf Scores

## Question

Do specific, fixed **course-design** features — (a) layout & length and
(b) hazards & green complexity — *causally* affect **professional tournament
scores**, beyond what player skill, field strength, and conditions explain?

Causal, not correlational: we want to estimate the effect of a design feature
on score holding confounders constant, not just observe that hard-looking
courses produce high scores.

## Context

- Project goal: U.S. golf courses, design → scoring relationships.
- Design scope (chosen): **Layout & length** (yardage, par, hole distances,
  dogleg count) + **Hazards & green complexity** (bunkers, water, rough,
  green size/slope/speed).
- Outcome scope (chosen): **Pro tournament scores** (PGA/LPGA-level events).
- Workflow stage: `shape-work` → research. No analysis/code yet.
- This is the first artifact created in this repo; establishes the pattern.

## Candidate Data Sources

| Source | Provides | Access / Notes | Confidence |
|---|---|---|---|
| PGA Tour ShotLink | Shot-level & round scores per event/course | Gold standard; full access is restricted/academic-licensed | Medium |
| Data Golf (datagolf.com) | Round scores, strokes-gained, course history | Paid API/subscription; well-structured | High |
| PGA Tour stats site | Aggregate course scoring averages | Free, scrapable; coarse (course-level, not hole-level) | High |
| USGA Course & Slope Rating | Difficulty rating derived from design | Public lookups; **already a design-derived metric** (see risk) | High |
| Course design specs (yardage books, GIS, architect DBs) | Hole length, par, bunker/water counts, green sq-ft | Fragmented; manual/scraped per course | Low |
| Weather APIs (historical) | Wind, temp, precip per event-day | Available (NOAA, etc.); key confounder control | Medium |

## Findings

| Finding | Evidence | Confidence |
|---|---|---|
| Score data for pros is the most accessible, cleanest leg of the project | Data Golf + PGA stats are structured and public/affordable | High |
| **Design-feature data is the bottleneck**, not score data | No single DB couples green size/slope + bunker counts to courses at scale | High |
| Course difficulty is partly *endogenous to setup*, not just fixed design | Same course plays differently by tee/pin/firmness week to week | High |
| A panel structure is feasible: many courses × many events × many players | Tour visits same courses yearly; enables within-course variation | Medium |
| USGA rating as an outcome would be near-circular | Rating is computed from design features → predicting design with design | High |

## Risks

- **Correlation ≠ causation (the central risk).** Hard courses get tough setups,
  draw stronger fields, and host majors — all confounded with design. Naive
  regression of score on bunkers will be badly biased.
- **Selection / endogeneity.** Architects design difficulty intentionally;
  tournament courses are a non-random sample of all courses.
- **Confounders:** weather, field strength, pin/tee setup, green firmness,
  season, altitude. Must be measured or differenced out.
- **Feature measurement cost.** Hand-collecting green-complexity data for many
  courses may dominate the project's effort budget.
- **"Causal" may be unachievable from observational data alone** — likely the
  honest deliverable is *credible causal-leaning estimates with stated
  assumptions*, not proof.

## Open Questions

- Scope of courses/events: a few flagship courses studied deeply, or a broad
  panel of all Tour stops? (Affects feasibility a lot.)
- Unit of analysis: hole-level, round-level, or course-event-level?
- Which identification strategy is realistic given the data? (course fixed
  effects, renovation natural experiments, weather as instrument?)
- Outcome metric: raw score, score-to-par, or strokes-gained (skill-adjusted)?
- Is paid data (Data Golf) in budget, or scrape-only?

## Recommendation

Proceed, but **reframe the headline from "find causal relationships" to
"build a credible causal-inference study design and estimate effects where the
data supports it."** The cleanest path:

1. Use **strokes-gained or score-to-par** as the outcome (skill/field-adjusted).
2. Exploit **within-course variation** — same course over many years, and
   especially **course renovations** as natural experiments (a redesign changes
   bunkers/length while the course identity holds constant).
3. Use **course fixed effects + weather controls** to fight confounding.
4. Treat **design-feature data collection as the project's hardest sub-task** —
   scope it early and narrowly (start with a handful of well-documented courses).

Suggested next step in the workflow: `plan` + `scorecard` to turn this into
phased, verifiable work — but first confirm the open questions above.
