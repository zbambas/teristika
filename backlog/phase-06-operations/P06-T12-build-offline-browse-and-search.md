# P06-T12 - Build Offline Browse and Search

- Type: Task
- Phase: 06 - Operations and Release
- Parent: P06-S03
- Depends on: P06-T11
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

Users can browse and search synchronized Jira content without sending a Jira request.

## Work

- Add Online, Automatic, and Offline modes with visible source, snapshot, completeness, and freshness state.
- Add repository search and browsing across projects, issues, configuration, comments, worklogs, changelog, users, boards, sprints, links, and permitted attachment content.

## Success Criteria

- [ ] Offline mode blocks all Jira requests and serves results only from the selected complete snapshot.
- [ ] Search supports text, project, entity type, status, date, and relationship filters with permission-scoped result counts and snippets.
- [ ] Stale, incomplete, empty, purged, partial-visibility, and no-attachment-content states are explicit and cannot appear live.
- [ ] Switching back online refreshes live state only after an explicit request or configured automatic policy.

## Evidence

- [ ] Network-denial, mode, search, filters, authorization, stale, incomplete, empty, attachment, keyboard, and responsive tests.