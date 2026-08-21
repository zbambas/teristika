# P03-T07 - Guard Plan Execution

- Type: Task
- Phase: 03 - Safe Deployment
- Parent: P03-S01
- Depends on: P03-T06
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

Only an authorized, approved, current plan can create a deployment job.

## Work

- Require approver permission, explicit approval, immutable checksum, connection identity, and target fingerprint checks.
- Reject plans with blockers, changed inputs, expired approval, or stale target state.

## Success Criteria

- [ ] Every rejected condition creates no deployment job or Jira request.
- [ ] Approval records actor, timestamp, plan checksum, and target.
- [ ] A valid approval enqueues exactly one job for one idempotency key.

## Evidence

- [ ] Authorization, tampering, staleness, blocker, expiry, and duplicate-submit tests.