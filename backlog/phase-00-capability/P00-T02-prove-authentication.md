# P00-T02 - Prove Jira Authentication

- Type: Task
- Phase: 00 - Capability Proof
- Parent: P00-S01
- Depends on: P00-T01
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

One approved authentication method can call the sandbox with known scopes and permissions.

## Work

- Test the candidate authentication methods against one documented read endpoint.
- Record the selected method, required scopes, account permissions, and rotation owner.

## Success Criteria

- [ ] The selected method returns the expected identity or site response.
- [ ] Invalid credentials produce the expected sanitized failure.
- [ ] No credential value appears in source, shell history evidence, logs, or fixtures.

## Evidence

- [ ] Sanitized successful and failed request summaries reviewed by Senior QA.