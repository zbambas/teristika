# P06-T01 - Plan Issue Batches

- Type: Task
- Phase: 06 - Operations and Release
- Parent: P06-S01
- Depends on: P05-S01
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

An operator can preview a bounded JQL issue batch before any issue changes.

## Work

- Validate JQL and allow-listed actions for transition, set fields, add comment, and add labels.
- Persist an immutable plan with count, bounded sample, limits, action, and target fingerprint.

## Success Criteria

- [ ] Invalid JQL, action properties, or unavailable transitions block approval.
- [ ] A count above `maxIssues` blocks approval.
- [ ] Preview sends no Jira mutation request and does not persist sampled issue content.

## Evidence

- [ ] JQL, action-schema, over-limit, privacy, and read-only tests.