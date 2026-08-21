# P02-S01 - Deliver Read-Only Planning

- Type: Story
- Phase: 02 - Read-Only Planning
- Parent: None
- Depends on: P01-S02
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

An operator can select blueprint resources and approve an explainable plan without changing Jira.

## Work

- Manage connections and parse blueprints.
- Resolve dependencies and compare desired state with Jira.
- Persist and present immutable dry-run plans.

## Success Criteria

- [ ] Tasks P02-T01 through P02-T07 are Done.
- [ ] The example blueprint produces a stable plan against the sandbox.
- [ ] Planning sends no Jira mutation request.

## Evidence

- [ ] Approved sandbox plan and request log proving read-only operation.