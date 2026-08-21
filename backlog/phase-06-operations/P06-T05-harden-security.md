# P06-T05 - Complete Security Hardening

- Type: Task
- Phase: 06 - Operations and Release
- Parent: P06-S01
- Depends on: P06-T04
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

The MVP role, target, request, upload, and secret boundaries have automated security coverage.

## Work

- Test cross-connection, cross-project, privilege-escalation, CSRF, upload-limit, and object-access scenarios.
- Scan logs, errors, database diagnostics, task payloads, reports, and fixtures for seeded secrets.

## Success Criteria

- [ ] Every tested unauthorized operation returns the expected denial and creates no mutation.
- [ ] Oversized or invalid uploads are rejected before parsing or storage.
- [ ] The seeded-secret scan returns no exposure in any tested surface.
- [ ] No unresolved critical or high finding remains, where critical or high means a demonstrated path to unauthorized Jira mutation, privilege escalation, secret exposure, cross-connection or cross-project data access, or loss of required audit evidence.

## Evidence

- [ ] Reviewed security test report maps every finding to the stated severity boundary and records resolution or Product Owner rejection of release.