---
title: TurboFit Roadmap
updated: 2026-10-18
type: roadmap
status: living
---

# TurboFit Roadmap

The spine for the whole effort. Refreshed as scope is clarified (source: `raw/sources/2026-10-18-universal-scope.md`).

## The vision — what TurboFit is supposed to be

A **universal, self-managed local-inference server**: a public product (100+ likes, many users), not a personal-fleet tool. It:

1. Invents the hardware and serves the best model the machine can safely run (one OpenAI-compatible endpoint).
2. **Adds models AND inference engines over time** — it benchmarks models × hardware tiers and registers the winners.
3. **Publishes its benchmarks** so users can see the best model + engine per tier per machine.
4. Is **fleet-native** — every machine on the Tailscale appears in the picker.
5. Works on **every OS** (macOS / Linux / Windows) with no single-machine hacks.

Standing method: validate on the local fleet (this MacBook + the Omarchy Linux workstation, both on the Tailscale) **while keeping every change universal.**

## The two fit lists

The single TurboFit List splits into two lists by memory model:

| List | Targets | Favors | Why |
|------|---------|--------|-----|
| **GPU-dedicated** | VRAM machines — NVIDIA, AMD (ROCm), Intel, other GPUs | **Dense** models | Weights + KV want fast HBM/VRAM bandwidth |
| **Unified** | Mac unified memory + CPU-only | **MoE** models | Huge total params, tiny active set; bandwidth-bound |

Rationale: dense wins where VRAM bandwidth is the ceiling; MoE wins where total capacity is large but bandwidth is the ceiling (unified memory / CPU). **Today there is one combined `turbofit_list.py` — it needs to become two.**

## Phases (status)

- [x] **A. Cohesion + truth** — capture scope in the wiki; the hub README's Fit = the **canonical TurboFit List** (two ladders converging on Flash Next), with the live `model-catalog.json` as the shipped subset. *done*
- [ ] **B. Two fit lists** — split the list into GPU-dedicated (dense) + unified (MoE); pick each tier's winner inside the right list. Touches `turbofit_list.py` + `runtime-profiles/`.
- [ ] **C. Self-managed registry** — TurboFit can register **new models** and **new inference engines**; benchmark campaigns drive promotion. Model onboarding exists (`turbofit-model-onboard`); **engine registration is the gap.**
- [ ] **D. Benchmark publication** — a user-facing surface (wiki page + dashboard) showing best model + engine per tier per machine. Today `references/external-benchmarks.md` is discovery-only (every candidate row shows `-`); nothing is published to users.
- [ ] **E. SALT-core engine** — integrate SALT (fork `SouthpawIN/SALT-core`) as a new engine; use its **hard-drive streaming** + **deterministic KV offload** to push low-end tiers further.
- [ ] **F. Tailscale solidification** — auto-configure Tailscale on install; reliable discovery + federation across the fleet; the picker always shows auto + local + tailnet.
- [ ] **G. Universal hardening** — cross-OS: fix the 10 environmental test failures (Linux/Windows); one-command fresh install that survives reboot (macOS launchd / Linux systemd / Windows Task Scheduler).

## Roadblocks

- The README's Fit is the **canonical TurboFit List** (Maple, Cyber-Tiel, Qwen 3.8 Flash, DeepSeek V4.1 Flash); the live catalog is the **shipped subset** — align the live catalog toward the canonical list over time.
- No GPU-vs-unified list split in code.
- No engine registration (engines are a fixed set); no benchmark publication surface.
- SALT-core is a **dry-run public export, not a release** — needs a qualification gate before it becomes a real engine.
- 10 environmental test failures block a clean cross-OS claim.
- The self-install promise (2026-08-27) was still hand-run; the launchd/service path needs to be proven on a fresh machine.

## Next actions (this round)

1. Finish README lineup → catalog alignment (A).
2. Sketch the two-list data model in `turbofit_list.py` + profiles (B) — proposal first, not merged.
3. Draft the SALT engine integration spec + qualification gate (E).
