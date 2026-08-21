# P02-T06 - Generate Immutable Plans

- Type: Task
- Phase: 02 - Read-Only Planning
- Parent: P02-S01
- Depends on: P02-T05
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

Django persists an immutable plan that explains every requested resource outcome.

## Work

- Add plan and operation models, migrations, comparison service, and DRF endpoints.
- Store blueprint checksum, parameter hash, selection, dependencies, target fingerprint, and ordered operations.

## Success Criteria

- [ ] Operations classify as create, update, unchanged, conflict, unsupported, or blocked.
- [ ] The same inputs and observed state produce the same ordered plan.
- [ ] Approved plans and operations cannot be edited through models, admin, pages, or API.

## Evidence

- [ ] Comparison, persistence, immutability, and API tests.