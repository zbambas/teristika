# P00-T04 - Capture Jira Error Fixtures

- Type: Task
- Phase: 00 - Capability Proof
- Parent: P00-S01
- Depends on: P00-T02
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

The Jira adapter has safe fixtures for deterministic error classification tests.

## Work

- Capture representative `401`, `403`, `404`, conflict, `429`, and transient `5xx` responses.
- Sanitize headers, URLs, account data, issue content, and identifiers.

## Success Criteria

- [ ] One reviewed fixture exists for every obtainable error class.
- [ ] Unobtainable classes are documented with the planned synthetic fixture.
- [ ] A repository search finds no token or authorization header value.

## Evidence

- [ ] Senior QA fixture review and redaction scan result.