---
title: dispatched-m2s
created: 2026-09-17
updated: 2026-09-17
type: wiki
sources:
  - index.md
  - wiki/
  - raw/inbox/
  - .system/
---

# dispatched-m2s

Last updated: 2026-09-17 | Total pages: 11

---

## INTEGRATIONS

This wiki is fed by:

- **Raw inbox:** `raw/inbox/` — daily cuts from Hermes sessions
- **Sessions:** `.system/sessions/` — full conversation transcripts
- **Wiki pages:** `wiki/` — structured knowledge base

---

## README

### Entities

- [delegation batch deleg_56809b77](wiki/delegation-batch-56809b77.md) — A Hermes async delegation batch that completed successfully on `2026-09-07 10:08`, demonstrating the larger-fan-out success pattern noted after earlier owner-ex
- [delegation batch deleg_7418fbf4](wiki/delegation-batch-7418fbf4.md) — A Hermes async delegation batch reported complete on `2026-09-16 20:26` (message ID `20260914_200308_f9b029`, simulation `0.19`). The batch fanned out to `5` su
- [delegation batch deleg_dc36df32](wiki/delegation-batch-dc36df32.md) — A Hermes async delegation batch that completed successfully on `2026-09-07 10:39`, recorded immediately after the successful `deleg_56809b77` run.
- [delegation batch deleg_e76115bb](wiki/delegation-batch-e76115bb.md) — A Hermes async delegation batch dispatched at `2026-09-07 05:36:30` and reported from `2026-09-07 05:42`. The batch consisted of `1` subagent with role `leaf`;
- [dispatched-m2s](wiki/dispatched-m2s.md) — The topic covering Hermes async delegation batches that do not complete successfully. The current known instance is [[entities/delegation-batch-e76115bb|batch d
- [Hermes state.db message 20260903_001447_7bc70a](wiki/hermes-message-20260903-001447-7bc70a.md) — A Hermes state.db message filed under a recurring message ID `20260903_001447_7bc70a` — the same ID that previously carried the delegation-owner-exit timeout er

### Concepts

- [delegation owner exit timeout](wiki/delegation-timeout.md) — A failure mode in which the delegation owner process exits before recording a terminal result for its leaf subagent batch. The observable result is the error st

### Decisions

- [batch size mitigation pattern](wiki/batch-size-mitigation-pattern.md) — **What**: Reduce async delegation batch sizes to improve reliability and throughput.
- [TurboFit per-model wiki pages and consolidation](wiki/turbofit-model-pages.md) — **What**: Use this wiki as the source for building TurboFit — give each model its own page, collect setup-relevant nuggets about each model, and consolidate red

### Comparisons

- [owner-exit vs smaller-fan-out outcomes](wiki/owner-exit-success-patterns.md) — This page compares the failing owner-exit batch against the later successful batches to separate true failure causes from coincidence.

### Queries

- [query-index](wiki/query-index.md) — - `delegation batch outcome lookup`: Given a Hermes batch ID, retrieve dispatched time, fan-out size, role, terminal result, and known transcript path.

---

## SKILLS

No topic skills yet.

---

## BOTS

Proposed bots:

- **[delegation-auditor](agents/delegation-auditor.md.proposed) — **I see you're trying to separate owner-exit failures from batch-size effects — want a bot that instruments Hermes delegation batches to capture model
- **[turbofit-builder](agents/turbofit-builder.md.proposed) — **I see you're building TurboFit from this wiki — want a bot that reads each model's page and builds/updates the TurboFit config from the setup nugget
- **[turbofit-consolidator](agents/turbofit-consolidator.md.proposed) — **I see redundant notes piling up as each model page gets built — want a bot that periodically consolidates sat-down redundancy across the model pages


---

## LOOPS

Proposed loops:

- **[delegation-daily-digest](triggers-loops/delegation-daily-digest.md.proposed) — owner: looker · cadence: review yesterday's batches each morning · status: SUGGESTED
- **[turbofit-page-sync](triggers-loops/turbofit-page-sync.md.proposed) — owner: turbosovth · cadence: every 2h · status: SUGGESTED
