# P02-T01 - Manage Jira Connections

- Type: Task
- Phase: 02 - Read-Only Planning
- Parent: P02-S01
- Depends on: P01-S01
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

Administrators can manage Jira connection metadata and run a redacted connectivity check from Settings > Jira connections.

## Work

- Add the connection model, migration, admin, form, Settings section, and DRF serializer.
- Store a secret reference only and call the capability-proven identity endpoint.
- Present registered-site health and the latest capability snapshot together, with a direct route to the selected connection's credential settings.

## Success Criteria

- [ ] Valid metadata persists and duplicate site identities are rejected.
- [ ] Connectivity states distinguish success, authentication failure, permission failure, and unavailable site.
- [ ] Responses, logs, and database rows contain no credential value.
- [ ] Settings > Jira connections is the single application destination for registered sites and capability health; no duplicate top-level Connections destination exists.
- [ ] Opening Credentials from a connection preserves that connection as the credential target and cannot expose another connection's metadata.

## Evidence

- [ ] Model, view, API, and redaction tests with a fake Jira response.