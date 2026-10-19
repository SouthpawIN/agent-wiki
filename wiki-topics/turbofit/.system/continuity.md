# Continuity — turbofit

Raw understanding, 2026-08-27 (GitHub + live setup on this machine):

- Turbofit is the flagship: adaptive local-inference runtime for Hermes. One OpenAI-compatible
  gateway on 127.0.0.1:8091, stable provider IDs (auto / active:main / active:aux).
- Setup on this machine (Apple M1 Pro, 32 GB unified, Metal): clone at ~/turbofit, rev d6e4ff2.
- **User's chosen model: Qwen 3.8 27B Unleashed UD-Q3_K_XL** (outsourc-e, pinned rev 67a9992,
  13.2 GB, SHA-pinned in runtime-profiles/downloads.json). Curated because the per-tensor
  dynamic quant is more accurate than uniform quants (PPL 6.4036, MMLU 82.98%, 0/20 refusals).
- NOTE: code's `apple_mlx_main()` routes >=24GB Apple to OrcaRouter MLX 6-bit; user overrode —
  the Unleashed Q3_K_XL is the authority. This discrepancy is a GitHub fix candidate.
- User directive: the Fit List IS the fallback chain. Scan/recommend/Fit-List consolidation is the architectural fix; Bonsai-in-24gb.yaml and Apple->MLX misroute are symptoms of three divergent authorities.
- (Edit this file to correct my understanding; I never overwrite user-edited lines.)

## Refined scope, 2026-10-18 (Chris)
- TurboFit is a **universal product** (public, 100+ likes, many users), NOT a personal-fleet tool.
- Method: **validate on the local fleet** (MacBook + Omarchy Linux workstation, both on Tailscale) **while keeping it universal.**
- **Two fit lists:** GPU-dedicated (VRAM: NVIDIA/AMD/Intel) favors **dense**; Unified (Mac/CPU) favors **MoE.**
- TurboFit is a **self-managed server that adds models AND inference engines** via benchmarking.
- **Publish benchmarks** to users — best model + engine per tier per machine.
- Integrate **SALT-core** as an engine (HDD streaming + KV offload for low-end tiers).
- **Solidify Tailscale** (auto-config on install, reliable discovery/federation).
- Open debt: align the live catalog toward the canonical TurboFit List, cross-OS test failures, self-install promise. See ROADMAP.md.
