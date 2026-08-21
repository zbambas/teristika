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
- [ ] Publishing requires an unused version, valid content, explicit confirmation, configuration-owner permission, the exact validation-run identifier, and recorded warning acknowledgements.
- [ ] Concurrent draft edits are detected and cannot silently overwrite newer content.
- [ ] Any navigation, browser-history, or close attempt away from a dirty draft requires discard confirmation or preserves the draft for later recovery.

## Evidence

- [ ] Draft, clone, round-trip, version, validation-evidence, warning-acknowledgement, dirty-route, authorization, concurrency, keyboard, and responsive tests plus Senior QA screenshots.