# P02-T02 - Ingest and Validate Blueprints

- Type: Task
- Phase: 02 - Read-Only Planning
- Parent: P02-S01
- Depends on: P02-T01
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

Django stores immutable blueprint versions only after schema and parameter validation.

## Work

- Add blueprint and version models, migrations, upload form, parser, and checksum calculation.
- Validate YAML or JSON against the repository schema and resolve restricted placeholders.

## Success Criteria

- [ ] The example blueprint stores with its canonical SHA-256 checksum.
- [ ] Invalid syntax, schema, project key, and unresolved parameter errors include a document path.
- [ ] Reusing a blueprint ID and version with different content is rejected.

## Evidence

- [ ] Parser, model-constraint, upload, and parameter-resolution tests.