# Desire

## Core Intent

- Make Desire/Spec/Plan/Implementation the default way to start meaningful work in this
  repository.
- Give agents and humans one clear place to capture workstream intent, design,
  execution, and factual implementation notes.
- Keep the workflow lightweight enough for a reusable Django package repo instead of
  turning documentation into ceremony.

## Desired Operator Experience

- When a non-trivial feature or workflow change starts, the repo should have an obvious
  place to create or resume a workstream folder.
- Agents should know where active workstream docs belong and where cross-cutting notes
  belong.
- Existing notes that predate this structure should be easy to identify for later
  cleanup or migration.

## Scope Assumptions

- This change is about repository workflow and documentation structure, not package
  implementation behavior.
- The initial adoption can be minimal as long as the default path is clear.
- Older notes do not need to be fully migrated in the same patch, but the repo should
  record that migration follow-up explicitly.
