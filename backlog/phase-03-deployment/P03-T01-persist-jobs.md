# P03-T01 - Persist Jobs and Checkpoints

- Type: Task
- Phase: 03 - Safe Deployment
- Parent: P03-S01
- Depends on: P02-S01
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

Deployment jobs and resource-level checkpoints survive worker or broker interruption.

## Work

- Add job and step models, migrations, state transitions, idempotency keys, and Celery dispatch.
- Persist a checkpoint before and after every external operation.

## Success Criteria

- [ ] Invalid job and step state transitions are rejected.
- [ ] Duplicate idempotency keys cannot create duplicate jobs or steps.
- [ ] Restarting a worker resumes from the first incomplete step.

## Evidence

- [ ] State-machine, constraint, dispatch, and worker-restart integration tests.