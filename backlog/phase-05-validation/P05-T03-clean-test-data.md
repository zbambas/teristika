# P05-T03 - Clean One Test-Data Run

- Type: Task
- Phase: 05 - Test Data and Validation
- Parent: P05-S01
- Depends on: P05-T02
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

An operator can preview and remove only issues created by one test-data run.

## Work

- Match candidates by connection, project, pack, run, stored mapping, and Jira entity property.
- Require explicit cleanup approval and record every deletion outcome.

## Success Criteria

- [ ] Any marker or mapping mismatch excludes the issue and raises a warning.
- [ ] A manually created issue with the same label is never deleted.
- [ ] Repeating completed cleanup is a successful no-op.

## Evidence

- [ ] Mismatch matrix tests and sandbox cleanup report including a preserved control issue.