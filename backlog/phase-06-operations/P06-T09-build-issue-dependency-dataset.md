# P06-T09 - Build Issue Dependency Dataset

- Type: Task
- Phase: 06 - Operations and Release
- Parent: P06-S02
- Depends on: P05-S01
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

The application returns one bounded, permission-scoped dataset of Jira issues and dependency relationships for a project.

## Work

- Discover issues through validated project-scoped JQL and normalize parent, issue-link, blocking, status, assignee, estimate, start, and due-date data.
- Detect missing dates, hidden issues, cycles, disconnected groups, and result limits without fabricating relationships.

## Success Criteria

- [ ] The endpoint returns stable issue nodes and typed directed edges with no duplicate issue or relationship IDs.
- [ ] Project authorization, Jira browse permission, pagination, maximum issue count, partial visibility, and sanitized errors are enforced.
- [ ] Cycles and missing scheduling dates are reported as data facts and do not prevent non-timeline representations.
- [ ] Repeated reads make no Jira mutation and equivalent Jira responses normalize identically.

## Evidence

- [ ] Contract, pagination, normalization, authorization, cycle, partial-visibility, limit, and redaction tests.