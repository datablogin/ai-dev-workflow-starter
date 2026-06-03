# AGENTS.md Builder Interview Prompt

Paste this into Codex from the root of the project repository where you want to
build or improve `AGENTS.md`.

Use this before the environment setup prompt when `AGENTS.md` is missing,
generic, copied from the starter kit, or no longer accurate.

```text
You are helping me build a practical AGENTS.md operating contract for this
repository.

Your job is to interview me, inspect the repository, draft AGENTS.md, and help
me review it before any file is changed.

Read first, if present:
- README.md
- AGENTS.md
- docs/standalone-analyst-ai-development-guide.md
- prompts/new-developer-environment-setup.md
- prompts/codex-bootstrap-prompts.md
- package manager files such as package.json, pyproject.toml, uv.lock,
  requirements.txt, pnpm-lock.yaml, package-lock.json, yarn.lock, Makefile, or
  justfile
- CI files under .github/workflows/
- .env.example

Safety rules:
- Start with git status --short --branch.
- Do not edit files until you have shown me the proposed AGENTS.md outline and
  I have approved it.
- Do not install dependencies, change secrets, change global config, push
  commits, or create remote resources.
- Do not invent commands or rules. If something is unknown, mark it as TBD.
- Do not print or inspect secret values. If .env exists, only note that it
  exists and whether it appears tracked or untracked.

Step 1: Inspect before asking

Infer what you can from the repository:
- project name and purpose
- likely stack and package manager
- install/test/lint/format/build commands
- CI checks
- existing docs
- existing data/privacy signals
- whether .agents/skills and thoughts/shared are present

Report what you inferred and what still needs a human answer.

Step 2: Interview me in small groups

Ask one group of questions at a time. Keep each group to at most 5 questions.
After I answer a group, summarize the answers and move to the next group.

Group A: Project identity
- What is the project called?
- Who uses it or depends on it?
- What outcome should this repository protect or create?
- What would be costly or embarrassing if an agent broke it?
- Is this mostly code, analysis, automation, documentation, or a mix?

Group B: Development commands
- What command installs dependencies?
- What command runs the fastest useful test or smoke check?
- What command runs the full test suite?
- What command runs lint or static checks?
- What command formats code or docs?

Group C: Data, privacy, and secrets
- Does this repo handle personal data, client data, financial data, health data,
  credentials, or private exports?
- Which files or folders must agents never commit?
- Are sanitized fixtures available for tests?
- Are there environment variables agents should know by name, without values?
- Are there external systems agents should avoid touching without permission?

Group D: Agent permissions
- May agents create branches?
- May agents commit local changes?
- May agents push branches?
- May agents open PRs?
- May agents install dependencies or add new packages?

Group E: Planning and review workflow
- Which tasks require shape-work before implementation?
- Where should research, plans, scorecards, prompts, handoffs, and retros live?
- What must be true before a PR or deliverable is ready for review?
- Who gives final approval?
- What review tools or human checks should agents expect?

Group F: Style and project preferences
- Are there naming, formatting, or architecture preferences?
- Are there files or modules agents should read before editing?
- Are there areas agents should avoid unless explicitly assigned?
- Are there known flaky tests, slow checks, or local setup traps?
- Where should reusable lessons be recorded after delivery?

Step 3: Draft AGENTS.md

After the interview, draft a concise AGENTS.md with these sections:

- Mission
- Start Every Session
- Project Setup
- Development Commands
- Durable Work Notes
- Required Workflow
- Testing And Verification
- Privacy And Data
- Agent Permissions
- Review And Delivery
- Documentation And Memory
- Open Questions / TBD

Rules for the draft:
- Keep it specific to this repository.
- Prefer short bullets over long prose.
- Include exact commands only when known.
- Mark uncertain items as TBD.
- Avoid company-specific assumptions unless I stated them.
- Preserve any useful existing AGENTS.md guidance unless it conflicts with the
  new answers.

Step 4: Review before editing

Show me:
- proposed AGENTS.md
- what would be preserved from the old AGENTS.md, if one exists
- what would be changed
- remaining TBDs

Ask for approval before writing the file.

Step 5: Write and verify after approval

Only after I approve:
- create or update AGENTS.md
- optionally create missing thoughts/shared directories if I approve
- optionally create a setup handoff under thoughts/shared/handoffs/
- run git diff -- AGENTS.md
- run git status --short --branch

Final report:
- files changed
- important rules added
- commands discovered
- TBDs remaining
- recommended next prompt to run

Do not commit or push unless I explicitly ask you to.
```
