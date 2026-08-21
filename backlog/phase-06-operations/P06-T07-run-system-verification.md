# P06-T07 - Run MVP System Verification

- Type: Task
- Phase: 06 - Operations and Release
- Parent: P06-S01
- Depends on: P06-T06
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

The integrated Django application satisfies the critical MVP workflows in the Jira sandbox.

## Work

- Run clean deploy, idempotent rerun, partial deploy, drift, test cleanup, batch, cancellation, and scheduled validation scenarios.
- Run keyboard, screen-reader smoke, contrast, desktop, and mobile checks for core pages.

## Success Criteria

- [ ] Every critical scenario passes from a clean test environment.
- [ ] The verification report records a Jira sandbox/test-domain assertion and a local or isolated test-database assertion before scenarios run; no production Jira site or shared database is used.
- [ ] No unresolved defect remains that blocks a listed critical scenario, permits unauthorized mutation or data access, exposes a secret, or lacks a documented operator workaround accepted by the Product Owner.

## Evidence

- [ ] Versioned system, environment-isolation, defect-triage, accessibility, and responsive verification report.