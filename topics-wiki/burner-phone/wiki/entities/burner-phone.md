---
title: burner-phone
created: 2026-09-07
updated: 2026-09-16
type: entity
tags:
  - bot
  - skill
sources:
  - raw/inbox/2026-09-07.md
confidence: high
---

# burner-phone

Topic entity for the **burner-phone** skill: control an Android device with an agent. This page collects the topic's current pains, decisions, and open questions.

## Current focus

- Context-fit ceiling on 28GB hardware: 20.4GB model + 8GB KV at 131K triggers a **507**; active goal is to find the actual maximum context that fits. ^[raw/inbox/2026-09-07.md]
- MTPLX streaming token behavior: sub-token chunks with usage only in the last chunk require usage-based counting instead of chunk tallying. ^[raw/inbox/2026-09-07.md]
- Ornith is the selected local runtime target. The next step is to start it properly and update the config, but this is entangled with port/restart/config-write issues. ^[raw/inbox/2026-09-07.md]
- DFlash2 is downloaded as a 1GB speculative-decoder artifact and needs to be integrated with Ornith for the device; integration config now identified as `--spec-draft-model` + `--ctx-other` + `--hf-repo-draft`, run against the original qwen4 v0.4.0-dev service (`-ngl -c -t`), still unverified after an empty response (reasoning consumed the budget). ^[raw/inbox/2026-09-07.md] ^[raw/inbox/2026-09-15.md]
- GPU-offload root cause (2026-09-15): `-ngl 9999` fails because `CUDA_VISIBLE_DEVICES=1` isn't honored through `su`. ^[raw/inbox/2026-09-15.md]
- Omarchy 27B confirmed working (test echo: "2+2 equals 4, no more.") 2026-09-15; the local runtime probe continues on Ornith. ^[raw/inbox/2026-09-15.md]
|- Runtime rebuild (2026-09-15): `/tmp` was wiped on restart, losing the qwen4 v0.4.0-dev build; checking persistent runtimes and rebuilding. ^[raw/inbox/2026-09-15.md]
|- Fit calculation (2026-09-16): moved from trial 507s to a fit-calc approach over 28GB hardware — `model_size + KV_cache <= tier_size`, comfortable-fit `model_size + 2GB <= tier_size`, check every tier (CPU + Unified). ^[raw/inbox/2026-09-16.md]

## Links

- [[topics-wiki/burner-phone/wiki/entities/ornith|Ornith]]
- [[topics-wiki/burner-phone/wiki/entities/dflash2|DFlash2]]
- [[topics-wiki/burner-phone/wiki/concepts/context-limit-pain|507 / context-fit ceiling on 28GB hardware]]
- [[topics-wiki/burner-phone/wiki/queries/what-runs-on-28gb|What runs on 28GB]]
- [[topics-wiki/burner-phone/wiki/decisions/mtplx-streaming-test-rewrite|Rewrite streaming test to use usage-based token counting]]
- [[topics-wiki/burner-phone/wiki/decisions/select-ornith-as-runtime|Select Ornith as local runtime target]]
- [[topics-wiki/burner-phone/wiki/entities/ornith-config-state|Ornith config and port state]]
