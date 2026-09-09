---
title: burner-phone
created: 2026-09-07
updated: 2026-09-07
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
- DFlash2 is downloaded as a 1GB speculative-decoder artifact and needs to be integrated with Ornith for the device; no verified integration is recorded yet. ^[raw/inbox/2026-09-07.md]

## Links

- [[topics/burner-phone/wiki/entities/ornith|Ornith]]
- [[topics/burner-phone/wiki/entities/dflash2|DFlash2]]
- [[topics/burner-phone/wiki/concepts/context-limit-pain|507 / context-fit ceiling on 28GB hardware]]
- [[topics/burner-phone/wiki/queries/what-runs-on-28gb|What runs on 28GB]]
- [[topics/burner-phone/wiki/decisions/mtplx-streaming-test-rewrite|Rewrite streaming test to use usage-based token counting]]
- [[topics/burner-phone/wiki/decisions/select-ornith-as-runtime|Select Ornith as local runtime target]]
- [[topics/burner-phone/wiki/entities/ornith-config-state|Ornith config and port state]]
