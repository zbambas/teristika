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
- [ ] Successful mutations are read back and removed from the sandbox when supported.
- [ ] Undocumented endpoints are not used.

## Evidence

- [ ] Completed resource rows and sanitized request summaries in the capability matrix.