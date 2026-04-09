# Product Docs: Tiger Data `pg_textsearch` Guide

Source URL: <https://www.tigerdata.com/docs/use-timescale/latest/extensions/pg-textsearch#optimize-full-text-search-with-bm25>

## What This Source Is

This is the primary end-user product documentation page for `pg_textsearch`. It is the clearest source for supported versions, install steps, operational requirements, query syntax, and the vendor's intended usage patterns.

## Core Claims

- `pg_textsearch` brings BM25-based full-text search directly into PostgreSQL.
- It uses a memtable architecture for efficient indexing and ranking.
- It claims:
  - up to 4x faster top-k queries versus native BM25 implementations
  - 4x or greater parallel index build improvements on large tables
  - 41% smaller indexes from delta encoding and bitpacking
  - 10% to 20% better short-query performance from compression improvements
- `pg_textsearch` v1.0.0 is production ready as of March 2026.
- Supported PostgreSQL versions are 17 and 18.

## Concrete API And Operational Details

### Installation

- Install with:
  ```sql
  CREATE EXTENSION pg_textsearch;
  ```
- The docs imply managed-service availability concerns for existing services and maintenance windows.

### Index Creation

- Primary example:
  ```sql
  CREATE INDEX products_search_idx ON products
  USING bm25(description)
  WITH (text_config='english');
  ```
- BM25 indexes are single-column only.
- Best practice is to load data first, then create the BM25 index.

### Parallel Build Requirements

- PostgreSQL may use parallel workers automatically for large tables.
- Parallel build requires:
  - `maintenance_work_mem >= 64MB`
- Example tuning:
  ```sql
  SET max_parallel_maintenance_workers = 4;
  SET maintenance_work_mem = '256MB';
  ```

### Querying

- Ranked search with implicit operator:
  ```sql
  SELECT name, description, description <@> 'ergonomic work' AS score
  FROM products
  ORDER BY score
  LIMIT 3;
  ```
- Explicit query object form:
  ```sql
  SELECT name, description <@> to_bm25query('ergonomic work', 'products_search_idx') AS score
  FROM products
  ORDER BY score
  LIMIT 3;
  ```
- Use `to_bm25query()` for `WHERE` filtering and explicit index selection.
- The implicit `text <@> 'query'` form does not work inside PL/pgSQL functions or `DO` blocks.

### Score Semantics

- BM25 scores are returned as negative values.
- Lower or more negative values mean a better match.
- This is operationally important for API design because users will otherwise assume higher is better.

## Best-Practice Guidance In The Docs

- choose an appropriate `text_config` per language
- use parallel indexing for large builds
- use score thresholds carefully
- monitor index usage and memory
- combine with vector search for hybrid retrieval use cases

## Important Limitations Or Constraints Exposed Here

- single-column BM25 indexes only
- procedural contexts need explicit query objects
- ranking is corpus-aware and relative, so thresholding is not globally portable

## Integration Takeaways For Django

- A Django integration should generate `to_bm25query()` explicitly rather than leaning only on the implicit operator syntax.
- Model-level convenience APIs should not pretend BM25 scores are stable across datasets.
- If we want multi-field search, we should probably generate or recommend denormalized text columns instead of promising native multi-column BM25 support.
- Migration helpers should document the memory requirement for parallel builds.

## Confidence Notes

- High confidence on installation, supported versions, syntax, and stated limitations.
- Performance claims here are marketing-facing and should be treated as vendor claims until independently benchmarked.
