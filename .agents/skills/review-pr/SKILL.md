---
name: review-pr
description: Review an open PR, branch, or diff against the scorecard. Check CI, tests, coverage or claim verification, privacy/security risks, unresolved comments, and readiness for human approval.
---

# Review PR

Use this after a PR, branch, or review diff exists.

## Inputs

- PR number/URL, branch name, or diff.
- Optional plan and scorecard paths.

## Workflow

1. Identify review target:
   - current branch, PR URL, or supplied diff
   - base branch
2. Read context:
   - `AGENTS.md`
   - linked plan and scorecard
   - changed files
3. Check automated gates:
   - CI status, if available
   - tests
   - lint/format
   - coverage, if applicable
   - analysis claim verification, if applicable
4. Review the diff for:
   - correctness
   - privacy/security issues
   - scope drift
   - brittle assumptions
   - missing tests or checks
5. Fix blocking issues that are clearly in scope.
6. Report non-blocking issues separately.

## Blocking vs Non-Blocking

Blocking:

- failing tests or CI
- broken core behavior
- privacy/security risk
- unverified quantitative claim in a delivered analysis
- scorecard acceptance criteria not met

Non-blocking:

- style preference
- optional refactor
- future enhancement
- unrelated pre-existing issue

## Report Format

```text
Review complete.
  Target: <PR/branch/diff>
  Checks: <summary>
  Blocking issues fixed: <N>
  Blocking issues remaining: <N>
  Non-blocking items: <summary>
  Ready for human approval: <yes/no>
```

Do not merge without explicit human approval.
