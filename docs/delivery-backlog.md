# Jira Project Deployer - Delivery Backlog

Status: Proposed v0.1
Prioritization: `P0` is required for MVP, `P1` follows MVP, and `P2` is exploratory.
Estimates: relative size only (`S`, `M`, `L`, `XL`) until the delivery team establishes throughput.

## Delivery Strategy

Deliver thin vertical slices through the blueprint parser, planner, Jira adapter, worker, persistence, API, and web UI. Do not implement every Jira resource handler before proving one complete deployment path.

The first milestone is a time-boxed Jira Cloud capability proof. Public Jira APIs, permissions, and plan availability vary by resource. Its evidence controls the exact MVP resource matrix and avoids building workflows around unavailable mutation APIs.

The executable stories and tasks are maintained in [`backlog/`](../backlog/README.md). Those issue files are canonical for dependencies, status, success criteria, and Developer/QA evidence; this document remains the product-level roadmap.

## Milestone 0: Jira Capability Proof

Goal: prove supported operations against a dedicated Jira Cloud sandbox using only documented APIs.

| ID | Priority | Size | Backlog item | Acceptance outcome |
| --- | --- | --- | --- | --- |
| CAP-01 | P0 | S | Obtain sandbox and automation identity | Site URL, Jira plan, admin access, data policy, and cleanup owner are recorded |
| CAP-02 | P0 | M | Prove authentication choices | Approved auth method works without browser credentials reaching the worker logs or database |
| CAP-03 | P0 | L | Probe project and configuration APIs | Read/create/update/associate support is recorded for each proposed MVP resource type, including required scopes and permissions |
| CAP-04 | P0 | M | Probe rate limiting and errors | `401`, `403`, `404`, conflict, `429`, and transient `5xx` responses have sanitized fixtures and classifications |
| CAP-05 | P0 | M | Decide unsupported-resource behavior | Each gap is assigned to MVP exclusion, reference-only association, manual evidence step, or documented extension path |
| CAP-06 | P0 | S | Publish capability matrix | Product brief acceptance criteria are adjusted to the proven Jira plan and API surface |

Exit criterion: the team can create a sandbox project and identify, without undocumented APIs, which issue types, workflows, fields, screens, and schemes can be created or only associated.

## Milestone 1: Read-Only Planning Slice

Goal: connect a site, ingest a blueprint, and produce an explainable plan without mutating Jira.

| ID | Priority | Size | Backlog item | Acceptance outcome |
| --- | --- | --- | --- | --- |
| FND-01 | P0 | M | Scaffold Django modular monolith | Local environment starts Django web, Celery worker, Celery Beat, PostgreSQL, and Redis with one documented command |
| FND-02 | P0 | M | Add OIDC-ready user and role model | Local development login works; route policies distinguish viewer, operator, approver, and administrator |
| P01-T08 | P0 | M | Synchronize OIDC identities | Trusted issuer/subject and group claims update identities without local production passwords |
| P01-T09 | P0 | L | Manage scoped roles and groups | Group mappings and direct exceptions produce previewable global, connection, and project access |
| P01-T10 | P0 | L | Review and revoke user access | Administrators inspect effective access, revoke sessions, suspend access, and certify assignments |
| CON-01 | P0 | M | Manage Jira connection metadata | Administrator can add a site and secret reference, test it, and see a redacted result |
| CON-02 | P0 | L | Discover Jira capabilities | UI distinguishes supported, permission-denied, API-unavailable, and adapter-not-implemented capabilities |
| P02-T10 | P0 | M | Build Jira credential settings | Administrator stages secret values directly in the external secret store and sees metadata only |
| P02-T11 | P0 | M | Test and rotate Jira credentials | Candidate access is classified and only an explicitly confirmed tested version can activate |
| P02-T12 | P0 | L | Discover reference Jira project | Selected project configuration is read and classified without Jira mutation |
| P02-T13 | P0 | L | Generate blueprint draft from Jira | Selected normalized resources become portable logical IDs, dependencies, parameters, and provenance |
| BLP-01 | P0 | M | Parse and schema-validate blueprints | Example blueprint loads; invalid keys and unresolved parameters produce location-aware errors |
| BLP-02 | P0 | M | Add typed resource validation | Unknown resource properties, duplicate logical IDs, and dangling references are rejected |
| PLN-01 | P0 | L | Build dependency graph and selection expansion | Selecting a workflow includes required statuses and explains each dependency path |
| PLN-02 | P0 | L | Discover and normalize target state | Fake adapter and sandbox adapter produce the same domain representation from fixtures |
| PLN-03 | P0 | L | Generate immutable dry-run plan | Plan classifies create, update, unchanged, conflict, unsupported, and blocked operations |
| UI-01 | P0 | L | Build configuration selection and plan review | User can select resources, inspect added dependencies, filter outcomes, and see blockers |
| P02-T08 | P0 | L | Build blueprint editor | Configuration owners create or clone drafts, edit structured or raw content, and publish new immutable versions |
| P02-T09 | P0 | M | Build blueprint validation review | Uploaded YAML/JSON shows location-aware issues and errors block import and publication |

Exit criterion: administrators can govern scoped OIDC access and safely rotate Jira credentials; a configuration owner can author, upload, or capture and validate a blueprint version; and an operator can produce and approve a stable read-only plan for the example blueprint against the sandbox.

## Milestone 2: Safe Deployment Slice

Goal: execute a minimal project deployment with durable state and idempotent reruns.

Start with the smallest capability-proven set, expected to be project metadata and project-scoped components or versions. Add global configuration only after shared-resource controls are working.

| ID | Priority | Size | Backlog item | Acceptance outcome |
| --- | --- | --- | --- | --- |
| JOB-01 | P0 | L | Persist jobs and step checkpoints | Worker restart does not lose the job or repeat a completed idempotent step |
| JOB-02 | P0 | M | Add per-target locking and cancellation | Two writes to one project cannot overlap; cancellation stops before the next mutation |
| JOB-03 | P0 | M | Add Jira retry and rate-limit policy | `429` respects `Retry-After`; permanent errors are not retried as transient errors |
| DEP-01 | P0 | L | Implement project resource handler | Planner and executor create, discover, compare, and verify one company-managed project |
| DEP-02 | P0 | M | Implement first project-scoped handlers | Components and versions create/update without duplicates and are verified by read-back |
| DEP-03 | P0 | M | Persist logical-to-Jira resource mappings | Rerun uses Jira IDs; an ambiguous name match blocks adoption |
| DEP-04 | P0 | M | Enforce plan approval and staleness checks | Unapproved, changed, or stale plans cannot execute |
| UI-02 | P0 | M | Show live execution progress | Browser shows job and step state with reconnect-safe updates and actionable failures |
| AUD-01 | P0 | M | Record baseline audit events | Connection tests, plans, approvals, mutations, cancellations, and results are attributable |
| P03-T09 | P0 | M | Inspect Jira API calls | Job detail lists every ordered attempt with status and bounded sanitized request and response detail |

Exit criterion: the same approved blueprint can deploy to a clean sandbox and rerun with all supported resources classified unchanged.

## Milestone 3: Jira Configuration Catalog

Goal: support the configuration needed by the first real project blueprint.

Implement handlers in the order proven by Milestone 0 and required by dependency paths.

| ID | Priority | Size | Backlog item | Acceptance outcome |
| --- | --- | --- | --- | --- |
| CFG-01 | P0 | L | Add issue type and issue type scheme handlers | Requirement, Test, and Defect types are available and associated as planned |
| CFG-02 | P0 | XL | Add status and workflow handlers | Requirement workflow deploys or reports a precise capability gap; transition graph reads back correctly |
| CFG-03 | P0 | XL | Add custom field and field context handlers | Entities field and project context deploy without changing unrelated contexts |
| CFG-04 | P0 | XL | Add screen and screen scheme handlers | Supported create/edit/view placements compare deterministically and associate correctly |
| CFG-05 | P0 | L | Add workflow and field scheme association | Project uses the planned issue type, workflow, screen, and field configuration associations |
| CFG-06 | P0 | M | Add shared-resource impact policy | Updating a global resource lists affected projects and requires configured approval level |
| CFG-07 | P1 | M | Add permission and notification scheme references | Existing schemes can be resolved and associated where the API supports it |
| CFG-08 | P1 | L | Add filters and dashboards | Ownership, share permissions, and unsupported gadgets are explicit in the plan |

Exit criterion: the capability-supported subset of the first production candidate blueprint deploys end to end, and every unsupported part is visible as evidence rather than skipped.

## Milestone 4: Test Data and Validation

Goal: prove the deployment behaves correctly and provide repeatable sandbox data.

| ID | Priority | Size | Backlog item | Acceptance outcome |
| --- | --- | --- | --- | --- |
| TST-01 | P0 | L | Plan and create test-data packs | At least 50 issues with logical references and links are previewed and created deterministically |
| TST-02 | P0 | M | Mark and map generated issues | Every generated issue has a Jira-side run marker and durable logical mapping |
| TST-03 | P0 | M | Safely clean one test-data run | Preview excludes issues without matching run marker and stored mapping |
| VAL-01 | P0 | M | Validate blueprint and dependency rules | Schema, typed properties, references, cycles, and required parameters have structured results |
| VAL-02 | P0 | L | Add desired-versus-actual validation | Deliberate configuration drift produces expected/observed evidence and remediation hint |
| VAL-03 | P0 | L | Add workflow smoke validation | Temporary issue can be created, transitioned, verified, and cleaned when explicitly enabled |
| UI-03 | P0 | M | Present validation evidence | Results filter by status and severity and link back to resource and job steps |
| VAL-04 | P1 | M | Add validation waivers | Time-bounded waiver records actor, reason, rule, target, and expiry without changing raw result |

Exit criterion: a deliberate configuration mismatch and workflow failure are both detected; generated test data can be removed without touching a manually created control issue.

## Milestone 5: Batch and Scheduling

Goal: run safe issue operations and unattended validation.

| ID | Priority | Size | Backlog item | Acceptance outcome |
| --- | --- | --- | --- | --- |
| BAT-01 | P0 | M | Validate JQL and preview batch target | User sees count and bounded sample; over-limit plans are blocked |
| BAT-02 | P0 | L | Execute allow-listed issue actions | Add-label, set-field, comment, and transition actions record per-issue outcomes |
| BAT-03 | P0 | M | Apply batch safety policies | Rate, retry, maximum count, cancellation, and failure threshold are enforced |
| SCH-01 | P0 | L | Persist and trigger schedules | Time zone is explicit; disabled and missed schedules behave predictably |
| SCH-02 | P0 | M | Prevent overlapping target writes | Overlap policy queues, skips, or rejects a run and records the reason |
| RPT-01 | P0 | M | Export run evidence | JSON and human-readable report exclude secrets and contain plan, actor, target, steps, and validation summary |
| NTF-01 | P1 | M | Notify on completion and failure | Configured channel receives run link and bounded summary without sensitive Jira content |
| P06-T09 | P0 | L | Build issue dependency dataset | Project-scoped issue nodes and typed relationships are normalized, bounded, and permission-filtered |
| P06-T10 | P0 | L | Build issue dependency explorer | Gantt, radial, network, and matrix views share filters, selection, counts, and accessible detail |
| P06-T11 | P0 | XL | Build offline Jira synchronization | Full and incremental sync create complete manifests, tombstones, search data, and permitted encrypted attachments |
| P06-T12 | P0 | L | Build offline browse and search | Online, Automatic, and Offline modes expose source and freshness and Offline makes no Jira request |
| P06-T13 | P0 | L | Govern offline data lifecycle | Encryption, current authorization, quotas, retention, purge, backup, restore, and audit are enforced |

Exit criterion: a scheduled drift validation completes without a browser session, a capped JQL batch can be previewed, approved, retried, and audited, one project dependency dataset is consistent across all four representations, and a complete offline snapshot can be searched with Jira network access denied.

## Milestone 6: MVP Hardening and Release

| ID | Priority | Size | Backlog item | Acceptance outcome |
| --- | --- | --- | --- | --- |
| SEC-01 | P0 | L | Complete authorization threat review | Cross-connection, cross-project, and privilege-escalation tests pass |
| SEC-02 | P0 | M | Verify secret and data redaction | Automated tests cover logs, errors, database diagnostics, events, and exports |
| OPS-01 | P0 | M | Add health, metrics, and alert rules | Operators can identify queue backlog, worker loss, Jira throttling, and repeated failures |
| OPS-02 | P0 | M | Test backup and recovery | Database restore and pending-job reconciliation are demonstrated in a non-production environment |
| QLT-01 | P0 | L | Run sandbox system suite | Clean deploy, idempotent rerun, partial deploy, drift, test cleanup, and batch scenarios pass |
| QLT-02 | P0 | M | Complete accessibility and responsive checks | Core workflows pass keyboard, screen-reader smoke, contrast, and desktop/mobile layout checks |
| REL-01 | P0 | M | Create operator runbook | Connection failure, permission loss, stale plan, worker restart, rate limit, and partial failure are covered |
| REL-02 | P0 | S | Conduct MVP acceptance review | Product owner signs off every criterion or records an explicit exception |

## Post-MVP Backlog

| ID | Priority | Size | Backlog item |
| --- | --- | --- | --- |
| GIT-01 | P1 | L | Synchronize approved blueprint versions from Git pull requests |
| PRM-01 | P1 | L | Promote one release through multiple Jira environments |
| APR-01 | P1 | M | Add risk-based two-person approval policies |
| ROL-01 | P1 | XL | Add narrowly supported reversible operations using captured before-state |
| EXT-01 | P1 | XL | Add a supported extension for Jira configuration unavailable through public REST APIs |
| DC-01 | P2 | XL | Implement and qualify a Jira Data Center adapter |
| JSM-01 | P2 | XL | Add Jira Service Management project configuration |

## Definition of Ready

A backlog item is ready when its user or operator outcome, target Jira plan, API capability, security boundary, dependencies, acceptance examples, and test level are known. A Jira mutation item is not ready until a sanitized API fixture or sandbox proof exists.

## Definition of Done

A completed item has:

- implementation reviewed and merged;
- unit or contract coverage for success, permission failure, conflict, throttling, and redaction where applicable;
- database migration and recovery behavior reviewed where applicable;
- user-visible errors with correlation IDs and remediation hints;
- audit events for relevant commands and mutations;
- documentation and capability matrix updated;
- no unresolved high-severity security or accessibility findings;
- successful demonstration against the fake adapter and, for Jira integration, the sandbox.

## Product Decisions Needed Before Shared Deployment

These decisions are intentionally deferred until the relevant owner can provide facts:

- Jira Cloud product plan and sandbox ownership;
- approved service identity or OAuth model and scopes;
- identity provider, group names, and production approvers;
- hosting platform, regions, recovery objectives, and secret store;
- first production project blueprint and acceptable global-resource reuse policy;
- audit, diagnostic, and issue-level result retention periods;
- maximum issue batch size and production rate limits.