# Implementation Backlog

This folder is the canonical execution backlog. Work proceeds phase by phase and task by task; [`docs/delivery-backlog.md`](../docs/delivery-backlog.md) is the product-level roadmap.

## Agent Operating Model

- **Solution Manager** selects the next unblocked issue, provides context, controls scope, resolves disagreements, and changes issue status.
- **Senior Developer** implements only the selected task and adds the required automated checks.
- **Senior QA** reviews the task before implementation, identifies test cases from its criteria, and independently verifies the result.
- **Senior UX Specialist** optionally reviews user flows, templates, accessibility, interactions, and responsive behavior.
- **Senior Security Specialist** optionally reviews trust boundaries, authorization, secrets, inputs, external calls, audit, and data exposure.
- **Senior Data Modeler and Database Specialist** optionally reviews models, migrations, PostgreSQL constraints, indexes, transactions, locking, retention, and recovery.
- All delegated specialist agents use the `gemini-flash 3.7` model.
- The Developer and QA always work as a tandem on the same issue. A task is not done until both roles provide evidence and the Solution Manager accepts it.
- UX, security, and data/database specialists support the tandem when relevant; they do not replace QA or control issue status.
- Run one mutating task at a time. Read-only research may run in parallel when the Solution Manager explicitly requests it.

Workspace agents:

- [Solution Manager](../.github/agents/solution-manager.agent.md) is the user-facing entry point.
- [Senior Developer](../.github/agents/senior-developer.agent.md) is the implementation subagent.
- [Senior QA](../.github/agents/senior-qa.agent.md) is the read-only verification subagent.
- [Senior UX Specialist](../.github/agents/senior-ux-specialist.agent.md) is optional read-only UX support.
- [Senior Security Specialist](../.github/agents/senior-security-specialist.agent.md) is optional read-only security support.
- [Senior Data Modeler and Database Specialist](../.github/agents/senior-data-modeler-database-specialist.agent.md) is optional read-only data and database support.

## Issue Flow

`Backlog -> Ready -> In Progress -> QA -> Done`

1. The Solution Manager confirms that all `Depends on` issues are `Done` and changes the issue to `Ready`.
2. The Solution Manager records whether UX, security, or data/database support is needed and collects applicable specialist findings.
3. Senior QA translates the criteria and specialist findings into checks and flags ambiguity before code changes.
4. Senior Developer implements the smallest change that satisfies the issue and records implementation evidence.
5. Senior QA runs the listed checks plus relevant failure-path checks; consulted specialists verify their material concerns.
6. The Solution Manager accepts the evidence, updates documentation when required, and marks the issue `Done`.
7. A story is `Done` only after every task in its phase and the story-level evidence are complete.

If a task cannot meet its criteria without wider work, stop it and create or revise a dependent issue. Do not silently expand scope.

## Issue Structure

Every story and task uses [`ISSUE_TEMPLATE.md`](ISSUE_TEMPLATE.md):

- metadata: type, phase, parent, dependencies, pair, and status;
- outcome: one observable result;
- work: bounded implementation scope;
- success criteria: binary acceptance checks;
- evidence: commands, tests, screenshots, reports, or reviewed artifacts.

Stories use the same structure as tasks. Their work lists phase capabilities, and their evidence aggregates completed child tasks and the phase exit demonstration.

## Mockup Traceability Contract

- [`mockups/jira-project-deployer.html`](../mockups/jira-project-deployer.html) is the canonical visual, interaction, responsive, accessibility, and state contract for task-owned UI until an approved ticket and architecture update supersede it.
- A `data-ticket="Pxx-Tyy"` value maps that rendered surface to its owning task. Developer implements the mapped behavior and Senior QA verifies it at desktop and mobile sizes, including keyboard, focus, loading, empty, partial, error, stale, permission, and destructive states that apply to the task.
- Product data and safety decisions shown in the prototype must be backed by Django domain state, named URLs, forms or HTMX requests, server-side authorization, and server-side validation; client-side prototype guards are not sufficient implementation evidence.
- Ticket hover labels and the delivery-ticket inspector are prototype traceability aids. They help find ownership but are not shipped in the production application unless a task explicitly requires them.
- If a ticket, governing document, and mockup disagree, stop the task and ask Solution Manager to resolve and record the contract change before implementation continues.

## Phases

| Phase | Story | Goal |
| --- | --- | --- |
| 00 | [P00-S01](phase-00-capability/P00-S01-jira-capability-proof.md) | Prove Jira Cloud API capabilities |
| 01 | [P01-S01](phase-01-foundation/P01-S01-django-foundation.md), [P01-S02](phase-01-foundation/P01-S02-operator-workspace.md), [P01-S03](phase-01-foundation/P01-S03-user-access-management.md) | Establish the Django foundation, operator workspace, and access governance |
| 02 | [P02-S01](phase-02-planning/P02-S01-read-only-planning.md), [P02-S02](phase-02-planning/P02-S02-blueprint-authoring.md), [P02-S03](phase-02-planning/P02-S03-secure-jira-credentials.md), [P02-S04](phase-02-planning/P02-S04-capture-blueprint-from-jira.md) | Secure Jira access, capture or author blueprints, and produce explainable plans |
| 03 | [P03-S01](phase-03-deployment/P03-S01-safe-deployment.md) | Execute durable, idempotent deployments |
| 04 | [P04-S01](phase-04-configuration/P04-S01-configuration-catalog.md) | Deploy the required Jira configuration catalog |
| 05 | [P05-S01](phase-05-validation/P05-S01-test-data-validation.md) | Seed test data and verify deployed behavior |
| 06 | [P06-S01](phase-06-operations/P06-S01-batch-release.md), [P06-S02](phase-06-operations/P06-S02-issue-dependency-explorer.md), [P06-S03](phase-06-operations/P06-S03-offline-jira-repository.md) | Add operations, dependency exploration, and secure offline browsing |

## Global Done Rules

Unless an issue narrows them, all tasks require:

- implementation and tests follow the Django architecture and existing repository conventions;
- migrations are deterministic and reversible when a model changes;
- secrets and authorization values are absent from logs, errors, fixtures, and stored diagnostics;
- relevant automated checks pass from a clean environment;
- no unrelated files or behavior are changed;
- Developer evidence and independent QA evidence are attached to the issue or execution report.