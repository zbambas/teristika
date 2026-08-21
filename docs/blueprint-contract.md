# Blueprint Contract

The deployment input is a YAML or JSON document validated by [`jira-project-blueprint.schema.json`](../schemas/jira-project-blueprint.schema.json). The first schema version is `jira-deployer/v1alpha1` while resource-specific Jira behavior is proven against a sandbox.

## Identity and Versioning

- `metadata.id` identifies the blueprint across versions.
- `metadata.version` is an immutable author-provided release version.
- Every resource has a stable logical `id`. Renaming its Jira display name must not change this ID.
- The application stores a SHA-256 checksum of the canonical parsed document.
- A plan references the exact blueprint version and checksum it evaluated.

Logical IDs use lowercase letters, numbers, dots, and hyphens. Examples are `issue-type.requirement` and `workflow.requirement`.

## Draft and Publication Lifecycle

- A new blueprint or clone is stored as a mutable draft owned by its author.
- An uploaded YAML or JSON file is parsed into a draft candidate only after upload and content validation.
- Structured and raw-source editor modes represent the same parsed document and must round-trip without changing stable logical IDs or semantics.
- Any content change invalidates the previous validation result.
- Errors block import and publication. Warnings require acknowledgement when policy says so.
- Publication requires an unused version and creates a new immutable `blueprint_versions` record with its canonical checksum.
- A published version is never edited in place. Further changes begin by cloning it into another draft.
- Draft content cannot be selected by a deployment plan.

Validation findings include a stable code, severity, document path, line and column when available, message, remediation, and logical resource reference. Findings and logs must redact configured sensitive values.

## Capture from Jira

A blueprint can begin as a draft generated from one tested Jira connection and reference project. Capture uses capability-approved read-only APIs and follows these rules:

- every observed resource is classified as project-owned, shared, reference-only, unsupported, inaccessible, ambiguous, or policy-omitted before draft creation;
- the author explicitly selects included resources and shared-resource behavior;
- deterministic logical IDs derive from resource type and normalized stable meaning, not Jira object IDs;
- Jira IDs, connection ID, project ID and key, discovery boundary, actor, selected source items, omitted source items, and warnings are stored as application provenance outside portable deployment content;
- project key, name, lead, and other approved environment-specific values become explicit parameters;
- secrets, credential references, users, issue data, and unsupported properties are not copied into the blueprint;
- handler-inferred dependencies are added and shown as automatic additions;
- unresolved ambiguity and validation errors block draft creation;
- generated content is a mutable draft and must complete normal validation and explicit publication.

Equivalent normalized Jira state and capture decisions must produce equivalent canonical blueprint content.

## Parameters

Parameters contain environment-specific non-secret values such as project key, project name, and lead account ID. A scalar string can contain an exact placeholder such as `{{ parameters.projectKey }}`. The implementation must use a restricted placeholder resolver, not a general template or expression engine.

The first release does not permit sensitive blueprint parameters. Credentials and other secrets are represented by connection-level secret references managed outside the blueprint.

Parameter resolution happens before planning. Missing required values, invalid project keys, and unresolved placeholders are blocking errors.

## Resources

Resources are the smallest selectable and auditable deployment units:

```yaml
- id: workflow.requirement
  type: workflow
  scope: global
  dependsOn:
    - status.new
    - status.in-progress
    - status.done
  properties:
    name: Requirement Workflow
```

Top-level resource fields are schema-validated. Each Jira resource handler applies a stricter typed model to `properties`. A resource type with unknown properties is invalid; adapters must not discard unknown data.

`scope: global` means the Jira object may be shared by several projects. Updating it has a wider blast radius and can require additional approval. `scope: project` means the object is owned by, assigned to, or contained by the target project.

All dependencies are logical resource IDs. The planner combines explicit `dependsOn` entries with mandatory dependencies inferred by the typed resource handler. Cycles and missing references block planning.

## Selection Rules

- Selecting a resource selects its transitive dependencies.
- A user cannot deselect a required dependency while retaining the dependent resource.
- Automatically added resources are distinguished from directly selected resources.
- Selecting a parent group in the UI is only a convenience; the plan records concrete resource IDs.
- Test-data packs, validation suites, and batches are selected independently from configuration resources.

## Desired State and Deletion

The only accepted desired state in `v1alpha1` is `present`. A missing resource can be created and a mapped resource can be updated if the handler supports that action.

Absence from a blueprint does not request deletion. A future deletion contract must include explicit lifecycle policy, impact analysis, and stronger approval semantics.

## Test-Data Packs

Issues use logical IDs within a pack. The application creates all issues, stores their assigned Jira IDs and keys, and then creates links. Fields are resolved through Jira create metadata before mutation.

The application adds its run marker even when it is omitted from the file. Cleanup is allowed only for issues that match both durable mappings and the Jira-side run marker.

## Validation Suites

Validation rules have stable IDs so trends and waivers can be tracked. `resourceMatches` compares a blueprint resource with normalized Jira state. Workflow smoke rules can create temporary issues only when the user explicitly enables mutation for that validation run.

An unsupported check returns `unsupported`; it does not pass. A skipped dependent check reports the failed prerequisite.

## Batches

Batches define allow-listed issue actions and safety limits. The JQL and action are parameters to a generated plan, not commands sent directly from the browser to Jira.

Schedules are not stored in the blueprint because they are environment-specific operational state. A schedule references a blueprint version and batch or validation ID.

## Evolution Rules

- Additive compatible fields can remain within `v1alpha1` while it is experimental.
- A breaking field or semantic change requires a new `apiVersion` and a deterministic migration.
- The parser rejects unknown top-level keys and unknown typed resource properties.
- Stored blueprint versions are never rewritten during migration; a migrated document becomes a new version.

See [`erste-project.yaml`](../blueprints/examples/erste-project.yaml) for a representative starting point derived from the current SimpleMind model.