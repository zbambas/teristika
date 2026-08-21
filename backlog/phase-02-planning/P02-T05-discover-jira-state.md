# P02-T05 - Discover and Normalize Jira State

- Type: Task
- Phase: 02 - Read-Only Planning
- Parent: P02-S01
- Depends on: P02-T04
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

The Jira adapter returns deterministic observed resources and connection capabilities.

## Work

- Implement the shared Jira HTTP client and read-only discovery handler interface.
- Normalize pagination, ordering, Jira defaults, IDs, and capability outcomes.

## Success Criteria

- [ ] Sanitized fixtures and fake adapter produce the same domain objects.
- [ ] Pagination is complete and output ordering is stable.
- [ ] Planning requests use only capability-matrix read endpoints.

## Evidence

- [ ] Jira client contract tests and sandbox read-only request log.