# Jira Project Deployer

Product and architecture baseline for a web application that deploys and operates Jira project configuration from versioned blueprints.

The application is a Django 5.2 LTS modular monolith with Django templates and HTMX, Django REST Framework, PostgreSQL, Celery, and Redis.

## Product Capabilities

- Deploy a complete project configuration into an existing Jira site.
- Select and deploy dependency-safe parts of a project configuration.
- Seed and safely clean up traceable Jira test data.
- Validate blueprint structure, permissions, deployed state, workflows, and drift.
- Run immediate or scheduled deployments, validations, test-data jobs, and controlled JQL issue batches.

## Current Status

The repository is in product discovery and solution architecture. The current decision is to target Jira Cloud first and to use only documented, capability-proven Jira APIs. The next implementation milestone is the Jira sandbox capability proof in the delivery backlog.

## Start Here

- [Product brief](docs/product-brief.md): scope, users, requirements, acceptance criteria, and exclusions.
- [Solution architecture](docs/solution-architecture.md): components, domain model, job semantics, security, and Jira integration.
- [Blueprint contract](docs/blueprint-contract.md): identity, parameters, dependencies, selection, and evolution rules.
- [Delivery backlog](docs/delivery-backlog.md): prioritized milestones from API proof through MVP release.
- [Implementation issues](backlog/README.md): phased stories, deterministic tasks, issue template, and agent workflow.
- [Common prompts](docs/common-prompts.md): copy-ready prompts for delivery, specialist reviews, verification, and reporting.
- [Troubleshooting prompts](docs/troubleshooting-prompts.md): diagnosis and recovery prompts for the Django, PostgreSQL, Celery, Redis, HTMX, DRF, Jira, and blueprint stack.
- [Interactive UI mockup](mockups/jira-project-deployer.html): standalone responsive prototype and canonical interaction contract, with developer-only backlog-ticket hover and inspection mappings.
- [Solution Manager agent](.github/agents/solution-manager.agent.md): user-facing orchestrator for the Developer and QA tandem.
- [Senior UX Specialist](.github/agents/senior-ux-specialist.agent.md): read-only UX reviewer using the expert-method framework below.
- [Example blueprint](blueprints/examples/erste-project.yaml): representative Requirement, Test, and Defect project subset.
- [Blueprint JSON Schema](schemas/jira-project-blueprint.schema.json): machine-readable `v1alpha1` envelope.

## UX Review Framework

The project champions five complementary bodies of UX practice for reviewing its complex administrative workflows. These experts are methodological references; this project claims no affiliation with or endorsement by them.

- [Jakob Nielsen](https://www.nngroup.com/people/jakob-nielsen/): usability heuristics, visible system status, consistency, error prevention, recovery, and actionable feedback.
- [Indi Young](https://indiyoung.com/): mental-model research that organizes workflows around how administrators reason about impact, readiness, risk, and evidence.
- [Abby Covert](https://abbycovert.com/): information architecture, precise terminology, visible scope, navigation, taxonomy, and alternate representations of shared information.
- [Brad Frost](https://bradfrost.com/): reusable design-system components with consistent contracts for loading, empty, partial, success, warning, error, disabled, stale, and offline states.
- [Sara Soueidan](https://www.sarasoueidan.com/): semantic HTML, native controls, keyboard and focus behavior, accessible status updates, progressive enhancement, and textual equivalents for diagrams.

In practice, reviews must keep portfolio, connection, project, blueprint, job, and snapshot scope explicit; prevent unsafe actions before execution; reuse consistent Django and HTMX components; and provide equivalent information without relying only on color, hover, JavaScript, or visual diagrams.

The Senior UX Specialist applies these lenses and reports evidence, user impact, bounded recommendations, and verification criteria. The role is advisory and read-only; Senior QA remains the mandatory independent verification role, and the Solution Manager alone controls issue completion.

## Existing Discovery Artifacts

- `ErsteJiraSetUp.smmx` contains the detailed Jira issue, field, status, and workflow model used as source material.
- `RequirementWorkflow.smmx` contains an earlier requirement workflow model.
- `SimpleMind_Agent_Instructions.md` documents how to inspect `.smmx` archives.
- `generate_smmx.py` generates the requirement workflow map.

SimpleMind maps are discovery artifacts, not deployment input. Runtime deployment uses reviewed YAML or JSON blueprints with stable logical resource IDs.

## Key MVP Safety Rules

- Generate and approve a dry-run plan before every mutation.
- Add required dependencies to partial selections and explain why.
- Create and update configuration without deleting production configuration.
- Serialize concurrent writes to the same Jira project.
- Store credential references rather than credential values.
- Report unsupported Jira operations explicitly.
- Clean up only test issues carrying both a stored mapping and a Jira-side run marker.
