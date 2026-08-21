# P02-S03 - Deliver Secure Jira Credential Settings

- Type: Story
- Phase: 02 - Read-Only Planning
- Parent: None
- Depends on: P02-T01
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

Administrators can securely add, test, rotate, and disable Jira credentials without exposing secret values.

## Work

- Build role-restricted connection and credential settings backed by an external secret store.
- Build candidate-credential testing and explicit activation that preserves the current credential on failure.

## Success Criteria

- [ ] Tasks P02-T10 and P02-T11 are Done.
- [ ] The application database, browser storage, logs, errors, tasks, fixtures, and exports contain no Jira secret value.
- [ ] A failed candidate test leaves the active credential and connection state unchanged.
- [ ] Every credential create, test, activate, rotate, disable, and secret-reference change is audited without the secret.

## Evidence

- [ ] Secret-store, authorization, candidate-test, rotation, redaction, audit, accessibility, and responsive evidence.