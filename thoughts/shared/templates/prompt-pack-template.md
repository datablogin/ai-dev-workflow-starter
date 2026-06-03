---
date: YYYY-MM-DD
author: "<agent or human>"
status: draft
plan: ""
scorecard: ""
tags: []
---

# Prompt Pack: <Title>

## Global Rules

- Read `AGENTS.md` before changing files.
- Read the linked plan and scorecard.
- Work only on the assigned phase.
- Preserve user changes.
- Report commands/checks run.
- Stop before merge or final delivery unless explicitly approved.

## Agent Brief: <Phase Or Task>

Branch: `<branch-name>`

Read first:
- `<path>`

Objective:
- <Concrete deliverable>

Scope:
- In: <Allowed files/modules>
- Out: <Forbidden files/modules>

Tests or checks required:
- <Command or verification>

Exit condition:
- <What must be true before review>

Workflow:
1. Use tdd or check-driven development.
2. Implement the minimum change.
3. Use polish.
4. Prepare review.
5. Report results and remaining risks.
