# P03-T09 - Inspect Jira API Calls

- Type: Task
- Phase: 03 - Safe Deployment
- Parent: P03-S01
- Depends on: P03-T08
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

An authorized operator can inspect every Jira API call made by a job and understand its result.

## Work

- Add a job API-call ledger ordered by request time and linked to the owning job step.
- Add expandable call details for method, endpoint, attempt, duration, response status, sanitized request metadata, and bounded sanitized response.

## Success Criteria

- [ ] Expanding a job lists every Jira API attempt in stable chronological order and links each call to its step.
- [ ] Each call distinguishes queued, in progress, succeeded, retried, and failed states and shows HTTP status or transport error.
- [ ] Request and response details are size-bounded and redact credentials, authorization headers, cookies, account data, and configured sensitive fields.
- [ ] Authorization, empty, loading, pagination, retry, malformed-response, and refresh tests preserve ordering and expanded state.

## Evidence

- [ ] Django view, redaction, pagination, retry, status, accessibility, and responsive tests plus Senior QA screenshots.