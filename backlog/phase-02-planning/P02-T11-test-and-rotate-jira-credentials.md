# P02-T11 - Test and Rotate Jira Credentials

- Type: Task
- Phase: 02 - Read-Only Planning
- Parent: P02-S03
- Depends on: P02-T10
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

An administrator can test a staged Jira credential and explicitly activate it only after a successful access check.

## Work

- Test the candidate against capability-approved Jira identity, site, scope, permission, and representative read endpoints.
- Present sanitized identity, latency, scopes or permissions, capability summary, expiry metadata, and classified failures before activation.

## Success Criteria

- [ ] Testing distinguishes invalid credential, insufficient scope, insufficient Jira permission, wrong site, rate limit, timeout, and unavailable Jira.
- [ ] Only the tested candidate version can be activated and activation requires explicit confirmation.
- [ ] Failed or expired candidates cannot activate and leave the active secret reference unchanged.
- [ ] Test and activation responses, logs, audit, and diagnostics reveal no token or authorization value.

## Evidence

- [ ] Success and failure contract fixtures, stale-candidate, activation, rollback-preservation, rate-limit, redaction, and audit tests.