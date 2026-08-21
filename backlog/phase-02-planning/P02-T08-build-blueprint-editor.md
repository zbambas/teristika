# P02-T08 - Build Blueprint Editor

- Type: Task
- Phase: 02 - Read-Only Planning
- Parent: P02-S02
- Depends on: P02-S01
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

An authorized configuration owner can create or clone a blueprint draft and publish it as a new immutable version.

## Work

- Add draft create, clone, edit, discard, and publish workflows with metadata, parameter, resource, dependency, validation-suite, test-data, and batch sections.
- Provide synchronized structured form and raw YAML or JSON views using the restricted blueprint contract.

## Success Criteria

- [ ] Creating and cloning produce separate drafts without changing the source version.
- [ ] Stable logical resource IDs, dependencies, and parameter placeholders round-trip between structured and raw views.
- [ ] Publishing requires an unused version, valid content, explicit confirmation, and configuration-owner permission.
- [ ] Concurrent draft edits are detected and cannot silently overwrite newer content.

## Evidence

- [ ] Draft, clone, round-trip, version, authorization, concurrency, keyboard, and responsive tests plus Senior QA screenshots.