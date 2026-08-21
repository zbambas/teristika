# P04-T04 - Deploy Custom Fields and Contexts

- Type: Task
- Phase: 04 - Configuration Catalog
- Parent: P04-S01
- Depends on: P04-T03
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

Capability-supported custom fields and project contexts deploy without changing unrelated contexts.

## Work

- Implement custom field, option, and field context handlers.
- Resolve project and issue type references before creating or updating a context.

## Success Criteria

- [ ] The example Entities field and options match normalized Jira read-back.
- [ ] Context changes are limited to the planned projects and issue types.
- [ ] Duplicate field names without a mapping produce a conflict.

## Evidence

- [ ] Handler tests and sandbox field, option, scope-isolation, and rerun report.