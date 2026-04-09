# django-pg-ultrasearch

`django-pg-ultrasearch` is a reusable Django package scaffold for PostgreSQL-first search features.

The repository is intentionally set up with current tooling for a third-party Django extension:

- `uv` for dependency management, locking, and packaging
- `uv_build` as the build backend
- a `src/` layout for safe package imports
- `pytest` and `pytest-django` for tests
- `ruff` for linting and formatting
- `go-task` via `Taskfile.yml`
- `dotagents` for shared coding-agent skills
- `prek` for Git hooks and file-quality automation

## Support Targets

- Python `>=3.13`
- Django `>=5.2`
- PostgreSQL `>=17`

The local smoke tests fall back to SQLite when no PostgreSQL connection is configured, but CI is wired to run the test matrix against PostgreSQL 17.

## Current Status

This is an initial package scaffold, not a finished search implementation yet. The repository currently provides:

- package metadata and build configuration
- a Django app config scaffold
- a minimal test suite
- GitHub Actions CI
- task automation
- dotagents configuration for Codex-oriented agent workflows

## Development

Install dependencies with `uv`:

```bash
uv sync --group dev
```

If you use `go-task`, the common workflows are wrapped in the Taskfile:

```bash
task install
task check
task build
```

Set up Git hooks with `prek`:

```bash
task prek:install
```

### Local PostgreSQL

To run tests against PostgreSQL, export the usual `PG*` environment variables and use:

```bash
task test:postgres
```

Example:

```bash
export PGHOST=127.0.0.1
export PGPORT=5432
export PGDATABASE=django_pg_ultrasearch
export PGUSER=postgres
export PGPASSWORD=postgres
task test:postgres
```

## dotagents

The repository uses `dotagents` with `agents.toml` as the source of truth.

Current setup:

- agent target: `codex`
- trusted source org: `getsentry`
- installed skills:
  - `dotagents`
  - `find-bugs`
  - `code-review`
  - `commit`
  - `django-perf-review`

Useful commands:

```bash
task dotagents:install
task dotagents:sync
task dotagents:doctor
task dotagents:list
```

Or directly:

```bash
npx @sentry/dotagents install
```

## `prek`

The repository uses native `prek` configuration in `prek.toml` rather than `pre-commit`.

Useful commands:

```bash
task prek:install
task prek:run
task prek:update
task prek:validate
```

## Reference Repos

The ecosystem notes from studying strong third-party Django packages live in `docs/reference-projects.md`.

That note includes the four repos you called out plus several other mature Django libraries, with observations on:

- repo structure
- Python and Django support strategy
- CI and multi-version testing
- PostgreSQL and multi-database testing patterns
- packaging and release tooling
- which patterns this repository is intentionally copying or avoiding

## Package Notes

The package follows Django reusable-app conventions:

- distribution name: `django-pg-ultrasearch`
- import package: `django_pg_ultrasearch`
- Django app label: `pg_ultrasearch`

Keep templates, static files, migrations, and management commands under `src/django_pg_ultrasearch/` so `uv_build` includes them in wheels and source distributions.
