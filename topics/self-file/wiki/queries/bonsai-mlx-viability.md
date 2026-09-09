---
title: "Bonsai MLX viability"
created: 2026-09-07
updated: 2026-09-07
type: query
tags: [query, infra, plan]
sources: [raw/inbox/2026-09-07.md, raw/inbox/2026-09-08.md]
proposed: 2026-09-07 12:57
confidence: low
---

# Bonsai MLX viability

After Colibri was ruled out for standard `mlx_lm`, Hermes said, "Let me start Bonsai MLX and get things working." ^[raw/inbox/2026-09-07.md] On 2026-09-08, Hermes pivoted to a corrected ornith server instead of Bonsai MLX: after restarting with `--new-token`, a stale PID (63522) held the old token, and Hermes started a fresh server (PID 64361) with patched code. ^[raw/inbox/2026-09-08.md] Bonsai MLX was not revisited, so it remains unverified against the current `mlx_lm` stack.

## Questions

- Does Bonsai MLX run on Chris's macOS `mlx_lm` stack without custom code?
- Does it offer better prompt-throughput or cache behavior than ornith?
- Should Bonsai MLX replace ornith as the default local Hermes backend?

_Approve to research compatibility, setup steps, and any local performance notes._
