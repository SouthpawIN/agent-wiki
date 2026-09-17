# what-mean — wiki index
> One line per page. The wiki row's CONTEXT section renders this file.
> Last updated: 2026-09-15 | Total pages: 10

## Entities
- [[topics/what-mean/wiki/entities/local-27b-model|Local 27B model]] — The local 27B-parameter large language model Chris runs on his laptop to power Hermes. ^[raw/inbox/2026-09-06.md]
- [[topics/what-mean/wiki/entities/ornith-model|Ornith model]] — Chris reports "Ornith" running at 226 tokens per second in Hermes. ^[raw/inbox/2026-09-07.md]

## Concepts
- [[topics/what-mean/wiki/concepts/duplicate-downloads|Duplicate downloads]] — Chris flags a duplicate-download risk after Hermes reports a model as "downloaded" when it is already installed and running. ^[raw/inbox/2026-09-07.md] He says:
- [[topics/what-mean/wiki/concepts/model-downloads|Model downloads]] — On 2026-09-15 at 11:37 Hermes reports that model downloads are progressing well, with the Mac download at ~17GB and the Omarchy download at ~21GB of a ~21GB mod
- [[topics/what-mean/wiki/concepts/tokens-per-second|Tokens per second]] — A throughput metric Chris uses to judge the local 27B model running Hermes. He asks for tok/s during inference and treats it as evidence the setup is working. ^

## Decisions
- [[topics/what-mean/wiki/decisions/benchmark-methodology|Benchmark methodology — reasoning-first]] — Chris's standing preference for how to benchmark the local 27B / Ornith models: test at the context length the model will actually run at in Hermes, so the benc
- [[topics/what-mean/wiki/decisions/follow-through|Follow-through on requests]] — Chris expects requested work to be completed, not just acknowledged. At 11:50 he says: "you need to do everything that I asked. I mean, like you are not doing w

## Comparisons


## Queries
- [[topics/what-mean/wiki/queries/benchmark-readme-fetch-2026-09-07|Benchmark README fetch — 2026-09-07]] — At 14:46 Hermes notes that benchmark data was not available in JSON and switched to fetching the README containing the benchmark table. ^[raw/inbox/2026-09-07.m
- [[topics/what-mean/wiki/queries/benchmark-reasoning-tokens|Benchmark reasoning token count — 2026-09-15]] — At 12:31 on 2026-09-15, in response to Hermes reporting that downloads are progressing, Chris corrects the benchmark approach: "No, I want reasoning. I told you
- [[topics/what-mean/wiki/queries/tps-benchmark-2026-09-06|TPS benchmark — 2026-09-06]] — At 19:40 Chris asks, "What's your tokens per second?" regarding the local 27B model on his laptop powering Hermes. Hermes replies at 21:50 with 9 tok/s for 500 

