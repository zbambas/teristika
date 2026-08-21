# P06-S02 - Deliver Issue Dependency Explorer

- Type: Story
- Phase: 06 - Operations and Release
- Parent: None
- Depends on: P05-S01
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

An operator can inspect one Jira project's issue dependencies from several consistent visual perspectives.

## Work

- Build a permission-scoped issue and relationship dataset from Jira.
- Build synchronized Gantt, radial, network, and matrix representations with issue detail.

## Success Criteria

- [ ] Tasks P06-T09 and P06-T10 are Done.
- [ ] Every representation uses the same filtered issue and dependency dataset.
- [ ] Selecting an issue or dependency in one representation shows the same project-scoped detail and does not mutate Jira.
- [ ] Empty, partial-permission, cycle, large-result, loading, and Jira-error states are explicit.

## Evidence

- [ ] Dataset contract, authorization, representation consistency, accessibility, responsive, and Jira sandbox evidence.