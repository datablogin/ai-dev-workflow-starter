---
name: dispatch-wave
description: Convert approved shaped-work artifacts into a dispatch manifest, then optionally launch explicitly selected assignments after separate human launch approval. Default mode is brief-only. Use after review-plan and human approval when a plan or prompt pack may require multiple agents, phases, branches, or careful sequencing.
---

# Dispatch Wave

Use this after `shape-work` → `review-plan` → human approval, and before
implementation, when work may need one or more agents, branches, PRs, or
sessions.

If the current project ships its own `dispatch-wave` skill (e.g. in
`.claude/skills/dispatch-wave/`), prefer it — it carries repo-specific
operational rules and the project's agent preamble.

Default mode is `brief`: prepare or update the manifest and stop.

Launch mode is explicit and separately approval-gated: launch only the
assignments the human names, from an existing manifest, through the requested
harness or manual paste. Plan approval means "this work is worth doing";
launch approval means "start these assignments now." Never infer one from the
other.

## Pipeline Position

```
shape-work ─► review-plan ─► human approval ─► dispatch-wave brief ─► human launch approval ─► dispatch-wave launch ─► agents
                             (status: approved)  (manifest)             (assignment selection)      (explicit mode)
```

## Inputs

Brief mode:

- Plan path (required).
- Companion artifacts the plan's tier produced (scorecard, prompt pack) when
  they exist. Do not demand artifacts the tier never called for, but a
  multi-agent wave without a prompt pack is almost certainly `NOT_READY`.
- Optional maximum number of agents, branch naming pattern, or target output
  path.

Launch mode:

- Dispatch manifest path (required).
- Assignment name(s) or `all-ready` (required).
- Harness: `manual-paste`, `codex`, `claude-code`, `cursor`, or a repo-specific
  orchestrator skill (required).
- Optional dry-run flag. If unsure, dry-run.

## Non-Goals

In all modes, do not:

- merge anything
- deliver to a customer or external stakeholder
- install tools or dependencies unless the user explicitly approves
- launch assignments that are not `READY`
- launch assignments not named by the user

**One persistence exception:** the dispatch manifest itself is a planning
artifact and MUST be committed to the durable branch (usually `main`) and
pushed — via a throwaway worktree if you are on a feature branch, never a
stash. An uncommitted manifest stranded on a branch is a failed run.

## Mode Selection

- If the user asks to "dispatch", "prepare", "brief", "make a manifest", or
  supplies plan/scorecard/prompt paths, run **brief mode**.
- If the user asks to "launch", "start agents", "run assignment X", or supplies
  a dispatch manifest plus assignment selection, run **launch mode**.
- If launch intent is ambiguous, run brief mode or ask for explicit launch
  approval.

## Brief Workflow

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
    the launch options. Stop before launch unless the user explicitly asked
    for launch mode in the same request and supplied assignment selection.

## Launch Workflow

Launch mode starts only after brief mode produced a manifest and a human
explicitly selected what to launch.

1. Orient:
   - Read `AGENTS.md` and the dispatch manifest.
   - Run `git status --short --branch`.
   - Confirm the requested harness: `manual-paste`, `codex`, `claude-code`,
     `cursor`, or repo-specific orchestrator.
2. Validate launch gate:
   - Manifest approval gate passed.
   - Selected assignments exist and are `READY`.
   - No selected assignment has unresolved overlap/dependency blockers.
   - Each selected assignment has branch/session label, scope, tests/checks,
     exit condition, and verify-by.
   - Human selected the assignments in this turn or in a clearly referenced
     approval message. Do not rely on plan approval alone.
3. Decide launch action:
   - `manual-paste`: print the exact prompts and stop.
   - `codex`, `claude-code`, `cursor`: if a callable thread/subagent/harness
     tool is available, use it only after confirming selected assignments and
     reporting the launch plan; otherwise print exact prompts plus launch
     instructions and stop.
   - repo-specific orchestrator: hand off to that skill/tool if available;
     otherwise print the command/prompt to run it.
4. Record launch status in the manifest or a follow-up handoff when the repo's
   planning policy allows it:
   - selected assignments
   - launch mode/harness
   - launched session/thread/branch labels or manual-paste output
   - supervisor verify-by commands
   - any assignments skipped and why
5. Report:
   - assignments launched or prepared
   - harness used
   - prompts/session labels
   - supervisor verification commands
   - anything not launched and why

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

Brief mode:

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

Launch mode:

```text
Dispatch wave launch complete.
  Manifest: <path>
  Requested assignments: <names>
  Harness: manual-paste | codex | claude-code | cursor | <orchestrator>
  Launched/prepared: <N>
  Skipped: <N> — <reasons>
  Supervisor verify-by:
    - <assignment>: <command or URL>
```
