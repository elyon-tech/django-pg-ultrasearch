# AGENTS.md

## Instruction Map

Start here, then read the most specific file for the area you are touching.

- Root operational guidance: `AGENTS.md` (this file)
- Documentation workflow and note placement: `docs/AGENTS.md`
- Active workstream Desire/Spec/Plan/Implementation guidance: `docs/dsi/AGENTS.md`
- Cross-cutting durable note guidance: `docs/agent-notes/AGENTS.md`

## Project Context

This repository is a reusable Django package scaffold for PostgreSQL-first search
features.

When adding repo process, planning, or implementation guidance:

- keep the package-focused scope intact
- prefer lean structure over heavyweight process
- adapt shared workflow ideas to this repository instead of copying unrelated product
  assumptions

## Default Feature Workflow

For meaningful feature work, architecture work, workflow changes, or other efforts that
should leave a durable trail, start or resume a DSI workstream folder under:

`docs/dsi/{yyyy}-{mm}-{dd}-{feature-slug}/`

Treat that folder as the canonical record for:

- desire
- spec
- plan
- implementation

Use `docs/agent-notes/**` for cross-cutting durable learnings, workflow updates,
migration reminders, and closeout notes that are not owned by one active workstream.

## Instruction Maintenance Policy

When the user gives broad feedback about workflow, review expectations, note structure,
or agent behavior, update the relevant instruction docs in the same change unless the
user asks not to.

- Keep `AGENTS.md` concise and map-like.
- Put active workstream documentation rules in `docs/dsi/AGENTS.md`.
- Put cross-cutting note rules in `docs/agent-notes/AGENTS.md`.
- If a workflow change affects existing durable notes, add a concise migration note
  under `docs/agent-notes/`.

## Tooling

Use `uv` for Python dependency management and packaging.

Use `task` for the standard project workflows defined in `Taskfile.yml`.

Use `dotagents` through `agents.toml` for shared agent skills.

Use `prek.toml` for Git hook automation. Do not add `pre-commit`-specific config unless
there is a concrete compatibility reason.

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
