# dispatched-m2s — wiki index
> One line per page. The wiki row's CONTEXT section renders this file.
> Last updated: 2026-09-16 | Total pages: 10

## Entities
- [[topics/dispatched-m2s/wiki/entities/delegation-batch-56809b77|delegation batch deleg_56809b77]] — A Hermes async delegation batch that completed successfully on `2026-09-07 10:08`, demonstrating the larger-fan-out success pattern noted after earlier owner-ex
- [[topics/dispatched-m2s/wiki/entities/delegation-batch-7418fbf4|delegation batch deleg_7418fbf4]] — A Hermes async delegation batch reported complete on `2026-09-16 20:26` (message ID `20260914_200308_f9b029`, simulation `0.19`). The batch fanned out to `5` su
- [[topics/dispatched-m2s/wiki/entities/delegation-batch-dc36df32|delegation batch deleg_dc36df32]] — A Hermes async delegation batch that completed successfully on `2026-09-07 10:39`, recorded immediately after the successful `deleg_56809b77` run.
- [[topics/dispatched-m2s/wiki/entities/delegation-batch-e76115bb|delegation batch deleg_e76115bb]] — A Hermes async delegation batch dispatched at `2026-09-07 05:36:30` and reported from `2026-09-07 05:42`. The batch consisted of `1` subagent with role `leaf`; 
- [[topics/dispatched-m2s/wiki/entities/dispatched-m2s|dispatched-m2s]] — The topic covering Hermes async delegation batches that do not complete successfully. The current known instance is [[entities/delegation-batch-e76115bb|batch d
- [[topics/dispatched-m2s/wiki/entities/hermes-message-20260903-001447-7bc70a|Hermes state.db message 20260903_001447_7bc70a]] — A Hermes state.db message filed under a recurring message ID `20260903_001447_7bc70a` — the same ID that previously carried the delegation-owner-exit timeout er

## Concepts
- [[topics/dispatched-m2s/wiki/concepts/delegation-timeout|delegation owner exit timeout]] — A failure mode in which the delegation owner process exits before recording a terminal result for its leaf subagent batch. The observable result is the error st

## Decisions
- [[topics/dispatched-m2s/wiki/decisions/batch-size-mitigation-pattern|batch size mitigation pattern]] — **What**: Reduce async delegation batch sizes to improve reliability and throughput.

## Comparisons
- [[topics/dispatched-m2s/wiki/comparisons/owner-exit-success-patterns|owner-exit vs smaller-fan-out outcomes]] — This page compares the failing owner-exit batch against the later successful batches to separate true failure causes from coincidence.

## Queries
- [[topics/dispatched-m2s/wiki/queries/query-index|query-index]] — - `delegation batch outcome lookup`: Given a Hermes batch ID, retrieve dispatched time, fan-out size, role, terminal result, and known transcript path.

