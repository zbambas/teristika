# P02-T12 - Discover Reference Jira Project

- Type: Task
- Phase: 02 - Read-Only Planning
- Parent: P02-S04
- Depends on: P02-T05, P02-S03
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

The application produces a complete, bounded discovery report for a selected Jira connection and reference project.

## Work

- Select a tested Jira connection and project, then discover project metadata, issue types, statuses, workflows, fields, contexts, screens, schemes, components, versions, roles, priorities, resolutions, and other capability-supported configuration.
- Classify every discovered item as project-owned, shared, reference-only, unsupported, inaccessible, ambiguous, or omitted by policy.
- Bind the discovery report and provenance to the exact selected connection, Jira project ID and key, actor, capability set, and snapshot boundary; invalidate the report when any source input changes.

## Success Criteria

- [ ] The selected connection credential is tested and the project identity is read back before discovery.
- [ ] Discovery paginates every enabled capability-approved endpoint and records a stable snapshot boundary and normalized source identifiers.
- [ ] Connection and project must match before discovery; changing either after or during discovery hides stale results and blocks draft creation until a new report completes.
- [ ] Shared resources list discoverable affected projects and default to explicit include or reference decisions rather than silent copying.
- [ ] Permission failures, unsupported APIs, ambiguity, rate limits, Jira outages, and result limits appear in the report and no Jira mutation occurs.

## Evidence

- [ ] Contract, source-binding, stale-discovery, pagination, shared-resource, permission, unsupported, ambiguity, rate-limit, outage, normalization, and sandbox read-only request tests.