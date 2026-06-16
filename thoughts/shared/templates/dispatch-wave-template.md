---
date: YYYY-MM-DD
author: "<agent or human>"
status: draft
plan: ""
scorecard: ""
prompt_pack: ""
tags: []
---

# Dispatch Wave: <Title>

Mode: `brief`

## Approval Gate

| Check | Required | Status | Notes |
|---|---|---|---|
| Plan status | `approved` | PASS/FAIL | <notes> |
| Review verdict | no unresolved `REVISE` | PASS/FAIL | <notes> |
| Human approval | recorded before dispatch | PASS/FAIL | <notes> |

## Recommendation

Execution shape: `NO_WAVE | SERIAL | PARALLEL | STACKED`

Why:
- <Reason>

## Artifact Check

| Artifact | Path | Status | Notes |
|---|---|---|---|
| Plan | <path> | PASS/FAIL | <notes> |
| Scorecard | <path> | PASS/FAIL | <notes> |
| Prompt pack | <path> | PASS/FAIL | <notes> |

## Assignment Table

| Assignment | Branch/Label | Objective | Scope | Tests/Checks | Verify-By | Status |
|---|---|---|---|---|---|---|
| <Name> | `<branch>` | <objective> | <paths> | <commands> | <independent supervisor check> | READY/NOT_READY |

## Overlap And Dependency Check

| Risk | Assignments | Severity | Recommendation |
|---|---|---|---|
| <Overlap/dependency> | <assignments> | Low/Medium/High | <action> |

## Launch Prompts

### Assignment: <Name>

```text
Operational rules:
- Never merge or deliver; report final state and stop.
- Do not end your turn waiting on an external event. Poll to a reasonable
  deadline, retry once if appropriate, then report the remaining wait clearly.
- Verify CI/work-state with commands, not self-report.
- Your final message must separate what you verified from what you claim and
  include supervisor verification commands.

Read AGENTS.md and the linked shape-work artifacts.

Plan: <path>
Scorecard: <path>
Prompt pack: <path>

Assignment:
- Branch/label: <branch>
- Objective: <objective>
- Read first: <paths>
- In scope: <paths>
- Out of scope: <paths>
- Tests/checks required: <commands>
- Scorecard target: <target>
- Exit condition: <condition>
- Verify-by: <independent supervisor check>

Workflow:
1. Use tdd for code behavior, or check-driven development for analysis.
2. Implement only this assignment.
3. Use polish before review.
4. Prepare review.
5. Stop before merge or delivery.

Report:
- files changed
- tests/checks run
- review status
- remaining risks
```

## Human Decisions Needed

- <Decision>

## Final Dispatch Status

- Ready to launch now: <yes/no>
- Recommended first assignment: <assignment>
- Launch method: <orchestrator skill or direct paste>

## Launch Approval

Launch approval is separate from plan approval.

| Field | Value |
|---|---|
| Approved assignments | <assignment names or pending> |
| Approved harness | manual-paste / codex / claude-code / cursor / orchestrator / pending |
| Approved by | <human/date or pending> |
| Dry run first | yes/no |

## Launch Status

Fill this only after explicit launch approval.

| Assignment | Harness | Status | Session/Branch/Prompt | Verify-By |
|---|---|---|---|---|
| <Name> | <harness> | PREPARED/LAUNCHED/SKIPPED | <label or prompt reference> | <command or URL> |
