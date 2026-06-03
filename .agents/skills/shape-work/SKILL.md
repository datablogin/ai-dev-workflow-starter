---
name: shape-work
description: Turn a vague analysis or development goal into durable research, plan, scorecard, and prompt-pack artifacts before implementation. Use before multi-step work, client-facing analysis, data-sensitive work, automation, or any task where scope or verification is unclear.
---

# Shape Work

Use this skill before implementation. The output is planning context, not code.

## Inputs

- User goal, issue, brief, dataset description, report request, or bug report.
- Optional deadline, client/audience, target branch, or target files.

## Workflow

1. Orient:
   - Read `AGENTS.md`.
   - Run `git status --short --branch`.
   - Read relevant existing notes under `thoughts/shared/`.
2. Classify:
   - Tiny fix: short plan or scorecard note.
   - Single-session task: plan + scorecard.
   - Client-facing, data-sensitive, or multi-step work: research + plan +
     scorecard + prompt pack.
3. Research:
   - Inspect relevant files, data dictionaries, notebooks, scripts, docs, and
     issues.
   - Record findings in `thoughts/shared/research/YYYY-MM-DD-<slug>.md`.
4. Plan:
   - Split work into phases small enough to review.
   - Record files likely touched, tests/checks, non-goals, and rollback notes in
     `thoughts/shared/plans/YYYY-MM-DD-<slug>.md`.
5. Scorecard:
   - Define the primary outcome, delivery gates, acceptance criteria, scope
     guardrails, and regression risks.
   - Save to `thoughts/shared/scorecards/YYYY-MM-DD-<slug>.md`.
6. Prompt pack:
   - Write paste-ready briefs for each phase or agent.
   - Save to `thoughts/shared/prompts/YYYY-MM-DD-<slug>.md`.
7. Report:
   - List artifact paths.
   - Name the recommended first implementation step.
   - Name assumptions that need human confirmation.

## Rules

- Do not implement code while running shape-work.
- Use templates from `thoughts/shared/templates/` when available.
- Keep artifacts concise and specific.
- Ask only when a decision cannot be inferred safely.
