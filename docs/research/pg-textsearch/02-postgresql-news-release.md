# PostgreSQL News Post: `pg_textsearch v1.0`

Source URL: <https://www.postgresql.org/about/news/pg_textsearch-v10-3264/>

## What This Source Is

This is the official PostgreSQL news announcement page for the release. It is short, but it matters because it confirms how the project was presented publicly to the PostgreSQL ecosystem.

## Concrete Facts

- Title: `pg_textsearch v1.0`
- Posted: 2026-04-03
- Posted by: Tiger Data
- The announcement says `pg_textsearch` is open source under the PostgreSQL License.

## Main Positioning

- `pg_textsearch` is framed as a production-ready, BM25-based, relevance-ranked keyword search extension for PostgreSQL.
- The post emphasizes:
  - modern ranked keyword search
  - fast indexing
  - strong query performance
  - open-source availability

## Competitive Framing

- The announcement explicitly compares `pg_textsearch` against ParadeDB in the linked material.
- It also draws attention to licensing posture:
  - `pg_textsearch` uses the PostgreSQL License
  - ParadeDB is described as having a more restrictive AGPL license

This matters because licensing is not just a legal footnote here; it is part of the product pitch.

## Integration Takeaways For Django

- If `django-pg-ultrasearch` adopts `pg_textsearch`, license compatibility is straightforward and permissive.
- The project is being marketed as a serious production component, so our integration should assume users will expect operational discipline:
  - health checks
  - clear setup validation
  - explicit compatibility support
- Competitive claims are part of the surrounding story, but our package should stay focused on capabilities and correctness rather than reproducing benchmark marketing.

## Confidence Notes

- Very high confidence on release date and license statement.
- Low detail on implementation because this source is intentionally brief.
