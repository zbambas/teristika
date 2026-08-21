# P05-T06 - Run Workflow Smoke Validation

- Type: Task
- Phase: 05 - Test Data and Validation
- Parent: P05-S01
- Depends on: P05-T05
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

An explicitly approved smoke rule creates, transitions, verifies, and cleans one temporary Jira issue.

## Work

- Implement issue-createable and issue-transitionable validation rules.
- Mark the temporary issue before transitions and always attempt bounded cleanup.

## Success Criteria

- [ ] Mutation-disabled runs skip smoke rules and send no Jira mutation.
- [ ] Expected transition paths pass and missing transitions fail with evidence.
- [ ] Success and failure paths both attempt safe cleanup and report its result.

## Evidence

- [ ] Disabled, successful, failed-transition, and cleanup-failure tests plus sandbox report.