# P06-T11 - Build Offline Jira Synchronization

- Type: Task
- Phase: 06 - Operations and Release
- Parent: P06-S03
- Depends on: P02-S03
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

The application creates consistent full and incremental snapshots of authorized Jira data.

## Work

- Synchronize site and project metadata, configuration, users or account references, issues, fields, links, comments, worklogs, changelog, sprints, boards, attachments metadata, and attachment content when policy enables it.
- Store structured records in PostgreSQL, search documents in PostgreSQL full-text indexes, and encrypted attachment content through the configured blob-storage adapter.

## Success Criteria

- [ ] Full sync paginates every enabled entity and incremental sync applies updates, additions, and tombstones without duplicates.
- [ ] A versioned manifest records connection, projects, snapshot boundary, entity counts, API coverage, inaccessible or unsupported data, failures, attachment policy, and completion state.
- [ ] Interrupted sync resumes from durable checkpoints and does not expose a partial snapshot as complete.
- [ ] Rate limits, permission loss, deleted records, malformed responses, and Jira outages produce bounded classified outcomes.

## Evidence

- [ ] Entity contract, pagination, incremental, tombstone, checkpoint, manifest, attachment, rate-limit, permission, and outage tests.