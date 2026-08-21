# Common Prompts

Copy these prompts into the VS Code chat to use the repository's existing product, architecture, blueprint, backlog, and agent files. Replace values inside `{...}`.

For implementation work, select the **Solution Manager** agent. It orchestrates the mandatory Senior Developer and Senior QA tandem and calls UX, security, or data/database specialists when relevant.

## Source Priority

When files disagree, use this order and report the conflict:

1. The selected issue under [`backlog/`](../backlog/README.md) defines the immediate work and success criteria.
2. [`backlog/README.md`](../backlog/README.md) defines delivery flow and roles.
3. [`product-brief.md`](product-brief.md) defines product scope and MVP outcomes.
4. [`solution-architecture.md`](solution-architecture.md) defines the required Django architecture and quality boundaries.
5. [`blueprint-contract.md`](blueprint-contract.md), the [JSON Schema](../schemas/jira-project-blueprint.schema.json), and the [example blueprint](../blueprints/examples/erste-project.yaml) define deployment input.
6. [`delivery-backlog.md`](delivery-backlog.md) provides roadmap context; issue files remain authoritative for execution.

Never infer undocumented Jira API support. Phase 00 capability evidence controls what the application may claim or implement.

## Start or Resume Work

### Execute the Next Ready Task

```text
Work as Solution Manager. Read backlog/README.md and the product and architecture documents it references. Select the lowest-phase unblocked task, confirm every dependency is Done, and execute exactly that task through the required Senior QA pre-check, Senior Developer implementation, independent QA verification, and any relevant UX, security, or data/database review. Update issue status only according to the documented flow. Stop on a real blocker; do not widen scope. Report evidence and the next eligible task.
```

### Execute a Specific Task

```text
Work as Solution Manager on {ISSUE_ID}. Read its issue file, parent story, dependencies, backlog/README.md, docs/product-brief.md, and the relevant sections of docs/solution-architecture.md. Confirm the task is unblocked. Decide whether UX, security, or data/database support is required and record why. Run the complete Developer/QA workflow, satisfy every success criterion with evidence, and change status only as allowed. Do not work on another issue.
```

### Resume Interrupted Work

```text
Resume {ISSUE_ID} as Solution Manager. Inspect the issue status, current diff, available test results, and prior evidence. Determine the last completed workflow step without assuming success. Continue from that point with the same task and specialists. Re-run any check whose result is missing or stale. Do not discard unrelated user changes. Finish with the current status, verified evidence, blockers, and next action.
```

### Assess Status Without Editing

```text
Read backlog/README.md and all phase issue metadata without changing files. Report the current phase, Done/In Progress/Ready/Backlog counts, blocked tasks with unmet dependencies, the next eligible task, and any inconsistent status or dependency. Keep the report concise and link each mentioned issue.
```

## Planning and Backlog

### Prepare One Task for Implementation

```text
Review {ISSUE_ID} without implementing it. Read its parent, dependencies, product scope, architecture, and relevant blueprint contract. Confirm that the outcome is singular, work is bounded, dependencies are sufficient, and success criteria are binary and testable. Identify required UX, security, or data/database consultation. Propose only the smallest clarification needed; do not expand scope or change status.
```

### Create a New Backlog Issue

```text
Create one new {Story|Task} for this project using backlog/ISSUE_TEMPLATE.md. Place it in the correct phase, assign a unique ID, define explicit dependencies, keep one observable outcome, and add deterministic success criteria and evidence. Align it with docs/product-brief.md, docs/solution-architecture.md, and docs/blueprint-contract.md. Update parent story task ranges or backlog indexes when required, then validate all issue references and links.
```

### Split an Oversized Task

```text
Review {ISSUE_ID} for scope only. If it cannot be completed and verified as one deterministic change, split it into the smallest ordered tasks using backlog/ISSUE_TEMPLATE.md. Preserve the original outcome at story level, make dependencies explicit, keep each task independently testable, and update affected references. Do not implement the tasks.
```

### Review Phase Readiness

```text
Review phase {PHASE_NUMBER} against its parent story, dependencies, product requirements, architecture, and previous phase exit criteria. Do not edit code. List missing prerequisites, ambiguous Jira capabilities, absent security or data controls, and untestable criteria. Finish with READY or NOT READY and the minimum actions needed.
```

## Specialist Support

These prompts are normally given to the **Solution Manager**, which invokes the hidden specialist and integrates its findings into the same issue.

### UX Review

```text
For {ISSUE_ID}, invoke Senior UX Specialist in design-review mode before implementation. Review the complete user journey and empty, loading, success, warning, error, disabled, keyboard, accessibility, desktop, and mobile states. Keep findings within the issue scope. Pass blocking findings to Senior QA and Senior Developer, then request UX verification after implementation when material UI behavior changed.
```

### Security Review

```text
For {ISSUE_ID}, invoke Senior Security Specialist in threat-review mode before implementation. Review trust boundaries, authorization, secrets, inputs, external Jira calls, mutation safeguards, audit, logging, task payloads, and sensitive data. Convert material risks into bounded checks. After implementation, request security verification and do not close the issue while a high-severity finding remains.
```

### Data and Database Review

```text
For {ISSUE_ID}, invoke Senior Data Modeler and Database Specialist in data-review mode before implementation. Review entities, ownership, cardinality, identifiers, constraints, indexes, migrations, transactions, locking, retention, recovery, and expected volume. Convert material invariants into deterministic checks. After implementation, request verification of migrations and PostgreSQL behavior before closure.
```

### Combined Specialist Review

```text
For {ISSUE_ID}, determine which optional specialists are relevant from the triggers in .github/agents/solution-manager.agent.md. Invoke all relevant specialists before implementation, deduplicate overlapping findings, and give Senior QA one consolidated check plan. After implementation, ask each consulted specialist to verify only its material findings. Specialists advise; Senior QA remains mandatory and Solution Manager controls status.
```

## Quality and Verification

### Verify an Implementation

```text
Work as Solution Manager and verify {ISSUE_ID}. Confirm the issue is in QA, inspect the diff and Developer evidence, then invoke Senior QA in verification mode. Re-run focused checks and relevant failure paths. Invoke previously consulted specialists for verification. Map evidence to every success criterion. Mark Done only if all criteria pass and no requested specialist has an unresolved blocking finding.
```

### Investigate a Failed Check

```text
Investigate the failure for {ISSUE_ID} without opening a new scope. Reproduce the exact failing command, identify whether the cause is implementation, test, environment, Jira capability, or stale assumption, and preserve unrelated changes. Have Senior Developer repair only the local defect, then have Senior QA independently rerun the focused check. Record any environmental blocker with exact evidence.
```

### Review a Django Migration

```text
For {ISSUE_ID}, ask Senior Data Modeler and Database Specialist and Senior QA to review the Django model and migration changes. Verify forward and reverse behavior, constraints, indexes, defaults, existing-row handling, transaction boundaries, deployment compatibility, and PostgreSQL execution. Do not use production data. Return PASS or FAIL with commands and the affected invariant.
```

### Review Security Boundaries

```text
For {ISSUE_ID}, ask Senior Security Specialist and Senior QA to verify authorization, CSRF, object ownership, upload limits, secret redaction, external request handling, audit completeness, and cross-project isolation as applicable. Use seeded fake secrets and non-production fixtures. Return findings by severity with reproduction steps and do not edit expected results to make tests pass.
```

### Review User Experience

```text
For {ISSUE_ID}, ask Senior UX Specialist and Senior QA to verify the implemented Django and HTMX flow. Check keyboard operation, visible focus, semantic status, validation messages, stable layout, responsive desktop/mobile behavior, and all asynchronous states. Return blocking and advisory findings separately with screenshots or exact reproduction steps.
```

## Product and Architecture

### Assess a Proposed Requirement

```text
Assess this proposal against docs/product-brief.md, docs/solution-architecture.md, docs/blueprint-contract.md, and the current backlog: {PROPOSAL}. Identify whether it is in MVP scope, affected users and workflows, architecture impact, Jira capability evidence needed, security and data implications, and the smallest backlog change. Do not implement or silently change scope.
```

### Check Architecture Consistency

```text
Review {FILES_OR_CHANGE} against docs/solution-architecture.md. Confirm it uses Django 5.2 LTS, Django templates and HTMX, DRF, Django ORM and migrations, PostgreSQL, Celery/Beat, Redis, and the shared HTTPX Jira adapter. Identify duplicated frameworks, boundary violations, unsafe state handling, or missing tests. Return findings first and do not edit unless explicitly asked.
```

### Change the Blueprint Contract

```text
Evaluate this blueprint change: {CHANGE}. Read docs/blueprint-contract.md, schemas/jira-project-blueprint.schema.json, blueprints/examples/erste-project.yaml, and affected backlog issues. Preserve stable logical IDs, dependency resolution, strict unknown-property rejection, non-destructive desired state, and versioning rules. Update schema, example, documentation, and focused validation together; report any breaking change requiring a new apiVersion.
```

### Run a Jira Capability Probe

```text
Execute the Phase 00 task {ISSUE_ID} against the approved Jira Cloud sandbox using only documented APIs. Never place credentials in prompts, files, logs, or fixtures. Record sanitized request metadata, response classification, permissions, scopes, cleanup result, and capability disposition. Update the capability matrix only with verified evidence and do not infer support from documentation alone.
```

### Review Jira Credential Rotation

```text
For {ISSUE_ID}, ask Senior Security Specialist and Senior QA to verify the staged Jira credential flow. Confirm the secret value goes directly to the external secret store, never appears in application persistence or diagnostics, candidate testing is read-only and classified, failed testing preserves the active reference, and only the exact successfully tested candidate can be explicitly activated. Use seeded fake tokens, not production credentials.
```

### Review Offline Repository

```text
For {ISSUE_ID}, ask Senior Security Specialist, Senior Data Modeler and Database Specialist, and Senior QA to verify offline synchronization and browsing. Confirm the manifest records scope, counts, omissions, failures, attachment policy, and completeness; partial snapshots are hidden; Offline mode denies every Jira request; local search uses only authorized encrypted repository data; and retention, purge, quota, backup, and restore preserve the last complete permitted snapshot.
```

### Review User and Access Management

```text
For {ISSUE_ID}, ask Senior Security Specialist, Senior Data Modeler and Database Specialist, and Senior QA to verify application access governance. Confirm issuer plus subject identifies users, production has no local password, group and direct assignments are scoped and time-aware, effective access denies by default, suspension and session revocation take effect within policy, the final administrator is protected, and access-review decisions are attributable and redacted.
```

### Review Blueprint Capture from Jira

```text
For {ISSUE_ID}, ask Senior Security Specialist and Senior QA to verify reference-project capture. Confirm only a tested connection and capability-approved read endpoints are used; project-owned, shared, reference-only, unsupported, inaccessible, ambiguous, and omitted resources are explicit; generated logical IDs and parameters are portable and deterministic; Jira IDs remain provenance; secrets and issue data are excluded; and the result is an unpublished draft that must pass normal validation.
```

## Reporting

### Concise Delivery Status

```text
Summarize delivery status from the issue files, not from memory. Report current phase, active issue and status, completed evidence, blockers, unresolved QA or specialist findings, and next eligible issue. Mention repository changes only when verified. Keep the report under 20 lines.
```

### Phase Acceptance

```text
Assess story {STORY_ID} for completion. Verify every child task is Done, every dependency and story success criterion has evidence, required QA and specialist findings are resolved, and the phase exit demonstration matches docs/delivery-backlog.md. Return ACCEPT or REJECT with missing evidence. Only Solution Manager may update the story status.
```

### Handoff to Another Session

```text
Prepare a session handoff for {ISSUE_ID}. State the exact issue status, files changed, commands and results, evidence already accepted, unresolved findings, blockers, preserved unrelated changes, and the next workflow step. Reference repository files instead of copying large content. Do not claim checks that were not run.
```

## Prompt Rules

- Use one issue per implementation prompt.
- Name the issue ID instead of describing work only in prose.
- Ask for evidence, not confidence statements.
- Keep production credentials and data out of prompts.
- Use the Solution Manager for status-changing work.
- Use direct specialist prompts only for read-only analysis; return their findings to the Solution Manager.
- Do not bypass Phase 00 capability evidence for Jira mutations.
- Do not mark work complete when tests, migrations, security checks, or specialist verification required by the issue are missing.