# P06-T03 - Schedule Jobs and Prevent Overlap

- Type: Task
- Phase: 06 - Operations and Release
- Parent: P06-S01
- Depends on: P06-T02
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

Celery Beat starts approved commands at the configured time without overlapping target writes.

## Work

- Add schedule model, form, API, time zone, command reference, enabled state, and overlap policy.
- Dispatch due schedules through the same authorization and job services as immediate runs.

## Success Criteria

- [ ] Disabled schedules dispatch nothing and time zones produce the expected UTC instant.
- [ ] Queue, skip, and reject overlap policies each record the expected result.
- [ ] A scheduled validation completes with no active browser session.

## Evidence

- [ ] Time-zone, disabled, dispatch, overlap, and unattended-run integration tests.