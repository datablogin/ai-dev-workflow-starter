---
name: retro-pr
description: Capture lessons after a PR, analysis, automation, or client-facing deliverable. Produces and persists a retro under thoughts/shared/retros, then identifies durable lessons for AGENTS.md, templates, skills, or a personal memory system.
---

# Retro PR

Use this after delivery, especially when the work involved data, automation,
client-facing outputs, or review findings.

If the current project ships its own `retro-pr` skill (e.g. in
`.claude/skills/retro-pr/`), prefer it — it carries repo-specific review tools,
artifact locations, and commit policy.

## Inputs

- PR URL/number, branch, report path, notebook, or delivered artifact.
- Optional plan, scorecard, prompt pack, dispatch manifest, and review notes.

## Workflow

1. Orient:
   - Read `AGENTS.md` and `CLAUDE.md` if present.
   - Run `git status --short --branch`.
   - Identify the delivered artifact, PR, branch, or report.
2. Inspect what shipped:
   - PR title/body/files/commits/comments/checks when available.
   - Linked plan, scorecard, prompt pack, dispatch manifest, and review notes.
   - Tests/checks, reviewer findings, CI failures, and human decisions.
3. Extract lessons:
   - outcome
   - what went well
   - issues caught
   - what was missed
   - process notes
   - lessons to carry forward
4. Write:
   - `thoughts/shared/retros/YYYY-MM-DD-<slug>.md`
   - Use `thoughts/shared/templates/retro-template.md` if available.
5. Persist:
   - Commit the retro to the repo's durable branch (usually `main`) and push.
   - If the current checkout is a feature branch or dirty, use a throwaway
     worktree instead of stashing or switching branches.
   - Verify the commit landed on the remote. A local-only retro is not done.
6. Carry lessons forward:
   - `AGENTS.md`
   - templates
   - skills
   - personal memory notes
   - backlog/follow-up issues, if needed

## Rules

- Do not rewrite delivered code while running the retro.
- Keep repo-specific details in the retro.
- Put reusable lessons in the user's personal memory system only if they apply
  beyond this one project.
- Do not bury process changes only in the retro; propose the concrete file or
  skill that should change.

## Output Summary

```text
Retro complete.
  Delivered: <PR/report/artifact>
  Retro: <path> (commit <sha>, verified on remote)
  Lessons for memory: <N>
  Proposed workflow updates: <summary>
  Follow-ups: <summary>
```
