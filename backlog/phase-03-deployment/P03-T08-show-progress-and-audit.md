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

- Add HTMX-polled job list and detail pages with progressbar semantics, ordered step state, retry/cancellation state, and actionable failure details.
- Add a filterable append-only audit view for plan, approval, dispatch, Jira mutation, cancellation request and acknowledgment, validation, export, and result events.

## Success Criteria

- [ ] Refreshing or reconnecting does not lose or reorder displayed progress.
- [ ] Job detail identifies connection, project, plan, progress count, active step, attempt, elapsed time, and requested versus acknowledged cancellation state.
- [ ] Audit events identify actor, target, blueprint checksum, job, step, time, and outcome.
- [ ] Events with the same timestamp retain deterministic append order and cancellation request and acknowledgment remain separate attributable events.
- [ ] Diagnostics and rendered pages expose no secret value.

## Evidence

- [ ] View, polling, progress semantics, cancellation-state, audit immutability, ordering, filtering, and redaction tests plus QA screenshots.