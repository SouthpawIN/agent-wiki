---
title: "Bonsai MLX viability"
created: 2026-09-07
updated: 2026-09-09
type: query
tags: [query, infra, plan]
sources: [raw/inbox/2026-09-07.md, raw/inbox/2026-09-08.md, raw/inbox/2026-09-13.md, raw/inbox/2026-09-15.md]
proposed: 2026-09-07 12:57
confidence: low
---

# Bonsai MLX viability

After Colibri was ruled out for standard `mlx_lm`, Hermes said, "Let me start Bonsai MLX and get things working." ^[raw/inbox/2026-09-07.md] On 2026-09-08, Hermes pivoted to a corrected ornith server instead of Bonsai MLX: after restarting with `--new-token`, a stale PID (63522) held the old token, and Hermes started a fresh server (PID 64361) with patched code. ^[raw/inbox/2026-09-08.md] During this same window Hermes also inspected the vault-live.html `loadLive` function and tested the `/file` endpoint with `.system-live.json`. ^[raw/inbox/2026-09-08.md] Bonsai MLX was not revisited, so it remains unverified against the current `mlx_lm` stack.

## Later context — 2026-09-13 and 2026-09-15

The operational path moved to a remote-host stack (nginx :8080 → model server :8100 over Tailscale) with the ornith model at a corrected context length of 65536. ^[raw/inbox/2026-09-13.md] ^[raw/inbox/2026-09-15.md] Bonsai MLX was never adopted as the default backend; the remote ornith stack is now the working target. ^[raw/inbox/2026-09-15.md]

## Questions

- Does Bonsai MLX run on Chris's macOS `mlx_lm` stack without custom code?
- Does it offer better prompt-throughput or cache behavior than ornith?
- Should Bonsai MLX replace ornith as the default local Hermes backend?

_Approve to research compatibility, setup steps, and any local performance notes._
