---
name: tdd
description: Use test-driven or check-driven development. Write failing tests before code behavior changes, or define verification checks before analysis deliverables.
---

# TDD

Use this skill before implementation when behavior or claims need verification.

## For Code

1. Write a failing test for the desired behavior or bug reproduction.
2. Run the test and confirm it fails for the expected reason.
3. Implement the minimum change that makes it pass.
4. Run the test again.
5. Refactor only while tests remain green.

## For Analysis

1. Write the claims or outputs the analysis must support.
2. Identify the source data, query, formula, or file that verifies each claim.
3. Produce the analysis.
4. Check every quantitative claim against its source.
5. Record any assumptions or unverified claims.

## Report

Include:

- test or check created
- initial failure or expected check
- final passing command or verification
- remaining gaps

## Stop Conditions

Stop and ask before continuing if:

- the project has no test or check mechanism and the work is high risk
- required data is missing
- verification would require credentials or systems the user has not provided
