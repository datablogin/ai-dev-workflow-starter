# Codex Bootstrap Prompts

Use these prompts from the repository root after copying this starter kit into a
project.

If `AGENTS.md` is missing, generic, or stale, run
`prompts/agents-builder-interview.md` before the prompts below.

## Prompt 1: Orientation

```text
Read AGENTS.md and docs/standalone-analyst-ai-development-guide.md.

Then inspect:
- .agents/skills/
- thoughts/shared/templates/
- the README or main project docs
- available test, lint, format, and build commands

Do not edit files yet.

Report:
1. the workflow sequence
2. which skills are available
3. which project commands are known
4. what is missing before agents can safely implement work
```

## Prompt 2: Adapt The Operating Contract

```text
Read AGENTS.md and the main project docs.

Update AGENTS.md so it accurately describes this project:
- mission
- setup commands
- test commands
- review expectations
- privacy or data constraints
- files agents should read before implementation

Keep it concise. Do not add company-specific assumptions that are not true for
this repository. After editing, report the changes and any open questions.
```

## Prompt 3: Shape A Project

```text
Use the shape-work skill.

Goal:
<describe the project or analysis>

Context:
- <link or path to issue, brief, notebook, dataset description, or doc>

Constraints:
- Do not implement yet.
- Use the templates under thoughts/shared/templates/.
- Create lightweight but durable artifacts under thoughts/shared/.
- If the task is too broad for one PR or session, split it into phases.

Produce:
- research
- plan
- scorecard
- prompt pack

Report:
- artifact paths
- recommended first implementation step
- risks or assumptions that need human confirmation
```

## Prompt 4: Review The Plan

```text
Use the review-plan skill.

Plan:
- <path>

Optional linked artifacts:
- Research: <path>
- Scorecard: <path>

Goal:
Stress-test this plan before human approval and dispatch.

Constraints:
- Do not implement.
- Do not review code.
- Use fresh reviewer context if this session authored or substantially edited
  the plan.
- Keep reviewers read-only.
- Append the review verdict to the plan.
- On SHIP, set plan status to reviewed.
- Do not set status to approved. Approval is human-only.
- Persist the updated plan to the durable branch and verify it reached the
  remote.

Report:
- plan path and status
- verdict: SHIP or REVISE
- blocking findings
- advisory findings
- commit SHA
- next human approval step
```

## Prompt 5: Dispatch A Brief-Only Wave

```text
Use the dispatch-wave skill in brief-only mode.

Read:
- AGENTS.md
- Plan: <path>
- Scorecard: <path>
- Prompt pack: <path>

Goal:
Create a dispatch manifest before any implementation starts.

Constraints:
- The plan must already be reviewed and human-approved.
- If plan frontmatter is not `status: approved`, stop and report that it is
  not dispatchable yet.
- Do not create branches.
- Do not create worktrees.
- Do not launch background agents.
- Do not open PRs.
- Create and persist only a brief-only dispatch manifest under
  thoughts/shared/handoffs/.

Check:
- whether all assignments are specific enough to launch
- whether any assignments overlap on files/modules
- whether any assignments depend on each other
- whether every assignment has an independent verify-by check
- whether this should be NO_WAVE, SERIAL, PARALLEL, or STACKED

Report:
- manifest path
- commit SHA
- execution recommendation
- ready assignments
- blocked assignments
- human decisions needed
```

## Prompt 6: Implement One Phase

```text
Read AGENTS.md and the following artifacts:
- Plan: <path>
- Scorecard: <path>
- Prompt pack: <path>

Implement only this phase:
- Phase: <phase name>
- Branch: <branch name>
- Objective: <single concrete outcome>
- In scope: <paths>
- Out of scope: <paths>
- Tests/checks required: <commands or checks>

Workflow:
1. Use tdd for code behavior, or check-driven development for analysis.
2. Implement the minimum change.
3. Use polish before review.
4. Open or prepare review.
5. Stop before merge or delivery.

Report:
- files changed
- tests/checks run
- review status
- remaining risks
```

## Prompt 7: Review A PR Or Diff

```text
Use the review-pr skill.

Review:
- PR or branch: <number, URL, or branch>
- Scorecard: <path>

Check:
- tests and CI
- lint/format
- coverage or claim verification
- privacy/security risks
- unresolved comments
- whether the work matches the scorecard

Fix blocking issues if they are in scope. Report non-blocking issues with a
recommendation. Do not merge.
```

## Prompt 8: Retro After Delivery

```text
Use the retro-pr skill.

Delivered work:
- PR, branch, report, or artifact: <path or URL>
- Plan: <path>
- Scorecard: <path>

Create a retro under thoughts/shared/retros/.

Capture:
- what shipped
- what checks caught
- what humans corrected
- what to improve next time
- durable lessons for my personal knowledge base
```
