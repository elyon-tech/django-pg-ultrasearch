# Spec

## Scope

This workstream establishes the repository's default documentation workflow for
meaningful work.

It covers:

- the root instruction map
- path-scoped docs instructions
- the default Desire/Spec/Plan/Implementation folder pattern
- a migration reminder for existing ecosystem notes and future agent-generated notes

It does not yet cover:

- a dedicated skill for creating DSI folders
- automated validation of DSI folder structure
- full migration of older notes into the new format

## Repository Shape

The workflow should use:

- `docs/dsi/` for active workstreams
- `docs/agent-notes/` for cross-cutting durable notes

The root [`AGENTS.md`](../../../AGENTS.md) should stay concise and map-like while
pointing agents to the more specific docs guidance.

## Behavioral Rules

- Meaningful feature work, architecture work, and workflow changes should start or
  resume a folder under `docs/dsi/{yyyy}-{mm}-{dd}-{feature-slug}/`.
- The DSI folder should be treated as the canonical workstream record for desire, spec,
  plan, and implementation.
- Cross-cutting notes that are not owned by one active workstream should live under
  `docs/agent-notes/`.
- Older notes that predate this structure should carry an explicit migration reminder
  instead of silently continuing as ad hoc planning surfaces.

## Initial Migration Expectation

The existing ecosystem note at
[`docs/reference-projects.md`](../../../docs/reference-projects.md) should be marked as
pre-DSI and queued for migration when it is materially updated next.

Future agent-generated notes should follow one of these homes:

- the owning `docs/dsi/...` workstream folder
- `docs/agent-notes/...` for cross-cutting durable notes
