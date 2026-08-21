# P02-T03 - Validate Typed Resource Properties

- Type: Task
- Phase: 02 - Read-Only Planning
- Parent: P02-S01
- Depends on: P02-T02
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

Each supported blueprint resource rejects unknown or invalid Jira properties before planning.

## Work

- Register one typed property validator per capability-supported resource type.
- Return structured errors with resource ID, property path, code, and message.

## Success Criteria

- [ ] Valid example resources pass their registered validators.
- [ ] Unknown resource types, unknown properties, wrong value types, and duplicate IDs fail.
- [ ] Validation performs no database write or Jira request.

## Evidence

- [ ] Parameterized validator tests for every supported resource type.