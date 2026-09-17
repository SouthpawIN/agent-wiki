# Queue — hey-look

## [CONTEXT]
- [ ] research ornith-llamacpp-long-context-viability — SUGGESTED 2026-09-07 06:53: Want me to look into whether Ornith through llama.cpp with DFlash2 can sustain usable speed at 131K on this box?
- [ ] research base-qwen-dflash2-availability — SUGGESTED 2026-09-07 05:38: Want me to look into whether a DFlash2 speculative decoder is actually available for the base Qwen 3.8 27B model?
- [ ] research mtplx-dflash2-base-model-research — SUGGESTED 2026-09-07 04:46: Want me to look into whether a DFlash2 draft model exists for the base Qwen 3.8 27B, and whether it is compatible with M
- [ ] research mtplx-131k-memory-compression-options — SUGGESTED 2026-09-07 01:11: Want me to look into whether MTPLX has KV-cache compression or quantization knobs that could fit 131K into your 32GB Mac
- [ ] research mtplx-65k-cap-docs — SUGGESTED 2026-09-07 00:41: Want me to look into whether MTPLX documents a configurable context cap that would explain the ~65K effective window on 
- [ ] research mtplx-32gb-131k-config-research — SUGGESTED 2026-09-07 00:28: Want me to look into whether community MTPLX users report stable 131K on 32GB M5/M4 Macs, and which config knobs they us
- [ ] research mtplx-65k-context-cap-investigation — SUGGESTED 2026-09-07 00:14: Want me to look into whether MTPLX is actually capping usable context below 131K, so the retest targets the real window 
- [ ] research mtplx-131k-retest-protocol-review — SUGGESTED 2026-09-07 00:07: Want me to look into what a single stable 131K retest protocol should require for this Mac?
- [ ] research mtplx-memory-budget-docs — SUGGESTED 2026-09-06 23:26: Want me to look into the exact MTPLX docs for `--memory-budget` behavior at 32GB on M5 Max?
- [ ] research mtplx-context-flag-fix — SUGGESTED 2026-09-06 23:01: Want me to look into what changed in MTPLX around the context-size flag that caused the 19G/20.4G stall then the 262K co
- [ ] research mtplx-131k-benchmark — SUGGESTED 2026-09-06 22:49: Want me to look into what the stable large-prompt 131K decode speed is for this MTPLX setup, and how that compares to Un
- [ ] research mtplx-131k-benchmark-lookup — SUGGESTED 2026-09-06 21:58: Want me to look into Qwen 27B MTPLX speed at 131K/262K context?
- [~] research — dispatched 2026-09-06 21:11

## [SKILLS]
- [ ] mtplx-reasoning-budget-troubleshoot — distilled 2026-09-15 14:46 → skills-capabilities/mtplx-reasoning-budget-troubleshoot/SKILL.md (auto-applied)
- [ ] mtplx-131k-q8-swap-runbook — distilled 2026-09-07 04:46 → skills-capabilities/mtplx-131k-q8-swap-runbook/SKILL.md (auto-applied)
- [ ] mtplx-memory-budget-override — distilled 2026-09-07 01:11 → skills-capabilities/mtplx-memory-budget-override/SKILL.md (auto-applied)
- [ ] mtplx-131k-retest-protocol — distilled 2026-09-06 23:36 → skills-capabilities/mtplx-131k-retest-protocol/SKILL.md (auto-applied)
- [ ] mtplx-model-setup — distilled 2026-09-06 21:58 → skills-capabilities/mtplx-model-setup/SKILL.md (auto-applied)

## [AGENTS]
- [ ] hey-look-dflash2-omarchy-setup — SUGGESTED 2026-09-15 14:46: I see you're trying to get DFlash2 working on Omarchy but the qwen4 llama.cpp build only has --hf-repo-draft (downloads  → agents/hey-look-dflash2-omarchy-setup.md.proposed
- [ ] ornith-dflash2-llamacpp-tester — SUGGESTED 2026-09-07 06:53: I see you've found Ornith as the short-context winner — want a bot that tests Ornith through llama.cpp with DFlash2 to s → agents/ornith-dflash2-llamacpp-tester.md.proposed
- [ ] mtplx-dflash2-base-model-researcher — SUGGESTED 2026-09-07 05:38: I see you're waiting on the DFlash2-for-base-Qwen lookup — want a bot that checks HuggingFace and tells you whether a DF → agents/mtplx-dflash2-base-model-researcher.md.proposed
- [ ] mtplx-catalog-compare-bot — SUGGESTED 2026-09-07 04:46: I see you want DFlash2 checked against the base Qwen model and MTPLX updated in the catalog — want a bot that resolves t → agents/mtplx-catalog-compare-bot.md.proposed
- [ ] mtplx-config-manager — SUGGESTED 2026-09-07 04:46: I see you're juggling MTPLX 65K/131K/q8 paths and env overrides — want a bot that writes the stable launch config, port  → agents/mtplx-config-manager.md.proposed
- [ ] mtplx-cap-prober — SUGGESTED 2026-09-07 00:28: I see you're trying to get 131K out of a 32GB box — want a bot that probes MTPLX `--memory-budget` settings and reports  → agents/mtplx-cap-prober.md.proposed
- [ ] mtplx-131k-stabilizer — SUGGESTED 2026-09-07 00:07: I see you still don't have one stable 131K benchmark result — want a bot that drives the exact retest protocol and recor → agents/mtplx-131k-stabilizer.md.proposed
- [ ] mtplx-catalog-sync-bot — SUGGESTED 2026-09-06 23:36: I see the wiki still has `auxiliary compression` and `model catalog` listed as pending MTPLX integrations — want a bot t → agents/mtplx-catalog-sync-bot.md.proposed
- [ ] mtplx-speedwatch — SUGGESTED 2026-09-06 23:01: I see you're tracking Qwen 27B MTPLX throughput on your 32GB Mac — want a bot that retests at 131K/262K and files a sing → agents/mtplx-speedwatch.md.proposed

## [LOOPS]
- [ ] mtplx-65k-admission-shed-monitor — SUGGESTED 2026-09-07 06:53: Want a loop that watches 65K memory_guard admission-shed events under your exact large-prompt shapes? → triggers-loops/mtplx-65k-admission-shed-monitor.md.proposed
- [ ] mtplx-131k-vs-unleashed-speedwatch — SUGGESTED 2026-09-07 05:38: Want a repeatable 65K/131K speedwatch that only compares MTPLX vs Unleashed + DFlash2 on this exact setup? → triggers-loops/mtplx-131k-vs-unleashed-speedwatch.md.proposed
- [ ] mtplx-131k-q8-stability-loop — SUGGESTED 2026-09-07 04:46: I see q8/swap is the only known non-OOM 131K path — want a loop that confirms it stays stable for the 35-token/800-token → triggers-loops/mtplx-131k-q8-stability-loop.md.proposed
- [ ] mtplx-65k-benchmark-loop — SUGGESTED 2026-09-07 04:46: I see 65K is the only proven stable window — want a loop that reruns the same 685/5010/1015-token benchmark weekly? → triggers-loops/mtplx-65k-benchmark-loop.md.proposed
- [ ] mtplx-65k-stability-check — SUGGESTED 2026-09-07 01:11: Want a loop that keeps your working 65K setup honest — confirming speed and memory behavior stay stable after restarts o → triggers-loops/mtplx-65k-stability-check.md.proposed
- [ ] mtplx-effective-context-ceiling — SUGGESTED 2026-09-07 00:28: Want a repeatable check that logs MTPLX's real usable context ceiling after each restart? → triggers-loops/mtplx-effective-context-ceiling.md.proposed
- [ ] mtplx-131k-retest-loop — SUGGESTED 2026-09-06 23:36: You've got two conflicting 131K numbers and an unfinished increase-size sweep — want a repeatable loop that locks one pr → triggers-loops/mtplx-131k-retest-loop.md.proposed
- [ ] mtplx-catalog-sync — SUGGESTED 2026-09-06 23:01: Want a weekly sync that refreshes the model catalog entry from MTPLX docs? → triggers-loops/mtplx-catalog-sync.md.proposed
- [ ] mtplx-131k-stable-bench — SUGGESTED 2026-09-06 23:01: Want a nightly 131K benchmark that collapses the contested figures into one stable number? → triggers-loops/mtplx-131k-stable-bench.md.proposed
