---
name: maple-mlx-server-runtime
description: Use when running or testing Maple MLX on Apple Silicon for Hermes aux or compression. Use deepgrove-ai fork flags and cache limits; avoid generic mlx_lm server mode.
version: 0.1.0
distilled: 2026-09-06 22:41
topic: turbofit
---
# maple-mlx-server-runtime
1. Use `/tmp/mlx-lm-deepgrove` fork installed from `deepgrove-ai/mlx-lm-deepgrove`.
2. Server command: `python -m mlx_lm server --model <maple-mlx-path> --port 11612 --host 127.0.0.1 --flash-head --prompt-cache-bytes 134217728 --trust-remote-code`.
3. Validate with `/v1/chat/completions` and `/v1/models`.
4. If server OOMs after a few requests, report exact traceback, do not restart blindly; prefer single-shot generate() evidence instead of claiming server stability.
5. Do not use stock `mlx_lm` server for Maple workloads on this box.
6. Keep Unleashed on :11606 as main+vision; do not start aux on the same port.

## Evidence
> Maple MLX works for small prompts (<=1000 tokens) but still fails for larger ones
> Found it. The README says to use `deepgrove-ai/mlx-lm-deepgrove` — a custom MLX runtime specifically built for Maple on Apple Silicon
