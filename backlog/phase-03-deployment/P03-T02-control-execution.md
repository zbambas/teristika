# P03-T02 - Control Concurrent Execution

- Type: Task
- Phase: 03 - Safe Deployment
- Parent: P03-S01
- Depends on: P03-T01
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

Only one mutation job can run for a Jira project, and cancellation stops new mutations.

## Work

- Add owner-token target leases with expiry and renewal.
- Require a reasoned cancellation confirmation that identifies job, target, current progress, and recovery boundary; check cancellation before each mutation and record the acknowledgment point.

## Success Criteria

- [ ] A second job for the same connection and project cannot enter mutation execution.
- [ ] A stale lease can be recovered without releasing another worker's lease.
- [ ] Cancellation never changes a step already verified as complete.
- [ ] A cancellation request records actor, reason, job, target, and request time; the worker acknowledges it before the next Jira mutation and exposes requested versus acknowledged state.

## Evidence

- [ ] Concurrency, stale-lease, ownership, reason-required cancellation, acknowledgment-boundary, and audit integration tests.