# AI Development Workflow Starter

This is a portable starter kit for an analyst or solo operator who wants to use
AI agents for thoughtful, testable development work.

It is designed for Codex, GitHub, and ordinary local development. It does not
assume access to any private repository, internal customer data, or company
workflow.

## What This Gives You

- A narrative guide for working with AI agents.
- A repo-level `AGENTS.md` operating contract.
- Codex-native skills under `.agents/skills/`.
- Planning templates under `thoughts/shared/templates/`.
- Paste-ready prompts under `prompts/`.

The workflow is:

```text
shape-work -> tdd -> implement -> polish -> review-pr -> human approval -> retro-pr
```

## How To Use This Kit

1. Copy these files into the root of a project repository.
2. Edit `AGENTS.md` so it matches that project.
3. Start Codex from the repository root.
4. Ask Codex to read `AGENTS.md` and `docs/standalone-analyst-ai-development-guide.md`.
5. Use `prompts/codex-bootstrap-prompts.md` to run the first setup and planning pass.

## Minimum Tools

- Git
- GitHub or another remote repository host
- Codex
- A test runner for your project, if code is involved
- A private notes system for durable lessons, optional

If you do not use GitHub PRs, keep the same review step but adapt it to your
hosted review tool or a written human review checklist.
