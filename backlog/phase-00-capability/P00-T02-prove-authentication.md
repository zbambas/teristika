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

- [ ] The selected method returns an authenticated account and Jira site identity that match the recorded sandbox, scopes, and permissions.
- [ ] Invalid credentials produce a classified authentication or authorization failure whose stored and rendered evidence is sanitized.
- [ ] No credential value appears in source, shell history evidence, logs, or fixtures.

## Evidence

- [ ] Sanitized successful and failed request summaries reviewed by Senior QA.