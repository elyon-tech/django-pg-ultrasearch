# Agent Notes AGENTS

Use this file together with the root [`AGENTS.md`](../../AGENTS.md) when touching
`docs/agent-notes/**`.

## Default Use

`docs/agent-notes/**` is for cross-cutting durable notes that are not owned by one
active DSI workstream.

Common examples:

- workflow changes
- instruction-stack updates
- migration reminders
- durable implementation learnings that apply across multiple workstreams

## Boundaries

- Do not use `docs/agent-notes/**` as a substitute for an active DSI folder.
- If a note belongs to one active workstream, keep the main record in
  `docs/dsi/{yyyy}-{mm}-{dd}-{feature-slug}/` and link to it from the note when useful.
- Prefer one clear note over many overlapping fragments.

## Naming

- Use `YYYY-MM-DD Title.md` for note filenames.
- Keep titles short, concrete, and searchable.
