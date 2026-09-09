# burner-phone — wiki index
> One line per page. The wiki row's CONTEXT section renders this file.
> Last updated: 2026-09-08 | Total pages: 13

## Entities
- [[topics/burner-phone/wiki/entities/burner-phone|burner-phone]] — Topic entity for the **burner-phone** skill: control an Android device with an agent. This page collects the topic's current pains, decisions, and open question
- [[topics/burner-phone/wiki/entities/dflash2|DFlash2]] — DFlash2 is a **speculative decoder** artifact downloaded for use with Ornith. ^[raw/inbox/2026-09-07.md]
- [[topics/burner-phone/wiki/entities/ornith-1.5-35a3b|ornith 1.5 35A3B]] — Active lookup target: a build or source for **ornith 1.5 35A3B** that works with the burner-phone device **and** **DFlash2**. ^[raw/inbox/2026-09-07.md]
- [[topics/burner-phone/wiki/entities/ornith-config-state|Ornith config and port state]] — - Bonsai MLX was observed on **11623**.
- [[topics/burner-phone/wiki/entities/ornith|Ornith]] — Ornith is the local inference/runtime target for this topic's model work. ^[raw/inbox/2026-09-07.md] It is the selected runtime for the burner-phone device.

## Concepts
- [[topics/burner-phone/wiki/concepts/context-limit-pain|507 / context-fit ceiling on 28GB hardware]] — Chris reported that a **507 error persists even with a 28GB budget**. ^[raw/inbox/2026-09-07.md] In context, the fail condition is a **20.4GB model plus 8GB KV 
- [[topics/burner-phone/wiki/concepts/streaming-token-pain|Streaming returns only 1 token / sub-token MTPLX behavior]] — Chris observed that **MTPLX streaming returns only 1 token per chunk** ^[raw/inbox/2026-09-07.md] and then discovered this is structural: *"MTPLX sends sub-toke
- [[topics/burner-phone/wiki/concepts/token-counting-preference|Token counting preference — count from final usage, not chunks]] — Chris's preference is to **debug and rewrite the test** so completion is determined by the usage value in the last streaming chunk, not by counting chunks or ch

## Decisions
- [[topics/burner-phone/wiki/decisions/mtplx-chunk-count-fix|MTPLX chunk-counting must use final usage, not chunk tally]] — Fix chunk-counting so it does not treat chunks as tokens.
- [[topics/burner-phone/wiki/decisions/mtplx-streaming-test-rewrite|Rewrite streaming test to use usage-based token counting]] — Rewrite the streaming test so completion is driven by usage from the final chunk instead of chunk tallying.
- [[topics/burner-phone/wiki/decisions/select-ornith-as-runtime|Select Ornith as local runtime target]] — Chris selected Ornith as the local runtime target for this topic and directed that it be started properly and the config updated.

## Comparisons


## Queries
- [[topics/burner-phone/wiki/queries/find-ornith-1.5-35a3b-for-device-and-dflash2|Find ornith 1.5 35A3B for device and DFlash2]] — Open request: locate a build or source for **ornith 1.5 35A3B** that is compatible with the current burner-phone device **and** **DFlash2**. ^[raw/inbox/2026-09
- [[topics/burner-phone/wiki/queries/what-runs-on-28gb|What runs on 28GB]] — Open question: what combination of model size, KV size, and context length actually runs inside the 28GB hardware budget in this topic. ^[raw/inbox/2026-09-07.m

