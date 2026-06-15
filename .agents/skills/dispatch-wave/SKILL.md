---
name: dispatch-wave
description: Convert approved shaped-work artifacts into a brief-only dispatch manifest. Use after review-plan and human approval when a plan or prompt pack may require multiple agents, phases, branches, or careful sequencing. Validates readiness, file overlap, dependencies, and per-agent prompts without launching agents or creating branches. Refuses plans that are not human-approved.
---

# Dispatch Wave

Use this after `shape-work` → `review-plan` → human approval, and before
implementation, when work may need more than one agent, branch, PR, or session.

If the current project ships its own `dispatch-wave` skill (e.g. in
`.claude/skills/dispatch-wave/`), prefer it — it carries repo-specific
operational rules and the project's agent preamble.

Brief-only mode is the only supported mode. This skill prepares the wave; it
does not launch it. Launching belongs to the project's orchestrator skill
(e.g. sprint-orchestrator) or a direct prompt paste for single assignments.

## Pipeline Position

```
shape-work ─► review-plan ─► human approval ─► dispatch-wave ─► orchestrator ─► agents
                             (status: approved)  (this skill)
```

## Inputs

- Plan path (required).
- The companion artifacts the plan's tier produced (scorecard, prompt pack)
  when they exist — do not demand artifacts the tier never called for, but a
  multi-agent wave without a prompt pack is almost certainly `NOT_READY`.
- Optional maximum number of agents, branch naming pattern, or target output
  path.

## Non-Goals

Do not:

- create feature branches or implementation worktrees
- start background agents or threads
- open PRs or merge anything
- install tools or dependencies
- begin any implementation work

**One persistence exception:** the dispatch manifest itself is a planning
artifact and MUST be committed to the durable branch (usually `main`) and
pushed — via a throwaway worktree if you are on a feature branch, never a
stash. An uncommitted manifest stranded on a branch is a failed run.

## Workflow

1. Orient: read `AGENTS.md` (and `CLAUDE.md` if present), run
   `git status --short --branch`, read the plan and companion artifacts.
2. Approval gate (hard precondition):
   - The plan's frontmatter must read `status: approved`. `draft` or
     `reviewed` means the human has not signed off — stop and report "plan
     not approved" instead of building a manifest.
   - A plan whose `## Review` section ends in an unresolved REVISE verdict is
     never dispatchable regardless of status.
   - Approval is human-only. Never set `status: approved` yourself; do not
     proceed on a verbal "looks fine" without the frontmatter flip (ask the
     user to confirm, then set it).
3. Validate artifacts: the tier's artifacts exist, plan phases match
   prompt-pack assignments, each assignment has objective, scope,
   tests/checks, and exit condition.
4. Extract assignments: one row per agent/phase — branch, objective,
   read-first files, in/out-of-scope files, tests/checks, exit condition,
   and verify-by.
5. Check dispatch safety: overlapping in-scope files, dependencies between
   assignments, shared setup/credentials/fixtures, assignments too vague to
   launch.
6. Define the supervisor verification contract: every assignment gets a
   **verify-by** — the literal command or URL the supervisor runs to confirm
   the exit condition independently of the agent's self-report (PR state at a
   full SHA, `git ls-remote` for pushed work, an API check, a query). Agent
   self-reports are claims, not evidence; an unverifiable exit condition is
   `NOT_READY`.
7. Recommend execution shape: `NO_WAVE` | `SERIAL` | `PARALLEL` | `STACKED`.
8. Produce launch prompts: read-first files, branch, scope, tests/checks,
   workflow, report format, "stop before merge or delivery" unless the user
   says otherwise — and **prepend a standard agent preamble** covering the
   project's operational rules. At minimum:
   - never merge or deliver; report final state and stop
   - never end a turn waiting on an external event — poll to a deadline,
     re-trigger once, then proceed and note the skipped wait
   - verify CI/work-state with commands, not bot/watcher exit codes
   - final message must separate what was verified from what is claimed,
     with the commands a supervisor can run to confirm
9. Write the manifest (use the project's dispatch-wave template if one
   exists), then commit and push it; verify the commit is on the remote.
10. Report: manifest path + commit SHA, execution shape, ready/not-ready
    assignments, overlap and dependency risks, human decisions needed, and
    the launch handoff (orchestrator skill for multi-agent, direct paste for
    `NO_WAVE`).

## Readiness Rules

An assignment is launch-ready only when it has:

- clear objective
- branch or session label
- read-first files
- in-scope and out-of-scope boundaries
- tests or verification checks
- scorecard target (when the tier produced a scorecard)
- exit condition
- verify-by (independent supervisor check)

If any assignment is missing these, mark it `NOT_READY` and do not recommend
launching it.

## Output Summary

```text
Dispatch wave brief complete.
  Manifest: <path>  (commit <sha>, verified on remote)
  Execution shape: NO_WAVE | SERIAL | PARALLEL | STACKED
  Ready assignments: <N>
  Not-ready assignments: <N>
  Overlap risks: <summary>
  Dependency risks: <summary>
  Human decisions needed: <summary>

To launch: <orchestrator skill> with this manifest
           (or paste assignment 1's prompt directly if NO_WAVE)
```
