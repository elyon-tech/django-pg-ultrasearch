# Plan

## Execution Steps

1. Replace the root `AGENTS.md` with a map-style version that keeps the existing
   tooling, support, verification, and package-layout guidance while adding the new
   default DSI workflow.
2. Add scoped instructions for `docs/`, `docs/dsi/`, and `docs/agent-notes/` so note
   placement is explicit.
3. Create this DSI workstream folder as the first concrete example of the workflow in
   use.
4. Add a durable migration reminder for older ecosystem notes and future agent-generated
   notes that still need to move into the new structure.
5. Verify the changed docs and scan the repository for the forbidden imported product
   naming after the port.

## Validation

- Read the changed Markdown files for internal consistency.
- Run the standard project checks.
- Search the repository for the disallowed imported naming to confirm it was not added
  by this change.
