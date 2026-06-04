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

| Assignment | Branch/Label | Objective | Scope | Tests/Checks | Status |
|---|---|---|---|---|---|
| <Name> | `<branch>` | <objective> | <paths> | <commands> | READY/NOT_READY |

## Overlap And Dependency Check

| Risk | Assignments | Severity | Recommendation |
|---|---|---|---|
| <Overlap/dependency> | <assignments> | Low/Medium/High | <action> |

## Launch Prompts

### Assignment: <Name>

```text
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
