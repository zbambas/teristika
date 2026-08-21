# P03-T08 - Show Progress and Audit Evidence

- Type: Task
- Phase: 03 - Safe Deployment
- Parent: P03-S01
- Depends on: P03-T07
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

Operators can monitor a job and auditors can trace every approval and mutation.

## Work

- Add HTMX-polled job pages with ordered step state and actionable failure details.
- Add append-only audit events for plan, approval, dispatch, Jira mutation, cancellation, and result.

## Success Criteria

- [ ] Refreshing or reconnecting does not lose or reorder displayed progress.
- [ ] Audit events identify actor, target, blueprint checksum, job, step, time, and outcome.
- [ ] Diagnostics and rendered pages expose no secret value.

## Evidence

- [ ] View, polling, audit immutability, ordering, and redaction tests plus QA screenshot.