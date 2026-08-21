# P02-T09 - Build Blueprint Validation Review

- Type: Task
- Phase: 02 - Read-Only Planning
- Parent: P02-S02
- Depends on: P02-T08
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

An authorized user can upload YAML or JSON and review every blueprint issue before saving or publishing it.

## Work

- Add size-limited file upload and validation for syntax, envelope schema, typed resource properties, identifiers, parameters, references, dependencies, and cycles.
- Present severity, code, document path, line and column when available, message, remediation, and navigation to the affected editor field or source line.

## Success Criteria

- [ ] Unsupported extension, oversized file, invalid encoding, malformed syntax, schema, typed-property, duplicate-ID, missing-reference, cycle, and unresolved-parameter cases are reported distinctly.
- [ ] Selecting a finding opens the affected structured field or raw source location without changing content.
- [ ] Errors block draft import and publication; warnings require acknowledgement according to policy.
- [ ] Upload and validation persist no invalid version, make no Jira request, and redact configured sensitive values from findings and logs.

## Evidence

- [ ] Upload boundary, issue-location, navigation, publication-guard, no-write, redaction, accessibility, and responsive tests.