# `pg_textsearch` Research Notes

As of 2026-04-08, these notes capture the most relevant facts, claims, caveats, and community reactions from the current `pg_textsearch` documentation, announcement material, discussions, and source repository.

This bundle exists because `django-pg-ultrasearch` is likely to integrate with `pg_textsearch`, and we need a durable record of:

- what the extension claims to do
- what operational constraints it has
- what features are missing in v1.0
- what benchmark claims were actually published
- what community questions came up immediately
- what parts of the repo are worth studying directly before designing a Django integration

## High-Level Conclusions

- `pg_textsearch` is positioned as a production-ready BM25 extension for PostgreSQL 17 and 18, released as v1.0.0 in late March and early April 2026.
- Its strongest value proposition is fast top-k ranked keyword search inside PostgreSQL, especially for short queries, without an external search service.
- The design is intentionally Postgres-native: Postgres pages, WAL participation, replication friendliness, `pg_dump`, and standard extension deployment semantics.
- The main technical tradeoff is that v1.0 is deliberately narrower than a full search engine:
  - no phrase queries
  - no positional indexing
  - no boolean query syntax yet
  - no expression indexes yet
  - no background compaction yet
  - no built-in typo tolerance
- For a Django package, the biggest practical integration concerns are:
  - `shared_preload_libraries` requirement
  - extension installation lifecycle
  - single-column BM25 indexing
  - explicit query construction in procedural contexts
  - score semantics being negative and corpus-relative
  - write-path behavior under update-heavy workloads

## Immediate Design Implications For `django-pg-ultrasearch`

- Treat `pg_textsearch` as a PostgreSQL-specific optional backend, not a generic Django search abstraction.
- Build around explicit configuration and capability detection:
  - extension present or not
  - server version supported or not
  - preload configured or not
- Expect single-column index primitives first.
  - Multi-field search will likely need generated columns or application-managed denormalized text fields.
- Avoid promising phrase queries or boolean query syntax in an initial API layer unless we implement post-filtering or query rewriting ourselves.
- Benchmark and test against real PostgreSQL instances, not SQLite.
- Keep ranking APIs explicit about score interpretation and threshold caveats.

## Source Notes

- [01 Product Docs](./01-product-docs.md)
  Source: <https://www.tigerdata.com/docs/use-timescale/latest/extensions/pg-textsearch#optimize-full-text-search-with-bm25>
- [02 PostgreSQL News Post](./02-postgresql-news-release.md)
  Source: <https://www.postgresql.org/about/news/pg_textsearch-v10-3264/>
- [03 Tiger Data Design And Benchmark Article](./03-tigerdata-blog-design-benchmarks.md)
  Source: <https://www.tigerdata.com/blog/pg-textsearch-bm25-full-text-search-postgres>
- [04 Reddit `r/PostgreSQL` Thread](./04-reddit-postgresql-thread.md)
  Source: <https://www.reddit.com/r/PostgreSQL/comments/1pt8z6y/pg_textsearch_modern_bm25_ranked_text_search_with/>
- [05 Hacker News Thread](./05-hacker-news-thread.md)
  Source: <https://news.ycombinator.com/item?id=47589856>
- [06 Timescale Docs Source File](./06-timescale-docs-source-file.md)
  Source: <https://github.com/timescale/docs/blob/latest/use-timescale/extensions/pg-textsearch.md>
- [07 `timescale/pg_textsearch` Repository](./07-pg-textsearch-repo.md)
  Source: <https://github.com/timescale/pg_textsearch>

## Suggested Next Research Steps

- Read the benchmark workflow and generated benchmark site in detail before making any performance claims in this project.
- Study the extension SQL and C entry points to understand index creation, operator classes, and planner hook behavior.
- Prototype a Django migration and health-check story around:
  - preload detection
  - `CREATE EXTENSION`
  - generated-column indexing
  - explicit query generation with `to_bm25query()`
- Verify what version pinning and packaging story will be needed for self-hosted PostgreSQL versus managed Tiger Data deployments.
