# Implementation

## Files Added Or Updated

- [`AGENTS.md`](../../../AGENTS.md)
- [`docs/AGENTS.md`](../../../docs/AGENTS.md)
- [`docs/dsi/AGENTS.md`](../../../docs/dsi/AGENTS.md)
- [`docs/agent-notes/AGENTS.md`](../../../docs/agent-notes/AGENTS.md)
- [`docs/dsi/2026-04-08-dsi-workflow-adoption/desire.md`](../desire.md)
- [`docs/dsi/2026-04-08-dsi-workflow-adoption/specs/initial.md`](../specs/initial.md)
- [`docs/dsi/2026-04-08-dsi-workflow-adoption/plans/initial.md`](../plans/initial.md)
- [`docs/dsi/2026-04-08-dsi-workflow-adoption/implementations/initial.md`](./initial.md)
- [`docs/agent-notes/2026-04-08 DSI Workflow Adoption And Notes Migration.md`](../../../docs/agent-notes/2026-04-08%20DSI%20Workflow%20Adoption%20And%20Notes%20Migration.md)
- [`docs/reference-projects.md`](../../../docs/reference-projects.md)

## Notes

- The root instruction file now points agents to a path-scoped documentation workflow
  instead of only listing tooling and verification commands.
- `docs/dsi/` is now the declared default home for active workstream desire, spec,
  plan, and implementation docs.
- `docs/agent-notes/` is now the declared default home for cross-cutting durable notes.
- The existing ecosystem note now carries an explicit migration reminder instead of
  silently remaining outside the new structure.

## Follow-Up

- Migrate the ecosystem notes into the newer structure when they are materially revised.
- Keep future agent-generated notes in either the owning DSI folder or
  `docs/agent-notes/`.
