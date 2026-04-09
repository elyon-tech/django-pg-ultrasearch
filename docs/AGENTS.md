# Docs AGENTS

Use this file together with the root [`AGENTS.md`](../AGENTS.md) when touching
`docs/**`.

## Default Placement

- Use `docs/dsi/**` for active workstream documentation that should track desire, spec,
  plan, and implementation for one feature or effort.
- Use `docs/agent-notes/**` for cross-cutting durable notes, workflow updates, and
  migration reminders that are not owned by one active workstream.

## Working Style

- Prefer updating the owning DSI folder over creating ad hoc planning files elsewhere.
- Keep cross-cutting notes concise and explicit about why they exist.
- Use repo-relative Markdown links in documentation files.
- When a docs change updates workflow expectations, make the relevant `AGENTS.md`
  change in the same patch.
