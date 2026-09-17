# merge-topics.py v1.1.0 — DRY RUN 2026-09-02

Plan: `topics/senter/plans/topic-consolidation-2026-09-02.md` (anser audit signed · senter re-confirm ACCEPT · Chris GO 2026-09-02).
Topic dirs now: 63 → after: 20 (50 absorbed, 7 new targets created, 8 kept, 0 unassigned).

## 1. Moves — `absorbed → target` (original goes to `topics/_archive/<absorbed>/`)
- pocket-shop-pricing → pocket-shop
- turbohaul-llmfit → turbofit
- turbohaul-manager → turbofit
- southpaw-turbohaul → turbofit
- sirvir → turbofit
- hermes-android → hermes-agent
- hermes-test-skill → hermes-agent
- herm-sovth → hermes-agent
- sovth-config → hermes-agent
- nous-test → hermes-agent
- test-bot → hermes-agent
- openskills → hermes-agent
- senter-consolidation → senter
- senter-archive → senter
- senter-mcp-server → senter
- senter-alignment-arxivddl → senter
- dev-orch → senter
- hermes-wiki-dashboard → senter-wiki
- sovthpaw-omni-senter-3b → omnisenter-models (NEW topic)
- sovthpaw-omnisenter-base-16b → omnisenter-models (NEW topic)
- sovthpaw-omnistep-12a3b → omnisenter-models (NEW topic)
- sovthpaw-omnistep-new → omnisenter-models (NEW topic)
- sovthpaw-senter-omni-data → omnisenter-models (NEW topic)
- omnistep-fusion → omnisenter-models (NEW topic)
- multimodal-expansion → omnisenter-models (NEW topic)
- omnisenter-blog → omnisenter-models (NEW topic)
- evolutionary-model-merging → evolutionary (NEW topic)
- evolutionary-training → evolutionary (NEW topic)
- ace-step-daw → music (NEW topic)
- jammit → music (NEW topic)
- hermes-music-lora-pipeline → music (NEW topic)
- llmc → music (NEW topic)
- evolutionary-radio → music (NEW topic)
- veiled → music (NEW topic)
- nous-girl → nous-community (NEW topic)
- nous-girl-agent → nous-community (NEW topic)
- nous-discord-archive → nous-community (NEW topic)
- nous-style-guide → nous-community (NEW topic)
- discordsam → nous-community (NEW topic)
- jestur → nous-community (NEW topic)
- southpawin-github-io → youtube (NEW topic)
- benchmark-infographics → youtube (NEW topic)
- dev-coder → dev-tooling (NEW topic)
- dev-review → dev-tooling (NEW topic)
- sidecar → dev-tooling (NEW topic)
- niwa → dev-tooling (NEW topic)
- flavored-nanocode → dev-tooling (NEW topic)
- frieza → legacy-bots (NEW topic)
- chizul → legacy-bots (NEW topic)
- aichess → legacy-bots (NEW topic)

Kept as own topics: anser, klerik, _global, memento, pirouette-framework-core-003, crow, kashik, burner-phone
Unassigned: none (Chris ruled veiled → music, aichess → legacy-bots).

## 2. Wikilinks rewritten: 102 in 4 files (18 in hand-maintained files; the rest in catalogs that are regenerated anyway)
- catalogs/topic-index.md: 42  (regenerated)
- catalogs/fleet-dashboard.md: 42  (regenerated)
- catalogs/agent-roster.md: 9
- topics/_global/.system/agent-roster.md: 9

## 3. `## Absorbed` blocks each target README gains

### pocket-shop
```
## Absorbed
_Consolidated 2026-09-02 per [[topics/senter/plans/topic-consolidation-2026-09-02|topic-consolidation-2026-09-02]]. Originals live verbatim under `topics/_archive/`._

- [[topics/_archive/pocket-shop-pricing/README|pocket-shop-pricing]] — TCGPlayer price lookup system using Hermes browser automation for Pocket-Shop (absorbed 2026-09-02; was DORMANT (since 2026-07-08))
## Repos
| Repo | Link | Status | ⭐ |
|---|---|---|---|
| pocket-shop | [repo](https://github.com/SouthpawIN/pocket-shop) | DORMANT (since 2026-07-08) | 7 |
| pocket-shop-pricing | [repo](https://github.com/SouthpawIN/pocket-shop-pricing) | DORMANT (since 2026-07-08) | 1 |
```

### turbofit
```
## Absorbed
_Consolidated 2026-09-02 per [[topics/senter/plans/topic-consolidation-2026-09-02|topic-consolidation-2026-09-02]]. Originals live verbatim under `topics/_archive/`._

- [[topics/_archive/turbohaul-llmfit/README|turbohaul-llmfit]] — Generate optimized llama-server launch strings and turbohaul-manager manifests using llmfit hardware detection + TurboQuant flag doctrine (absorbed 2026-09-02; was DORMANT (since 2026-07-08))
- [[topics/_archive/turbohaul-manager/README|turbohaul-manager]] — Ollama-shape inference manager using Tom's TurboQuant llama.cpp. FIFO queue + grace + IDLE_HOT hot-hold + model swap on Blackwell. (absorbed 2026-09-02; was DORMANT (since 2026-07-08))
- [[topics/_archive/southpaw-turbohaul/README|southpaw-turbohaul]] — Curated model server for Nous Research community. Fork of turbohaul-manager with AtomicBot llama.cpp (TQ3/TQ4 + MTP + NextN) and Southpaw… (absorbed 2026-09-02; was DORMANT (since 2026-07-26))
- [[topics/_archive/sirvir/README|sirvir]] — Sirvir — GitHub-current TurboFit support for Hermes; installs TurboFit when missing, compares machine fit, answers Q&A, troubleshoots, an… (absorbed 2026-09-02; was ACTIVE)
## Repos
| Repo | Link | Status | ⭐ |
|---|---|---|---|
| turbofit | [repo](https://github.com/SouthpawIN/turbofit) | ACTIVE | 83 |
| turbohaul-llmfit | [repo](https://github.com/SouthpawIN/turbohaul-llmfit) | DORMANT (since 2026-07-08) | 2 |
| turbohaul-manager | [repo](https://github.com/SouthpawIN/turbohaul-manager) | DORMANT (since 2026-07-08) | 1 |
| southpaw-turbohaul | [repo](https://github.com/SouthpawIN/southpaw-turbohaul) | DORMANT (since 2026-07-26) | 7 |
| sirvir | [repo](https://github.com/SouthpawIN/sirvir) | ACTIVE | 27 |
```

### hermes-agent
```
## Absorbed
_Consolidated 2026-09-02 per [[topics/senter/plans/topic-consolidation-2026-09-02|topic-consolidation-2026-09-02]]. Originals live verbatim under `topics/_archive/`._

- [[topics/_archive/hermes-android/README|hermes-android]] — Hermes Agent Android builds (absorbed 2026-09-02; was DORMANT (since 2026-07-14))
- [[topics/_archive/hermes-test-skill/README|hermes-test-skill]] — A test skill for verifying profile-forge works (absorbed 2026-09-02; was DORMANT (since 2026-07-08))
- [[topics/_archive/herm-sovth/README|herm-sovth]] — The Hermes TUI built with OpenTUI (absorbed 2026-09-02; was DORMANT (since 2026-07-14))
- [[topics/_archive/sovth-config/README|sovth-config]] — Southpaw's hermes-agent config toolkit: /reading-list deep-research plugin, profile character cards, ^<profile> background invocation. Di… (absorbed 2026-09-02; was DORMANT (since 2026-07-08))
- [[topics/_archive/nous-test/README|nous-test]] — Test profile for forge verification (absorbed 2026-09-02; was DORMANT (since 2026-07-08))
- [[topics/_archive/test-bot/README|test-bot]] — Creative operations bot — Discord DM companion for image, music, and video generation (absorbed 2026-09-02; was DORMANT (since 2026-07-08))
- [[topics/_archive/openskills/README|openskills]] — Universal skills loader for AI coding agents - npm i -g openskills (absorbed 2026-09-02; was DORMANT (since 2026-01-18))
## Repos
| Repo | Link | Status | ⭐ |
|---|---|---|---|
| hermes-agent | [repo](https://github.com/SouthpawIN/hermes-agent) | ACTIVE | 2 |
| hermes-android | [repo](https://github.com/SouthpawIN/hermes-android) | DORMANT (since 2026-07-14) | 3 |
| hermes-test-skill | [repo](https://github.com/SouthpawIN/hermes-test-skill) | DORMANT (since 2026-07-08) | 0 |
| herm-sovth | [repo](https://github.com/SouthpawIN/herm-sovth) | DORMANT (since 2026-07-14) | 3 |
| sovth-config | [repo](https://github.com/SouthpawIN/sovth-config) | DORMANT (since 2026-07-08) | 17 |
| nous-test | [repo](https://github.com/SouthpawIN/nous-test) | DORMANT (since 2026-07-08) | 1 |
| test-bot | [repo](https://github.com/SouthpawIN/test-bot) | DORMANT (since 2026-07-08) | 0 |
| openskills | [repo](https://github.com/SouthpawIN/openskills) | DORMANT (since 2026-01-18) | 1 |
```

### senter
```
## Absorbed
_Consolidated 2026-09-02 per [[topics/senter/plans/topic-consolidation-2026-09-02|topic-consolidation-2026-09-02]]. Originals live verbatim under `topics/_archive/`._

- [[topics/_archive/senter-consolidation/README|senter-consolidation]] — Mission (Chris, 2026-08-28): Absorb everything from the Linux workstation `senter` into this (absorbed 2026-09-02; was NOTE (no repo))
- [[topics/_archive/senter-archive/README|senter-archive]] — A lightweight, skill-aware AI agent that uses RAG-based capability discovery. (absorbed 2026-09-02; was ARCHIVED)
- [[topics/_archive/senter-mcp-server/README|senter-mcp-server]] — idea-wiki entity `senter-mcp-server` (from github) (absorbed 2026-09-02; was ENTITY (idea-wiki capture))
- [[topics/_archive/senter-alignment-arxivddl/README|senter-alignment-arxivddl]] — idea-wiki entity `Senter-Alignment/arxivddl` (from huggingface) (absorbed 2026-09-02; was ENTITY (idea-wiki capture))
- [[topics/_archive/dev-orch/README|dev-orch]] — Task orchestrator agent for Hermes Agent — decompose and route via Kanban (absorbed 2026-09-02; was DORMANT (since 2026-07-08))
## Repos
| Repo | Link | Status | ⭐ |
|---|---|---|---|
| senter | [repo](https://github.com/SouthpawIN/Senter) | ACTIVE — repo rename agent-wiki → Senter executed 2026-08-29 | 0 |
| senter-consolidation | _(no repo — note (no repo))_ | NOTE (no repo) | — |
| senter-archive | [repo](https://github.com/SouthpawIN/Senter-archive) | ARCHIVED | 6 |
| senter-mcp-server | _(no repo — entity (idea-wiki capture))_ | ENTITY (idea-wiki capture) | — |
| senter-alignment-arxivddl | _(no repo — entity (idea-wiki capture))_ | ENTITY (idea-wiki capture) | — |
| dev-orch | [repo](https://github.com/SouthpawIN/dev-orch) | DORMANT (since 2026-07-08) | 1 |
```

### senter-wiki
```
## Absorbed
_Consolidated 2026-09-02 per [[topics/senter/plans/topic-consolidation-2026-09-02|topic-consolidation-2026-09-02]]. Originals live verbatim under `topics/_archive/`._

- [[topics/_archive/hermes-wiki-dashboard/README|hermes-wiki-dashboard]] — Hermes dashboard tab: browse ~/.hermes/wiki markdown and queue agent-wiki factory tasks (absorbed 2026-09-02; was DORMANT (since 2026-07-15))
## Repos
| Repo | Link | Status | ⭐ |
|---|---|---|---|
| hermes-wiki-dashboard | [repo](https://github.com/SouthpawIN/hermes-wiki-dashboard) | DORMANT (since 2026-07-15) | 1 |
```

### omnisenter-models — NEW: The OmniSenter / OmniStep model family: base models, fusion, multimodal expansion, training data and the model blog.
```
## Absorbed
_Consolidated 2026-09-02 per [[topics/senter/plans/topic-consolidation-2026-09-02|topic-consolidation-2026-09-02]]. Originals live verbatim under `topics/_archive/`._

- [[topics/_archive/sovthpaw-omni-senter-3b/README|sovthpaw-omni-senter-3b]] — idea-wiki entity `sovthpaw/Omni-Senter-3B` (from huggingface) (absorbed 2026-09-02; was ENTITY (idea-wiki capture))
- [[topics/_archive/sovthpaw-omnisenter-base-16b/README|sovthpaw-omnisenter-base-16b]] — idea-wiki entity `sovthpaw/OmniSenter-Base-16B` (from huggingface) (absorbed 2026-09-02; was ENTITY (idea-wiki capture))
- [[topics/_archive/sovthpaw-omnistep-12a3b/README|sovthpaw-omnistep-12a3b]] — idea-wiki entity `sovthpaw/omnistep-12a3b` (from huggingface) (absorbed 2026-09-02; was ENTITY (idea-wiki capture))
- [[topics/_archive/sovthpaw-omnistep-new/README|sovthpaw-omnistep-new]] — idea-wiki entity `sovthpaw/omnistep-new` (from huggingface) (absorbed 2026-09-02; was ENTITY (idea-wiki capture))
- [[topics/_archive/sovthpaw-senter-omni-data/README|sovthpaw-senter-omni-data]] — idea-wiki entity `sovthpaw/senter-omni-data` (from huggingface) (absorbed 2026-09-02; was ENTITY (idea-wiki capture))
- [[topics/_archive/omnistep-fusion/README|omnistep-fusion]] — Fuse Cosmos3-Nano + AceStep into one omni-modal model: see, hear, generate video, generate music, think. (absorbed 2026-09-02; was DORMANT (since 2026-07-08))
- [[topics/_archive/multimodal-expansion/README|multimodal-expansion]] — Add audio, speech, or vision modalities to an existing LLM. Three approaches — LLaVA-style adapter, REAP + expert replacement, EvoMoE-sty… (absorbed 2026-09-02; was DORMANT (since 2026-07-08))
- [[topics/_archive/omnisenter-blog/README|omnisenter-blog]] — OmniSenter blog — a multi-stage agentic MoE with the Ohm self-evolution engine. (absorbed 2026-09-02; was DORMANT (since 2026-07-08))
## Repos
| Repo | Link | Status | ⭐ |
|---|---|---|---|
| sovthpaw-omni-senter-3b | _(no repo — entity (idea-wiki capture))_ | ENTITY (idea-wiki capture) | — |
| sovthpaw-omnisenter-base-16b | _(no repo — entity (idea-wiki capture))_ | ENTITY (idea-wiki capture) | — |
| sovthpaw-omnistep-12a3b | _(no repo — entity (idea-wiki capture))_ | ENTITY (idea-wiki capture) | — |
| sovthpaw-omnistep-new | _(no repo — entity (idea-wiki capture))_ | ENTITY (idea-wiki capture) | — |
| sovthpaw-senter-omni-data | _(no repo — entity (idea-wiki capture))_ | ENTITY (idea-wiki capture) | — |
| omnistep-fusion | [repo](https://github.com/SouthpawIN/omnistep-fusion) | DORMANT (since 2026-07-08) | 2 |
| multimodal-expansion | [repo](https://github.com/SouthpawIN/multimodal-expansion) | DORMANT (since 2026-07-08) | 4 |
| omnisenter-blog | [repo](https://github.com/SouthpawIN/omnisenter-blog) | DORMANT (since 2026-07-08) | 1 |
```

### evolutionary — NEW: Evolutionary ML research — model merging and training (the Darwin family).
```
## Absorbed
_Consolidated 2026-09-02 per [[topics/senter/plans/topic-consolidation-2026-09-02|topic-consolidation-2026-09-02]]. Originals live verbatim under `topics/_archive/`._

- [[topics/_archive/evolutionary-model-merging/README|evolutionary-model-merging]] — Training-free weight-space recombination of LLMs using evolutionary algorithms. Implements the Darwin Family paper (arXiv:2605.14386) met… (absorbed 2026-09-02; was DORMANT (since 2026-07-08))
- [[topics/_archive/evolutionary-training/README|evolutionary-training]] — No description (absorbed 2026-09-02; was DORMANT (since 2026-07-08))
## Repos
| Repo | Link | Status | ⭐ |
|---|---|---|---|
| evolutionary-model-merging | [repo](https://github.com/SouthpawIN/evolutionary-model-merging) | DORMANT (since 2026-07-08) | 19 |
| evolutionary-training | [repo](https://github.com/SouthpawIN/evolutionary-training) | DORMANT (since 2026-07-08) | 6 |
```

### music — NEW: Generative music/audio products: DAW, terminal radio, music LoRA pipeline, lyric companion, evolution radio.
```
## Absorbed
_Consolidated 2026-09-02 per [[topics/senter/plans/topic-consolidation-2026-09-02|topic-consolidation-2026-09-02]]. Originals live verbatim under `topics/_archive/`._

- [[topics/_archive/ace-step-daw/README|ace-step-daw]] — WIP... (absorbed 2026-09-02; was DORMANT (since 2026-07-08))
- [[topics/_archive/jammit/README|jammit]] — infinite ai generated radio in your terminal (absorbed 2026-09-02; was DORMANT (since 2026-07-08))
- [[topics/_archive/hermes-music-lora-pipeline/README|hermes-music-lora-pipeline]] — A Hermes-native pipeline for downloading, processing, captioning, and LoRA fine-tuning music generation models (AceStep/HeartMuLa). (absorbed 2026-09-02; was DORMANT (since 2026-07-08))
- [[topics/_archive/llmc/README|llmc]] — LLMC — LLM + MC. Your lyric and song companion. Hermes Agent profile. (absorbed 2026-09-02; was DORMANT (since 2026-07-08))
- [[topics/_archive/evolutionary-radio/README|evolutionary-radio]] — Continuous-play generative music radio — OmniStep 6B brain + ACE-Step 2B voice, with GEPA prompt evolution and Darwin weight evolution. (absorbed 2026-09-02; was DORMANT (since 2026-07-08))
- [[topics/_archive/veiled/README|veiled]] — Veiled — cosmic prose lyricist & song forge Hermes Agent profile (absorbed 2026-09-02; was DORMANT (since 2026-07-08))
## Repos
| Repo | Link | Status | ⭐ |
|---|---|---|---|
| ace-step-daw | [repo](https://github.com/SouthpawIN/ACE-Step-DAW) | DORMANT (since 2026-07-08) | 0 |
| jammit | [repo](https://github.com/SouthpawIN/jammit) | DORMANT (since 2026-07-08) | 11 |
| hermes-music-lora-pipeline | [repo](https://github.com/SouthpawIN/hermes-music-lora-pipeline) | DORMANT (since 2026-07-08) | 5 |
| llmc | [repo](https://github.com/SouthpawIN/llmc) | DORMANT (since 2026-07-08) | 5 |
| evolutionary-radio | [repo](https://github.com/SouthpawIN/evolutionary-radio) | DORMANT (since 2026-07-08) | 9 |
| veiled | [repo](https://github.com/SouthpawIN/veiled) | DORMANT (since 2026-07-08) | 1 |
```

### nous-community — NEW: Nous community bots, Discord archive, style guide and companions.
```
## Absorbed
_Consolidated 2026-09-02 per [[topics/senter/plans/topic-consolidation-2026-09-02|topic-consolidation-2026-09-02]]. Originals live verbatim under `topics/_archive/`._

- [[topics/_archive/nous-girl/README|nous-girl]] — Hermes Agent profile distribution (absorbed 2026-09-02; was DORMANT (since 2026-07-08))
- [[topics/_archive/nous-girl-agent/README|nous-girl-agent]] — Nous Girl agent + OmniStep Evolution Radio plugin — curated local model pet, multimodal by default, voice + music from the model (absorbed 2026-09-02; was DORMANT (since 2026-07-08))
- [[topics/_archive/nous-discord-archive/README|nous-discord-archive]] — Auto-archived text logs of Nous Research Discord channels (polled every 6h) (absorbed 2026-09-02; was DORMANT (since 2026-07-08))
- [[topics/_archive/nous-style-guide/README|nous-style-guide]] — Distributable Hermes Agent skill: Nous Research brand identity, monochrome design rules, image generation templates (absorbed 2026-09-02; was DORMANT (since 2026-07-08))
- [[topics/_archive/discordsam/README|discordsam]] — An intelligent, context-aware Discord bot powered by local or remote LLMs, featuring RAG, web scraping, TTS, and more. (absorbed 2026-09-02; was DORMANT (since 2026-07-08))
- [[topics/_archive/jestur/README|jestur]] — Creative studio gremlin Discord DM companion for Hermes Agent (absorbed 2026-09-02; was DORMANT (since 2026-07-08))
## Repos
| Repo | Link | Status | ⭐ |
|---|---|---|---|
| nous-girl | [repo](https://github.com/SouthpawIN/nous-girl) | DORMANT (since 2026-07-08) | 1 |
| nous-girl-agent | [repo](https://github.com/SouthpawIN/nous-girl-agent) | DORMANT (since 2026-07-08) | 5 |
| nous-discord-archive | [repo](https://github.com/SouthpawIN/nous-discord-archive) | DORMANT (since 2026-07-08) | 0 |
| nous-style-guide | [repo](https://github.com/SouthpawIN/nous-style-guide) | DORMANT (since 2026-07-08) | 2 |
| discordsam | [repo](https://github.com/SouthpawIN/DiscordSam) | DORMANT (since 2026-07-08) | 1 |
| jestur | [repo](https://github.com/SouthpawIN/jestur) | DORMANT (since 2026-07-08) | 1 |
```

### youtube — NEW: dogeman's content + publishing surfaces (YouTube, personal site, infographics).
```
## Absorbed
_Consolidated 2026-09-02 per [[topics/senter/plans/topic-consolidation-2026-09-02|topic-consolidation-2026-09-02]]. Originals live verbatim under `topics/_archive/`._

- [[topics/_archive/southpawin-github-io/README|southpawin-github-io]] — Southpaw personal site — TOWARDS SELF-IMPROVEMENT. Blog, projects, models, the pet. (absorbed 2026-09-02; was DORMANT (since 2026-07-08))
- [[topics/_archive/benchmark-infographics/README|benchmark-infographics]] — AI model benchmark comparison infographics (absorbed 2026-09-02; was DORMANT (since 2026-07-08))
## Repos
| Repo | Link | Status | ⭐ |
|---|---|---|---|
| southpawin-github-io | [repo](https://github.com/SouthpawIN/southpawin.github.io) | DORMANT (since 2026-07-08) | 1 |
| benchmark-infographics | [repo](https://github.com/SouthpawIN/benchmark-infographics) | DORMANT (since 2026-07-08) | 0 |
```

### dev-tooling — NEW: Coding-assistant experiments: coder/review agents, sidecar, niwa, minimal Claude-Code alternative.
```
## Absorbed
_Consolidated 2026-09-02 per [[topics/senter/plans/topic-consolidation-2026-09-02|topic-consolidation-2026-09-02]]. Originals live verbatim under `topics/_archive/`._

- [[topics/_archive/dev-coder/README|dev-coder]] — Senior backend engineer coding agent for Hermes Agent (absorbed 2026-09-02; was DORMANT (since 2026-07-08))
- [[topics/_archive/dev-review/README|dev-review]] — Code reviewer quality gate agent for Hermes Agent (absorbed 2026-09-02; was DORMANT (since 2026-07-08))
- [[topics/_archive/sidecar/README|sidecar]] — Use sidecar next to CLI agents for diffs, file trees, conversation history, and task management with td (absorbed 2026-09-02; was DORMANT (since 2026-07-08))
- [[topics/_archive/niwa/README|niwa]] — Async conflict-aware spec/planning, for me, you and your LLM/agent (absorbed 2026-09-02; was DORMANT (since 2026-07-08))
- [[topics/_archive/flavored-nanocode/README|flavored-nanocode]] — Minimal Claude Code alternative. Different languages and frameworks flavors (absorbed 2026-09-02; was DORMANT (since 2026-01-19))
## Repos
| Repo | Link | Status | ⭐ |
|---|---|---|---|
| dev-coder | [repo](https://github.com/SouthpawIN/dev-coder) | DORMANT (since 2026-07-08) | 1 |
| dev-review | [repo](https://github.com/SouthpawIN/dev-review) | DORMANT (since 2026-07-08) | 1 |
| sidecar | [repo](https://github.com/SouthpawIN/sidecar) | DORMANT (since 2026-07-08) | 1 |
| niwa | [repo](https://github.com/SouthpawIN/niwa) | DORMANT (since 2026-07-08) | 1 |
| flavored-nanocode | [repo](https://github.com/SouthpawIN/flavored-nanocode) | DORMANT (since 2026-01-19) | 1 |
```

### legacy-bots — NEW: Retired bot profiles and dormant one-off projects with no product continuity (kept for history).
```
## Absorbed
_Consolidated 2026-09-02 per [[topics/senter/plans/topic-consolidation-2026-09-02|topic-consolidation-2026-09-02]]. Originals live verbatim under `topics/_archive/`._

- [[topics/_archive/frieza/README|frieza]] — Galactic Emperor of Discord — server admin agent for Hermes Agent (absorbed 2026-09-02; was DORMANT (since 2026-07-08))
- [[topics/_archive/chizul/README|chizul]] — Hermes Agent profile distribution (absorbed 2026-09-02; was DORMANT (since 2026-07-08))
- [[topics/_archive/aichess/README|aichess]] — No description (absorbed 2026-09-02; was DORMANT (since 2025-07-25))
## Repos
| Repo | Link | Status | ⭐ |
|---|---|---|---|
| frieza | [repo](https://github.com/SouthpawIN/frieza) | DORMANT (since 2026-07-08) | 0 |
| chizul | [repo](https://github.com/SouthpawIN/chizul) | DORMANT (since 2026-07-08) | 1 |
| aichess | [repo](https://github.com/SouthpawIN/AIChess) | DORMANT (since 2025-07-25) | 1 |
```

## 4. session.md moves (absorbed `.system/` → target `.system/session.md`, dated heading)
- pocket-shop-pricing → topics/pocket-shop/.system/session.md  `## 2026-09-02 — absorbed pocket-shop-pricing`  (session.md 0 lines, + continuity; injections.md stays in archive)
- turbohaul-llmfit → topics/turbofit/.system/session.md  `## 2026-09-02 — absorbed turbohaul-llmfit`  (session.md 0 lines, + continuity; injections.md stays in archive)
- turbohaul-manager → topics/turbofit/.system/session.md  `## 2026-09-02 — absorbed turbohaul-manager`  (session.md 0 lines, + continuity; injections.md stays in archive)
- southpaw-turbohaul → topics/turbofit/.system/session.md  `## 2026-09-02 — absorbed southpaw-turbohaul`  (session.md 0 lines, + continuity; injections.md stays in archive)
- sirvir → topics/turbofit/.system/session.md  `## 2026-09-02 — absorbed sirvir`  (session.md 0 lines, + continuity; injections.md stays in archive)
- hermes-android → topics/hermes-agent/.system/session.md  `## 2026-09-02 — absorbed hermes-android`  (session.md 0 lines, + continuity; injections.md stays in archive)
- hermes-test-skill → topics/hermes-agent/.system/session.md  `## 2026-09-02 — absorbed hermes-test-skill`  (session.md 0 lines, + continuity; injections.md stays in archive)
- herm-sovth → topics/hermes-agent/.system/session.md  `## 2026-09-02 — absorbed herm-sovth`  (session.md 0 lines, + continuity; injections.md stays in archive)
- sovth-config → topics/hermes-agent/.system/session.md  `## 2026-09-02 — absorbed sovth-config`  (session.md 0 lines, + continuity; injections.md stays in archive)
- nous-test → topics/hermes-agent/.system/session.md  `## 2026-09-02 — absorbed nous-test`  (session.md 0 lines, + continuity; injections.md stays in archive)
- test-bot → topics/hermes-agent/.system/session.md  `## 2026-09-02 — absorbed test-bot`  (session.md 0 lines, + continuity; injections.md stays in archive)
- openskills → topics/hermes-agent/.system/session.md  `## 2026-09-02 — absorbed openskills`  (session.md 0 lines, + continuity; injections.md stays in archive)
- senter-consolidation → topics/senter/.system/session.md  `## 2026-09-02 — absorbed senter-consolidation`  (session.md 26 lines; injections.md stays in archive)
- senter-archive → topics/senter/.system/session.md  `## 2026-09-02 — absorbed senter-archive`  (session.md 0 lines, + continuity; injections.md stays in archive)
- senter-mcp-server → topics/senter/.system/session.md  `## 2026-09-02 — absorbed senter-mcp-server`  (session.md 3 lines; injections.md stays in archive)
- senter-alignment-arxivddl → topics/senter/.system/session.md  `## 2026-09-02 — absorbed senter-alignment-arxivddl`  (session.md 3 lines; injections.md stays in archive)
- dev-orch → topics/senter/.system/session.md  `## 2026-09-02 — absorbed dev-orch`  (session.md 0 lines, + continuity; injections.md stays in archive)
- hermes-wiki-dashboard → topics/senter-wiki/.system/session.md  `## 2026-09-02 — absorbed hermes-wiki-dashboard`  (session.md 0 lines, + continuity; injections.md stays in archive)
- sovthpaw-omni-senter-3b → topics/omnisenter-models/.system/session.md  `## 2026-09-02 — absorbed sovthpaw-omni-senter-3b`  (session.md 3 lines; injections.md stays in archive)
- sovthpaw-omnisenter-base-16b → topics/omnisenter-models/.system/session.md  `## 2026-09-02 — absorbed sovthpaw-omnisenter-base-16b`  (session.md 3 lines; injections.md stays in archive)
- sovthpaw-omnistep-12a3b → topics/omnisenter-models/.system/session.md  `## 2026-09-02 — absorbed sovthpaw-omnistep-12a3b`  (session.md 3 lines; injections.md stays in archive)
- sovthpaw-omnistep-new → topics/omnisenter-models/.system/session.md  `## 2026-09-02 — absorbed sovthpaw-omnistep-new`  (session.md 3 lines; injections.md stays in archive)
- sovthpaw-senter-omni-data → topics/omnisenter-models/.system/session.md  `## 2026-09-02 — absorbed sovthpaw-senter-omni-data`  (session.md 3 lines; injections.md stays in archive)
- omnistep-fusion → topics/omnisenter-models/.system/session.md  `## 2026-09-02 — absorbed omnistep-fusion`  (session.md 0 lines, + continuity; injections.md stays in archive)
- multimodal-expansion → topics/omnisenter-models/.system/session.md  `## 2026-09-02 — absorbed multimodal-expansion`  (session.md 0 lines, + continuity; injections.md stays in archive)
- omnisenter-blog → topics/omnisenter-models/.system/session.md  `## 2026-09-02 — absorbed omnisenter-blog`  (session.md 0 lines, + continuity; injections.md stays in archive)
- evolutionary-model-merging → topics/evolutionary/.system/session.md  `## 2026-09-02 — absorbed evolutionary-model-merging`  (session.md 0 lines, + continuity; injections.md stays in archive)
- evolutionary-training → topics/evolutionary/.system/session.md  `## 2026-09-02 — absorbed evolutionary-training`  (session.md 0 lines, + continuity; injections.md stays in archive)
- ace-step-daw → topics/music/.system/session.md  `## 2026-09-02 — absorbed ace-step-daw`  (session.md 0 lines, + continuity; injections.md stays in archive)
- jammit → topics/music/.system/session.md  `## 2026-09-02 — absorbed jammit`  (session.md 0 lines, + continuity; injections.md stays in archive)
- hermes-music-lora-pipeline → topics/music/.system/session.md  `## 2026-09-02 — absorbed hermes-music-lora-pipeline`  (session.md 0 lines, + continuity; injections.md stays in archive)
- llmc → topics/music/.system/session.md  `## 2026-09-02 — absorbed llmc`  (session.md 0 lines, + continuity; injections.md stays in archive)
- evolutionary-radio → topics/music/.system/session.md  `## 2026-09-02 — absorbed evolutionary-radio`  (session.md 0 lines, + continuity; injections.md stays in archive)
- veiled → topics/music/.system/session.md  `## 2026-09-02 — absorbed veiled`  (session.md 0 lines, + continuity; injections.md stays in archive)
- nous-girl → topics/nous-community/.system/session.md  `## 2026-09-02 — absorbed nous-girl`  (session.md 0 lines, + continuity; injections.md stays in archive)
- nous-girl-agent → topics/nous-community/.system/session.md  `## 2026-09-02 — absorbed nous-girl-agent`  (session.md 0 lines, + continuity; injections.md stays in archive)
- nous-discord-archive → topics/nous-community/.system/session.md  `## 2026-09-02 — absorbed nous-discord-archive`  (session.md 0 lines, + continuity; injections.md stays in archive)
- nous-style-guide → topics/nous-community/.system/session.md  `## 2026-09-02 — absorbed nous-style-guide`  (session.md 0 lines, + continuity; injections.md stays in archive)
- discordsam → topics/nous-community/.system/session.md  `## 2026-09-02 — absorbed discordsam`  (session.md 0 lines, + continuity; injections.md stays in archive)
- jestur → topics/nous-community/.system/session.md  `## 2026-09-02 — absorbed jestur`  (session.md 0 lines, + continuity; injections.md stays in archive)
- southpawin-github-io → topics/youtube/.system/session.md  `## 2026-09-02 — absorbed southpawin-github-io`  (session.md 0 lines, + continuity; injections.md stays in archive)
- benchmark-infographics → topics/youtube/.system/session.md  `## 2026-09-02 — absorbed benchmark-infographics`  (session.md 0 lines, + continuity; injections.md stays in archive)
- dev-coder → topics/dev-tooling/.system/session.md  `## 2026-09-02 — absorbed dev-coder`  (session.md 0 lines, + continuity; injections.md stays in archive)
- dev-review → topics/dev-tooling/.system/session.md  `## 2026-09-02 — absorbed dev-review`  (session.md 0 lines, + continuity; injections.md stays in archive)
- sidecar → topics/dev-tooling/.system/session.md  `## 2026-09-02 — absorbed sidecar`  (session.md 0 lines, + continuity; injections.md stays in archive)
- niwa → topics/dev-tooling/.system/session.md  `## 2026-09-02 — absorbed niwa`  (session.md 0 lines, + continuity; injections.md stays in archive)
- flavored-nanocode → topics/dev-tooling/.system/session.md  `## 2026-09-02 — absorbed flavored-nanocode`  (session.md 0 lines, + continuity; injections.md stays in archive)
- frieza → topics/legacy-bots/.system/session.md  `## 2026-09-02 — absorbed frieza`  (session.md 0 lines, + continuity; injections.md stays in archive)
- chizul → topics/legacy-bots/.system/session.md  `## 2026-09-02 — absorbed chizul`  (session.md 0 lines, + continuity; injections.md stays in archive)
- aichess → topics/legacy-bots/.system/session.md  `## 2026-09-02 — absorbed aichess`  (session.md 0 lines, + continuity; injections.md stays in archive)

## 5. After: regenerate index.md, catalogs/topic-index.md, catalogs/fleet-dashboard.md; append `## Archived` footer to each archived README pointing at its target.

