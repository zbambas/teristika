# P02-T04 - Resolve Resource Dependencies

- Type: Task
- Phase: 02 - Read-Only Planning
- Parent: P02-S01
- Depends on: P02-T03
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

A selected resource set expands to a valid, ordered dependency graph with explanations.

## Work

- Combine explicit blueprint dependencies with handler-inferred dependencies.
- Detect missing references and cycles and produce a stable topological order.

## Success Criteria

- [ ] Selecting the example workflow includes its statuses and explains each path.
- [ ] Input order does not change the resulting operation order.
- [ ] Missing references and cycles return blocking structured errors.

## Evidence

- [ ] Graph tests for transitive expansion, stable order, missing nodes, and cycles.