# P01-T01 - Scaffold Django Project

- Type: Task
- Phase: 01 - Django Foundation
- Parent: P01-S01
- Depends on: P00-S01
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

The repository contains a runnable Django 5.2 LTS project matching the architecture layout.

## Work

- Create `pyproject.toml`, `manage.py`, `config/`, declared Django apps, and environment-based settings.
- Add a server-rendered home page and `/health/live/` endpoint.

## Success Criteria

- [ ] `uv run python manage.py check` passes.
- [ ] The home page and liveness endpoint return `200` in Django tests.
- [ ] No secret or environment-specific value is committed.

## Evidence

- [ ] Clean-install, Django check, and focused test output.