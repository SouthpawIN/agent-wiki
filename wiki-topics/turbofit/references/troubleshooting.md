# Troubleshooting

Common failures and the first move for each.

> Grounded in the product repo `README.md` (Troubleshooting) and the Fit Ladder.

| Symptom | First move |
|---|---|
| **VRAM OOM / `ollama run` crashes** | Walk the Fit Ladder: protect the main, offload MoE experts, drop context last. Don't just restart. |
| **Local benchmark shows all dashes** | Run a local benchmark run — this is the #1 evidence gap. Capture tok/s + peak ctx per model. |
| **Gateway not reachable over the network** | Check the box is bound to `0.0.0.0:8091` and the Tailscale hostname resolves; try the tailnet name, not the public IP. |
| **Aux is blind (main + aux both text-only)** | Pair a text-only main with a **vision-capable aux** (MiniMax M3, Qwen 3.7 Plus). Never two blind models. |
| **Main degrades after context fill** | Make sure the aux has 262K+ context so compression doesn't lose information. |
| **Model won't fit on this card** | Switch to the API fallback tier (`serve auto` / `--api` / `--free`). |

TurboSouth (the bundled support profile) inspects real status before proposing changes and distinguishes measured support from aspiration.
