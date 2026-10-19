# Multimodal Status

Local multimodal (vision + long context) is the hard frontier.

> Grounded in [`ROADMAP.md`](../ROADMAP.md) and [`model-intel.md`](../../../../../turbofit/references/model-intel.md).

- **MoE + vision + 300K+ ctx doesn't fit one GPU.** A 24B dense or 744B MoE plus a vision tower plus 300K ctx exceeds 24GB. This is why there's no single local multimodal flagship yet.
- **Qwen3-Next-80B-A3B** — 3.4 tok/s, 300K ctx, MoE 3B active. The multimodal flagship, but needs ~2× 40GB to run at quality.
- **Qwen2.5-Omni-3B** — 49 tok/s, 3B, 300K ctx. The small always-on multimodal (fits anything). **3B models don't reach Tier S** — this is an aux, not a main.
- **Best current vision pairing**: Qwen3.5-35B-A3B + qwen3-vl-8b-instruct-v2 (76.31%).
- **Principle:** a 3B multimodal is an always-on aux; a real local multimodal main is a 2-GPU job today.
