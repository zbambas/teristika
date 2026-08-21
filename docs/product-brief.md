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

Authorized configuration owners can create a blueprint, clone a published version into a draft, edit through structured forms or raw YAML/JSON, validate the draft, and publish a new immutable version. Editing never changes an existing published version.

An uploaded YAML or JSON file is validated before import. Findings distinguish syntax, schema, typed-property, identifier, parameter, reference, dependency, and cycle issues and include severity, code, document path, line and column when available, message, and remediation. Errors block import and publication.

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

Within a job, an authorized user can inspect Jira API attempts in chronological order. Each call shows its owning step, method, endpoint, attempt, duration, transport or HTTP status, and bounded sanitized request and response details.

### FR-10: Audit and Evidence

The application records the actor, target, blueprint and version, selected components, generated plan, approvals, timestamps, step outcomes, redacted API diagnostics, and final validation report. A user can export a run summary as JSON and human-readable HTML or PDF.

### FR-11: Issue Dependency Exploration

A user can inspect issue relationships within one Jira project using a shared, permission-scoped dataset. The application provides:

- a Gantt representation for dates, estimates, dependency order, and critical path;
- a radial or star representation centered on one issue and its immediate neighborhood;
- a directional network representation for end-to-end dependency flow;
- a dependency matrix for dense row and column comparison;
- shared project, issue type, status, and relationship filters;
- issue and relationship detail that remains consistent across representations.

The explorer is read-only. It reports cycles, missing dates, hidden issues, partial visibility, and result limits instead of inventing data.

### FR-12: Secure Jira Credential Settings

An administrator can add, test, rotate, and disable Jira API-token or OAuth credentials from Settings. The application:

- sends a newly entered value over TLS directly to an external secret store;
- stores only secret reference, provider version, safe fingerprint, status, actor, and timestamps in PostgreSQL;
- never returns an active secret value to the browser;
- tests an expiring staged candidate against capability-approved Jira identity, site, scope, permission, and representative read endpoints;
- classifies invalid credential, insufficient scope, insufficient permission, wrong site, rate limit, timeout, and Jira-unavailable results;
- requires explicit confirmation before activating a successfully tested candidate;
- keeps the active credential unchanged when candidate testing or activation fails;
- audits credential lifecycle actions without recording the secret.

### FR-13: Offline Jira Repository

An authorized user can synchronize Jira data and browse or search it when Jira is unavailable or Offline mode is explicitly selected. "Offline" means disconnected from Jira while the Django application and its repository remain available.

The repository synchronizes all data exposed by supported public Jira APIs and visible to the configured identity for selected sites and projects. This includes project configuration, issues, fields, links, comments, worklogs, changelog, users or account references, boards, sprints, attachment metadata, and attachment content when policy permits it. A versioned manifest reports entity counts, snapshot boundary, completeness, failures, inaccessible data, unsupported APIs, and attachment policy.

Access modes are:

- Online: live Jira reads are allowed;
- Automatic: live Jira is preferred and a complete snapshot is used only through a visible freshness policy;
- Offline: Jira requests are blocked and browse/search uses only a selected complete snapshot.

Offline access is read-only. It never queues, replays, or implies a Jira mutation. Results always show source, snapshot time, scope, completeness, and freshness.

### FR-14: User and Access Management

The application authenticates production users through a trusted OIDC provider and governs application authorization. It does not create local production passwords, manage MFA, create an Atlassian account, or edit Jira users.

Administrators can:

- synchronize trusted issuer, subject, display metadata, provider state, and group claims;
- map OIDC groups to viewer, operator, approver, or administrator roles;
- scope viewer, operator, and approver assignments to Jira connections or projects;
- create time-bounded direct exceptions with owner, reason, start, and expiry;
- inspect each user's effective access, assignment source, group memberships, last sign-in, sessions, and security activity;
- suspend application access and revoke active application sessions without modifying the OIDC or Atlassian account;
- run periodic access reviews and certify, modify, or revoke privileged and direct assignments.

Authorization is deny by default. Issuer plus provider subject identifies a user; email is display metadata and may change. The application prevents removal of the final active global administrator path.

### FR-15: Capture Blueprint from Jira Project

An authorized configuration owner can select a tested Jira connection and reference project, discover its supported configuration through read-only APIs, and generate a new blueprint draft.

Before draft creation, the application classifies project-owned, shared, reference-only, unsupported, inaccessible, ambiguous, and policy-omitted resources. The user explicitly selects resources and shared-resource behavior. The transformation generates deterministic portable logical IDs, inferred dependencies, and parameters for environment-specific values. Jira IDs remain provenance or mapping metadata rather than portable logical IDs.

The draft records source connection, Jira project ID and key, discovery snapshot, capture time, actor, selected and omitted source items, and transformation warnings. It opens in the Blueprint Editor and must pass normal validation before publication. Capture never mutates Jira or publishes automatically.

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

### Author or Upload a Blueprint

1. Create a draft, clone an existing version, or upload YAML or JSON.
2. Edit structured sections or raw source while preserving stable logical IDs.
3. Run syntax, schema, resource, parameter, reference, and dependency validation.
4. Select a finding to open its affected field or source location.
5. Resolve errors and acknowledge policy-controlled warnings.
6. Confirm publication of a new immutable version.

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

### Explore Project Issue Dependencies

1. Open a project and select Issue dependencies.
2. Filter the project issues and relationship types.
3. Switch among Gantt, radial, network, and matrix representations.
4. Select an issue or relationship and inspect its consistent detail.
5. Export or share the current read-only view when permitted.

### Rotate a Jira API Token

1. Open Settings and select the Jira connection.
2. Review active secret-store metadata without seeing the token value.
3. Enter a replacement token as an expiring candidate.
4. Test the candidate identity, site, scopes, permissions, and representative reads.
5. Resolve any classified failure while the current credential remains active.
6. Explicitly confirm activation of the tested candidate.
7. Review the redacted audit event and new secret-store version.

### Synchronize and Browse Offline Data

1. Configure selected connections, projects, retention, attachment policy, schedule, and storage quota.
2. Run a full synchronization and inspect its completeness manifest.
3. Run incremental synchronization to apply additions, updates, and tombstones.
4. Select Offline mode and verify that Jira calls are blocked.
5. Browse or search the complete snapshot and inspect source and freshness on every result.
6. Switch Online or Automatic only through an explicit mode change.

### Govern Application Access

1. Synchronize users and groups from the trusted OIDC provider.
2. Map provider groups to application roles and connection or project scopes.
3. Review a user's effective assignments and their group or direct source.
4. Preview and save a time-bounded direct exception when justified.
5. Revoke sessions or suspend application access when required.
6. Complete periodic access review decisions with attributable evidence.

### Capture a Blueprint from Jira

1. Select a tested Jira connection and reference project.
2. Run read-only discovery and inspect its snapshot and API coverage.
3. Review project-owned, shared, unsupported, inaccessible, ambiguous, and omitted resources.
4. Select resources, shared behavior, and parameterization rules.
5. Generate a provenance-linked mutable draft.
6. Validate and edit the draft before explicitly publishing an immutable version.

## 7. MVP Acceptance Criteria

The MVP is complete when all of the following are demonstrated against a Jira Cloud sandbox:

- A user can connect one site without exposing credentials in logs or the database.
- A valid blueprint can create one company-managed Jira project.
- A configuration owner can create or clone a draft, validate it, and publish a new immutable version without changing its source version.
- An invalid uploaded blueprint reports location-aware issues and cannot be imported or published.
- The project deployment supports at minimum project metadata, issue types, statuses and workflows, custom fields, screens, components, versions, and scheme association where the Jira API permits it.
- The planner reports unsupported configuration instead of silently skipping it.
- A user can select a subset and see all added dependencies before approval.
- Re-running the same plan is idempotent and does not create duplicates.
- A test-data pack can create at least 50 linked issues and clean up only those issues.
- A validation report identifies a deliberately introduced field, workflow, or component mismatch.
- A JQL-selected issue batch can be previewed, capped, executed, retried, and audited.
- A scheduled validation runs without an active browser session.
- A job displays every Jira API attempt with its status and sanitized response while preserving retry order.
- One project dependency dataset renders consistently as Gantt, radial, network, and matrix views.
- An invalid staged Jira token cannot replace the active credential; a valid token requires successful testing and explicit activation.
- Credential values do not appear in the application database, browser storage, logs, jobs, fixtures, diagnostics, audit, or exports.
- A complete offline snapshot contains every supported and authorized enabled entity or reports its omission in the manifest.
- Offline-mode browsing and search succeed while all Jira network requests are denied and clearly identify repository source and snapshot freshness.
- OIDC group removal, assignment expiry, suspension, and session revocation stop authorizing within their configured bounds and reveal no unauthorized scope.
- The final active administrator path cannot be removed, expired, or self-suspended.
- A reference Jira project can generate a deterministic draft with explicit shared, unsupported, inaccessible, and omitted configuration and no Jira mutation.
- Concurrent writes to the same Jira project are serialized.
- An interrupted worker resumes or safely retries without losing job state.

## 8. Non-Functional Requirements

- Security: least-privilege Jira access, encrypted transport, external secret storage, role-based application access, redacted logs, and no secret values in exports.
- Reliability: idempotency keys, bounded retries with backoff, durable job state, and per-target locking.
- Offline data: encryption at rest, explicit completeness and freshness, permission-scoped search, incremental synchronization, tombstones, quotas, retention, purge, and verified recovery.
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
- Queueing Jira changes while Offline mode is active.

## 10. Later Candidates

- Jira Data Center adapter.
- Git pull-request workflow for blueprint authoring and approval.
- Promotion of one immutable release across development, test, and production Jira sites.
- Approval policies based on risk, environment, or component type.
- Marketplace-app extension points for configuration unavailable through public Jira APIs.
- Notifications to email, Microsoft Teams, or Slack.
- Rollback plans based on captured before-state for safely reversible updates.