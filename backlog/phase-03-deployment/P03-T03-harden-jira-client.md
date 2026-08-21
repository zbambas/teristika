# P03-T03 - Harden Jira HTTP Client

- Type: Task
- Phase: 03 - Safe Deployment
- Parent: P03-S01
- Depends on: P03-T02
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

All Jira calls use one bounded retry, throttling, correlation, and redaction policy.

## Work

- Extend the shared client with timeout, retry classification, `Retry-After`, rate limiting, and problem mapping.
- Redact configured headers and sensitive JSON fields before diagnostics are stored or logged.

## Success Criteria

- [ ] `429` and transient `5xx` responses retry within configured bounds.
- [ ] Authentication, permission, validation, and conflict responses do not retry.
- [ ] Every request has a correlation ID and every tested secret is redacted.

## Evidence

- [ ] Contract tests using the Phase 00 error fixtures and a redaction scan.