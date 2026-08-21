# P02-T13 - Generate Blueprint Draft from Jira

- Type: Task
- Phase: 02 - Read-Only Planning
- Parent: P02-S04
- Depends on: P02-T12, P02-T09
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

Selected reference-project configuration becomes a provenance-linked, validated blueprint draft.

## Work

- Convert selected normalized Jira resources into deterministic logical IDs, typed properties, dependency edges, reusable parameters, and shared-resource references.
- Create a mutable draft with source connection, project ID and key, discovery snapshot, capture time, actor, selected and omitted resource IDs, and transformation warnings.

## Success Criteria

- [ ] Equivalent normalized project state produces the same canonical draft content and logical IDs.
- [ ] Jira object IDs remain provenance or mapping metadata and are not used as portable logical IDs.
- [ ] Environment-specific project key, name, lead, and approved values become explicit parameters; secrets never enter the draft.
- [ ] The review shows selected, automatic dependency, shared, reference-only, unsupported, inaccessible, and omitted counts before draft creation.
- [ ] Draft creation is blocked by unresolved ambiguity or validation errors and never publishes automatically.

## Evidence

- [ ] Determinism, logical-ID, dependency, parameterization, provenance, classification, validation-guard, redaction, editor-routing, and sandbox capture tests.