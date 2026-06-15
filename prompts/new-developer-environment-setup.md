# New Developer Environment Setup Prompt

Paste this into Codex from the repository root after cloning this starter kit or
after copying the starter kit into a project repository.

```text
You are helping me set up a standalone AI development workflow on this machine
and in this repository.

Read first:
- README.md
- AGENTS.md
- docs/standalone-analyst-ai-development-guide.md
- prompts/agents-builder-interview.md
- prompts/codex-bootstrap-prompts.md

Then inspect:
- .agents/skills/
- thoughts/shared/templates/
- git status and remotes
- README or project documentation
- package manager files such as package.json, pyproject.toml, uv.lock,
  requirements.txt, pnpm-lock.yaml, package-lock.json, yarn.lock, Makefile, or
  justfile
- CI files under .github/workflows/, if present
- .env.example, if present

First, determine which situation we are in:

1. Starter-kit repo only:
   I am still inside the AI workflow starter repository and have not copied it
   into a real project yet.

2. Target project repo:
   I am inside the real project where this workflow should be installed or
   adapted.

3. Unclear:
   The repo state does not make it obvious whether this is the starter kit or a
   target project.

If situation 1:
- Do not make changes.
- Explain how to copy this starter kit into a real project.
- Tell me the next command or prompt to run from the target project root.

If situation 3:
- Do not make changes.
- Ask me which repository should receive the workflow.

If situation 2, continue with setup.

If AGENTS.md is missing, generic, copied from the starter kit without project
adaptation, or stale, stop and recommend running
prompts/agents-builder-interview.md before continuing.

Setup goals:
- Make Codex able to read repo instructions from AGENTS.md.
- Make Codex able to discover workflow skills from .agents/skills/.
- Make durable planning folders available under thoughts/shared/.
- Identify the project's real install, test, lint, format, build, and review
  commands.
- Adapt AGENTS.md to this project without adding false assumptions.
- Preserve all user work and avoid committing secrets or private data.

Safety rules:
- Run git status --short --branch before editing.
- Do not overwrite existing AGENTS.md, .agents/skills, or thoughts/shared files
  without showing the diff plan first.
- Do not install dependencies, change shell profiles, create global config,
  create a GitHub repo, push commits, or add paid/external services without my
  explicit approval.
- Do not print, copy, or commit secrets.
- If a .env file exists, leave it untracked and untouched unless I explicitly
  ask for help.
- If environment variables are needed, create or update .env.example with
  placeholder names only.

Implementation steps for situation 2:

1. Orientation
   - Run git status --short --branch.
   - Run git remote -v.
   - Run gh auth status if GitHub CLI is installed.
   - List .agents/skills and confirm each skill has a SKILL.md.
   - List thoughts/shared/templates and confirm the workflow templates exist.

2. Project command discovery
   - Inspect package manager and CI files.
   - Identify install commands, test commands, lint commands, format commands,
     build commands, and any coverage commands.
   - Do not run network install commands yet. Propose them first.

3. Workflow installation check
   - Confirm AGENTS.md exists and is project-specific.
   - Confirm .agents/skills contains:
     - shape-work
     - review-plan
     - dispatch-wave
     - tdd
     - polish
     - review-pr
     - retro-pr
   - Confirm thoughts/shared contains:
     - research
     - plans
     - scorecards
     - prompts
     - handoffs
     - retros
     - templates
   - Create missing directories or starter files only after confirming they are
     missing and safe to add.

4. Adapt AGENTS.md
   Update AGENTS.md so it includes:
   - project mission
   - setup commands
   - test/lint/format/build commands
   - privacy and data rules
   - review workflow
   - where planning artifacts live
   - what agents should read before changing files

   Keep it concise. If you are unsure about a command or project rule, mark it
   as "TBD" rather than inventing it.

5. Verify
   - Run non-destructive checks only, such as git status and file listings.
   - If dependencies are already installed, run the safest available smoke
     check or test command.
   - If dependencies are not installed, ask before installing them.

6. Create a setup handoff
   If edits were made, create:
   thoughts/shared/handoffs/YYYY-MM-DD-new-developer-environment-setup.md

   Include:
   - commands discovered
   - files added or changed
   - checks run
   - credentials or manual setup still needed
   - recommended first shape-work pilot

7. Final report
   Report:
   - situation detected
   - files changed
   - commands run
   - commands I should run manually, if any
   - whether Codex skills are ready
   - whether GitHub CLI is authenticated
   - recommended first project to run through shape-work

Do not commit or push unless I explicitly ask you to.
```
