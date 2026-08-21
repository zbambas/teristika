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
- Require enablement confirmation that identifies target, command, source version, local time and time zone, and overlap policy.

## Success Criteria

- [ ] Disabled schedules dispatch nothing and time zones produce the expected UTC instant.
- [ ] Queue, skip, and reject overlap policies each record the expected result.
- [ ] Editing a confirmed target, command, source version, time zone, or overlap policy requires review before the schedule can be enabled again.
- [ ] A scheduled validation completes with no active browser session.

## Evidence

- [ ] Time-zone, enable-confirmation, stale-review, disabled, dispatch, overlap, and unattended-run integration tests.