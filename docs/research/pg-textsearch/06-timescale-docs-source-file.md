# Timescale Docs Source File: Editorial Source Of Truth

Source URL: <https://github.com/timescale/docs/blob/latest/use-timescale/extensions/pg-textsearch.md>

## What This Source Is

This is the Markdown source file behind the rendered Tiger Data documentation page. It is useful because it shows the same product guidance in a source-controlled form, including some version-gated and editorial cues that are less obvious on the rendered page.

## Why This Matters Separately From The Rendered Docs Page

- It confirms that the public product guide is backed by a maintained docs repository rather than a one-off marketing page.
- It exposes docs structure directly:
  - frontmatter
  - version include markers
  - partial references
  - product tags and keywords
- It is easier to diff over time than the rendered docs site.

## Notable Source-Level Observations

- Frontmatter explicitly positions the page around:
  - BM25
  - ranking
  - performance
  - hybrid search
- The source imports version-partial snippets, including `SINCE100`, which confirms the docs are built with version-aware editorial components.
- The same source explicitly states:
  - v1.0.0 is production ready
  - PostgreSQL 17 and 18 are supported
  - single-column BM25 indexes only
  - parallel builds require at least 64MB `maintenance_work_mem`
  - PL/pgSQL requires `to_bm25query()` and explicit index names

## Why This Is Useful For Ongoing Tracking

- If `pg_textsearch` evolves quickly, this file is one of the easiest places to monitor changes in official guidance.
- It is likely to reflect support-matrix changes and newly documented limitations before secondary sources catch up.
- For this Django package, it is a good canonical doc to watch when deciding:
  - what versions to support
  - which limitations are still current
  - whether expression indexes or boolean queries have landed

## Integration Takeaways For Django

- Keep a note to periodically re-review this docs source file, not just the marketing blog.
- Use it as a release-tracking source for documented capabilities.
- Treat it as more authoritative than community-thread summaries when questions conflict.

## Confidence Notes

- Very high confidence because this is direct source material for the official documentation page.
