# Loop registry
| loop | owner | cadence | status |
|---|---|---|---|
| REFLECT loop pass | anser | 0 */2 * * * | on |
| klerik-queue-drain | klerik | every 30m | off |
| fleet-tick | klerik | every 15m | off |
| player-regression-check | looker | every 120m | on |
| wiki-dedupe-sweep | paladin | every 30m | on |
| weaver verify-nightly | senter | 30 3 * * * | on |
| anser REFLECT loop | senter | 0 */2 * * * | off |
| fit-table-tok-s-benchmark-tracker | turbosovth |  | PROPOSED |
| fit-table-tok-s-updater | turbosovth |  | PROPOSED |
| model-benchmark-tracker | turbosovth |  | PROPOSED |
| turbo-fit-tok-s-updater | turbosovth |  | PROPOSED |
| anser-queue-scan | anser |  | PROPOSED |
| 27b-speed-target-loop | teknium |  | PROPOSED |
| 27b-speed-watch | turbosovth |  | PROPOSED |
| download-completion-watch | looker |  | PROPOSED |
| looker | looker |  | PROPOSED |
| weaver | weaver |  | PROPOSED |
| orchestration-state-sync | senter-wiki-bot |  | PROPOSED |
| orchestrator-sync | senter-wiki-bot |  | PROPOSED |
| revert-recovery-watch | paladin |  | PROPOSED |
| verification-loop | none |  | PROPOSED |
| watch-loop-sync | none |  | PROPOSED |
| wiki-orchestrator-sync | weaver |  | PROPOSED |
| benchmark-refresh-watch | looker |  | PROPOSED |
| model-lane-health | looker |  | PROPOSED |
| unified-memory-model-watch | looker |  | PROPOSED |
| preview-wiki-combine-check | weaver |  | PROPOSED |
| vault-refresh-loop | weaver |  | PROPOSED |
| turbofit-picker-watch-daily | looker |  | PROPOSED |
| turbofit-picker-watch | looker |  | PROPOSED |
| turbofit-roster-daily | turbosovth |  | PROPOSED |
| delegation-daily-digest | looker |  | PROPOSED |
| turbofit-page-sync | turbosovth |  | PROPOSED |
| d-flash2-checkpoint-watch | d-flash-benchmarker |  | PROPOSED |
| d-flash2-daily-speed-watch | d-flash-benchmarker |  | PROPOSED |
| daily-131k-speed-check | teknium |  | PROPOSED |
| daily-model-check | looker |  | PROPOSED |
| mtplx-config-drift-check | looker |  | PROPOSED |
| runtime-provider-drift-watch | looker |  | PROPOSED |
| mtplx-131k-q8-stability-loop | mtplx-131k-stabilizer |  | PROPOSED |
| mtplx-131k-retest-loop | mtplx-speedwatch |  | PROPOSED |
| mtplx-131k-stable-bench | looker |  | PROPOSED |
| mtplx-131k-vs-unleashed-speedwatch | mtplx-speedwatch |  | PROPOSED |
| mtplx-65k-admission-shed-monitor | mtplx-cap-prober |  | PROPOSED |
| mtplx-65k-benchmark-loop | mtplx-speedwatch |  | PROPOSED |
| mtplx-65k-stability-check | mtplx-speedwatch |  | PROPOSED |
| mtplx-catalog-sync | looker |  | PROPOSED |
| mtplx-effective-context-ceiling | teknium |  | PROPOSED |
| frontmatter-progressive-disclosure-check | senter-wiki-bot |  | PROPOSED |
| integrations-order-audit | integrations-above-overview |  | PROPOSED |
| integrations-reconcile | integrations-maintainer |  | PROPOSED |
| memory-shard-scan | looker |  | PROPOSED |
| optimization-flag-scan | looker |  | PROPOSED |
| librarian-daily-sync | weaver |  | PROPOSED |
| local-music-runner-support | anser |  | PROPOSED |
| mtplx-music-swap-watch | teknium |  | PROPOSED |
| music-download-verify | music-model-runner |  | PROPOSED |
| music-model-artifact-watch | looker |  | PROPOSED |
| music-model-runtime-check | teknium |  | PROPOSED |
| vault-diff | paladin |  | PROPOSED |
| live-json-size-watch | teknium |  | PROPOSED |
| pocket-shop-funding-check | anser |  | PROPOSED |
| portal-credit-sweep | looker |  | PROPOSED |
| fleet-health-tick | model-fleet-keeper |  | PROPOSED |
| gpu-memory-watch | local-inference-monitor |  | PROPOSED |
| large-prompt-regression | teknium |  | PROPOSED |
| local-endpoint-verification | local-inference-monitor |  | PROPOSED |
| local-server-health-check | looker |  | PROPOSED |
| local-watch-process-monitor | klerik |  | PROPOSED |
| remote-stack-health-tick | local-server-health-check |  | PROPOSED |
| context-to-wiki-rename-sweep | klerik |  | PROPOSED |
| hermes-config-drift-audit | klerik |  | PROPOSED |
| kanban-dispatch | senter | Continuous (gateway). Board is empty today → nothing to migrate, but every bot prompt (looker AGENTS.md etc.) must be rewritten. | [ADOPTED 2026-09-05] The kanban dispatcher is the fleet's PRIMARY spawn path (council items 1+5; policy: [[topics-wiki/senter/process/spawn-policy]]). `senter-bridge/dispatch.py` routes items through `hermes kanban create --assignee <bot>`; direct `hermes chat -q` spawn survives only as the documented emergency hatch (`SENTER_EMERGENCY_SPAWN=1` or manual, §2 of the policy). CLAIM v2 + sentinel RETIRED 2026-09-05 (t_f1b1eba1): sentinel daemon unplugged, sentinel.py deleted, CLAIM sections replaced in all builder/looker AGENTS.md. |
| librarian-discovery | senter |  | PROPOSED |
| model-fallback-sticky-audit | klerik |  | PROPOSED |
| new-topic-activation | paladin |  | PROPOSED |
| record-vs-reality-audit | looker |  | PROPOSED |
| REFLECT loop — the fleet watches itself for repetition and fixes the process | senter |  | on |
| session-finalize | senter | Per session end. Hook payload carries no transcript; the hook pulls it. Distillation (raw md → one-liners) stays custom or an LLM cron step. | [QUEUED] WRAP. First: `hermes sessions export --format md --dry-run`. |
| snapshot-schema-audit | paladin |  | PROPOSED |
| approval-relay | senter | Event-driven (no cron). Requires `hermes serve` running — the desktop app spawns it. | [QUEUED] — first replacement to do (smallest blast radius). First command: `hermes serve --status`. |
| bot-schema-watch | paladin |  | PROPOSED |
| cron-fire-witness | looker |  | PROPOSED |
| entity-discovery | topic-agent |  | PROPOSED |
| fleet-feed | senter | Continuous watcher. Dispatcher lives in the gateway → `hermes gateway start` must be on. | DONE 2026-09-05 — CLAIM v2 → kanban migration complete (t_f1b1eba1); `hermes kanban watch` + fleet-tick (cron 7a2ec814f125) supersede this loop. |
| git-vault-sync | paladin |  | PROPOSED |
| scan-watch | senter | FSEvents via watchdog; launchd `com.senter.scanwatch`; 20 s poll fallback. | KEEP-CUSTOM (watcher) · [QUEUED] swap bots-profiles/skills sources to the dashboard API. |
| topic-agent | senter |  | on |
| umbrella | senter |  | on |
| usage-heat | senter | On every scanner pass (watchdog, launchd `com.senter.scanwatch`). | [QUEUED] — WRAP: same output, native data path. |
| verify-nightly | weaver |  | on |
| watcher | senter |  | on |
| criteria-audit | paladin |  | PROPOSED |
| ace-step-run-check | teknium |  | PROPOSED |
| apple-silicon-engine-smoke | teknium |  | PROPOSED |
| inference-engine-smoke | turbosovth |  | PROPOSED |
| warmup-speed-test-loop | turbosovth |  | PROPOSED |
| 131k-attempt-blocker | turbofit-memory-monitor |  | PROPOSED |
| candidate-65k-benchmark-sweep | turbosovth |  | PROPOSED |
| candidate-quant-comparator | anser |  | PROPOSED |
| compression-timeout-watch | looker |  | PROPOSED |
| hermes-model-change-detector | anser |  | PROPOSED |
| mac-memory-watch | looker |  | PROPOSED |
| mtplx-telemetry-watch | turbosovth |  | PROPOSED |
| turbo-context-budget-watch | turbofit-runtime-scout |  | PROPOSED |
| turbofit-candidate-discovery | looker |  | PROPOSED |
| turbofit-health-check | senter-wiki-bot |  | PROPOSED |
| turbofit-memory-monitor | senter-wiki-bot |  | PROPOSED |
| turbofit-memory-threshold-monitor | anser |  | PROPOSED |
| turbofit-runtime-watch | turbofit-bot |  | PROPOSED |