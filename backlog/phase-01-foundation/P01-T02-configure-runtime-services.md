# P01-T02 - Configure Runtime Services

- Type: Task
- Phase: 01 - Django Foundation
- Parent: P01-S01
- Depends on: P01-T01
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

Django, PostgreSQL, Redis, Celery, and Celery Beat run together locally.

## Work

- Add Docker Compose services and Django database, cache, broker, and Celery settings.
- Add one diagnostic Celery task and database-managed scheduler configuration.

## Success Criteria

- [ ] One documented command starts all services.
- [ ] Django migrations complete against PostgreSQL.
- [ ] The diagnostic task executes once and records no result as authoritative application state.

## Evidence

- [ ] Startup, migration, worker, and task execution transcript.