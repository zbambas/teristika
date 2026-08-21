# P06-T02 - Execute Issue Batches Safely

- Type: Task
- Phase: 06 - Operations and Release
- Parent: P06-S01
- Depends on: P06-T01
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

An approved batch executes at a bounded rate with resumable per-issue outcomes.

## Work

- Execute the frozen action by Jira page with rate, retry, cancellation, and failure-threshold controls.
- Store only issue ID, outcome, attempt count, error class, and correlation ID.

## Success Criteria

- [ ] Rate and maximum issue count cannot exceed the approved plan.
- [ ] Retry resumes failed or incomplete issues without repeating completed idempotent actions.
- [ ] Execution stops when cancellation or the approved permanent-failure threshold is reached.

## Evidence

- [ ] Rate, resume, idempotency, cancellation, threshold, and data-minimization tests.