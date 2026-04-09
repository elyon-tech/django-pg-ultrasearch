# Django Package Reference Notes

Migration note: this document predates the repository's Desire/Spec/Plan/Implementation
workflow. When it is materially updated next, migrate the active planning portions into
`docs/dsi/` or `docs/agent-notes/` instead of extending this file as an ad hoc
workstream note.

As of 2026-04-08, these are the reference repositories and patterns reviewed while shaping this project's structure and tooling.

## User-Requested Repos

### `SmileyChris/django-countries`

- URL: <https://github.com/SmileyChris/django-countries>
- License: MIT
- Current shape:
  - modern `pyproject.toml`
  - `uv_build`
  - `justfile`
  - GitHub Actions
  - `docs/`, `changes/`, and package-owned test settings inside the app tree
  - `.pre-commit-config.yaml`
- Notable patterns:
  - support policy is declared in package classifiers and enforced in CI
  - `uv` is used seriously, not just incidentally
  - app data and tests stay close to the package
  - lint, type-check, docs, security, and coverage are split into dedicated CI jobs
- Main takeaway for this repo:
  - this is the strongest example in the set of a modern Django reusable package that already moved to `uv`

### `SectorLabs/django-postgres-extra`

- URL: <https://github.com/SectorLabs/django-postgres-extra>
- License: MIT
- Current shape:
  - `pyproject.toml` plus `setup.py` and `setup.cfg`
  - `tox.ini`
  - CircleCI
  - separate requirements files
  - `poethepoet` tasks in `pyproject.toml`
- Notable patterns:
  - extremely broad version matrix across Python, Django, and psycopg variants
  - explicit focus on PostgreSQL-specific behavior
  - tests are treated as first-class compatibility checks, not only unit smoke tests
- Main takeaway for this repo:
  - broad compatibility matrices matter for a Postgres-centric Django library, but the surrounding tooling stack is more legacy and more file-heavy than the direction we want here

### `dimagi/django-cte`

- URL: <https://github.com/dimagi/django-cte>
- License: BSD-3-Clause
- Current shape:
  - lean root layout
  - `pyproject.toml`
  - `uv.lock`
  - GitHub Actions
  - top-level `tests/`
- Notable patterns:
  - support versions are read from `pyproject.toml` into the GitHub Actions matrix
  - tests run on both PostgreSQL and SQLite
  - CI uses a real PostgreSQL service
  - very little top-level clutter for a mature package
- Main takeaway for this repo:
  - this is the clearest example in the set of a lean, modern, package-focused repository with good matrix discipline

### `django-phonenumber-field/django-phonenumber-field`

- URL: <https://github.com/django-phonenumber-field/django-phonenumber-field>
- License: MIT
- Current shape:
  - `pyproject.toml`
  - `tox.ini`
  - GitHub Actions
  - top-level `tests/`
  - `docs/`
- Notable patterns:
  - broad Python coverage including Python 3.14
  - explicit testing against Django release lines and Django `main`
  - `tox-gh` drives matrix selection from GitHub Actions
  - stable package metadata and conservative build tooling
- Main takeaway for this repo:
  - tracking Django `main` early is a good habit for reusable Django packages that want to stay ahead of compatibility breakage

## Additional Repos Studied

### `carltongibson/django-filter`

- URL: <https://github.com/carltongibson/django-filter>
- License: BSD-3-Clause
- Notable patterns:
  - classic mature Django package layout
  - `pyproject.toml`, `setup.cfg`, `tox.ini`, `requirements/`, docs, and tests
  - broad compatibility and long project history
- Takeaway:
  - mature projects often accrete compatibility files over time; that does not mean a fresh package should start with all of them

### `django-commons/django-debug-toolbar`

- URL: <https://github.com/django-commons/django-debug-toolbar>
- License: BSD-3-Clause
- Notable patterns:
  - one of the strongest CI examples in the ecosystem
  - multiple database backends in CI: SQLite, MySQL/MariaDB, PostgreSQL, PostGIS variants
  - separate lint and release workflows
  - strong hook setup around formatting and config validation
- Takeaway:
  - if database behavior is central, real services in CI are worth the cost

### `jazzband/django-model-utils`

- URL: <https://github.com/jazzband/django-model-utils>
- License: BSD-3-Clause
- Notable patterns:
  - older but still strong reusable-app layout
  - `setup.py`, `setup.cfg`, requirements files, tox, docs, tests
  - broad support and conservative release discipline
- Takeaway:
  - good example of what established maintenance discipline looks like, even if the toolchain itself is older

### `jschneier/django-storages`

- URL: <https://github.com/jschneier/django-storages>
- License: BSD-3-Clause
- Notable patterns:
  - top-level docs and tests
  - `pyproject.toml` plus `setup.py`
  - `tox.ini`
  - strong external-service integration story
- Takeaway:
  - widely used packages still often keep transitional packaging files for compatibility, but new packages do not need to begin there

## License Check Summary

Of the four repos originally called out:

- `django-countries`: MIT
- `django-postgres-extra`: MIT
- `django-cte`: BSD-3-Clause
- `django-phonenumber-field`: MIT

So the answer is no: all four are not MIT.

## Cross-Cutting Patterns Worth Copying

### Structure

- Keep the reusable package itself small and focused.
- Put package code in a dedicated package directory or `src/` layout.
- Keep `tests/` and `docs/` top-level.
- Keep package data inside the package tree.

### Version Support

- Declare Python and Django support in package classifiers.
- Mirror that support policy in CI.
- For reusable libraries, compatibility policy is part of the product surface.

### CI

- Use GitHub Actions unless there is a strong reason not to.
- Test against real services for database-specific features.
- Split quality checks from runtime tests when it improves clarity.
- Keep matrix exclusions explicit and justified.

### Packaging

- Centralize metadata in `pyproject.toml`.
- Avoid duplicating metadata across `setup.py`, `setup.cfg`, and requirements files unless compatibility truly requires it.
- Keep build and runtime dependencies easy to audit.

### Maintenance

- Use automated formatting and linting hooks.
- Treat documentation, changelog discipline, and release metadata as normal maintenance, not optional extras.
- Prefer a small number of well-defined task entry points over a sprawl of ad hoc scripts.

## Decisions Applied In This Repository

Based on the repos above, this project intentionally prefers:

- `uv` and `uv_build`
- a `src/` layout
- a lean root layout
- GitHub Actions
- PostgreSQL 17 service coverage in CI
- `Taskfile.yml` for repeatable local workflows
- `dotagents` for agent configuration
- native `prek.toml` instead of `pre-commit`

This project intentionally avoids, unless future requirements force them:

- `setup.py`
- `setup.cfg`
- `tox.ini`
- separate `requirements*.txt` files
- older CI systems like CircleCI for core validation

## Implementation Learnings From This Repository

These are concrete things learned while actually setting up `django-pg-ultrasearch`, not just from reading other projects.

### `prek`

- Native `prek.toml` works well and keeps the repo free of a `.pre-commit-config.yaml`.
- `prek` can consume the broader pre-commit hook ecosystem, so switching to `prek` does not require giving up the existing hook universe.
- `prek validate-config` expects the config path as a positional argument.
- A first full `prek run --all-files` is useful because it reveals the real formatting policy that tools like `pyproject-fmt` will enforce, instead of leaving that implicit.
- Installing local Git shims with `prek install --prepare-hooks` is worth doing immediately so `pre-commit` and `pre-push` stay aligned with CI.

### `pyproject.toml`

- `pyproject-fmt` rewrites the file structure more aggressively than Ruff does; once adopted, it should be treated as authoritative formatting policy.
- A modern Django package can keep almost all packaging, test, lint, and support metadata in `pyproject.toml` without needing `setup.py`, `setup.cfg`, or `tox.ini`.
- Keeping support policy in classifiers remains valuable because some projects derive CI matrices from those declarations.

### `uv`

- `uv` is fully sufficient for a modern Django library workflow here: init, sync, lock, run, and build all work cleanly.
- `uv_build` fits the goal of a minimal top-level layout well.
- Adding `prek` as a dev dependency keeps hook execution consistent between local runs and CI.

### CI

- For a PostgreSQL-focused library, using a real PostgreSQL service in GitHub Actions is the right default.
- Even a tiny test suite benefits from being exercised against PostgreSQL directly, because it verifies the package wiring and dependency surface under the intended database backend.
- Separating hook checks from lint/test jobs keeps failures easier to diagnose.

### Project Operations

- `Taskfile.yml` is useful as the human-facing command surface even when the underlying tools are `uv`, `prek`, and `dotagents`.
- The Taskfile can be committed even if `task` is not installed in the current environment; what matters is that the underlying commands are verified.
- `dotagents` works well as committed project configuration when the trust boundary is kept explicit and the installed skill set stays curated instead of wildcard-based.

## Bottom Line

The strongest direct inspirations for this repository are:

- `django-countries` for modern `uv` adoption in a reusable Django package
- `django-cte` for a lean root and dynamic support-matrix discipline
- `django-debug-toolbar` for serious CI coverage across databases
- `django-phonenumber-field` for explicit Django-version coverage and testing strategy
