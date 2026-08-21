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
- Present approval and execution confirmations from the immutable plan rather than editable form state.

## Success Criteria

- [ ] Every rejected condition creates no deployment job or Jira request.
- [ ] Approval records actor, timestamp, plan checksum, and target.
- [ ] Approval confirmation identifies plan ID, connection and project, blueprint version, checksum, operation totals, shared impact, unsupported exclusions, and recovery boundary.
- [ ] Any target, blueprint, parameter, or resource-selection change invalidates the displayed plan and disables approval and execution until regeneration.
- [ ] A valid approval enqueues exactly one job for one idempotency key.

## Evidence

- [ ] Authorization, confirmation-payload, changed-input, tampering, staleness, blocker, expiry, and duplicate-submit tests.