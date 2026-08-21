# P01-T03 - Add Application Roles

- Type: Task
- Phase: 01 - Django Foundation
- Parent: P01-S01
- Depends on: P01-T01
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

Django enforces viewer, operator, approver, and administrator roles.

## Work

- Create the four roles and their baseline Django permissions in a data migration.
- Add reusable view and DRF permission checks with local-development login support.

## Success Criteria

- [ ] The migration creates the same roles on repeated runs.
- [ ] Authorization tests cover anonymous access and every role.
- [ ] An unauthorized mutation returns `403` and creates no state change.

## Evidence

- [ ] Role matrix and passing authorization tests reviewed by Senior QA.