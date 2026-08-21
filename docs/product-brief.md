# Jira Project Deployer - Product Brief

Status: Draft v0.1
Date: 2026-08-21
Product owner: Project team

## 1. Product Vision

Provide Jira administrators with a controlled way to describe, preview, deploy, test, and validate Jira project configurations without repeating error-prone manual administration.

The product turns a versioned project blueprint into an execution plan. An administrator can deploy the complete blueprint or select a dependency-safe subset, seed disposable test data, validate the resulting Jira project, and run the same operations immediately or on a schedule.

## 2. Product Decisions

These decisions remove ambiguity for the first release:

- The first target is Jira Cloud in an existing Jira site.
- "Deploy from scratch" means create and configure a Jira project in that site. Creating an Atlassian organization or Jira site is out of scope.
- Jira Data Center support is a later adapter, not an MVP requirement.
- A blueprint is the version-controlled source of desired configuration.
- Every mutation starts with a dry-run plan that shows creates, updates, unchanged items, unsupported items, and conflicts.
- MVP reconciliation is non-destructive. It creates and updates configuration but does not delete existing Jira configuration.
- The only MVP delete operation is cleanup of test issues created and tagged by this application.
- A partial deployment automatically includes required dependencies. The user must see and approve those additions before execution.
- "Batch processing" initially covers scheduled or immediate deployments, validations, test-data operations, and a controlled set of issue actions over a JQL selection. It does not allow arbitrary scripts.

## 3. Users

### Jira Administrator

Connects Jira sites, manages credentials and capabilities, approves plans, executes deployments, and investigates failures.

### Project Configuration Owner

Authors and reviews blueprints, chooses deployable components, prepares test-data packs, and checks validation results.

### Release or Test Manager

Runs approved deployments, seeds test data, starts validation suites, schedules recurring checks, and exports evidence.

### Auditor

Reads immutable execution history: who ran what, against which site and project, from which blueprint version, and with what result.

## 4. Outcomes and Measures

- A standard project can be deployed to a clean Jira site in less than 30 minutes of elapsed time and less than 10 minutes of operator effort.
- At least 90% of supported configuration drift is detected by automated validation.
- Re-running a successful deployment causes no duplicate Jira objects and no unintended changes.
- Every Jira mutation can be traced to a user, blueprint version, plan, timestamp, and API result.
- A failed job can be retried without repeating completed idempotent steps.

## 5. Functional Scope

### FR-01: Jira Connections

An administrator can register a Jira Cloud site, authenticate it, test connectivity, and see the permissions and API capabilities available to the application.

### FR-02: Blueprint Management

The application can load, validate, version, and display declarative project blueprints. A blueprint can describe:

- project metadata and project roles;
- issue types and issue type schemes;
- statuses, workflows, transitions, and workflow schemes;
- custom fields, field contexts, screens, and field configurations;
- priorities, resolutions, components, versions, and labels;
- permission, notification, and issue-security scheme references;
- filters and dashboards where supported by public APIs;
- validation rules, test-data packs, and batch definitions.

The existing `ErsteJiraSetUp.smmx` content is source material for the first blueprint, especially its issue types, statuses, fields, priorities, components, and requirement/test/deployment issue models. The SimpleMind file is not the deployment format.

### FR-03: Deployment Planning

Before execution, the application compares the blueprint with the target Jira site and produces a plan containing:

- requested components;
- automatically included dependencies;
- create, update, unchanged, conflict, and unsupported actions;
- required permissions and missing capabilities;
- warnings and blocking errors;
- a stable plan identifier and blueprint checksum.

### FR-04: Full Project Deployment

An authorized user can create a project and apply every supported component in dependency order. The job reports progress at component and resource level.

### FR-05: Partial Deployment

An authorized user can select individual configuration domains or resources in a tree. The application resolves dependencies, explains why they were added, and prevents an invalid selection from executing.

Example: selecting a workflow can include its statuses, custom fields used by transition rules, and the target workflow scheme.

### FR-06: Test Data

A user can preview and deploy a named test-data pack containing users or account references, epics, stories, tasks, tests, defects, links, comments, and field values. References between test issues are resolved deterministically.

Created issues carry an application run marker. A user can clean up only data created by that pack and run.

### FR-07: Validation

A user can run one or more validation suites:

- blueprint schema and dependency validation;
- connection, permission, and capability preflight;
- post-deployment read-back and desired-versus-actual comparison;
- workflow and field configuration checks;
- optional smoke tests that create, transition, verify, and clean up a temporary issue;
- drift detection against a previously deployed blueprint version.

Results distinguish pass, warning, fail, skipped, and unsupported.

### FR-08: Batch Processing

A user can run immediately or schedule an approved batch definition. MVP batch types are:

- deploy or validate one blueprint against one or more target projects;
- seed or clean up a test-data pack;
- transition issues selected by JQL;
- set an approved list of fields on issues selected by JQL;
- add a comment or label to issues selected by JQL.

Every issue batch shows a preview count and sample before approval. It has a configurable maximum issue count, rate limit, retry policy, and failure threshold.

### FR-09: Execution Control

Users can view queued, running, completed, failed, canceled, and partially completed jobs. Supported steps can be retried from the failed point. New mutations stop after cancellation is acknowledged.

### FR-10: Audit and Evidence

The application records the actor, target, blueprint and version, selected components, generated plan, approvals, timestamps, step outcomes, redacted API diagnostics, and final validation report. A user can export a run summary as JSON and human-readable HTML or PDF.

## 6. Core User Journeys

### Deploy a Complete Project

1. Select a Jira connection and blueprint version.
2. Enter project-specific parameters such as key, name, lead, and scheme references.
3. Generate a dry-run plan.
4. Resolve blocking permissions, conflicts, or unsupported components.
5. Approve and execute the immutable plan.
6. Follow live progress and inspect any failed step.
7. Run the default post-deployment validation suite.
8. Export the run report.

### Deploy Selected Configuration

1. Select a target project and blueprint version.
2. Choose resources from the configuration tree.
3. Review dependencies automatically included by the planner.
4. Generate and approve the dry-run plan.
5. Execute and validate only the approved scope.

### Seed and Remove Test Data

1. Select a target project and test-data pack.
2. Preview issue count, links, account references, and required fields.
3. Execute the pack and retain its run identifier.
4. Run smoke or acceptance validation.
5. Clean up issues belonging to that run when permitted.

### Run a Scheduled Validation

1. Select a validation suite, connection, project, and blueprint baseline.
2. Choose a schedule and notification policy.
3. Review and enable the schedule.
4. Inspect drift findings and acknowledge or remediate them.

## 7. MVP Acceptance Criteria

The MVP is complete when all of the following are demonstrated against a Jira Cloud sandbox:

- A user can connect one site without exposing credentials in logs or the database.
- A valid blueprint can create one company-managed Jira project.
- The project deployment supports at minimum project metadata, issue types, statuses and workflows, custom fields, screens, components, versions, and scheme association where the Jira API permits it.
- The planner reports unsupported configuration instead of silently skipping it.
- A user can select a subset and see all added dependencies before approval.
- Re-running the same plan is idempotent and does not create duplicates.
- A test-data pack can create at least 50 linked issues and clean up only those issues.
- A validation report identifies a deliberately introduced field, workflow, or component mismatch.
- A JQL-selected issue batch can be previewed, capped, executed, retried, and audited.
- A scheduled validation runs without an active browser session.
- Concurrent writes to the same Jira project are serialized.
- An interrupted worker resumes or safely retries without losing job state.

## 8. Non-Functional Requirements

- Security: least-privilege Jira access, encrypted transport, external secret storage, role-based application access, redacted logs, and no secret values in exports.
- Reliability: idempotency keys, bounded retries with backoff, durable job state, and per-target locking.
- Performance: plan 1,000 configuration resources in under 60 seconds, excluding Jira throttling; process issue batches at a configurable safe rate.
- Usability: every mutation has a preview; errors name the affected resource and a corrective action; progress is visible without refreshing the page.
- Maintainability: Jira-specific API behavior is isolated behind an adapter and capabilities are data-driven.
- Observability: structured logs, job and API metrics, correlation IDs, health checks, and an operator-visible failure reason.
- Accessibility: keyboard-operable controls, visible focus, semantic status text, and WCAG 2.2 AA contrast for the web application.

## 9. MVP Exclusions

- Provisioning an Atlassian organization, Jira Cloud site, or Jira Data Center installation.
- Supporting Jira Service Management portals, assets, SLAs, or customer organizations.
- Installing or configuring Marketplace applications.
- Migrating issue history, attachments, users, or production data between Jira sites.
- Deleting production configuration to force exact reconciliation.
- Executing arbitrary user-supplied code or unrestricted Jira REST requests.
- Providing a general-purpose Jira backup or disaster-recovery system.

## 10. Later Candidates

- Jira Data Center adapter.
- Git pull-request workflow for blueprint authoring and approval.
- Promotion of one immutable release across development, test, and production Jira sites.
- Approval policies based on risk, environment, or component type.
- Marketplace-app extension points for configuration unavailable through public Jira APIs.
- Notifications to email, Microsoft Teams, or Slack.
- Rollback plans based on captured before-state for safely reversible updates.