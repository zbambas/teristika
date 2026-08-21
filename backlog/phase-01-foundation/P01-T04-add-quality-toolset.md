# P01-T04 - Add Quality Toolset

- Type: Task
- Phase: 01 - Django Foundation
- Parent: P01-S01
- Depends on: P01-T01
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

One deterministic command validates formatting, linting, typing, migrations, and tests.

## Work

- Configure Ruff, mypy with Django stubs, pytest, and pytest-django in `pyproject.toml`.
- Add CI steps for dependency sync, Django checks, missing migrations, static checks, and tests.

## Success Criteria

- [ ] The documented quality command passes from a clean dependency install.
- [ ] CI fails for a lint error, type error, missing migration, or failing test.
- [ ] Test settings never connect to a shared or production database.

## Evidence

- [ ] Successful local quality output and CI run link or transcript.