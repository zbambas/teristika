# P03-T05 - Deploy Components and Versions

- Type: Task
- Phase: 03 - Safe Deployment
- Parent: P03-S01
- Depends on: P03-T04
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

Project-scoped components and versions deploy idempotently after their project.

## Work

- Implement component and version discovery, comparison, create, update, and verification handlers.
- Register project dependencies and stable normalization rules.

## Success Criteria

- [ ] A component and version create only after the target project exists.
- [ ] Rerunning identical desired state performs no mutation.
- [ ] Duplicate or ambiguous Jira names block planning with a clear conflict.

## Evidence

- [ ] Handler tests and sandbox create, update, conflict, and rerun results.