---
name: review-plan
description: >
  Fresh-context adversarial review of an implementation plan BEFORE human
  approval and dispatch. Spawns independent reviewer agents (feasibility,
  verifiability, scope/risk lenses) that critique the plan against repo
  reality, then appends a verdict to the plan doc and advances its status to
  `reviewed`. Use after shape-work, before dispatch-wave, or on any stored
  plan that is about to be executed.
---

# Review Plan

Pre-critique a plan so the human reviews a stress-tested document instead of a
first draft. Reviews planning artifacts only — not code, and it implements
nothing.

If the current project ships its own `review-plan` skill (e.g. in
`.claude/skills/review-plan/`), prefer it.

## Plan Status Lifecycle

```
draft  ──/review-plan──►  reviewed  ──human──►  approved  ──►  /dispatch-wave
```

Only a human moves a plan to `approved`.

## The One Hard Rule

**The reviewers must not be the author.** If this session wrote the plan,
delegate the review to fresh subagents via the Agent tool. You dispatch and
synthesize; you do not review your own plan.

## Workflow

1. Read the plan (default: the one the user names, else the newest in the
   repo's plans location) plus linked research/scorecard. Add
   `status: draft` frontmatter if missing.
2. Launch three read-only reviewer agents in parallel, each with one lens and
   no conversation context:
   - **Feasibility** — named files/tables/services exist; phase file sets
     don't overlap; assumptions match repo reality and recent history.
   - **Verifiability** — every success criterion and data claim names a
     runnable check (command, query, CI job); flag anything unverifiable.
   - **Scope & risk** — missing rollback/migrations/secrets/comms; non-goals
     stated; most-plausible regression per phase.
   Findings must cite repo evidence and carry severity `BLOCKING` or
   `ADVISORY`.
3. Synthesize: drop evidence-free findings, dedupe. Verdict **SHIP** (no
   blocking) or **REVISE** (list the required revisions; don't rewrite the
   plan unless asked — if asked, apply agreed edits and re-review once).
4. Append a `## Review (YYYY-MM-DD)` section (verdict + findings table) to
   the plan doc. On SHIP, set frontmatter `status: reviewed`; a REVISE plan
   stays `draft`.
5. Persist the updated plan the same way shape-work persists artifacts:
   commit to the durable branch and push (throwaway worktree if on a feature
   branch), then verify the commit is on the remote.
6. Report: plan path + status, verdict, blocking/advisory findings, commit
   SHA, and the next step — human approval (`status: approved`), then
   dispatch-wave.

## Rules

- Reviewers are read-only: no commits, branches, or code edits.
- Never auto-advance a plan to `approved` — human-only, even on SHIP.
- Stale plans deserve a fresh pass before execution; repo reality drifts.
