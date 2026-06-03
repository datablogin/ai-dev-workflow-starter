---
name: retro-pr
description: Capture lessons after a PR, analysis, automation, or client-facing deliverable. Produces a retro under thoughts/shared/retros and identifies durable lessons for a personal memory system.
---

# Retro PR

Use this after delivery, especially when the work involved data, automation,
client-facing outputs, or review findings.

## Inputs

- PR URL/number, branch, report path, notebook, or delivered artifact.
- Optional plan and scorecard paths.

## Workflow

1. Inspect what changed or shipped.
2. Read the plan and scorecard, if available.
3. Review tests, checks, comments, review notes, and human decisions.
4. Capture:
   - outcome
   - what went well
   - issues caught
   - what was missed
   - process notes
   - lessons to carry forward
5. Write:
   - `thoughts/shared/retros/YYYY-MM-DD-<slug>.md`
6. Recommend updates:
   - `AGENTS.md`
   - templates
   - skills
   - personal memory notes

## Rules

- Do not rewrite delivered code while running the retro.
- Keep repo-specific details in the retro.
- Put reusable lessons in the user's personal memory system only if they apply
  beyond this one project.
