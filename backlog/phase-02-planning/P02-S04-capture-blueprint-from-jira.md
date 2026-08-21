# P02-S04 - Capture Blueprint from Jira Project

- Type: Story
- Phase: 02 - Read-Only Planning
- Parent: None
- Depends on: P02-S02, P02-S03
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

An authorized configuration owner can select an existing Jira project and create a validated blueprint draft from its supported configuration.

## Work

- Discover and classify the selected reference project's project-scoped and shared Jira configuration.
- Select resources, transform observed Jira IDs into stable logical references and parameters, and generate a provenance-linked draft.

## Success Criteria

- [ ] Tasks P02-T12 and P02-T13 are Done.
- [ ] Capture uses only capability-approved read APIs and makes no Jira mutation.
- [ ] Unsupported, inaccessible, shared, ambiguous, and omitted configuration is explicit before draft creation.
- [ ] The generated draft passes through the existing Blueprint Editor and validator before publication.

## Evidence

- [ ] Jira sandbox discovery, classification, transformation, provenance, validation, authorization, accessibility, and responsive evidence.