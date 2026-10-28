# Ecosystem — every repo that feeds TurboFit

> The TurboFit project is not one repo. This page is the map: what each repo is, whether it is **shipped**, **support**, **side tool**, or **legacy line**, and which vault page carries its knowledge.
> Absorbed 2026-10-28 from each repo's README (see [source map](../raw/sources/2026-10-28-github-consolidation.md)).

## The map

| Repo | Role | Status | Vault page |
| --- | --- | --- | --- |
| [turbofit](https://github.com/SouthpawIN/turbofit) | **The product** — adaptive local-inference runtime + first-class Hermes provider | shipped (v2.4.0) | [turbofit](../wiki/entities/turbofit.md) · hub [README](../README.md) |
| [sirvir](https://github.com/SouthpawIN/sirvir) | Customer service bot (TurboSouth) — install, configure, troubleshoot, upstream tested PRs | support surface, ships inside the TurboFit install | [sirvir](../wiki/entities/sirvir.md) |
| [SALT-core](https://github.com/SouthpawIN/SALT-core) | State-assured latent-transition engine (KV/state ownership, exportable state) | dry-run public export | [salt-core](../wiki/entities/salt-core.md) |
| [model-momento](https://github.com/SouthpawIN/model-momento) | SQLite model database — HF metadata, benchmark runs, notes | active side tool | [model-momento](../wiki/entities/model-momento.md) |
| [benchmark-infographics](https://github.com/SouthpawIN/benchmark-infographics) | Shareable benchmark visuals with sources | content repo | [benchmark-infographics](../wiki/entities/benchmark-infographics.md) |
| [southpaw-turbohaul](https://github.com/SouthpawIN/southpaw-turbohaul) | Curated turbohaul fork — AtomicBot llama.cpp (TQ3/TQ4 + MTP + NextN) + model presets | legacy line | [southpaw-turbohaul](../wiki/entities/southpaw-turbohaul.md) |
| [turbohaul-manager](https://github.com/SouthpawIN/turbohaul-manager) | Ollama-shape manager on Tom's TurboQuant fork — FIFO + grace + IDLE_HOT + swap | legacy line | [turbohaul-manager](../wiki/entities/turbohaul-manager.md) |
| [turbohaul-llmfit](https://github.com/SouthpawIN/turbohaul-llmfit) | Launch-string / manifest generator skill (llmfit + TurboQuant doctrine) | skill repo | [turbohaul-llmfit](../wiki/entities/turbohaul-llmfit.md) |

## Machines and shells

| Thing | What | Where |
| --- | --- | --- |
| Omarchy | Primary GPU server — RTX 3090 ×2, 377 GB RAM, 16 TB; runs Strata (`turbofit-strata.service`) | [tailscale](tailscale.md) |
| MacBook M1 Pro 32 GB | Unified-memory target — the tier that exposed every memory bug | [troubleshooting](troubleshooting.md) · [apple-arm64-unmeasured-gap](apple-arm64-unmeasured-gap.md) |
| Hermes Agent | The provider host — TurboFit registers as `custom:turbofit` | [skill-contract](skill-contract.md) · [remote-hermes-model-server](remote-hermes-model-server.md) |
| agent-wiki vault | This vault — the knowledge home for all of the above | [README](../README.md) |

## Pattern

Three generations of the same idea, in order:

1. **turbohaul** (manager + curated fork + llmfit generator) — hand-tuned TurboQuant flags, hot-hold a model, swap on demand.
2. **TurboFit** — same job, but the machine is inventoried and the *ladder* decides the fit instead of a human writing flags.
3. **Sirvir** — the support layer that carries untested hardware into the ladder, then returns measured results upstream as PRs.

Read the legacy pages when a flag/engine question comes up; read TurboFit when a fit decision comes up.
