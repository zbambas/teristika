# P05-T01 - Plan Test-Data Packs

- Type: Task
- Phase: 05 - Test Data and Validation
- Parent: P05-S01
- Depends on: P04-S01
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

An operator can preview a fully resolved test-data pack before creating issues.

## Work

- Validate logical issue IDs, issue type references, field values, links, and account references.
- Resolve Jira create metadata and persist an immutable test-data plan.

## Success Criteria

- [ ] Preview shows issue and link counts, resolved types, and blocking field errors.
- [ ] Missing logical references, required fields, or account IDs block approval.
- [ ] Planning creates no Jira issue, comment, link, or attachment.

## Evidence

- [ ] Parser, create-metadata, reference, field-error, and read-only tests.