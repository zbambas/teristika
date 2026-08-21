# P04-T01 - Protect Shared Jira Resources

- Type: Task
- Phase: 04 - Configuration Catalog
- Parent: P04-S01
- Depends on: P03-S01
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

Plans identify the impact of changing a global Jira resource before approval.

## Work

- Discover projects and schemes that use a mapped global resource.
- Add shared-impact details and elevated approval policy to planning and execution guards.

## Success Criteria

- [ ] A shared update lists every discoverable affected project.
- [ ] Missing impact-read permission blocks the update rather than assuming no impact.
- [ ] The configured elevated role is required before execution.

## Evidence

- [ ] Policy, permission-failure, affected-project, and authorization tests.