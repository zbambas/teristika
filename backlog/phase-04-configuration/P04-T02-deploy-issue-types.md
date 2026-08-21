# P04-T02 - Deploy Issue Types and Scheme

- Type: Task
- Phase: 04 - Configuration Catalog
- Parent: P04-S01
- Depends on: P04-T01
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

Capability-supported issue types and their scheme deploy and verify idempotently.

## Work

- Implement handlers for issue types and issue type schemes using logical references.
- Support Requirement, Test, and Defect from the example blueprint.

## Success Criteria

- [ ] Create, supported update, unchanged, conflict, and unsupported outcomes are tested.
- [ ] The scheme contains the expected default and ordered issue types after read-back.
- [ ] Rerunning the same desired state performs no mutation.

## Evidence

- [ ] Contract tests and sandbox plan, deploy, verify, and rerun report.