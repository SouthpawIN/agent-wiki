---
title: Ornith
created: 2026-09-07
updated: 2026-09-07
type: entities
tags:
  - tool
sources:
  - raw/inbox/2026-09-07.md
confidence: high
---

# Ornith

Ornith is the local inference/runtime target for this topic's model work. ^[raw/inbox/2026-09-07.md] It is the selected runtime for the burner-phone device.

## Selected as runtime

- Ornith is the winner. Let me start it properly and update the config. ^[raw/inbox/2026-09-07.md]
- Chris's explicit preference: reuse Ornith MLX and keep the config aligned with the selected runtime. ^[raw/inbox/2026-09-07.md]

## Known facts

- Ornith MLX server was brought up for testing. ^[raw/inbox/2026-09-07.md]
- Measured throughput: **28.5 tok/s** with Ornith MLX **4-bit**. ^[raw/inbox/2026-09-07.md]
- The tested model under Ornith is **~18GB**, which Chris contrasts with 27B models at **20–25GB**. ^[raw/inbox/2026-09-07.md]
- The smaller model footprint is seen as a way to leave **more room for KV cache** when testing 131K context on 28GB hardware. ^[raw/inbox/2026-09-07.md]
- The active lookup target is **ornith 1.5 35A3B**, requested specifically for the burner-phone device and DFlash2. ^[raw/inbox/2026-09-07.md]
- The 507 context-fit ceiling is still under investigation; Ornith is part of the live attempt to find the actual maximum context that fits. ^[raw/inbox/2026-09-07.md]
- Tested fallback: the model runs with `-ngl 0` (all on CPU); a previous attempt timed out before this restart. ^[raw/inbox/2026-09-07.md]
- 131K context testing is pending a full rerun after the `-ngl 0` fallback success. ^[raw/inbox/2026-09-07.md]
- Startup path is entangled with port/restart/config-write issues: Bonsai MLX occupied **11623**, Hermes direct config writes were blocked, and a patch attempt was made before restart+config update. ^[raw/inbox/2026-09-07.md]
- **Contested:** one log line claims Ornith MLX is *"confirmed working at 131K context"* ^[raw/inbox/2026-09-07.md], but the surrounding state still lists 131K as pending and unfinished, so that claim is not treated as verified. ^[raw/inbox/2026-09-07.md]

## Configuration state

- Hermes recorded direct config edits as blocked, then attempted a patch route; later entries say restart and update are still intended. ^[raw/inbox/2026-09-07.md]
- Port conflict evidence: Bonsai MLX was observed on **11623**, and Ornith MLX was restarted on a different port. ^[raw/inbox/2026-09-07.md]

## Open questions

- Has ornith **1.5 35A3B** been located for the burner-phone device and DFlash2?
- Did the 131K context test with Ornith complete successfully after the `-ngl 0` restart?
- Is the Hermes config updated after the patch/restart sequence?
- Is the downloaded DFlash2 build integrated with the Ornith 131K test?

## Related

- [[topics/burner-phone/wiki/queries/find-ornith-1.5-35a3b-for-device-and-dflash2|Find ornith 1.5 35A3B for device and DFlash2]]
- [[topics/burner-phone/wiki/entities/dflash2|DFlash2]]
- [[topics/burner-phone/wiki/decisions/select-ornith-as-runtime|Select Ornith as local runtime target]]
- [[topics/burner-phone/wiki/concepts/context-limit-pain|507 / context-fit ceiling on 28GB hardware]]
- [[topics/burner-phone/wiki/queries/what-runs-on-28gb|What runs on 28GB]]
