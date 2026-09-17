# senter-consolidation — One Hermes, One Source of Truth

**Mission** (Chris, 2026-08-28): Absorb everything from the Linux workstation `senter` into this
Mac's agent wiki + Hermes, dedupe redundant early attempts, then wipe senter → install Omarchy →
fresh Hermes. End state: ONE Hermes reachable from all devices, Mac = orchestrator/home control,
senter = workhorse, Surface Duo 2 = mobile.

## Fleet facts (verified 2026-08-28)

| Device | Tailnet IP | Role | State |
|---|---|---|---|
| christophers-macbook-pro | 100.81.37.77 | Home control (lights/TV) + wiki orchestrator | Active, this machine |
| senter | 100.84.195.22 | Main workhorse (Ubuntu 24.04.3, kernel 7.0.0-30, 17T disk 90% full) | Active — to be wiped+rebuilt |
| surface-duo-2 | 100.79.15.54 | Mobile connection | Reachable |
| chriss-s10 | 100.93.96.90 | ? | Offline |
| localhost-0 | 100.99.15.71 | ? | Offline |

Tailnet: `tail6ff78b.ts.net`, Tailscale account Christopher Hardwick.
senter SSH: `sovthpaw@100.84.195.22` (password auth working; password shared in chat — ROTATE).

## What lives on senter (surveyed 2026-08-28)

### Hermes on senter (`~/.hermes`, 13 GB)
- **memories/** (12K, ~20 rich entries): Turbofit API fallback bypasses, scaling-watcher rules,
  media-tool consent policy, GOOP north-star (optimize Chris's life, named hook mechanisms only,
  wiki live-view = Herm sidecar first, topic colors = operating state), Turbofit native ladder
  (8G=Maple TQ2_0 64K/128K; 16G=Unleashed UD-IQ3_XXS+DFlash2; 24–95G=UD-Q3_K_XL+DFlash2;
  aux=Ornith oQ4e/oQ8e MTP 40G+; GRM retired), Sirvir spec, TurboFit self-configuring contract,
  bench discipline (LiteLLM banned; real-context ladders; GPU residency; honest medians),
  Chris comms prefs (metric-first, no preamble, concept-based org, aggressive dedupe,
  git repos > installed dirs; live-rambler mode = preserve intent, build top-level plans, no
  execution until approved), Discord tokens self-managed, lyric journal ~/lyrics/journal.md.
- **skills-capabilities/** (78M, 57 skills): heavy turbofit cluster (turbofit, -adaptive-runtime,
  -architecture, -graceful-degradation, -runtime-policy, -troubleshooting, -validation, -wiki),
  southpaw-models, local-llm-fleet-management, herm/herm-tui-radio/agent-hub, omni-va-local-server,
  youtube-playlist-to-acestep-lora, song-catalog, evolutionary-training, micro-agent-pipeline,
  multi-agent-shared-checkpoint, long-running-process-detachment, continuity-ingestion, yuanbao…
- **sessions/** 448 files (225M) + sessions.json gateway routing (5 Discord threads).
- **cron/**: executions.db, jobs.json (1 active job), ticker heartbeats — LIVE system.
- eikons (1.4M), kanban.db (860K), checkpoints, backups (59M), continuity/stream.jsonl
  (synthetic filler — verify before absorbing), hermes-agent repo inside .hermes.
- Also `~/.hermes-phone-agent`, `~/.hermes_history`.
- Live processes: note_taker.py serve, lemond (lemonade 11.5.1), ollama serve, llama.cpp.

### Projects (`~/projects`, 1.3 TB, ~80 entries, 49 git repos)
Heavyweights: evolutionary-training (874G), AI-ML (205G), ds4 (83G), LLM-Infra (39G),
ACE-Step-1.5 (37G), Media (12G), turbofit (5G, 3 recent commits: Nous fallback catalog fix,
retired-model fallback preserve, sparse-MoE expert offload + Qwen3.8-Flash-Next; dirty:
plugin.js, plugin_tools.py, sparse-moe-offload ref).
Active-flagged: turbofit, sirvir, agent-wiki (GOOP source: goop-whitepaper, spec.md,
SENTER.md/SENTER_AGENT.md, INTEGRATED_STATUS.md), herm-tui, hermes-wiki-dashboard,
turbohaul-manager(+upstream), omnistudio-daw, ACE-Step/music pipeline cluster.
Redundancy clusters (dedupe targets): hermes-agent vs hermes-agent-local vs herm-source vs
herm-sandbox vs hermes-agent-plugin-guard; pocket-shop vs pocket_shop; turbofit-promo vs
turbofit-update-promo vs turbofit_qwen_pr vs turbofit-automation; hermes-browser-extension vs
-inspect; hermes-wiki-dashboard vs -inspect; llama.cpp-glm5 vs llama.cpp-latest;
turbohaul-manager vs -upstream; nous-girl vs nous-girl-agent; senter vs senter-omni;
kashi vs kashik; evolutionary-{training,radio,model-merging-local}.
Non-git (scratch/legacy): Agents, AI-ML, asher, autonomous-orchestrator, dani-projects,
diffusers-minimax-h3, discord-automation, Finance, h3-comedy-reels-local, h3-storyboard-practice,
Hardware, herm-sandbox, kashi, llama.cpp-glm5, LLM-Infra, Media, Mobile, night-shift-cryptids,
omni-fusion, profile-banner, rap-lora-training, Research, senter-omni, southpaw,
southpaw-breakdown-video, southpaw-docs, southpawin.github.io, transformers-h3, turbofit-automation,
turbofit-promo, turbofit_qwen_pr, turbofit-update-promo, videos, Web.

### Data outside projects
- `~/Models` **8.3 TB** (52 entries: ace-step, hf, hf_cache, LTX-2/LTX-Video, nemotron,
  ik_llama-models-backup, ai-toolbox-models-backup, MODEL-REGISTRY.md, repos…) — too big to
  move wholesale; registry-documented, selective.
- `~/models` 358G. `~/idea-wiki` 79M (agent-wiki precursor: concepts/, entities/, queries/,
  raw/, SCHEMA.md). `~/obsidian-sync`, `~/lyrics/journal.md`, `~/stt-server`, `~/research`,
  `~/Sync`, `~/venvs`, `~/Data`, `~/docs`, stray FAL video iterations (alligator_tank v1-3),
  display-debug logs, bench-fleet.sh, build_idea_wiki.py.
- Gateway: turbofit-gateway/2.0 at https://senter.tail6ff78b.ts.net (nginx), /main/v1/ +
  /aux/v1/ → llama.cpp :11606, model `qwen3-8-27b-unleashed-unleashedq3kxl262144-main`
  (state ready, runtime hardware-48gb, ~70 tok/s predicted, draft 32/47 accepted).

## Phase plan

- **P1 ABSORB** (this phase): pull senter Hermes (memories, skills, sessions, cron, kanban,
  eikons, config refs) + wiki-relevant repo docs into vault + Mac backup. Dedupe pass → merge
  decisions into topic READMEs. DO NOT move 8.3T Models — document registry, transfer on demand.
- **P2 SAFE-COPY**: full backup of senter's unique data to Mac/external before any wipe
  (target: git repos incl. dirty turbofit worktree, .hermes minus caches, idea-wiki,
  obsidian-sync, lyrics, Finance/personal dirs).
- **P3 WIPE+OMARCHY**: Chris-approved wipe, Omarchy install, fresh Hermes.
- **P4 FEDERATE**: senter = workhorse Hermes, Mac = orchestrator/home control, Duo = mobile;
  one source of truth in vault; cross-device session continuity.

## Session state
- [x] SSH access working (password; key-install pending to deprecate password)
- [x] Full survey done (this README is the absorption v1)
- [ ] Pull senter memories/skills-capabilities/session inventory into Mac vault
- [ ] Dedupe matrix for redundancy clusters → Chris approves merges
- [ ] Backup P2 sweep
- [ ] Turbofit dirty worktree on senter: commit or stash before anything touches it
- [ ] SSH key auth setup; password rotation

## Queue
- [SKILLS] Merge senter's 8 turbofit-* skills with Mac's turbofit skill set (Mac side thinner).
- [SKILLS] Absorb southpaw-models, local-llm-fleet-management, herm* skills into vault skill registry.
- [AGENTS] Decide fate of running cron job on senter (executions.db live) before wipe.
- [LOOPS] continuity/stream.jsonl looks synthetic/fixture — verify before ingesting.


## Archived
Archived 2026-09-02 — absorbed into [[topics-wiki/senter/README|senter]] by merge-topics.py v1.1.0. Nothing here was deleted or rewritten.
