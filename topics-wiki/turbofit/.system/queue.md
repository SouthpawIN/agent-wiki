# Queue — turbofit

## [SKILLS]
- [ ] dflash2-fork-flag-boundary — distilled 2026-09-07 20:13 → skills-capabilities/dflash2-fork-flag-boundary/SKILL.md (auto-applied)
- [ ] turbo-model-store-cleanup — distilled 2026-09-07 17:12 → skills-capabilities/turbo-model-store-cleanup/SKILL.md (auto-applied)
- [ ] candidate-quant-comparison — distilled 2026-09-07 09:43 → skills-capabilities/candidate-quant-comparison/SKILL.md (auto-applied)
- [ ] turbo-artifact-download-spec — distilled 2026-09-07 08:45 → skills-capabilities/turbo-artifact-download-spec/SKILL.md (auto-applied)
- [ ] mtplx-32gb-macos-tuning — distilled 2026-09-07 01:02 → skills-capabilities/mtplx-32gb-macos-tuning/SKILL.md (auto-applied)
- [ ] turbo-fit-evidence-capture — distilled 2026-09-07 00:30 → skills-capabilities/turbo-fit-evidence-capture/SKILL.md (auto-applied)
- [ ] maple-mlx-server-runtime — distilled 2026-09-06 22:41 → skills-capabilities/maple-mlx-server-runtime/SKILL.md (auto-applied)
- [~] turbofit-macos-setup — in progress: macOS (M1 Pro) setup runbook; see `skills-capabilities/turbofit-macos-setup.md`

## [AGENTS]
- [ ] orchestrator — SUGGESTED 2026-09-08 12:10: I see you want automatic evidence capture for all TurboFit route changes — want a bot that triggers verification wheneve → agents/orchestrator.md.proposed
- [ ] turbofit-route-stabilizer — SUGGESTED 2026-09-08 12:10: I see Hermes is still flipping to cloud models despite your intent — want a bot that locks the fallback_providers chain  → agents/turbofit-route-stabilizer.md.proposed
- [ ] candidate-benchmark-scout — SUGGESTED 2026-09-07 09:43: I see you're queuing Dirk, Nail, and Tiel-Coder with a Q3 preference — want a bot that benchmarks each candidate on 65K  → agents/candidate-benchmark-scout.md.proposed
- [ ] turbofit-runtime-scout — SUGGESTED 2026-09-07 08:45: I see you're assembling Nail/Dirk/Tiel/Ornith candidates — want a bot that tracks each one's actual Hermes path: downloa → agents/turbofit-runtime-scout.md.proposed
- [ ] turbofit-evidence-capture — SUGGESTED 2026-09-07 08:27: Want me to capture a desktop_preview of the Hermes window showing the Ornith MLX runtime is stable at 65K context with o → agents/turbofit-evidence-capture.md.proposed
- [ ] turbofit-launcher — SUGGESTED 2026-09-07 08:27: Want me to lock in Ornith MLX 4-bit as the main provider with 65K context, and Unleashed+DFlash2 as the 131K long-contex → agents/turbofit-launcher.md.proposed
- [ ] turbofit-benchmark — SUGGESTED 2026-09-07 06:30: I see you're collecting Apple Silicon runtime speed data — want a bot that runs controlled tok/s benchmarks on the downl → agents/turbofit-benchmark.md.proposed
- [ ] mtplx-runtime-scout — SUGGESTED 2026-09-07 01:02: I see you're trying to pin a stable MTPLX config — want a bot that finds the supported runtime knob for memory budgeting → agents/mtplx-runtime-scout.md.proposed
- [ ] turbofit-verifier — SUGGESTED 2026-09-06 22:41: I see you’re testing end-to-end TurboFit stability — want a bot that runs a live 131K compression probe against :11606/: → agents/turbofit-verifier.md.proposed
- [ ] *(empty)*

## [PLUGINS]
- [ ] obsidian-plugin — **Hermes for Obsidian (Cursor-for-Obsidian)**: Hermes Agent client inside Obsidian with agent-wiki structure as the DEFAULT mode. Chat panel to Hermes, .system/ queue editor, agent spawning, vault-aware context, optional speedometer tab. Shares gauge design with desktop speedometer plugin. (user 2026-08-27)
- [ ] speedometer-menu — redesign desktop/plugin.js: TurboFit Check rendered as a speedometer gauge (needle = memory pressure / tier position); themable via CSS custom properties (theme packs, not hardcoded colors)
- [ ] plugin-menu-contract — decide menu structure before building: what lives in the speedometer view vs palette commands (open / shift up/down / theme / update) vs settings
- [ ] expansion-option — one-rung-at-a-time recovery is the DEFAULT (per user); expose "jump-to-fit" as an option in the plugin menu (expansion policy toggle: conservative | direct)

## [SKILLS]
- [ ] turbofit-self-install — ONE-COMMAND fresh-Mac installer: deps, clone, venv, build, download, set auto, launchd services (macOS), Hermes config wiring. Acceptance in .system/critical-gaps.md. (Also upstream PR material.)

## [LOOPS]
- [ ] candidate-quant-comparator — SUGGESTED 2026-09-08 12:10: Want me to check the next candidate model's HuggingFace page for Q3 near-base-quality notes? → triggers-loops/candidate-quant-comparator.md.proposed
- [ ] turbofit-memory-threshold-monitor — SUGGESTED 2026-09-08 12:10: Want me to watch for prefill_admission_shed events that indicate memory pressure before OOM kills? → triggers-loops/turbofit-memory-threshold-monitor.md.proposed
- [ ] hermes-model-change-detector — SUGGESTED 2026-09-08 12:10: Want me to watch for unexpected model switches and alert you before they affect your work? → triggers-loops/hermes-model-change-detector.md.proposed
- [ ] 131k-attempt-blocker — SUGGESTED 2026-09-07 09:43: Want a watch that warns when a large candidate is queued or launched for 131K on this 32 GB box? → triggers-loops/131k-attempt-blocker.md.proposed
- [ ] candidate-65k-benchmark-sweep — SUGGESTED 2026-09-07 09:43: Want a daily sweep that benchmarks the next queued candidate at 65K and updates the engine report? → triggers-loops/candidate-65k-benchmark-sweep.md.proposed
- [ ] turbo-context-budget-watch — SUGGESTED 2026-09-07 08:45: Want a repeatable check that compares Hermes prompt size against the stable 65K cap before each request so 131K only hap → triggers-loops/turbo-context-budget-watch.md.proposed
- [ ] turbofit-health-check — SUGGESTED 2026-09-07 08:27: Do you want a cron to verify both Ornith and Unleashed servers remain available at their expected ports? → triggers-loops/turbofit-health-check.md.proposed
- [ ] turbofit-runtime-watch — SUGGESTED 2026-09-07 08:27: Want me to periodically test all three runtime paths (Ornith, Unleashed+DFlash2, MTPLX at 65K) and record tok/s metrics? → triggers-loops/turbofit-runtime-watch.md.proposed
- [ ] turbofit-memory-monitor — SUGGESTED 2026-09-07 08:27: Want me to watch for memory overcommit and automatically log when KV cache usage approaches the 32GB limit? → triggers-loops/turbofit-memory-monitor.md.proposed
- [ ] mtplx-telemetry-watch — SUGGESTED 2026-09-07 06:30: Want a loop that samples MTPLX `/metrics` and `/health` during live Hermes loads and flags prefill admission shed or pre → triggers-loops/mtplx-telemetry-watch.md.proposed
- [ ] turbofit-candidate-discovery — SUGGESTED 2026-09-07 06:30: Want a loop that scans HuggingFace and known feeds for new Qwen/Ornith/Unleashed/DFlash2 artifacts matching the TurboFit → triggers-loops/turbofit-candidate-discovery.md.proposed
- [ ] compression-timeout-watch — SUGGESTED 2026-09-06 22:41: Watch Hermes compression timeout errors and correlate them to active model/provider state. → triggers-loops/compression-timeout-watch.md.proposed
- [ ] mac-memory-watch — SUGGESTED 2026-09-06 22:41: Watch your box memory while TurboFit runs, so we can catch server kills before you see them. → triggers-loops/mac-memory-watch.md.proposed
- [ ] upstream-watch — periodic check of SouthpawIN/turbofit for macOS/Apple fixes to pull

*(Setup fixes recorded 2026-08-27 — candidates for GitHub PRs, priority order (0 = architectural root cause, 1-2 are symptoms):)*
0. **ARCH — consolidate scan/recommend/Fit-List into one authority; fallback chain = the Fit List** (user directive). Today there are three divergent sources of truth: (a) `allowed_lineup.check_local_options()` (hardcoded heuristic ladder: Apple >=24GB -> MLX 6-bit), (b) `runtime-profiles/<N>gb.yaml` Turbofiles (Bonsai rungs), (c) `references/successful-runtime-profiles.json` (evidence table). The Auto path (`selection.py::_auto` -> canonical Turbofile rungs) never consults the Fit List winners; `turbofit-runtime-recommend` consults allowed_lineup + evidence but is only advisory. FIX: make `turbofit-list` output the single ordered ladder; `set auto` maps hardware fingerprint -> Fit List tier -> top evidence-backed profile for that tier; Turbofile rungs become contraction policy only (context/aux steps), not model identity. Bonsai retirement then falls out naturally.
   Live-refit (user directive): contraction must RE-RUN the fit check under current pressure
   (usable memory from pressure_probe), not walk a static rung ladder. 32GB -> 16GB usable
   re-fits to Unleashed UD-IQ3_XXS; 8GB -> Maple/Ornith; exhausted -> API. policy.py's
   _first_fitting_contraction() walks pre-baked rung requirements only — replace the rung
   ladder with a fit function f(available_memory) -> tier profile. Hysteresis/dwell logic
   stays; only the target-selection input changes from static rungs to live re-fit.
   _first_fitting_contraction() walks pre-baked rung requirements only — replace the rung
   ladder with a fit function f(available_memory) -> tier profile. Hysteresis/dwell logic
   stays; only the target-selection input changes from static rungs to live re-fit.
1. **HIGH — hardware-24gb profile still serves retired Bonsai**: runtime-profiles/24gb.yaml rungs are all `local-bonsai-*`; `set auto` on M1 Pro 32GB selected `local-bonsai-65536`. Bonsai was retired as the 8GB default in v2.4 (CHANGELOG/README) but never replaced in the 24GB profile. Fit List authority says 24GB+ shared memory = Unleashed UD-Q3_K_XL. Fix: swap 24gb.yaml rungs to Unleashed Q3_K_XL (evidence exists: qwen-3-8-27b-unleashed-ud-q3-k-xl-auto-262k, 37.99 tok/s baseline).
2. **HIGH — allowed_lineup.py vs Fit List on Apple**: `apple_mlx_main()` routes >=24GB Apple to OrcaRouter Uncensored MLX 6-bit; Fit List says Unleashed UD-Q3_K_XL. Superseded by fix 1 (profile-level misroute happens first), but same root cause.
3. Declare Python >=3.10 (no pyproject/requires-python; system 3.9 crashes on `int | str` in routes.py)
4. successful-runtime-profiles.json evidence has Linux-only paths (/home/sovthpaw); recommend --fit-only on darwin/arm64 returns [] (correct per spec, but no Apple on-box validation path exists)
5. install-native-runtimes assumes cmake; no prereq check
6. download-models.py only exposes group-level selection; single-quant selection pulls siblings too
7. **HIGH — plugin `turbofit_configure` tool hangs/times out (420s) on a fresh Hermes venv**: `apply_configuration()` -> `ensure_recommended_models()` exec's `scripts/download-artifacts`, which does `from huggingface_hub import hf_hub_download`. `huggingface_hub` is NOT in the repo's `.venv` (skill says install only `pyyaml cmake`) nor guaranteed in the Hermes agent venv. Two-part failure: (a) setup path under-documents the dep, so the plugin's configure tool dies; (b) the tool call surfaces as a silent 420s timeout rather than a fast error, because plugin_tools.py:110's HTTP timeout of 300s masks the import crash. FIX (PR): declare/install `huggingface_hub` in setup + add fast-fail (import check at tool entry with a clear error) + lower timeout/propagate. Workaround applied locally 2026-08-27: `uv pip install --python .venv/bin/python huggingface_hub` and run `apply_configuration(primary=True, fallback_chain=NOUS_FREE_FALLBACK_CHAIN)` via the Hermes venv python — succeeded in 23s, config now primary custom:turbofit.
8. **FIXED 2026-08-28 — Unknown provider 'turbofit' on fresh macOS profiles**: `apply_configuration` and `serve_tailnet` only wrote `providers.turbofit` to the default `~/.hermes/config.yaml`. Fresh macOS profiles (`turbosovth`, `sirvir`) keep their own `~/.hermes/profiles/<name>/config.yaml`, so any session launched from those profiles failed at agent init with `Unknown provider 'turbofit'` / `Unknown provider 'custom:turbofit'` — the exact error reported on 2026-08-28. **Fix**: added `_save_configuration_to_all_homes` (fans canonical provider to every `hermes_homes()`), `ensure_provider_registered` heal (registers minimal provider in every home missing it, called from `__init__.register`), and updated `product_ops.serve_tailnet` to use the same fan-out. Manual heal applied to `turbosovth` profile; verified `resolve_runtime_provider('turbofit')` now succeeds from both homes and gateway `GET /v1/models` returns `auto` on the M1 Pro (Metal, 32GB). Commit `4cc6b06` on `feat/live-refit`.

---

## [TURBOSOVTH — TurboFit push 2026-08-30] — PLAN (written for Senter, DM pipeline drops bodies)

### 1. TurboSouth rebrand — Sirvir → TurboSouth

**Final repo target (for confirmation): SouthpawIN/turbosouth** (rename SouthpawIN/sirvir, GitHub keeps redirect). Alternative if Chris wants namespacing: SouthpawIN/turbofit-turbosouth — default proposal is SouthpawIN/turbosouth.

**Scope (I own repo/README/imagery, Senter routes profile via klerik):**
- Assets: turbofit/assets currently has turbofit-hero.png but TurboSouth hero still points to sirvir URL `https://raw.githubusercontent.com/SouthpawIN/sirvir/main/assets/sirvir-hero.png`. Create new `turbosouth-hero.png` with **sovthpaw pet** (long auburn hair, black sunglasses, sleeveless black vest pink strap) as default avatar. Update refs in `turbofit/README.md`, `dashboard/`, `desktop/`. Gallery slug `s0uthpaw`, alias `turbofit`.
- Repo rename: GitHub rename + update `turbofit/plugin.yaml`, `distribution.yaml`, `SKILL.md` (`install_sirvir: true` docs), and `README` manual bootstrap `git clone https://github.com/SouthpawIN/sirvir.git` → `https://github.com/SouthpawIN/turbosouth.git`. Keep redirect for old clones.
- README overhaul: rewrite TurboSouth section to reflect actual job — *TurboFit install support, machine-fit comparison, Q&A with citations, troubleshooting, tested upstream PRs*. Current README already says "TurboSouth (formerly Sirvir) is Turbofit's customer service agent" — expand to match spec + add install-with-TurboFit guarantee.
- Install with TurboFit + self-registration: verify `hermes plugins install --enable https://github.com/SouthpawIN/turbofit.git` installs TurboSouth + auto-selects pet `s0uthpaw` for default home + TurboSouth profile via `turbofit_configure(install_sirvir=true)` / `after-install.md`. Pet selection is `hermes pets install s0uthpaw --select`. No memory/user-state wipe on update.
- Profile/SOUL: I do not edit SOUL/profile — Senter routes via klerik per instruction. I will hand diff for repo/README/imagery + pet verification; klerik applies soul/profile rename.
- Verification: fresh `hermes plugins install --enable` on clean profile → `turbofit_status` shows TurboSouth installed + pet selected; `hermes bots list` includes turbosouth; `curl http://127.0.0.1:8091/v1/models` returns `auto`.

**Next step:** confirm SouthpawIN/turbosouth is final; I then execute asset + README + plugin.yaml/distribution updates.

### 2. Cleaned dedicated-lane roster — audit + proposal

**Current truth:**
- Code: `src/turbofit_runtime/turbofit_list.py: TIERS = (8, 16, 24, 48, 64, 96, 200, 300)` — 8 lanes.
- Docs: `docs/turbofit-list.md` same 8 rows, only **48 GB has winner** (`Qwen 3.8 27B Unleashed UD-Q3_K_XL + Route auxiliary, 262K, intelligence 46.875, TPS 39.39`); other 7 are `pending benchmarks`. `references/hardware-tier-report.json` tiers all `catalog-candidates-only` except 48 GB `physically-validated`.
- Check spec: `docs/turbofit-check.md` + `SKILL.md` 2.4 model authority describes more classes than lanes cover: dedicated VRAM, unified/Apple Silicon (8–15 GB Maple, 16–23 GB Ornith), 32 GB class referenced, 96 GB+ etc.

**Gaps/duplicates flagged:**
- Missing **32 GB** — SKILL.md 2.4 references 32 GB class, but no lane. Fleet/Apple unified often land 32–36 GB. Candidate at 8 GB needs 22 GB recommended, 16 GB needs 30 GB — indicates candidate vs lane mismatch.
- Coarse 96→200→300 jumps — missing 128/192 common workstation/server configs (host+accelerator totals; current_hardware `usable_memory_mb 427 GB` → native 48). 200/300 are very coarse.
- 24 GB vs 48 GB both use `UD-Q3_K_XL` family with different contexts — if both validate, Check must keep lane isolation by exact hardware fingerprint, not model name.

**Proposed cleaned roster (needs approval before code change): 8, 16, 24, 32, 48, 64, 96, 128, 192, 256, 384 (11 lanes).** Keep 200/300 as aliases to 192/256 if needed for backwards compat. Covers Apple unified 8/16/32, consumer dedicated 8/12/16/24, workstation 48/96/128, server 192/256/384. Prioritize campaigns: 48→32→24→64→16→96→128 based on fleet frequency. Alternative minimal proposal if Chris wants to keep 8-lane shape: just add 32 + 128 (so 10 lanes: 8,16,24,32,48,64,96,128,200,300).

**Execution after approval:** (i) update `TIERS` tuple, (ii) regenerate `references/hardware-tier-report.json` with new tiers, (iii) `scripts/turbofit-list` rebuild → `references/turbofit-list.json` + `docs/turbofit-list.md`, (iv) audit `docs/turbofit-check.md` + `docs/campaigns.md` promotion criteria (lexicographic: intelligence →128K→30TPS→262K→50TPS→1M→fastest), (v) verify `scripts/turbofit-hardware-tiers` renders new levels.

### 3. Tiel Coder audition — dedicated clean benchmark lanes

**Status:** pending source identifier (HF repo/URL) from Chris. Past benchmark campaigns never landed, so lane setup is its own deliverable.

**Design (no execution until identifier lands):**
- Isolated lanes `TIERS_TIEL` separate from TurboFit main `TIERS` — same `campaign.py` + `turbofit-intelligence-campaign` harness, but evidence under `references/results/tiel-coder/` with hardware-fingerprint-bound evidence, resumable state, `status`/`run-one`/`--orchestrator` support.
- Prevents contamination of current 48 GB winner. Slots unknown candidate in: candidate config `tiel-coder--*--64k/128k/262k` with its own `hardware-tier-report-tiel.json` + `turbofit-list-tiel.md`.
- Deliverable: lane structure + harness wiring + docs; benchmark run waits on identifier.

**Awaiting:** confirm repo name + lane roster, then I execute 1+2. Forward Tiel Coder identifier when you have it.

---

## [SENTER — APPROVAL RECORD 2026-08-30]
- Repo name FINAL: **SouthpawIN/turbosouth** — replace sirvir with turbosouth in ALL places (user directive).
- Identity framing (user verbatim intent): "TurboFit is the whole project, TurboSouth is the dedicated Bot to assist installing, configuring, and sending fixes upstream to turbofit."
- Lane roster APPROVED: full 11-lane proposal (8,16,24,32,48,64,96,128,192,256,384; 200/300 aliases). Campaign priority 48→32→24→64→16→96→128.
- Tiel Coder: lane structure may proceed; benchmark runs blocked on source identifier from Chris.
- Profile/SOUL rename for turbosovth/sirvir → route via klerik (pending turbosovth's diff handoff).

## [TURBOSOVTH — EXECUTION COMPLETE 2026-08-31]

**1. TurboSouth rebrand (FINAL: SouthpawIN/turbosouth) — DONE**
- README: hero URL `sirvir/main/assets/sirvir-hero.png` → `turbosouth/main/assets/turbosouth-hero.png`, clone `SouthpawIN/sirvir.git` → `SouthpawIN/turbosouth.git` (`cd turbosouth`), identity one-liner added: "TurboFit is the whole project. TurboSouth is the dedicated bot that assists with installing, configuring, and sending fixes upstream to TurboFit." Pet description now includes vest/pink strap, slug `s0uthpaw`.
- `assets/turbosouth-hero.png` created (placeholder copy of turbofit-hero.png; sovthpaw auburn hair/sunglasses/vest art to be finalized).
- `plugin_tools.py`: `TURBOSOUTH_GIT` → `https://github.com/SouthpawIN/turbosouth.git`
- `SKILL.md`: install_sirvir now notes alias install_turbosouth, tiers line updated to 11 lanes.
- `references/auto-update.yaml` + `skills-capabilities/turbofit/references/auto-update.yaml`: `sirvir: ~/projects/sirvir` → `turbosouth: ~/projects/turbosouth`
- `__init__.py` comment `turbosovth/sirvir` → `turbosovth/turbosouth`
- `dashboard/plugin_api.py` handles both `install_sirvir` and `install_turbosouth`
- SOUL/profile: prepared diff at `/tmp/turbosouth-soul-diff-for-klerik.md` for klerik (references/SOUL.md + skills-capabilities/.../SOUL.md + profiles/sirvir → turbosouth rename). Not applied directly per protection rail.
- Remaining sirvir in `CHANGELOG.md` historical + `product_ops.py:66` legacy key + `tests/` legacy aliases retained for backwards compat (GitHub redirect).

**2. Cleaned dedicated lanes (11) — DONE**
- TIERS updated in 4 places: `src/turbofit_runtime/turbofit_list.py`, `src/turbofit_runtime/tier_report.py`, `src/turbofit_runtime/tier_tournament.py`, `src/turbofit_runtime/wiki.py` → `(8, 16, 24, 32, 48, 64, 96, 128, 192, 256, 384)` + `TIERS_ALIASES {200:192, 300:256}`
- `intelligence.py` validation updated to 11-tier allowlist.
- Runtime profiles: created `32gb.yaml` (1x32), `128gb.yaml` (4x32), `192gb.yaml` (4x48), `256gb.yaml` (8x32), `384gb.yaml` (8x48) — derived from nearest existing.
- `references/hardware-tier-tournaments.json` rebuilt to 11 tiers (8,16,24,32,48,64,96,128,192,256,384) — 200/300 replaced.
- `references/turbofit-list.json` rebuilt to 11 levels — only 48 GB winner, others pending.
- `docs/turbofit-list.md` rendered 11 rows + alias note.
- `references/hardware-tier-report.json` — 200/300 aliases retained; 32/128/384 tiers will populate on next hardware probe (tournaments + profiles ready). Legacy 200/300 yaml kept for alias.
- Check/campaigns audit: promotion lexicographic unchanged, now applies to 11 lanes. Audit done.

**3. Tiel Coder lanes — DONE (structure, awaiting identifier)**
- `references/tiel-coder-lanes.json` created (11 isolated tiers, status awaiting-identifier, harness config, evidence root `references/results/tiel-coder/`, campaign priority same as main).
- `references/results/tiel-coder/` directory created.
- Benchmark runs blocked pending Chris HF identifier.

**Verification**
- Lane table: `docs/turbofit-list.md` shows 11 rows, 48 GB winner intact, others pending.
- `references/turbofit-list.json` levels == 11, hardware_level_gb list verified: 8,16,24,32,48,64,96,128,192,256,384.
- `references/hardware-tier-tournaments.json` tiers == 11.
- `assets/turbosouth-hero.png` exists.
- README turbosouth references verified via grep.
- Fresh-profile install / /v1/models=auto / bots list: code now points to SouthpawIN/turbosouth + pet s0uthpaw; manual verification on clean profile pending (blocked by single-query mode python execution — will verify on next interactive shell).

**Klerik handoff:** `/tmp/turbosouth-soul-diff-for-klerik.md` ready for Senter → klerik.
**Next:** Chris Tiel Coder identifier → slot candidate into tiel-coder lanes.

## [SENTER — FULL-EFFORT TURBOFIT PUSH 2026-08-30] (Chris directive: "full effort, do not cut corners")
1. README overhaul: TurboSouth help callout moved UP top; condense 280-line README (quick-start first, detail → docs/ links); replace all 19 sirvir refs (verified: lines 93,107,126,128,139,223-235,253 + hero URL).
2. TPS estimates for ALL 11 lanes — table in docs (measured | derived | estimated evidence classes). Existing evidence: 48GB=39.39 TPS measured; M5 Max 128GB MLX=17.97 extended (PR #30); MTPLX 66.5/85.6 TPS (PR #31); 2x24 TPS doc exists.
3. Sandbox-per-tier testing (user approved): isolated bench env per lane; Docker/Daytona/Modal; CPU/RAM tiers automatable now, GPU tiers need real hardware → publish "hardware needed" queue. 
4. PR triage: #29 macOS py3.9 (priority — top user error), #28 Maple contexts, #30 Apple MLX managed runtime, #31 MTPLX (stacked on #30), Issue #24 SGLang 96GB.
0. BLOCKER FIRST: main has 15 failing tests + broken docs link gate (per PR #30/#31 baseline notes) — fix before everything.
Order: main fix → rename+README → PR verdicts → TPS table → sandbox design.

## [TIEL CODER IDENTIFIED 2026-08-30] (Chris clue: "same crew who makes Dirk 27B")
- Model: **peculiar-ragdoll/Tiel-Coder-35B-A3B** (Saga team, same as Dirk 27B). 35B MoE, ~3.4B active (256 experts, 8 routed/token), base ornith-ai/Ornith-1.5-35B-A3B, Sharp template, temp 1.0/top_p 0.95/top_k 20 (agentic 0.6).
- Variants pinned 2026-08-31 from HF cards: GGUF (peculiar-ragdoll/Tiel-Coder-35B-A3B-GGUF), GGUF-MTP (…-GGUF-MTP, +0.9 GB head), MLX-oQ4e (…-MLX-oQ4e 21 GB), MLX-oQ4e-MTP. imatrix 183 MiB, mmproj-BF16.gguf 903 MB shared.
- Lane fit verified: UD-Q4_K_XL 22.4 GB → 24 GB dedicated (snug) / 32 GB unified comfortable; Q5 26.6 → 32 GB pick; MTP +0.9 GB → 32 GB spec-decode lane (--spec-type draft-mtp); MLX oQ4e → Apple unified 32/128 GB vision-capable.
- Audition: isolated TIERS_TIEL lanes per turbosovth's design — pin artifact SHAs, candidate configs, run what fleet hardware allows. No contamination of 48 GB Unleashed winner.

## [TURBOSOVTH — TIEL CODER PINNED 2026-08-31]
- Identifier landed via senter: peculiar-ragdoll/Tiel-Coder-35B-A3B + 4 repos (GGUF, GGUF-MTP, MLX-oQ4e, MLX-oQ4e-MTP). Verified cards via HF web_extract — sizes: Q2 12.3 / IQ3_XXS 13.2 / Q3 16.8 / IQ4_XS 17.7 / Q4_K_S 20.9 / Q4_K_XL 22.4 / Q5 26.6 / Q6 31.8 / Q8 38.5; MTP adds 0.9 GB pinned block; MLX oQ4e 21 GB.
- Rewrote `references/tiel-coder-lanes.json` v1 → identifier-pinned: full artifact table, candidate_configs_per_lane (8=not-viable <12.3 GB, 16=IQ3_XXS 13.2, 24=Q4_K_XL 22.4 primary + IQ4_XS/Q4_S alternates, 32=Q5 26.6 + MTP 23.3/27.5, 48=Q6 31.8, 96=Q8 38.5, 128=MLX oQ4e 21 unified, 192/256/384=Q8 1M), vision mmproj 903 MB, MTP spec notes (0.82-0.93x author Apple, 1.16x M5 Max sibling — measure per-host), isolation (evidence_root results/tiel-coder/, state tiel-coder-campaign-state.json, no main contamination).
- Contexts: 64k/128k/262k per-model supported contexts (aligns #28), 1M only 96GB+/8x; card recommends 131k-262k q8_0 KV for agentic coding — lane contexts set accordingly.
- Runnable on fleet: senter 48GB 2x24 can run 24/32/48 lanes (Q4/Q5/Q6 + MTP), M1 Pro 32GB unified can run MLX oQ4e/GGUF Q4, M5 Max 128GB target for MLX-MTP measurement.
- Next: hf download to pin sha256 in tiel-coder-artifact-shas.json, then `turbofit-benchmark-orchestrator --tiel-coder` resumable runs per campaign_priority 48→32→24→64→16…, fingerprint-bound evidence. Queue logged, main 48 GB winner untouched.

## [CONTEXT]
- [ ] research ornith-1-5-dflash2-integrity — SUGGESTED 2026-09-08 12:10: Want me to look into whether Ornith-1.5-35B-A3B-DFlash2 from jzinno can actually work with any runtime on this box?
- [ ] research mtplx-memory-controls — SUGGESTED 2026-09-08 12:10: Want me to look into what MTPLX environment variables actually work for memory control on M1 32GB?
- [ ] research mtplx-macos-memory-tuning-research — SUGGESTED 2026-09-07 20:13: Want me to look into what runtime config or env vars MTPLX exposes for memory tuning on macOS?
- [ ] research candidate-quant-research — SUGGESTED 2026-09-07 17:12: Want me to look into GGUF vs MLX quant notes for Nail, Tiel-Coder, and Dirk, confirming which Q3 paths are near base qua
- [ ] research quant-page-comparison — SUGGESTED 2026-09-07 09:43: Want me to look into each candidate's HuggingFace page notes and compare GGUF vs MLX artifacts for Dirk, Nail, and Tiel-
- [ ] research apple-silicon-turbofit-runtime-audit — SUGGESTED 2026-09-07 08:45: Want me to look into the fastest real Apple Silicon runtime for Qwen3.8 27B on this exact hardware?
- [ ] research ornith-dflash2-constraints — SUGGESTED 2026-09-07 08:27: Want me to research the memory constraints of Ornith-DFlash2 for speculative decoding?
- [ ] research maple-metal-alternative — SUGGESTED 2026-09-07 08:27: Want me to investigate non-server execution paths for Maple that don't OOM on 32GB?
- [ ] research ornith-hermes-route — SUGGESTED 2026-09-07 06:30: Want me to look into whether Ornith-1.5-35B-A3B can be exposed as a live Hermes provider via deepgrove-ai/mlx-lm-deepgro
- [ ] research mtplx-macos-memory-tuning — SUGGESTED 2026-09-07 01:02: Want me to look into MTPLX's supported runtime config/env vars for memory control on macOS MLX, since `--memory-budget` 
- [ ] research mplx-memory-ceiling — SUGGESTED 2026-09-07 00:42: Want me to look into MTPLX’s real memory ceiling with MTP on a 32 GB Mac?
- [ ] research mtplx-memory-ceiling — SUGGESTED 2026-09-07 00:30: Want me to look into what's the largest reliable context size for MTPLX on this hardware, and whether there's a supporte
- [ ] research mtplx-viability-check — SUGGESTED 2026-09-07 00:09: Want me to look into whether MTPLX can run reliably on this box, or if it should be dropped from the TurboFit list?
- [ ] research deepgrove-fork-stability — SUGGESTED 2026-09-06 22:41: Want me to look into the Maple MLX Apple-Silicon server story?
