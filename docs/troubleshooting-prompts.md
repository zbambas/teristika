# Troubleshooting Prompts

Use these prompts for failures in the Jira Project Deployer. Replace values inside `{...}`. For any investigation that may change files or issue status, select the **Solution Manager** agent so the mandatory Senior Developer and Senior QA workflow remains intact.

See [`common-prompts.md`](common-prompts.md) for normal delivery, planning, specialist review, and reporting prompts.

## Troubleshooting Contract

Apply this contract to every prompt below unless the prompt explicitly narrows it:

1. Read the active issue, [`backlog/README.md`](../backlog/README.md), and the relevant sections of [`solution-architecture.md`](solution-architecture.md).
2. Preserve unrelated user changes and investigate one failure at a time.
3. Reproduce the failure with the narrowest deterministic command or request before editing.
4. Separate observed facts from hypotheses. Capture the exact command, status, correlation ID, and sanitized error.
5. Classify the failing layer: environment, Django, HTMX, DRF, PostgreSQL, Celery, Redis, Jira, blueprint, planning, execution, or test.
6. Do not expose credentials, authorization headers, personal data, issue content, or production payloads.
7. Use non-production data. Do not mutate production Jira or run destructive database or Redis commands.
8. Identify the root cause and smallest task-scoped repair. Do not mask the failure with retries, sleeps, broad exception handling, disabled checks, or changed expected results.
9. After a repair, rerun the original reproducer, focused regression tests, and applicable quality checks.
10. Report root cause, evidence, changed files, verification, residual risk, and whether a new backlog issue is required.

## Routing Guide

- **Senior QA**: always prepares or verifies reproduction and regression evidence.
- **Senior Developer**: implements a repair only after the failure is reproduced and scoped.
- **Senior UX Specialist**: HTMX behavior, forms, navigation, accessibility, interaction states, responsive layout, and user-facing errors.
- **Senior Security Specialist**: authentication, authorization, CSRF, secrets, uploads, Jira calls, audit, redaction, and sensitive data.
- **Senior Data Modeler and Database Specialist**: Django models, migrations, PostgreSQL constraints, indexes, transactions, locks, retention, and recovery.

## General Triage

### Diagnose an Unknown Failure

```text
Work as Solution Manager on {ISSUE_ID_OR_INCIDENT}. Apply docs/troubleshooting-prompts.md. Reproduce this failure exactly: {ERROR_OR_BEHAVIOR}. Identify the first failing boundary and classify it as environment, Django, HTMX, DRF, PostgreSQL, Celery, Redis, Jira, blueprint, planning, execution, or test. Invoke Senior QA for independent reproduction and the relevant optional specialists. Do not edit until one falsifiable root-cause hypothesis and one discriminating check are identified. If a repair is in scope, route it through Senior Developer and verify the original reproducer.
```

### Diagnose an Intermittent Failure

```text
Investigate intermittent failure {ERROR_OR_BEHAVIOR} for {ISSUE_ID}. Do not add sleeps or unbounded retries. Record timestamps, correlation IDs, job and step IDs, worker identity, target lock owner, request attempt, and state transitions for repeated controlled runs. Compare one passing and one failing run, identify the first divergent fact, and test one race, timeout, ordering, or stale-state hypothesis at a time. Preserve a deterministic regression test before repair.
```

### Determine Whether the Environment Is Broken

```text
Before changing project code for {ERROR}, verify the selected Python interpreter, uv lock state, environment variables by name only, service reachability, Django settings module, database migration state, Redis connectivity, worker heartbeat, and current Git diff. Compare the failing environment with the documented local setup. Report ENVIRONMENT BLOCKER or APPLICATION DEFECT with evidence; do not modify application behavior to compensate for a local configuration error.
```

### Turn an Unscoped Defect into a Task

```text
Reproduce {DEFECT} without editing. If it is not already covered by {ISSUE_ID}, create one minimal task using backlog/ISSUE_TEMPLATE.md. Include the observed behavior, owning layer, dependency, deterministic reproducer, expected behavior from existing documents, success criteria, regression evidence, and required specialists. Do not combine unrelated symptoms or implement the new task.
```

## Python and Tooling

### Diagnose uv or Dependency Resolution

```text
Diagnose {UV_OR_DEPENDENCY_ERROR}. Inspect pyproject.toml, the lock file, Python 3.13 availability, package indexes, environment markers, and the exact uv command. Reproduce from a clean isolated environment without deleting the existing environment first. Identify whether the cause is an incompatible constraint, stale lock, unavailable wheel, interpreter mismatch, or network/index failure. Change dependency constraints only with evidence and validate a clean sync plus Django checks.
```

### Diagnose Ruff or mypy Failures

```text
Diagnose the Ruff or mypy failure from {COMMAND}. Run the narrow check on the reported file, inspect project configuration and Django plugin settings, and determine whether the defect is code, missing annotation, generated migration noise, or configuration. Fix the typed or linted behavior rather than suppressing the rule unless the architecture documents a justified exception. Re-run the narrow check and the full static-quality command.
```

### Diagnose a Failing pytest Test

```text
Investigate test {TEST_NODE_ID}. Run it alone with full failure output, then determine whether it fails from application logic, fixture isolation, ordering, time, database state, broker state, network leakage, or an incorrect expectation. Prove order dependence by running it alone and with the relevant group. Do not weaken assertions or add retries. Repair the root cause and rerun the test, its module, and the relevant integration suite.
```

### Diagnose Docker Compose Startup

```text
Diagnose the local Docker Compose failure for service {SERVICE}. Inspect rendered Compose configuration, image build output, container exit status, health checks, port conflicts, volume permissions, and dependency readiness. Do not delete volumes because a service is unhealthy. Identify the first failed service and validate the repair with a clean service restart, Django readiness, PostgreSQL connection, Redis ping, and Celery heartbeat.
```

## Django Web and API

### Diagnose Django Startup or Settings

```text
Diagnose Django startup failure {ERROR}. Run the documented Django check with the same settings module and environment. Inspect the first project frame, installed apps, middleware order, URL imports, ASGI configuration, and required environment-variable names. Do not print secret values. Fix the smallest configuration or import defect and verify Django checks, migrations check, liveness, and one representative page test.
```

### Diagnose a Django 500 Response

```text
Diagnose the 500 response for {METHOD} {PATH}. Reproduce with a Django test client or focused request using non-sensitive fixtures. Trace the request through URL, middleware, permission, form or serializer, application service, ORM, and template boundaries using the correlation ID. Find the first invalid assumption; do not return a generic success or swallow the exception. Add a regression test for the failing input and verify the intended error contract.
```

### Diagnose Unexpected 404 or URL Resolution

```text
Diagnose unexpected 404 for {PATH}. Use Django URL resolution to distinguish missing route, namespace mismatch, converter mismatch, trailing-slash behavior, hidden object, and permission-based not-found behavior. Check named URL reversal in templates and redirects. Repair only the owning URL or lookup logic and verify resolve, reverse, authorized request, and unauthorized request cases.
```

### Diagnose Authentication, 403, or CSRF

```text
For {METHOD} {PATH}, diagnose the unexpected authentication, 403, or CSRF result. Invoke Senior Security Specialist and Senior QA. Distinguish anonymous authentication, missing role permission, object-level target authorization, CSRF token or origin failure, and deliberate resource hiding. Verify no state change occurred on denial. Fix the narrow policy or request flow and test anonymous plus viewer, operator, approver, and administrator roles.
```

### Diagnose Django Form Validation

```text
Diagnose form failure {BEHAVIOR} on {PATH}. Reproduce GET, valid POST, invalid POST, duplicate submit, and permission-denied cases. Inspect bound data, field and non-field errors, model constraints, transaction boundary, redirect, and rendered error association. Ask Senior UX Specialist to verify wording, focus, and error placement. Ensure invalid input creates no partial state.
```

### Diagnose a DRF Response Mismatch

```text
Diagnose DRF endpoint {METHOD} {API_PATH}, expected {EXPECTED_STATUS_OR_BODY}, observed {OBSERVED_STATUS_OR_BODY}. Trace URL routing, authentication, permission, serializer validation, application service, transaction, and problem-details mapping. Verify idempotency behavior for mutations and redact sensitive fields. Add API tests for valid, invalid, unauthorized, duplicate, and conflict requests as applicable.
```

### Diagnose HTMX Behavior

```text
Diagnose HTMX behavior {BEHAVIOR} on {PATH}. Reproduce the initial full-page request and the HX request separately. Inspect request headers, target, swap mode, returned fragment, response status and HX headers, browser console, focus, loading, empty, success, and error states. Invoke Senior UX Specialist. Fix server-rendered behavior first and verify the core workflow remains usable without HTMX enhancement.
```

## PostgreSQL and Django ORM

### Diagnose Database Connectivity

```text
Diagnose PostgreSQL connection failure {ERROR}. Invoke Senior Data Modeler and Database Specialist. Verify host, port, database name, user identity, TLS mode, DNS, container health, connection limits, and Django database settings without printing passwords. Distinguish network, authentication, database absence, permission, pool exhaustion, and server recovery. Validate with Django's configured connection and a read-only query.
```

### Diagnose Migration Failure or Drift

```text
Diagnose Django migration problem {ERROR}. Invoke Senior Data Modeler and Database Specialist and Senior QA. Inspect showmigrations, migration graph, model state, generated SQL, applied rows, and PostgreSQL compatibility. Reproduce on a fresh database and a copy of representative non-production prior-schema data. Do not fake or delete migration history. Repair ordering or migration operations and verify forward migration, reverse behavior where supported, and no pending model changes.
```

### Diagnose Constraint or IntegrityError

```text
Diagnose IntegrityError {ERROR} for {OPERATION}. Identify the exact PostgreSQL constraint, transaction boundary, concurrent actors, and expected domain invariant. Determine whether validation is missing, the constraint is wrong, the operation is not idempotent, or existing data violates a new invariant. Preserve the database constraint when it protects valid behavior. Test valid, duplicate, conflicting, and concurrent writes.
```

### Diagnose Slow ORM Query

```text
Diagnose slow operation {OPERATION} using representative non-production volume. Invoke Senior Data Modeler and Database Specialist. Capture query count and PostgreSQL EXPLAIN ANALYZE without sensitive literals. Identify N+1 access, missing index, poor selectivity, unnecessary locking, large serialization, or unbounded pagination. Optimize the measured bottleneck only, then compare query plan, query count, latency, and result equivalence.
```

### Diagnose Lock Wait or Deadlock

```text
Diagnose lock wait or deadlock {ERROR}. Invoke Senior Data Modeler and Database Specialist. Reproduce with controlled concurrent transactions, record lock order and transaction boundaries, and identify the conflicting rows or advisory keys. Do not fix by globally raising timeouts. Establish deterministic lock order or narrower transactions, then test concurrent success, timeout handling, rollback, and absence of partial state.
```

### Diagnose Backup or Restore Failure

```text
Diagnose non-production PostgreSQL backup or restore failure {ERROR}. Verify tool and server versions, roles, extensions, ownership, migration level, encoding, and restore ordering. Never use or overwrite production. After repair, run Django checks, migration checks, row-count and constraint checks, and pending-job reconciliation. Record recovery time and any data excluded by policy.
```

## Celery and Redis

### Diagnose a Task Not Running

```text
Diagnose Celery task {TASK_NAME_OR_ID} that remains queued. Check transaction-on-commit publication, broker URL by location only, queue and routing key, worker subscription, task registration, serializer, heartbeat, and revoked or expired state. Distinguish unpublished, broker-held, unregistered, reserved, active, and failed. Do not republish blindly. Verify one dispatch creates one durable job and one execution attempt.
```

### Diagnose Duplicate Task Execution

```text
Diagnose duplicate execution for job {JOB_ID}. Trace API idempotency key, database uniqueness, transaction commit, broker delivery, Celery acknowledgment, retry, worker loss, and step checkpoint. Assume at-least-once delivery and identify which idempotency guard failed. Repair the guard, not broker semantics, then test duplicate submit, redelivery, lost response, and worker restart.
```

### Diagnose Retry Loop or Poison Task

```text
Diagnose repeated retries for task {TASK_ID}. Classify the exception using the Jira and application retry policy, inspect attempt count, backoff, Retry-After, maximum retries, and persisted step state. Ensure permanent authentication, permission, validation, and conflict errors do not retry. Verify transient recovery and terminal failure with bounded deterministic tests.
```

### Diagnose Celery Beat Scheduling

```text
Diagnose schedule {SCHEDULE_ID} that ran late, twice, or not at all. Check enabled state, time zone conversion, database scheduler row, last-run metadata, scheduler singleton, clock assumptions, due calculation, and overlap policy. Do not run multiple schedulers to fix missed work. Verify one expected UTC trigger and queue, skip, or reject behavior for overlap.
```

### Diagnose Redis Outage or Stale Lock

```text
Diagnose Redis or target-lock failure {ERROR}. Determine whether broker delivery, rate-limit coordination, cache, or lease handling failed. Inspect lock key scope, owner token, expiry, renewal, and PostgreSQL job truth without deleting all Redis keys. Prove that Redis loss does not lose plans or jobs. Verify stale-lock recovery cannot release another worker's lease or replay completed steps.
```

## Jira Integration

### Diagnose Jira 401 or 403

```text
Diagnose Jira {401|403} for {METHOD} {ENDPOINT}. Invoke Senior Security Specialist. Compare the connection identity, approved auth method, token status, OAuth scopes, Jira product permissions, project permissions, and capability matrix. Do not print or rotate credentials through chat. Distinguish authentication from authorization, sanitize evidence, and update capability claims only after a verified sandbox result.
```

### Diagnose Jira 404 or Wrong Resource

```text
Diagnose Jira 404 or wrong-resource response for {METHOD} {ENDPOINT}. Verify site base URL, cloud ID, API version, project key, Jira object ID, resource mapping scope, URL encoding, and endpoint availability in the capability matrix. Distinguish absent resource, hidden resource, stale mapping, and unsupported endpoint. Do not create a replacement until identity is unambiguous.
```

### Diagnose Jira 409 or Mapping Conflict

```text
Diagnose Jira conflict {ERROR} for logical resource {RESOURCE_ID}. Inspect the approved plan, desired identity, observed candidates, resource mappings, global versus project scope, and concurrent jobs. Do not adopt by display name when multiple candidates exist. Produce either one verified mapping, an unchanged result, or a blocking conflict with remediation.
```

### Diagnose Jira 429, Timeout, or 5xx

```text
Diagnose Jira transient failure {STATUS_OR_TIMEOUT}. Inspect correlation ID, attempt, elapsed time, Retry-After, rate limiter state, timeout phase, request idempotency, and Jira status evidence. Do not use unbounded retries or immediate loops. Verify bounded backoff, cancellation responsiveness, permanent exhaustion behavior, and safe replay for the specific operation.
```

### Diagnose Jira Payload or Response Changes

```text
Diagnose Jira contract mismatch {ERROR} for {ENDPOINT}. Compare the sanitized actual response with the capability-approved fixture and documented API version. Identify missing, renamed, nullable, paginated, or newly defaulted fields. Do not loosen validation globally. Update normalization and the smallest sanitized fixture, then test old and new supported shapes and explicit failure for unsupported shapes.
```

### Diagnose Incomplete Jira Pagination

```text
Diagnose missing or duplicated Jira resources from {ENDPOINT}. Trace start offset or cursor, page size, total or last-page signal, ordering, deduplication key, and rate-limit retries. Test zero, one, exact-page, multi-page, duplicate-page, and changed-total cases. Verify normalized output is complete and stable regardless of page boundaries.
```

## Blueprint and Planning

### Diagnose Blueprint Parse or Schema Failure

```text
Diagnose blueprint failure {ERROR} using docs/blueprint-contract.md, the JSON Schema, and the example blueprint. Distinguish YAML or JSON syntax, envelope schema, unknown key, typed resource property, duplicate logical ID, and unsupported apiVersion. Preserve strict unknown-property rejection. Return the exact document path and smallest valid correction, then validate schema and typed resources.
```

### Diagnose Parameter Resolution

```text
Diagnose parameter error {ERROR}. Inspect declared type, required or default value, restricted placeholder syntax, project-key pattern, and unresolved references. Do not introduce a general template engine or evaluate expressions. Verify valid substitution, missing required value, invalid type or pattern, unknown parameter, and absence of secrets from hashes and diagnostics.
```

### Diagnose Dependency Cycle or Missing Reference

```text
Diagnose planning graph failure for {RESOURCE_ID_OR_BLUEPRINT}. List explicit and handler-inferred edges, reproduce the exact cycle or dangling reference, and show the dependency path. Do not remove a valid dependency to make sorting pass. Correct the owning resource or handler rule and verify transitive expansion, cycle detection, missing-reference failure, and stable topological order.
```

### Diagnose Perpetual Configuration Drift

```text
Diagnose resource {RESOURCE_ID} that always plans as update. Compare canonical desired state, raw Jira response, normalized observed state, prior mapping, and previous apply payload. Identify volatile IDs, ordering, defaults, null-versus-absent values, unsupported properties, or failed read-back. Fix normalization only for semantically irrelevant differences and verify create, immediate reread, and second plan become unchanged.
```

### Diagnose Stale or Rejected Plan

```text
Diagnose plan {PLAN_ID} rejected as stale, changed, blocked, or unapproved. Compare blueprint checksum, parameter hash, connection identity, target fingerprint, capabilities, approval actor and expiry, and current blockers. Do not bypass the guard or edit an approved plan. Explain the changed precondition and generate a new plan only when required.
```

## Jobs, Deployment, and Validation

### Diagnose a Stuck Job or Step

```text
Diagnose job {JOB_ID} stuck in {STATE}. Inspect durable job and step state, worker heartbeat, task delivery state, target lease, cancellation flag, last correlation ID, attempt count, and Jira response. PostgreSQL is authoritative; do not manually mark completion. Determine whether to resume, safely retry, cancel, or fail the step, and prove completed steps are not replayed.
```

### Diagnose Partial Deployment Failure

```text
Diagnose partial deployment job {JOB_ID}. List completed, verified, failed, blocked-dependent, and not-started operations in dependency order. Identify whether the failure is transient, capability, conflict, stale state, or implementation. Do not promise general rollback or undo verified shared configuration. Produce the smallest corrected forward plan and preserve complete audit evidence.
```

### Diagnose Cancellation Failure

```text
Diagnose cancellation for job {JOB_ID}. Trace request authorization, cancellation timestamp, worker observation point, current external call, step checkpoint, and final state. Verify cancellation stops before the next mutation but does not falsify a completed operation. Add a deterministic test around the exact missed cancellation boundary.
```

### Diagnose Validation Result Mismatch

```text
Diagnose validation rule {RULE_ID}, expected {EXPECTED_STATUS}, observed {OBSERVED_STATUS}. Compare prerequisites, normalized expected and observed values, capability status, rule severity, and aggregation. Unsupported must not pass, and failed prerequisites must produce skipped dependents. Repair the rule or evidence mapping and verify individual plus suite summary results.
```

### Diagnose Unsafe Test-Data Cleanup

```text
Diagnose test-data cleanup for run {RUN_ID}. Invoke Senior Security Specialist and Senior Data Modeler and Database Specialist. Compare connection, project, pack, run, durable issue mapping, Jira entity property, and application label for every candidate. Never delete on a partial match. Verify mismatches are excluded, manually created control issues survive, and repeated cleanup is a no-op.
```

### Diagnose Batch Count or Outcome Mismatch

```text
Diagnose batch {JOB_ID}, planned {PLANNED_COUNT}, observed {OBSERVED_COUNT_OR_RESULT}. Compare frozen JQL, target fingerprint, pagination, maximum count, per-issue checkpoint, rate limit, retries, cancellation, and failure threshold. Do not rerun the whole batch blindly. Identify exactly which issue IDs are complete, failed, or unattempted and verify safe resumption.
```

## Security and Audit

### Diagnose a Suspected Secret Exposure

```text
Treat suspected exposure {LOCATION_OR_ERROR} as a security incident. Invoke Senior Security Specialist. Stop further reproduction with real credentials, identify affected secret references and surfaces, preserve sanitized evidence, and follow the approved rotation owner process outside chat. Search source, logs, errors, task payloads, diagnostics, fixtures, and exports using seeded values. Repair redaction and add regression tests without committing the exposed value.
```

### Diagnose Missing or Incorrect Audit Evidence

```text
Diagnose audit gap for {ACTION_OR_JOB_ID}. Trace actor, authorization, target, blueprint checksum, plan, approval, job, step, Jira mutation, timestamp, outcome, and correlation ID. Verify audit creation occurs at the correct transaction boundary and rows are immutable through application and admin paths. Do not reconstruct uncertain facts as if they were observed; mark unavailable evidence explicitly.
```

### Diagnose Cross-Project or Cross-Connection Access

```text
Diagnose suspected isolation failure for {USER_OR_REQUEST}. Invoke Senior Security Specialist and Senior QA. Reproduce with two connections, two projects, and the minimum roles. Trace queryset scoping, object lookup, permission policy, serializer or form input, and task payload authorization. Verify denial returns the intended status, reveals no hidden metadata, creates no mutation, and emits an audit event.
```

## UI and Accessibility

### Diagnose Layout or Responsive Failure

```text
Diagnose UI failure {BEHAVIOR} on {PATH} at {VIEWPORT}. Invoke Senior UX Specialist. Capture the rendered page and inspect container constraints, grid or flex tracks, text wrapping, controls, dynamic content, and HTMX states. Check desktop and mobile without viewport-based font scaling. Repair the owning template or style and verify no overlap, clipping, unexpected layout shift, or inaccessible control.
```

### Diagnose Keyboard or Screen-Reader Failure

```text
Diagnose accessibility failure {BEHAVIOR} on {PATH}. Invoke Senior UX Specialist and Senior QA. Reproduce using keyboard order and semantic inspection. Check labels, names, roles, states, focus movement, focus visibility, validation association, live updates, dialog behavior, and contrast. Preserve native semantics where possible and verify the full affected workflow, not only the isolated control.
```

## Observability and CI

### Trace a Failure Across Components

```text
Trace correlation ID {CORRELATION_ID} across Django request, plan, job, Celery task, step, PostgreSQL state, Redis delivery, and Jira request. Build a timestamped sequence from structured sanitized evidence, identify the first missing or contradictory event, and classify whether behavior failed or observability failed. Repair the owning boundary and verify one correlation ID survives the complete flow.
```

### Diagnose CI-Only Failure

```text
Diagnose CI failure {JOB_OR_COMMAND} that passes locally. Compare Python and dependency lock versions, operating system, environment-variable names, time zone, locale, database and Redis versions, service readiness, test order, concurrency, generated files, and cache use. Reproduce in the closest clean local or container environment. Do not weaken the test for CI; fix the deterministic environment or application assumption and verify both contexts.
```

### Diagnose Readiness or Health Failure

```text
Diagnose health endpoint {PATH} returning {STATUS}. Distinguish liveness from readiness and inspect PostgreSQL, Redis, migration, worker, and scheduler checks. One unavailable Jira connection must not make the application globally unready. Verify each dependency failure independently, bounded timeout behavior, sanitized output, and recovery after the dependency returns.
```

## Closure and Handoff

### Verify a Troubleshooting Repair

```text
Work as Solution Manager and verify the repair for {ISSUE_ID}. Have Senior QA run the original reproducer first, then focused regression, failure-path, and relevant quality checks. Ask every consulted specialist to verify its material findings. Confirm no unrelated behavior changed and evidence maps to each success criterion. Mark Done only after the original failure is no longer reproducible for the intended reason.
```

### Record an Unresolved Blocker

```text
Record blocker {BLOCKER} for {ISSUE_ID}. Include the exact sanitized reproducer, first failing boundary, evidence collected, hypotheses rejected, access or external dependency needed, owner, and the condition that permits work to resume. Keep the issue out of Done, do not invent a workaround, and identify any independent task that remains eligible.
```

### Prepare a Troubleshooting Handoff

```text
Prepare a handoff for failure {ERROR_OR_BEHAVIOR} on {ISSUE_ID}. State environment, exact reproducer, observed output, correlation and job IDs, affected layer, leading hypothesis, checks already run, files changed, preserved unrelated changes, specialist findings, blocker, and next discriminating action. Redact sensitive data and link to repository evidence instead of copying large logs.
```

## Troubleshooting Rules

- Reproduce before repair and rerun the same reproducer afterward.
- Prefer one discriminating check over broad logging or speculative changes.
- Treat PostgreSQL as authoritative for plans, jobs, steps, schedules, and audit state.
- Treat Celery delivery as at least once; solve duplicates with idempotency and checkpoints.
- Never clear Redis, delete database rows, fake migrations, or reset Jira configuration as a diagnostic shortcut.
- Never bypass plan approval, staleness, target locking, batch limits, or test-data cleanup markers.
- Never log raw Jira payloads, credentials, authorization headers, or sensitive issue fields.
- Do not convert unsupported Jira operations into successful or skipped results.
- Keep fixes within the active issue; create a new dependent task for a separate root cause.
- Report commands actually run and checks that could not run.