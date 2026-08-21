# P05-T07 - Show Validation Evidence

- Type: Task
- Phase: 05 - Test Data and Validation
- Parent: P05-S01
- Depends on: P05-T06
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

Users can start a suite and inspect actionable validation evidence in Django pages.

## Work

- Add suite selection, run progress, summary, filtering, and result detail pages.
- Link each result to its blueprint resource, prerequisite, and originating job step when present.
- Before a suite starts, review target, suite version, rule count, baseline, any temporary smoke mutation, and cleanup guarantee in an explicit confirmation.

## Success Criteria

- [ ] Status and severity filters return the expected result set.
- [ ] Failure details show expected, observed, and remediation without secrets.
- [ ] A suite that creates a temporary smoke issue cannot start until confirmation; the run reports cleanup success or an actionable cleanup failure.
- [ ] Keyboard checks reach suite controls, filters, result rows, and remediation links with visible focus and announced run status.
- [ ] At 320px and 768px widths, all result evidence and actions remain reachable without page-level horizontal overflow.

## Evidence

- [ ] Django view, confirmation, smoke-cleanup, status-announcement, filter, redaction, desktop, 320px, 768px, and keyboard evidence.