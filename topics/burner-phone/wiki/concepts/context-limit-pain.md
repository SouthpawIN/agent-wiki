---
title: 507 / context-fit ceiling on 28GB hardware
created: 2026-09-07
updated: 2026-09-07
type: concept
tags:
  - pain
  - question
sources:
  - raw/inbox/2026-09-07.md
confidence: high
---

# 507 / context-fit ceiling on 28GB hardware

Chris reported that a **507 error persists even with a 28GB budget**. ^[raw/inbox/2026-09-07.md] In context, the fail condition is a **20.4GB model plus 8GB KV at 131K** — which the physical hardware cannot hold. ^[raw/inbox/2026-09-07.md] The stated goal is to find the actual maximum context that fits. ^[raw/inbox/2026-09-07.md]

Chris said: *"The 507 error persists even with 28GB budget. The physical hardware can't hold 20.4GB model + 8GB KV at 131K. Let me find the actual maximum context that fits."* ^[raw/inbox/2026-09-07.md]

- What "done" looks like: a known-working context length for this hardware/model/KV combination, not another trial 507.
- Standing constraint in this topic: prefer root cause over band-aid, and keep everything live/visible rather than a hidden workaround.
- Chris's current phrasing: *"Let me find the actual maximum context that fits."* ^[raw/inbox/2026-09-07.md]
- Ornith offers an alternative path: the tested model is **~18GB**, smaller than 20–25GB 27B models, so more KV cache may fit on the same 28GB hardware. ^[raw/inbox/2026-09-07.md]
- A CPU fallback (`-ngl 0`) succeeded where a previous attempt timed out, so the failure mode is not simply offload capability. ^[raw/inbox/2026-09-07.md]
- Server timeout was observed again after the CPU fallback restart, reinforcing that config/process stability is part of the context-test path, not only model fit. ^[raw/inbox/2026-09-07.md]

## Supersedes

Trial-and-error context increases without measuring the physical memory ceiling.

## Open questions

- Is the 507 triggered by model-load OOM, KV alloc failure, or combined RAM+swap pressure?
- What is the maximum context length achievable with Ornith on this hardware?
- Did the 131K test complete after the `-ngl 0` restart?
- Has the config been updated to start Ornith properly after selecting it as the winner?

## Links

- [[topics/burner-phone/wiki/entities/burner-phone|burner-phone]]
- [[topics/burner-phone/wiki/queries/what-runs-on-28gb|What runs on 28GB]]
- [[topics/burner-phone/wiki/decisions/select-ornith-as-runtime|Select Ornith as local runtime target]]
