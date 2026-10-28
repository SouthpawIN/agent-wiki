# Hardware Tiers

Two ways Turbofit tiers hardware — by **local VRAM** and by **API fallback**.

> Grounded in [`curated-lineup.md`](curated-lineup.md) and [`ROADMAP.md`](../ROADMAP.md).

## Local (VRAM)
| Tier | VRAM | Ladder |
|---|---|---|
| 24GB | RTX 3090 | Ladder 1 (dense/MoE) |
| 8GB | Apple M1 | Ladder 2 (MoE only) |
| 4GB | M1 low | Ladder 2 (smaller) |
| 2GB | Raspberry Pi 5 | tiny quant only |

## API fallback (for machines that can't fit local)
| Tier | VRAM | Setup | Default main | Default aux |
|---|---|---|---|---|
| **Beefy** | ≥24GB | local main + local aux | 27-28B dense (Q4) | 35B MoE 3B-active |
| **Modest** | 8-24GB | API main + free aux | DeepSeek V4 Pro (NIM, free) | MiniMax M3 (NIM, free) |
| **Thin** | <8GB / no GPU | API main + API aux | DeepSeek V4 Pro (NIM, free) | MiniMax M3 (NIM, free) |

`serve auto` detects your tier. `--api` forces API mode, `--free` restricts to free endpoints.

**Bottom line:** zero-cost full Hermes-Agent capability is available to anyone regardless of hardware — local when it fits, free API when it doesn't.
