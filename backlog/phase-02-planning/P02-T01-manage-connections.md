# P02-T01 - Manage Jira Connections

- Type: Task
- Phase: 02 - Read-Only Planning
- Parent: P02-S01
- Depends on: P01-S01
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

Administrators can store Jira connection metadata and run a redacted connectivity check.

## Work

- Add the connection model, migration, admin, form, page, and DRF serializer.
- Store a secret reference only and call the capability-proven identity endpoint.

## Success Criteria

- [ ] Valid metadata persists and duplicate site identities are rejected.
- [ ] Connectivity states distinguish success, authentication failure, permission failure, and unavailable site.
- [ ] Responses, logs, and database rows contain no credential value.

## Evidence

- [ ] Model, view, API, and redaction tests with a fake Jira response.