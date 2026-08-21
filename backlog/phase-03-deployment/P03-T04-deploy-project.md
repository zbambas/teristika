# P03-T04 - Deploy Jira Project

- Type: Task
- Phase: 03 - Safe Deployment
- Parent: P03-S01
- Depends on: P03-T03
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

The project resource handler can discover, compare, create, update, and verify a company-managed project.

## Work

- Implement the project handler only for operations approved in the capability matrix.
- Verify every mutation by reading the project back and normalizing it.

## Success Criteria

- [ ] Missing project plans as create and matching project plans as unchanged.
- [ ] Supported differences plan and apply as update; unsupported differences are explicit.
- [ ] Repeating create after a lost response does not create a duplicate project.

## Evidence

- [ ] Handler contract tests and sandbox create, verify, and rerun report.