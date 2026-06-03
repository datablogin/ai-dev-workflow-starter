# Standalone Analyst AI Development Guide

This guide is for an analyst, consultant, or solo builder who wants to use AI
agents to do better technical work without depending on a private company
repository or internal process.

The working style is simple:

```text
shape-work -> tdd -> implement -> polish -> review-pr -> human approval -> retro-pr
```

For non-code analysis work, use the same loop with lighter gates:

```text
shape-work -> produce analysis -> fact-check -> review -> retro
```

## Mental Model

AI agents are useful when they have:

- context
- boundaries
- examples
- tests or checks
- a definition of done
- a place to write down what they learned

They are risky when given a vague command like "build this" or "analyze this"
with no artifact trail. The workflow in this kit slows the first ten minutes
down so the rest of the work can move faster and stay inspectable.

## The Three-Layer System

| Layer | Purpose | Files |
|---|---|---|
| Operating contract | Standing rules for the repo | `AGENTS.md` |
| Durable work notes | Research, plans, scorecards, prompts, retros | `thoughts/shared/` |
| Skills | Repeatable agent workflows | `.agents/skills/*/SKILL.md` |

## Phase 1: Shape Work

Use shape-work before coding or analysis when:

- the task is vague
- the output matters to a client, team, or decision
- data quality or privacy matters
- the work may become multiple PRs or sessions
- the agent needs to choose between approaches

Shape-work produces:

- research: what is known, unknown, and risky
- plan: the sequence of work
- scorecard: what good looks like
- prompt pack: briefs for implementation agents

For tiny fixes, this can be short. For important work, use the full templates.

## Phase 2: Write A Scorecard

A scorecard gives the agent something to optimize toward.

Good scorecards include:

- primary KPI or outcome
- delivery gates
- tests or checks
- acceptance criteria
- out-of-scope boundaries
- regression risks

If the work is an analysis deliverable, the scorecard should include fact-check
requirements: source rows, formulas, date ranges, and claims that must be
verified.

## Phase 3: Implement With Tests

For code, use test-driven development when behavior changes:

1. Write a failing test.
2. Run it and confirm it fails for the expected reason.
3. Implement the smallest change that makes it pass.
4. Refactor only after tests pass.

For analysis, use check-driven development:

1. Write the claims you expect to make.
2. Identify the source data or query for each claim.
3. Produce the analysis.
4. Verify every quantitative claim before delivery.

## Phase 4: Polish

Polish before review. The agent should:

- simplify unnecessary complexity
- run formatters
- run lint or static checks
- run targeted tests
- verify coverage or claim checks where relevant
- summarize what passed and what could not be run

Polish is not vanity. It prevents review tools and humans from spending time on
avoidable problems.

## Phase 5: Review

If the project uses GitHub, open a pull request and run review-pr.

The review should check:

- CI status
- tests and coverage
- unresolved comments
- PR description
- security or privacy concerns
- whether the change matches the scorecard

If there is no PR system, use a written review checklist and attach it to the
work notes.

## Phase 6: Retro

After delivery, run retro-pr or write a short retro.

Capture:

- what shipped
- what worked
- what broke or surprised you
- what review caught
- what tests missed
- what to change in templates, skills, or habits

Put reusable lessons somewhere durable. For a solo analyst, this can be a
private notes repository, a knowledge base, or a simple `memory/` folder.

## Codex Setup Notes

Codex reads repo instructions from `AGENTS.md` and discovers repo skills from:

```text
.agents/skills/<skill-name>/SKILL.md
```

Start Codex from the repository root so it can see `AGENTS.md`, `.agents/`, and
the project files.

Use skills for reusable workflows. Use ordinary prompts for one-off task
briefs.

## First Practice Task

Use a small, low-risk project:

- clean one messy notebook
- add one utility function with tests
- build one tiny dashboard page
- automate one recurring CSV cleanup
- write one analysis memo from a sanitized sample dataset

Ask Codex to shape the work first. Do not start with implementation.

Starter prompt:

```text
Read AGENTS.md and docs/standalone-analyst-ai-development-guide.md.
Use the shape-work skill.

Goal:
<describe the small project>

Do not implement yet. Produce research, a plan, a scorecard, and a prompt pack
under thoughts/shared/. Keep it lightweight and suitable for a first pilot.
```
