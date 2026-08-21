# P03-T06 - Persist Jira Resource Mappings

- Type: Task
- Phase: 03 - Safe Deployment
- Parent: P03-S01
- Depends on: P03-T05
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

Logical blueprint IDs resolve to stable Jira object IDs within the correct target scope.

## Work

- Add the resource mapping model, constraints, repository service, and admin read view.
- Create or update a mapping only after successful read-back verification.

## Success Criteria

- [ ] A logical ID maps to at most one Jira ID per connection and scope.
- [ ] A Jira ID cannot be adopted by conflicting logical resources in that scope.
- [ ] Failed or unverified mutations create no mapping.

## Evidence

- [ ] Constraint, adoption-conflict, verification, and rerun tests.