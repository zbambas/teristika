# P05-T05 - Detect Configuration Drift

- Type: Task
- Phase: 05 - Test Data and Validation
- Parent: P05-S01
- Depends on: P05-T04
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

Validation identifies meaningful differences between a blueprint version and current Jira state.

## Work

- Reuse handler normalization and comparison for `resourceMatches` rules.
- Report expected and observed values without volatile ordering or Jira defaults.

## Success Criteria

- [ ] Deliberate field, workflow, and component differences fail the matching rules.
- [ ] Reordering ignored values does not produce drift.
- [ ] Unsupported read-back returns unsupported rather than pass.

## Evidence

- [ ] Drift fixture tests and sandbox before-change and after-change reports.