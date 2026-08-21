# P06-T10 - Build Issue Dependency Explorer

- Type: Task
- Phase: 06 - Operations and Release
- Parent: P06-S02
- Depends on: P06-T09
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

An operator can switch among Gantt, radial, network, and matrix views of the same project dependency data.

## Work

- Add project-scoped filters, representation switcher, legend, issue selection, dependency detail, and shareable view state.
- Render Gantt schedule and critical path, radial issue neighborhood, directional network flow, and dependency matrix with accessible alternatives.

## Success Criteria

- [ ] Filters, selected issue, relationship types, and counts remain consistent when representations change.
- [ ] Gantt distinguishes missing dates and cycles; radial and network views distinguish direction and relationship type; matrix supports row and column inspection.
- [ ] Keyboard users can select issues and dependencies and access equivalent textual detail without relying on color or pointer position.
- [ ] Desktop and mobile views avoid overlap and large datasets use an explicit limit or aggregation state.

## Evidence

- [ ] Django view, state, representation consistency, keyboard, screen-reader, responsive, large-result, and Senior QA screenshot evidence.