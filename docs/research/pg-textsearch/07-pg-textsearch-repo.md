# `timescale/pg_textsearch` Repository

Source URL: <https://github.com/timescale/pg_textsearch>

## What This Source Is

This is the upstream source repository. It is the most useful source for understanding actual maintenance maturity, repository structure, roadmap, license, benchmark assets, and what parts of the extension are likely stable enough for integration work.

## Current Repository Shape

Top-level contents include:

- `README.md`
- `CHANGELOG.md`
- `ROADMAP.md`
- `OPTIMIZATION_ROADMAP.md`
- `benchmarks/`
- `sql/`
- `src/`
- `test/`
- `scripts/`
- substantial GitHub Actions coverage

This is not a toy repo. It has the structure of a serious extension project.

## License

- SPDX identifier: `PostgreSQL`
- The repository `LICENSE` file is the PostgreSQL License.

This is a strong fit for downstream integration in a permissively licensed Django package.

## Key Facts From The README

- v1.0.0 is marked production ready.
- Supported PostgreSQL versions are 17 and 18.
- Installation requires:
  - `shared_preload_libraries = 'pg_textsearch'`
  - server restart
  - `CREATE EXTENSION pg_textsearch`
- Query patterns include:
  - implicit `ORDER BY content <@> 'search terms'`
  - explicit `to_bm25query()` usage
- Scores are intentionally negated so ascending order returns best matches first.
- The README spends real time on pre-filter vs post-filter behavior, which suggests the authors know this is a practical pain point.

## Signals Of Engineering Maturity

### Benchmarks

The repo includes a real `benchmarks/` directory with:

- multiple datasets
- runner scripts
- benchmark-specific SQL
- CI integration guidance
- benchmark reporting

The benchmark README documents:

- Cranfield for quick correctness checks
- MS MARCO for large-scale performance and ranking evaluation
- Wikipedia for real-world corpus tests

That is useful for us because it means upstream has at least some repeatable performance evaluation infrastructure.

### Roadmap

`ROADMAP.md` shows a fast release cadence from preview builds in late 2025 to production-ready v1.0.0 in March 2026.

Post-v1.0 roadmap items include:

- boolean queries
- background compaction
- expression index support
- multi-tenant support
- positional queries
- faceted-query optimizations

### Optimization Roadmap

`OPTIMIZATION_ROADMAP.md` is especially valuable. It states that major v1.0 optimizations already shipped, including:

- Block-Max WAND
- block-based posting storage
- skip indexes with block-max metadata
- compression
- doc ID mapping
- parallel builds

It also documents unfinished work such as:

- SIMD decoding improvements
- dictionary compression
- write concurrency improvements
- many-token query optimization

This is excellent context for downstream design because it tells us where performance may still move significantly.

### CI Surface

The repo's workflows include:

- `ci.yml`
- `benchmark.yml`
- `nightly-stress.yml`
- `upgrade-tests.yml`
- sanitizer and formatting workflows
- release and packaging workflows

That indicates a mature extension-maintenance posture, including stress and upgrade concerns, not just unit tests.

## Integration Takeaways For Django

- We should read upstream as an evolving, serious dependency, not a thin demo extension.
- `shared_preload_libraries` must be treated as a first-class deployment requirement.
- Our APIs should lean toward explicit query construction and documented filtering tradeoffs.
- We should expect some current rough edges in:
  - write-heavy workloads
  - many-token queries
  - phrase and boolean semantics
- Upstream benchmark assets may become useful for future integration benchmarks or compatibility test fixtures.

## What To Study Next In This Repo

- `sql/` to understand extension-exposed SQL objects and operator names
- `src/` to understand planner hooks and index behavior
- `test/` to see the real semantics the extension considers stable
- benchmark SQL to understand representative query forms

## Confidence Notes

- High confidence on repository structure, license, README behavior, and roadmap items because these are direct repo artifacts.
