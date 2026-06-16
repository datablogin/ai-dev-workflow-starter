# Agent Operating Contract

This file tells AI agents how to work in this repository. Keep it short,
specific, and current.

## Mission

Make small, understandable, well-tested changes. Protect user trust, data
correctness, privacy, security, and the project history.

## Start Every Session

1. Read this file.
2. Run `git status --short --branch`.
3. Identify the active branch and any uncommitted user changes.
4. Read relevant files under `thoughts/shared/` before implementing.
5. If the task is vague, risky, or larger than one small change, shape the work
   before coding.

## Durable Work Notes

Use `thoughts/shared/` for durable planning and learning artifacts:

- `research/` - findings, audits, feasibility checks, data exploration.
- `plans/` - implementation plans and decisions.
- `scorecards/` - KPI, verification, and acceptance contracts.
- `prompts/` - paste-ready agent briefs.
- `handoffs/` - continuity notes between sessions.
- `retros/` - lessons after delivery.
- `templates/` - reusable artifact formats.

For important work, prefer this sequence:

```text
research -> plan -> scorecard -> prompt pack -> plan review -> human approval -> dispatch manifest -> launch approval -> implementation -> retro
```

## Required Shipping Workflow

For code changes:

```text
tdd -> implement -> polish -> review-pr -> human approval
```

- Use `tdd` before implementation for new behavior or bug fixes.
- Use `polish` before opening or requesting review.
- Use `review-pr` after a pull request or review diff exists.
- Do not merge without explicit human approval.

## Agent Dispatch Rules

For parallel work:

- Use `review-plan` before dispatching shaped work.
- Require human approval before `dispatch-wave`.
- Use `dispatch-wave` brief mode before launching multiple agents.
- Require explicit human launch approval before `dispatch-wave` launch mode.
- Use one branch or worktree per agent.
- Assign one objective and one scorecard per agent.
- Avoid overlapping files unless the plan explicitly says the work is stacked.
- Give each agent read-first files, in-scope paths, out-of-scope paths, tests,
  and an exit condition.

## Verification Bias

Prefer evidence over narration:

- tests for code behavior
- source queries for data claims
- screenshots or browser checks for UI changes
- logs for deploy or automation claims
- clear PR comments for review decisions

If a verification step cannot run locally, say why and name the closest
available substitute.

## Privacy And Data

- Do not commit secrets, tokens, credentials, private exports, or raw customer
  data.
- Use small sanitized fixtures for tests.
- Redact personal data in notes and examples.
- Ask before adding new external dependencies or services.
