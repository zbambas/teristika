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

## Evidence

- [ ] Reviewed security test report with no unresolved high-severity finding.