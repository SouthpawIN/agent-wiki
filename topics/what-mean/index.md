---
title: what-mean
created: 2026-09-17
updated: 2026-09-17
type: wiki
sources:
  - index.md
  - wiki/
  - raw/inbox/
  - .system/
---

# what-mean

Last updated: 2026-09-15 | Total pages: 10

---

## INTEGRATIONS

This wiki is fed by:

- **Raw inbox:** `raw/inbox/` — daily cuts from Hermes sessions
- **Sessions:** `.system/sessions/` — full conversation transcripts
- **Wiki pages:** `wiki/` — structured knowledge base

---

## README

### Entities

- [Local 27B model](wiki/local-27b-model.md) — The local 27B-parameter large language model Chris runs on his laptop to power Hermes. ^[raw/inbox/2026-09-06.md]
- [Ornith model](wiki/ornith-model.md) — Chris reports "Ornith" running at 226 tokens per second in Hermes. ^[raw/inbox/2026-09-07.md]

### Concepts

- [Duplicate downloads](wiki/duplicate-downloads.md) — Chris flags a duplicate-download risk after Hermes reports a model as "downloaded" when it is already installed and running. ^[raw/inbox/2026-09-07.md] He says:
- [Model downloads](wiki/model-downloads.md) — On 2026-09-15 at 11:37 Hermes reports that model downloads are progressing well, with the Mac download at ~17GB and the Omarchy download at ~21GB of a ~21GB mod
- [Tokens per second](wiki/tokens-per-second.md) — A throughput metric Chris uses to judge the local 27B model running Hermes. He asks for tok/s during inference and treats it as evidence the setup is working. ^

### Decisions

- [Benchmark methodology — reasoning-first](wiki/benchmark-methodology.md) — Chris's standing preference for how to benchmark the local 27B / Ornith models: test at the context length the model will actually run at in Hermes, so the benc
- [Follow-through on requests](wiki/follow-through.md) — Chris expects requested work to be completed, not just acknowledged. At 11:50 he says: "you need to do everything that I asked. I mean, like you are not doing w

### Queries

- [Benchmark README fetch — 2026-09-07](wiki/benchmark-readme-fetch-2026-09-07.md) — At 14:46 Hermes notes that benchmark data was not available in JSON and switched to fetching the README containing the benchmark table. ^[raw/inbox/2026-09-07.m
- [Benchmark reasoning token count — 2026-09-15](wiki/benchmark-reasoning-tokens.md) — At 12:31 on 2026-09-15, in response to Hermes reporting that downloads are progressing, Chris corrects the benchmark approach: "No, I want reasoning. I told you
- [TPS benchmark — 2026-09-06](wiki/tps-benchmark-2026-09-06.md) — At 19:40 Chris asks, "What's your tokens per second?" regarding the local 27B model on his laptop powering Hermes. Hermes replies at 21:50 with 9 tok/s for 500

---

## SKILLS

No topic skills yet.

---

## BOTS

Proposed bots:

- **[benchmark-bot](agents/benchmark-bot.md.proposed) — **I see you're benchmarking your local 27B/Ornith model — want a bot that runs fair benchmarks at the context length Hermes actually uses, so it captu
- **[download-watch-bot](agents/download-watch-bot.md.proposed) — **I see model downloads just finished (Omarchy ~21GB) — want a bot that watches model downloads and confirms completion without re-downloading, so it 


---

## LOOPS

No loops yet.