# P01-T07 - Build Project Workspace

- Type: Task
- Phase: 01 - Django Foundation
- Parent: P01-S02
- Depends on: P01-T06
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

An operator can open one Jira project to inspect its details, setup readiness, and permitted project-scoped actions.

## Work

- Build project registry and detail pages with connection, Jira identity, blueprint baseline, ownership, configuration status, and recent activity.
- Add project tabs for overview, setup, and operations that route to the existing planning, jobs, validation, test-data, batch, and audit workflows with project context.

## Success Criteria

- [ ] Portfolio and project registry links preserve the selected connection and project context.
- [ ] Project details and setup status come from persisted project, mapping, plan, job, and validation records.
- [ ] Project actions are permission-aware and open preview or planning workflows without mutating Jira directly.
- [ ] Unknown or unauthorized projects reveal no metadata and project tabs work by keyboard and mobile viewport.

## Evidence

- [ ] Registry, detail, context, permission, routing, keyboard, and responsive tests plus Senior QA screenshots.