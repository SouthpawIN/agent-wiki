---
title: session-state
updated: 2026-08-27
type: session
---

# Live Session State — turbofit setup

Read this FIRST each turn. This is the working state of the concurrent setup+design effort.
Updated every turn. Ideas below the line are ready to LAUNCH with async agents.

## Machine
Apple M1 Pro, 32 GB unified, macOS 26.5.2. Metal backend. Repo at ~/turbofit (d6e4ff2).
Python 3.12 venv at ~/turbofit/.venv (pyyaml, cmake). Scripts run via `.venv/bin/python`.

## Completed (verified)
1. Clone + venv (fix #3 workaround)
2. `set auto` -> hardware-24gb / local-bonsai-65536 (stale rung — see fixes)
3. Metal prism-llama.cpp built+SHA-verified (rev 9ca265a5, binary sha 3237b095)
   — JANITOR AUDIT 2026-08-27: no llama-server/llama-cli binary found on disk
   (~/turbofit has no build dir; nothing in ~/Models); runtime NOT present — rebuild needed
4. Unleashed UD-Q3_K_XL downloaded+SHA-verified (12.31 GiB, outsourc-e rev 67a9992) — verified on disk
5. UD-IQ3_XXS (10.21 GiB) also down (group-level download, fix #6) — verified on disk

## Agents RUNNING (deleg_9f9b062c, spawned 2026-08-27)
- A PR-fixes (sa-0): branch fix/macos-vault-audit — fixes 1-6, tests, no push
- B Speedometer (sa-1): branch feat/speedometer-gauge — plugin.js gauge rebuild
- C Live-refit (sa-2): branch feat/live-refit — policy.py fit function, expansion_mode option
- D Vault-janitor (sa-3): vault audit/sync (mechanical only)
Agent E (Obsidian plugin) NOT spawned — blocked on Hermes interface contract decision.
Results will re-enter chat when all four finish; then: merge/verify branches, run controller.

## Agent status (checked 13:20)
- A PR-fixes (sa-0): STILL RUNNING (25 min, working in worktree ~/turbofit-vault-audit,
  branch fix/macos-vault-audit, commit 39272f1: Bonsai->Unleashed rungs done; tests fail
  only due to PYTHONPATH needed - verified separately)
- B Speedometer: DONE - commit 9893fb9, plugin.js parses (node --check OK), already
  merged into feat/live-refit lineage
- C Live-refit: DONE - commit 89914ad (fit_check.py 112 lines, policy.py +96, tests 24+35 pass)
- D Vault-janitor: DONE (silent completion, no errors returned)
Consolidated child report re-enters when A finishes. Branches verified locally.

## Merged + verified (13:35)
- feat/live-refit <- fix/macos-vault-audit merged (one test conflict resolved:
  stale-Bonsai refusal path gone now that profile is fixed + live-refit active)
- 72 tests pass (policy, runtime_service, runtime_profile, recommend)
- set auto now selects local-unleashed-q3kxl-65536 (fix verified end-to-end)
- Building mainline-llama.cpp metal runtime (Unleashed rung uses mainline pinned rev,
  Prism was for Bonsai/DFlash2) — background proc_4030041247ae
- NEXT: controller --once -> curl 127.0.0.1:8091/v1/models -> Unleashed live

## LIVE (14:12)
- Gateway :8091 UP (turbofit-gateway/2.0, graceful degradation, /main stall-while-loading)
- Main: qwen3-8-27b-unleashed-ud-q3-k-xl, state=ready, rung local-unleashed-q3kxl-262144
  (262K context, shared-main aux, port 11606, mainline metal llama.cpp rev 1c3c9674)
- Chat completion VERIFIED: model answers via active:main (reasoning model, thinking tokens first)
- Hermes provider config: provider: custom:turbofit / model: auto (or active:main)
- Full chain complete: fingerprint -> Fit List (fixed 24gb.yaml) -> Unleashed rung -> native
  metal llama-server -> gateway. Live-refit + speedometer branch merged (72 tests pass).

## LIVE (later 2026-08-27)
- Plugin `turbofit` (v2.4.0, git source) ENABLED in Hermes: `hermes plugins doctor` passes,
  tools turbofit_status/turbofit_configure registered. turbofit_status OK (full runtime JSON).
- turbofit_configure TOOL timed out at 420s -> root cause: `huggingface_hub` missing from
  .venv (scripts/download-artifacts imports it); fix #7 added to queue.md. Workaround:
  installed hf_hub into .venv + ran apply_configuration via Hermes venv python (23s, ok).
- Hermes config NOW: model.provider=custom:turbofit, model.default=auto, fallbacks =
  Nous free (ox-alpha, step-3.7-flash). restart_required=true (desktop restart pending user).

## CRITICAL (user directive 2026-08-27): fulfill self-install promises
- Obsidian freeze root-caused: ran from AppTranslocation (dmg). Installed to /Applications, relaunched.
- Hermes provider block ADDED manually (providers.turbofit -> :8091). install.sh never did it.
- Controller/gateway NOT a launchd service — not automatic, dies on reboot. macOS installer missing.
- Full audit + acceptance list: .system/critical-gaps.md. Next agent: G self-installer.

## In flight
- mmproj LANDED (audit 2026-08-27): mmproj-Unleashed-f16.gguf (0.87 GiB) complete in
  ~/Models/storage/gguf/Qwen3.8-27B-Unleashed/ — all 3 group files now on disk
- NEXT: controller --once -> curl 127.0.0.1:8091/v1/models -> serve Unleashed
  (force rung; do NOT let stale Bonsai rung serve)
- Audit 2026-08-27 (branches): local = main + feat/speedometer-gauge (checked out,
  desktop/plugin.js modified); fix/macos-vault-audit + feat/live-refit NOT yet created;
  no runtime binary built

## Fixes (GitHub PR candidates, vault .system/queue.md is source of truth)
0. ARCH: Fit List = single authority + constant live fit-check (contraction re-fits;
   expansion = one-rung-at-a-time DEFAULT, jump-to-fit as menu option)
1. 24gb.yaml serves retired Bonsai (HIGH)
2. allowed_lineup Apple >=24GB -> MLX misroute (HIGH, symptom of 0)
3. No pyproject/requires-python (3.9 crashes)
4. Evidence Linux-only paths; darwin/arm64 unmeasured class
5. install-native-runtimes assumes cmake
6. download-models group-level only

## Design (speedometer plugin menu) — see skills-capabilities/speedometer-menu-design.md
- Gauge: static arc = Fit List tiers; needle = live pressure probe; readout = model/aux/ctx
- Themable via --tf-* CSS tokens inheriting Hermes --ui-* palette; theme packs later
- plugin.js is 781-line single file, no build step — keep it that way
- OPEN: settings placement (palette vs drawer vs route); theme picker now or later

---
## Ready to launch (async agents, once user says go)
A. PR-fixes agent — implement fixes 1-6 in ~/turbofit on a branch, tests, no push (per
   llama.cpp-style AGENTS.md norms: no auto-push/PR without user)
B. Speedometer agent — rebuild desktop/plugin.js gauge per design skill (needs runtime live
   for realistic data; can mock status JSON meanwhile)
C. Live-refit agent — policy.py _first_fitting_contraction -> fit function f(usable_mem)
   + expansion policy option; needs design sign-off on menu placement first (blocks on A/B?)
E. Obsidian-plugin agent — Hermes for Obsidian, Cursor-style: Hermes client in Obsidian, agent-wiki layout as default. manifest.json + main.js, no build step. Needs: Hermes gateway/CLI interface contract before coding.
D. Vault-janitor agent — keep .system/queue.md + session.md synced to actual repo state

## 2026-09-02 — absorbed turbohaul-llmfit
_Merged into `turbofit` by merge-topics.py v1.1.0. Verbatim originals: `wiki-topics/_archive/turbohaul-llmfit/.system/`._

### continuity.md (from turbohaul-llmfit)

# Continuity — turbohaul-llmfit

Raw understanding, 2026-08-27 (from GitHub metadata + README):
- Generate optimized llama-server launch strings and turbohaul-manager manifests using llmfit hardware detection + TurboQuant flag doctrine
- Language: None; 2 stars; last push 2026-07-08; original work.
- (Edit this file to correct my understanding; I never overwrite user-edited lines.)

## 2026-09-02 — absorbed turbohaul-manager
_Merged into `turbofit` by merge-topics.py v1.1.0. Verbatim originals: `wiki-topics/_archive/turbohaul-manager/.system/`._

### continuity.md (from turbohaul-manager)

# Continuity — turbohaul-manager

Raw understanding, 2026-08-27 (from GitHub metadata + README):
- Ollama-shape inference manager using Tom's TurboQuant llama.cpp. FIFO queue + grace + IDLE_HOT hot-hold + model swap on Blackwell.
- Language: Python; 1 stars; last push 2026-07-08; original work.
- (Edit this file to correct my understanding; I never overwrite user-edited lines.)

## 2026-09-02 — absorbed southpaw-turbohaul
_Merged into `turbofit` by merge-topics.py v1.1.0. Verbatim originals: `wiki-topics/_archive/southpaw-turbohaul/.system/`._

### continuity.md (from southpaw-turbohaul)

# Continuity — southpaw-turbohaul

Raw understanding, 2026-08-27 (from GitHub metadata + README):
- Curated model server for Nous Research community. Fork of turbohaul-manager with AtomicBot llama.cpp (TQ3/TQ4 + MTP + NextN) and Southpaw's hand-picked models.
- Language: Python; 7 stars; last push 2026-07-26; original work.
- (Edit this file to correct my understanding; I never overwrite user-edited lines.)

## 2026-09-02 — absorbed sirvir
_Merged into `turbofit` by merge-topics.py v1.1.0. Verbatim originals: `wiki-topics/_archive/sirvir/.system/`._

### continuity.md (from sirvir)

# Continuity — sirvir

Raw understanding, 2026-08-27 (from GitHub metadata + README):
- Sirvir — GitHub-current TurboFit support for Hermes; installs TurboFit when missing, compares machine fit, answers Q&A, troubleshoots, and writes tested upstream PRs.
- Language: Python; 27 stars; last push 2026-08-24; original work.
- (Edit this file to correct my understanding; I never overwrite user-edited lines.)
