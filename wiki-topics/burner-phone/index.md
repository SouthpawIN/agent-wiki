---
title: burner-phone
created: 2026-09-17
updated: 2026-09-17
type: wiki
sources:
  - index.md
  - wiki/
  - raw/inbox/
  - .system/
---

# burner-phone

Last updated: 2026-09-17 | Total pages: 13

---

## INTEGRATIONS

This wiki is fed by:

- **Raw inbox:** `raw/inbox/` — daily cuts from Hermes sessions
- **Sessions:** `.system/sessions/` — full conversation transcripts
- **Wiki pages:** `wiki/` — structured knowledge base

---

## README

### Entities

- [burner-phone](wiki/burner-phone.md) — Topic entity for the **burner-phone** skill: control an Android device with an agent. This page collects the topic's current pains, decisions, and open question
- [DFlash2](wiki/dflash2.md) — DFlash2 is a **speculative decoder** artifact downloaded for use with Ornith. ^[raw/inbox/2026-09-07.md]
- [ornith 1.5 35A3B](wiki/ornith-1.5-35a3b.md) — Active lookup target: a build or source for **ornith 1.5 35A3B** that works with the burner-phone device **and** **DFlash2**. ^[raw/inbox/2026-09-07.md]
- [Ornith config and port state](wiki/ornith-config-state.md) — - Bonsai MLX was observed on **11623**.
- [Ornith](wiki/ornith.md) — Ornith is the local inference/runtime target for this topic's model work. ^[raw/inbox/2026-09-07.md] It is the selected runtime for the burner-phone device.

### Concepts

- [507 / context-fit ceiling on 28GB hardware](wiki/context-limit-pain.md) — Chris reported that a **507 error persists even with a 28GB budget**. ^[raw/inbox/2026-09-07.md] In context, the fail condition is a **20.4GB model plus 8GB KV
- [Streaming returns only 1 token / sub-token MTPLX behavior](wiki/streaming-token-pain.md) — Chris observed that **MTPLX streaming returns only 1 token per chunk** ^[raw/inbox/2026-09-07.md] and then discovered this is structural: *"MTPLX sends sub-toke
- [Token counting preference — count from final usage, not chunks](wiki/token-counting-preference.md) — Chris's preference is to **debug and rewrite the test** so completion is determined by the usage value in the last streaming chunk, not by counting chunks or ch

### Decisions

- [MTPLX chunk-counting must use final usage, not chunk tally](wiki/mtplx-chunk-count-fix.md) — Fix chunk-counting so it does not treat chunks as tokens.
- [Rewrite streaming test to use usage-based token counting](wiki/mtplx-streaming-test-rewrite.md) — Rewrite the streaming test so completion is driven by usage from the final chunk instead of chunk tallying.
- [Select Ornith as local runtime target](wiki/select-ornith-as-runtime.md) — Chris selected Ornith as the local runtime target for this topic and directed that it be started properly and the config updated.

### Queries

- [Find ornith 1.5 35A3B for device and DFlash2](wiki/find-ornith-1.5-35a3b-for-device-and-dflash2.md) — Open request: locate a build or source for **ornith 1.5 35A3B** that is compatible with the current burner-phone device **and** **DFlash2**. ^[raw/inbox/2026-09
- [What runs on 28GB](wiki/what-runs-on-28gb.md) — Open question: what combination of model size, KV size, and context length actually runs inside the 28GB hardware budget in this topic. ^[raw/inbox/2026-09-07.m

---

## SKILLS

Topic skills stored in this wiki:

- **[mtplx-streaming-count](skills-capabilities/mtplx-streaming-count/SKILL.md) — Count streamed tokens from `usage` in the final chunk, not from chunk count or chunk size.

---

## BOTS

Proposed bots:

- **[context-ceiling-lookup](agents/context-ceiling-lookup.md.proposed) — **I see you're hitting a 507 at 131K with 20.4GB model + 8GB KV on 28GB — want a bot that researches the exact maximum context length this hardware/mo
- **[dflash2-integrator](agents/dflash2-integrator.md.proposed) — **I see you're still trying to get DFlash2 speculative decoding working with Ornith — want a bot that runs the `--spec-draft-model` + `--ctx-other` + 
- **[ornith-context-prober](agents/ornith-context-prober.md.proposed) — **I see the fit-calc says Ornith fits at some context — want a bot that then actually runs Ornith at that computed context to confirm the real-world m
- **[ornith-runner](agents/ornith-runner.md.proposed) — **I see you're selecting Ornith as runtime — want a bot that starts it with proper config?**
- **[ornith-runtime-keeper](agents/ornith-runtime-keeper.md.proposed) — **I see Ornith's working build keeps getting lost to `/tmp` wipes and port conflicts — want a keeper bot to pin Ornith to a persistent runtime on a fi


---

## LOOPS

No loops yet.