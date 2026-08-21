# P05-T04 - Run Static Validation Suites

- Type: Task
- Phase: 05 - Test Data and Validation
- Parent: P05-S01
- Depends on: P05-T03
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

Blueprint, dependency, connection, permission, and capability checks produce structured results.

## Work

- Add validation run and result models, Celery task, rule registry, and status aggregation.
- Record rule ID, target, expected, observed, status, severity, message, and remediation.

## Success Criteria

- [ ] Results distinguish pass, warning, fail, skipped, and unsupported.
- [ ] A failed prerequisite marks dependent rules skipped with its rule ID.
- [ ] Repeating a suite preserves each run as immutable evidence.

## Evidence

- [ ] Rule, aggregation, prerequisite, immutability, and worker tests.