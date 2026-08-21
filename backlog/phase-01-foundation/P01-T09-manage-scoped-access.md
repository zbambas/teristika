# P01-T09 - Manage Scoped Roles and Groups

- Type: Task
- Phase: 01 - Django Foundation
- Parent: P01-S03
- Depends on: P01-T08
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

Administrators can map OIDC groups and time-bounded direct exceptions to application roles and permitted scopes.

## Work

- Add user, group-mapping, role-assignment, and effective-access screens and APIs for viewer, operator, approver, and administrator roles.
- Support global, connection, and project scopes, with group mappings preferred and direct assignments requiring reason, owner, and optional expiry.

## Success Criteria

- [ ] Effective permission is the union of active role assignments only within their scopes and defaults to no access.
- [ ] Administrator scope is global; viewer, operator, and approver can be limited to connections or projects.
- [ ] Expired, suspended, disabled, or removed assignments stop authorizing immediately.
- [ ] The last active administrator cannot remove or expire their own final administrative path.
- [ ] Assignment preview shows source group or direct exception, role, scope, start, expiry, and resulting permissions before save.

## Evidence

- [ ] Role matrix, group mapping, direct exception, scope isolation, expiry, last-administrator, preview, and audit tests.