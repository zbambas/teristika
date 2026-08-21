# P05-T02 - Create and Map Test Data

- Type: Task
- Phase: 05 - Test Data and Validation
- Parent: P05-S01
- Depends on: P05-T01
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

An approved pack creates traceable issues and then resolves their links deterministically.

## Work

- Create issues in logical-ID order, persist mappings, and add the run label and entity property.
- Create links and comments only after all referenced issue IDs exist.

## Success Criteria

- [ ] At least 50 linked issues can be created from one pack.
- [ ] Every issue has the expected run marker and durable mapping.
- [ ] Retrying after interruption creates no duplicate issue or link.

## Evidence

- [ ] Two-phase creation, interruption, retry, marker, and mapping tests plus sandbox report.