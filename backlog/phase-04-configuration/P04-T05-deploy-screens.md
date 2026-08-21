# P04-T05 - Deploy Screens and Screen Schemes

- Type: Task
- Phase: 04 - Configuration Catalog
- Parent: P04-S01
- Depends on: P04-T04
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

Capability-supported screens, tabs, field placements, and screen schemes deploy deterministically.

## Work

- Implement screen, screen scheme, and issue type screen scheme handlers.
- Normalize tab and field order only where Jira preserves order through the approved API.

## Success Criteria

- [ ] Required fields resolve before placement and duplicate placements are prevented.
- [ ] Create, edit, and view operations map to the expected screens after read-back.
- [ ] API order limitations are reported instead of causing perpetual drift.

## Evidence

- [ ] Contract tests and sandbox placement, association, and rerun report.