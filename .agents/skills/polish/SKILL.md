---
name: polish
description: Pre-review quality pass. Simplify changed work, run format/lint/tests/checks, verify the scorecard, and prepare a concise review summary before PR or delivery.
---

# Polish

Use this before opening a PR, requesting review, or delivering an analysis.

## Workflow

1. Identify changed files:
   - `git status --short`
   - `git diff --name-only`
2. Simplify:
   - remove dead code, duplicate logic, and unnecessary abstractions
   - keep changes scoped to the plan
3. Run project checks:
   - formatter, if available
   - linter or static checks, if available
   - targeted tests, if available
   - build or type checks, if available
4. Verify the scorecard:
   - acceptance criteria
   - privacy/security constraints
   - data or claim checks
5. Fix issues found.
6. Report results.

## Report Format

```text
Polish complete.
  Files reviewed: <N>
  Simplifications: <summary>
  Format/lint: <pass/fail/not available>
  Tests/checks: <commands and result>
  Scorecard: <pass/fail>
  Ready for review: <yes/no>
```

If a check cannot run, say why and identify the closest substitute.
