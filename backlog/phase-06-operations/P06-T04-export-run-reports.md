# P06-T04 - Export Run Reports

- Type: Task
- Phase: 06 - Operations and Release
- Parent: P06-S01
- Depends on: P06-T03
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

Authorized users can export stable JSON and human-readable run evidence.

## Work

- Export actor, target, blueprint checksum, plan summary, steps, batch summary, and validation summary.
- Apply the shared redaction policy and record the export audit event.

## Success Criteria

- [ ] JSON output validates against a versioned report schema.
- [ ] HTML is the minimum human-readable MVP format and contains the same result totals, identifiers, actor, target, blueprint version, and timestamp as the JSON export; PDF may be added without changing content.
- [ ] Unauthorized users receive `403`; exports contain no configured secret values.

## Evidence

- [ ] Schema, JSON-to-HTML parity, totals, authorization, audit, and redaction tests with sample exports.