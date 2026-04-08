# django-pg-ultrasearch

`django-pg-ultrasearch` is a reusable Django app scaffold for PostgreSQL-first search features.

The repository is set up as a modern third-party Django package with:

- `uv` project management and locking
- `uv_build` as the build backend
- a `src/` layout for distribution-safe imports
- `pytest` and `pytest-django` for tests
- `ruff` for linting and formatting
- GitHub Actions CI

## Supported Versions

- Python 3.12, 3.13, and 3.14
- Django 5.2 and 6.0

## Installation

```bash
uv add django-pg-ultrasearch
```

Or with `pip`:

```bash
python -m pip install django-pg-ultrasearch
```

## Quick Start

Add the app to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...,
    "django_pg_ultrasearch",
]
```

## Development

```bash
uv sync --group dev
uv run pytest
uv run ruff check .
uv run ruff format --check .
uv build
```

## Packaging Notes

The package follows Django's reusable-app guidance:

- the distribution name uses the `django-` prefix
- the import package uses the `django_` prefix
- the Django app label stays short as `pg_ultrasearch`

When you add templates, static assets, migrations, or management commands, keep them inside `src/django_pg_ultrasearch/` so `uv_build` includes them in wheels and source distributions.
