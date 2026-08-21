# P00-T03 - Probe Jira Configuration APIs

- Type: Task
- Phase: 00 - Capability Proof
- Parent: P00-S01
- Depends on: P00-T02
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

Every proposed MVP Jira resource has verified read and mutation capabilities.

## Work

- Probe project, component, version, issue type, status, workflow, field, screen, and scheme APIs.
- Record endpoint, method, scope, permission, result, and cleanup action for each probe.

## Success Criteria

- [ ] Each resource is classified as create, update, associate, read-only, or unavailable.
- [ ] Each successful mutation is read back and its Jira ID and capability-relevant properties match the request.
- [ ] Every created probe resource is removed from the sandbox, or the matrix records that no supported deletion operation exists plus the owner's approved cleanup disposition.
- [ ] Undocumented endpoints are not used.

## Evidence

- [ ] Completed resource rows and sanitized request summaries in the capability matrix.