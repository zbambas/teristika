# P04-T03 - Deploy Statuses and Workflows

- Type: Task
- Phase: 04 - Configuration Catalog
- Parent: P04-S01
- Depends on: P04-T02
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

Capability-supported statuses and workflow transitions deploy with a verified graph.

## Work

- Implement status and workflow handlers for the approved API operations.
- Normalize initial status and transition names, sources, targets, and supported rules.

## Success Criteria

- [ ] Every workflow status and transition reference resolves before mutation.
- [ ] Jira read-back produces the expected normalized transition graph.
- [ ] Unsupported conditions, validators, or properties appear as blocking or unsupported plan items.

## Evidence

- [ ] Graph comparison tests and sandbox workflow deployment report.