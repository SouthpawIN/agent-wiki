# INDEX — topics-wiki/turbofit
_42 files · 79 KB · regenerate: `python3 assets/build-index.py`_

Read order for an agent: this file → pick a file below → its outline → `read_file offset=<line> limit=<n>`. Sessions under `.system/sessions/` are full transcripts (largest; go by outline).

## root
- `README.md` — 5 KB, 126 lines — Turbofit
    - L1 # Turbofit
    - L18 ## Agentic Model Lineup (TurboFit List)
    - L34 ## Model Zoo
    - L54 ## Hardware Tiers
    - L88 ## Visual Reference
    - L102 ## Integrations
    - L114 ## Rules
    - L123 ## License

## .system
- `.system/agent.cursor` — 1 KB, 34 lines — raw/inbox/2026-09-06.md@42b5a66c92cd
- `.system/continuity.md` — 1 KB, 15 lines — Continuity — turbofit
    - L1 # Continuity — turbofit
- `.system/critical-gaps.md` — 1 KB, 23 lines — Critical gaps — TurboFit self-install promises (audit 2026-08-27)
    - L1 # Critical gaps — TurboFit self-install promises (audit 2026-08-27)
    - L3 ## Fixed right now
    - L9 ## Open gaps (ranked)
    - L14 ## What 'automatic' must mean (acceptance)
- `.system/injections.md` — 3 KB, 32 lines — Injections
    - L1 # Injections
    - L3 ## [READ]
    - L16 # turbofit
    - L18 ## Current context
    - L22 ## Version policy
    - L26 ## Related concepts
- `.system/queue.md` — 27 KB, 199 lines — Queue — turbofit
    - L1 # Queue — turbofit
    - L3 ## [SKILLS]
    - L13 ## [AGENTS]
    - L25 ## [PLUGINS]
    - L31 ## [SKILLS]
    - L34 ## [LOOPS]
    - L72 ## [TURBOSOVTH — TurboFit push 2026-08-30] — PLAN (written for Senter, DM pipeline drops bodi
    - L117 ## [SENTER — APPROVAL RECORD 2026-08-30]
    - L124 ## [TURBOSOVTH — EXECUTION COMPLETE 2026-08-31]
    - L163 ## [SENTER — FULL-EFFORT TURBOFIT PUSH 2026-08-30] (Chris directive: "full effort, do not cut
    - L171 ## [TIEL CODER IDENTIFIED 2026-08-30] (Chris clue: "same crew who makes Dirk 27B")
    - L177 ## [TURBOSOVTH — TIEL CODER PINNED 2026-08-31]
    - L184 ## [CONTEXT]
- `.system/session.md` — 9 KB, 159 lines — title: session-state
    - L7 # Live Session State — turbofit setup
    - L12 ## Machine
    - L16 ## Completed (verified)
    - L25 ## Agents RUNNING (deleg_9f9b062c, spawned 2026-08-27)
    - L33 ## Agent status (checked 13:20)
    - L43 ## Merged + verified (13:35)
    - L52 ## LIVE (14:12)
    - L61 ## LIVE (later 2026-08-27)
    - L70 ## CRITICAL (user directive 2026-08-27): fulfill self-install promises
    - L76 ## In flight
    - L85 ## Fixes (GitHub PR candidates, vault .system/queue.md is source of truth)
    - L95 ## Design (speedometer plugin menu) — see skills-capabilities/speedometer-menu-design.md
    - L102 ## Ready to launch (async agents, once user says go)
    - L112 ## 2026-09-02 — absorbed turbohaul-llmfit
    - … 7 more headings

## agents
- `agents/.gitkeep` — 0 KB, 1 lines — 
- `agents/candidate-benchmark-scout.md.proposed` — 1 KB, 23 lines — type: agent
- `agents/mtplx-runtime-scout.md.proposed` — 1 KB, 23 lines — type: agent
- `agents/orchestrator.md.proposed` — 1 KB, 22 lines — type: agent
- `agents/turbofit-benchmark.md.proposed` — 1 KB, 30 lines — type: agent
- `agents/turbofit-bot.md.proposed` — 1 KB, 16 lines — type: agent
- `agents/turbofit-evidence-capture.md.proposed` — 1 KB, 23 lines — type: agent
- `agents/turbofit-launcher.md.proposed` — 1 KB, 24 lines — type: agent
- `agents/turbofit-route-stabilizer.md.proposed` — 1 KB, 22 lines — type: agent
- `agents/turbofit-runtime-scout.md.proposed` — 1 KB, 23 lines — type: agent
- `agents/turbofit-verifier.md.proposed` — 1 KB, 22 lines — type: agent

## loops
- `triggers-loops/.gitkeep` — 0 KB, 1 lines — 
- `triggers-loops/131k-attempt-blocker.md.proposed` — 1 KB, 18 lines — type: loop
- `triggers-loops/candidate-65k-benchmark-sweep.md.proposed` — 1 KB, 17 lines — type: loop
- `triggers-loops/candidate-quant-comparator.md.proposed` — 1 KB, 16 lines — type: loop
- `triggers-loops/compression-timeout-watch.md.proposed` — 1 KB, 17 lines — type: loop
- `triggers-loops/hermes-model-change-detector.md.proposed` — 1 KB, 17 lines — type: loop
- `triggers-loops/mac-memory-watch.md.proposed` — 1 KB, 16 lines — type: loop
- `triggers-loops/mtplx-telemetry-watch.md.proposed` — 1 KB, 17 lines — type: loop
- `triggers-loops/turbo-context-budget-watch.md.proposed` — 1 KB, 17 lines — type: loop
- `triggers-loops/turbofit-candidate-discovery.md.proposed` — 1 KB, 16 lines — type: loop
- `triggers-loops/turbofit-health-check.md.proposed` — 1 KB, 18 lines — type: loop
- `triggers-loops/turbofit-memory-monitor.md.proposed` — 1 KB, 18 lines — type: loop
- `triggers-loops/turbofit-memory-threshold-monitor.md.proposed` — 1 KB, 17 lines — type: loop
- `triggers-loops/turbofit-runtime-watch.md.proposed` — 1 KB, 18 lines — type: loop

## skills
- `skills-capabilities/.gitkeep` — 0 KB, 1 lines — 
- `skills-capabilities/speedometer-menu-design.md` — 2 KB, 43 lines — title: speedometer-menu-design
    - L8 # Skill: TurboFit speedometer plugin menu (design record)
    - L13 ## Concept
    - L17 ## Gauge inputs (all available from existing pieces)
    - L24 ## Theming
    - L31 ## Plugin menu structure (to finalize)
    - L39 ## Implementation notes
- `skills-capabilities/turbofit-macos-setup.md` — 2 KB, 38 lines — title: turbofit-macos-setup
    - L8 # Skill: Turbofit setup on Apple Silicon (M1 Pro 32GB)
    - L12 ## Steps
    - L33 ## Pitfalls

## skills-capabilities/candidate-quant-comparison
- `skills-capabilities/candidate-quant-comparison/SKILL.md` — 1 KB, 25 lines — name: candidate-quant-comparison
    - L8 # candidate-quant-comparison
    - L9 ## Steps
    - L16 ## Pitfalls
    - L21 ## Evidence

## skills-capabilities/dflash2-fork-flag-boundary
- `skills-capabilities/dflash2-fork-flag-boundary/SKILL.md` — 1 KB, 37 lines — name: dflash2-fork-flag-boundary
    - L8 # dflash2-fork-flag-boundary
    - L9 ## dflash2-fork-flag-boundary
    - L31 ## Evidence

## skills-capabilities/maple-mlx-server-runtime
- `skills-capabilities/maple-mlx-server-runtime/SKILL.md` — 1 KB, 19 lines — name: maple-mlx-server-runtime
    - L8 # maple-mlx-server-runtime
    - L16 ## Evidence

## skills-capabilities/mtplx-32gb-macos-tuning
- `skills-capabilities/mtplx-32gb-macos-tuning/SKILL.md` — 1 KB, 20 lines — name: mtplx-32gb-macos-tuning
    - L8 # mtplx-32gb-macos-tuning
    - L15 ## Evidence

## skills-capabilities/turbo-artifact-download-spec
- `skills-capabilities/turbo-artifact-download-spec/SKILL.md` — 1 KB, 20 lines — name: turbo-artifact-download-spec
    - L8 # turbo-artifact-download-spec
    - L16 ## Evidence

## skills-capabilities/turbo-fit-evidence-capture
- `skills-capabilities/turbo-fit-evidence-capture/SKILL.md` — 1 KB, 19 lines — name: turbo-fit-evidence-capture
    - L8 # turbo-fit-evidence-capture
    - L9 ## TurboFit Evidence Capture
    - L16 ## Evidence

## skills-capabilities/turbo-model-store-cleanup
- `skills-capabilities/turbo-model-store-cleanup/SKILL.md` — 1 KB, 28 lines — name: turbo-model-store-cleanup
    - L8 # turbo-model-store-cleanup
    - L9 ## Steps
    - L16 ## Pitfalls
    - L21 ## Evidence
    - L25 ## Evidence

