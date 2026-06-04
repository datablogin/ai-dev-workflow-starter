---
name: dispatch-wave
description: Convert shaped work artifacts into a brief-only dispatch manifest. Use after shape-work when a plan or prompt pack may require multiple agents, phases, branches, or careful sequencing. Validates readiness, file overlap, dependencies, and per-agent prompts without launching agents or creating branches.
---

# Dispatch Wave

Use this after `shape-work` and before implementation when work may need more
than one agent, branch, PR, or session.

Brief-only mode is the only supported mode. This skill prepares the wave; it
does not launch it.

## Inputs

- Plan path.
- Scorecard path.
- Prompt pack path.
- Optional maximum number of agents.
- Optional preferred branch naming pattern.
- Optional target output path under `thoughts/shared/handoffs/`.

## Non-Goals

Do not:

- create branches
- create worktrees
- start background agents or threads
- push commits
- open PRs
- merge anything
- install tools or dependencies

## Workflow

1. Orient:
   - Read `AGENTS.md`.
   - Run `git status --short --branch`.
   - Read the supplied plan, scorecard, and prompt pack.
2. Validate artifacts:
   - Confirm all three artifacts exist.
   - Confirm the plan phases match the prompt-pack assignments.
   - Confirm each assignment has objective, scope, tests/checks, and exit
     condition.
   - Flag missing scorecard gates or unclear acceptance criteria.
3. Extract assignments:
   - Build one row per proposed agent or phase.
   - Capture branch name, objective, read-first files, in-scope files,
     out-of-scope files, tests/checks, and exit condition.
4. Check dispatch safety:
   - Identify overlapping in-scope files or modules.
   - Identify dependencies between assignments.
   - Identify shared setup, credentials, fixtures, or data requirements.
   - Identify assignments that are too vague to launch.
5. Recommend execution shape:
   - `NO_WAVE`: one assignment; run the prompt directly.
   - `SERIAL`: assignments depend on one another or overlap heavily.
   - `PARALLEL`: assignments are independent with low file overlap.
   - `STACKED`: assignments can run in order on stacked branches after human
     approval.
6. Produce launch prompts:
   - Write a paste-ready prompt for each assignment.
   - Include read-first files, branch name, scope, tests/checks, workflow, and
     report format.
   - Include "stop before merge or delivery" unless the user explicitly says
     otherwise.
7. Write dispatch manifest:
   - Save to `thoughts/shared/handoffs/YYYY-MM-DD-<slug>-dispatch-wave.md`
     unless the user asks for chat-only output.
   - Use `thoughts/shared/templates/dispatch-wave-template.md` if available.
8. Report:
   - Manifest path.
   - Recommended execution shape.
   - Assignments ready to launch.
   - Blockers before launch.
   - Human decisions needed.

## Readiness Rules

An assignment is launch-ready only when it has:

- clear objective
- branch or session label
- read-first files
- in-scope and out-of-scope boundaries
- tests or verification checks
- scorecard target
- exit condition

If any assignment is missing these, mark it `NOT_READY` and do not recommend
launching it.

## Output Summary

```text
Dispatch wave brief complete.
  Manifest: <path or chat-only>
  Execution shape: NO_WAVE | SERIAL | PARALLEL | STACKED
  Ready assignments: <N>
  Not-ready assignments: <N>
  Overlap risks: <summary>
  Dependency risks: <summary>
  Human decisions needed: <summary>
```
