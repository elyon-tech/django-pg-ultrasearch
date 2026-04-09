# Tiger Data Blog: Design, Architecture, Benchmarks, And Limitations

Source URL: <https://www.tigerdata.com/blog/pg-textsearch-bm25-full-text-search-postgres>

## What This Source Is

This is the most detailed public explanation of how `pg_textsearch` works internally and how Tiger Data benchmarked it. It is the best public source for understanding architecture choices, performance claims, tradeoffs, and explicit non-goals.

## What Shipped In v1.0

The article describes the path from an earlier preview to a production-ready release and highlights these shipped changes:

- disk-based segments replacing the earlier memory-only design
- Block-Max WAND plus WAND optimization for top-k search
- posting-list compression
- smaller indexes
- parallel index builds
- strong benchmark results on short queries
- materially better concurrent throughput in their published tests

## Architectural Details Worth Knowing

### Postgres-Native Storage Model

- The index lives in standard PostgreSQL pages.
- It participates in WAL.
- It works with `pg_dump`.
- It works with streaming replication.
- It does not require external index files or a separate search daemon.

This is central to the extension's identity.

### Hybrid Memtable Plus Segment Architecture

- The extension uses an LSM-inspired design.
- New writes land in an in-memory memtable.
- The memtable spills into immutable on-disk segments.
- Segments compact by level.

Why this matters:

- writes are optimized through the memtable
- reads rely on immutable segment structures
- segment count directly affects query cost
- background compaction is not yet implemented, so compaction behavior matters for write-heavy workloads

### Memtable Details

- The memtable is shared-memory based, one per index.
- It stores:
  - interned terms
  - per-term posting lists
  - document statistics needed for BM25 scoring
- Default spill trigger is 32 million posting entries.
- There is also a transaction-level trigger around 100K unique terms per transaction for large bulk loads.
- On startup, the memtable is rebuilt from heap state that has not yet spilled.

### Segment Layout

The article describes segment internals as including:

- a term dictionary
- posting blocks of up to 128 documents
- skip metadata for upper-bound scoring
- a fieldnorm table using 1-byte quantization similar to Lucene or Tantivy small-float encoding

### Block-Max WAND And WAND

- `pg_textsearch` uses WAND for cross-term skipping and Block-Max WAND for within-list block skipping.
- The main benefit is sub-linear practical behavior for top-k ranking on short queries.
- The article explicitly says the speedups are strongest for short queries and narrow as queries get longer.

This should affect how we evaluate the extension. If our future workloads are long natural-language prompts rather than short keyword queries, we should not expect the headline speedups to transfer directly.

## Benchmark Details Published In The Article

### Benchmark Methodology

- Dataset: MS MARCO
- Comparison target: ParadeDB v0.21.6
- Tokenization: English stemming plus stopword removal
- Query tests are warm-cache
- The published tests do not represent out-of-memory or cold-cache conditions

### Reported MS MARCO v2 Results

- Environment:
  - dedicated EC2 `c6i.4xlarge`
  - PostgreSQL 17.4
  - 123 GB RAM
  - `shared_buffers = 31 GB`
- Index size:
  - `pg_textsearch`: 17 GB
  - ParadeDB: 23 GB
- Build time:
  - `pg_textsearch`: 17m 37s
  - ParadeDB: 8m 55s
- Single-client top-10 median latency:
  - 1 lexeme: 11.7x faster
  - 2 lexemes: 6.5x faster
  - 3 lexemes: 3.9x faster
  - 4 lexemes: 2.4x faster
  - 7+ lexemes: roughly converged
- Weighted overall p50 advantage on v2:
  - 2.3x
- Concurrent throughput:
  - 198.7 tps vs 22.8 tps
  - 8.7x higher throughput in that benchmark

### Caveats The Article Admits

- ParadeDB builds indexes faster.
- The index size comparison is not fully apples-to-apples because `pg_textsearch` does not store term positions.
- The benchmarks are warm-cache.
- Tail-latency sample sizes are limited.
- They did not benchmark write-heavy workloads with concurrent queries.

These admissions make the article more useful than a pure marketing post.

## Explicit Limitations In v1.0

The article clearly lists several current limitations:

- no phrase queries
- OR-only query semantics for now
- no highlighting or snippet generation
- no expression indexing
- partition-local statistics
- no background compaction
- PL/pgSQL requires explicit index names
- `shared_preload_libraries` is required
- no fuzzy matching or typo tolerance

This is one of the most important sections for us because these are exactly the kinds of limitations a Django package can accidentally hide from users.

## Post-1.0 Roadmap Mentioned Here

- boolean query operators
- background compaction
- expression index support
- dictionary compression
- improved write concurrency

## Integration Takeaways For Django

- We should not start with a generic "search engine" API. The extension surface is currently more constrained than that.
- Our first integration should likely focus on:
  - index management
  - generated-column patterns
  - explicit query helpers
  - score ordering
  - operational checks
- We should document phrase-query and typo-tolerance gaps up front.
- If we eventually offer hybrid search helpers, they should be explicit composition helpers rather than pretending the extension already solves ranking fusion.

## Confidence Notes

- High confidence on architecture and benchmark claims because they are described in depth by the project authors.
- Still a first-party source, so benchmark claims should be treated as published vendor benchmarks, not independent verification.
