---
name: shape-work
description: Turn a vague analysis or development goal into durable research, plan, scorecard, and prompt-pack artifacts before implementation. Use before multi-step work, client-facing analysis, data-sensitive work, automation, or any task where scope or verification is unclear.
---

# Shape Work

Use this skill before implementation. The output is planning context, not code.

If the current project ships its own `shape-work` skill (e.g. in
`.claude/skills/shape-work/`), prefer it — it encodes repo-specific artifact
locations and commit policy that override this generic version.

## Inputs

- User goal, issue, brief, dataset description, report request, or bug report.
- Optional deadline, client/audience, target branch, or target files.

## Workflow

1. Orient:
   - Read `AGENTS.md` (and `CLAUDE.md` if present).
   - Run `git status --short --branch`.
   - Read relevant existing notes under the repo's planning-artifact location
     (`thoughts/shared/` where that convention exists; otherwise `docs/` or the
     repo's equivalent).
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
7. Persist:
   - Commit the artifacts to the repo's durable branch (usually `main`) and
     **push**. A local-only commit is not a handoff — verify with
     `git ls-remote` that the commit is on the remote.
   - Never leave planning artifacts uncommitted on a feature branch or
     disposable worktree; branch deletion and worktree cleanup destroy them.
   - From a feature branch or dirty checkout, do not stash or switch branches.
     Use a throwaway worktree:

     ```bash
     git fetch origin main
     git worktree add /tmp/shape-thoughts origin/main
     # write the artifacts inside /tmp/shape-thoughts, then:
     git -C /tmp/shape-thoughts add <artifact paths>
     git -C /tmp/shape-thoughts commit -m "Add <slug> planning artifacts"
     git -C /tmp/shape-thoughts push origin HEAD:main
     git worktree remove /tmp/shape-thoughts
     ```

   - If the push is rejected (branch protection), stop and ask the user — do
     not present unpushed artifacts as complete.
8. Report:
   - State the tier you classified, and list **only the artifacts that tier
     called for** — do not pad the report or create extras to fill it out.
   - Include the commit SHA and confirm it is on the remote.
   - Note the pipeline ahead: `/review-plan <plan>` (fresh-agent critique,
     sets `status: reviewed`) → human approval (`status: approved`,
     human-only) → `/dispatch-wave` (refuses unapproved plans). Name the
     recommended first implementation step after approval.
   - Name assumptions that need human confirmation.

## Rules

- Do not implement code while running shape-work.
- Use templates from `thoughts/shared/templates/` when available.
- Keep artifacts concise and specific.
- Ask only when a decision cannot be inferred safely.
