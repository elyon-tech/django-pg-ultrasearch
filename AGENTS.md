# Agent Instructions

## Tooling

Use `uv` for Python dependency management and packaging.

Use `task` for the standard project workflows defined in `Taskfile.yml`.

Use `dotagents` through `agents.toml` for shared agent skills.

Use `prek.toml` for Git hook automation. Do not add `pre-commit`-specific config unless there is a concrete compatibility reason.

## Support Policy

- Python `>=3.13`
- Django `>=5.2`
- PostgreSQL `>=17`

## Verification

For ordinary changes, run:

```bash
task check
```

For hook-visible file quality changes, also run:

```bash
task prek:run
```

When touching database-specific or PostgreSQL-specific behavior, also run:

```bash
task test:postgres
```

## Package Layout

Keep reusable package code under `src/django_pg_ultrasearch/`.

Keep package data inside the package tree so it is included in builds.

Keep tests under `tests/`.
