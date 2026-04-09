# DSI AGENTS

Use this file together with the root [`AGENTS.md`](../../AGENTS.md) when touching
`docs/dsi/**`.

## Default Use

`docs/dsi/**` is the default home for active feature and workstream documentation in
this repository.

Start or resume a DSI folder when work needs durable intent, design, execution, and
implementation notes rather than a one-off patch.

Use `docs/agent-notes/**` instead when the note is cross-cutting and not owned by one
active workstream.

## Purpose

`DSI` is the working folder name, and the default document set is:

- Desire
- Spec
- Plan
- Implementation

Not every workstream needs the same file shape on day one, but that is the default
concept agents should bring into new work here.

## Folder Naming

- Create one workstream folder per effort as
  `docs/dsi/{yyyy}-{mm}-{dd}-{feature-slug}/`.
- Keep the slug descriptive but compact.
- Treat the folder as the long-lived container for that effort's intent, design,
  execution planning, and implementation notes.

## Preferred File Shapes

Use the file shape that matches how iterative the work is expected to be.

- By default, expect the folder to cover desire, spec, plan, and implementation.
- If a category is likely to stay single-document for a while, a top-level file such
  as `desire.md` is fine.
- If the work is expected to evolve through multiple passes, prefer nested iterative
  files right away, for example:
  - `specs/initial.md`
  - `plans/initial.md`
  - `implementations/initial.md`

Valid shapes include:

- `desire.md`
- `spec.md`
- `plan.md`
- `implementation.md`
- `desires.md`
- `specs.md`
- `plans.md`
- `implementations.md`
- `desires/*.md`
- `specs/*.md`
- `plans/*.md`
- `implementations/*.md`

## Content Expectations

- Desires capture intended outcomes, goals, and success criteria.
- Specs capture the design decisions that emerge from those desires and follow-on
  discussion.
- Plans capture execution approach, sequencing, and validation strategy.
- Implementations capture factual notes about what changed in code, config, commands,
  files, validation, and important before/after behavior.

## Working Style

- Update DSI docs alongside code when scope, decisions, or implementation reality
  changes.
- When a workstream already has a DSI folder, extend it instead of creating separate ad
  hoc planning notes elsewhere.
- Keep implementation notes factual and concrete.
- Use repo-relative Markdown links inside DSI docs.
