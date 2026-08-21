# P01-T06 - Build Operator Overview

- Type: Task
- Phase: 01 - Django Foundation
- Parent: P01-S02
- Depends on: P01-T05
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

An operator can compare deployment readiness, recent activity, attention items, and permitted next actions across Jira projects on one page.

## Work

- Add query-backed portfolio summaries and per-project rows for connection health, plans, jobs, validations, schedules, and recent audit activity.
- Add role-aware quick actions that link to the owning workflow without performing a mutation from the overview.

## Success Criteria

- [ ] Portfolio totals, project rows, and recent activity match their persisted source records.
- [ ] Each project row links to its project-scoped workspace without changing configuration.
- [ ] Empty, loading, warning, failure, and healthy states have distinct semantic text.
- [ ] Quick actions respect role permissions and navigate to preview or planning workflows only.

## Evidence

- [ ] Query, permission, state, navigation, accessibility, and responsive tests plus QA screenshots.