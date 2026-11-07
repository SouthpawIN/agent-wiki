---
name: model-matrix-add
description: Add a model to the TurboFit catalog and fit ladders across tiers.
version: 1.0.0
author: Fitment
license: MIT
metadata:
  hermes:
    tags: [turbofit, catalog, models, quantization, hardware]
---

# Model matrix add

Use when Chris names a model to support. Produces catalog entries plus fit rungs,
never a claim that something fits.

## Procedure

1. **Measure the repo first.**
   ```bash
   curl -s "https://huggingface.co/api/models/<repo>/tree/main?recursive=true" \
     | jq -r '.[] | select(.type=="file") | "\(.path)\t\(.size)"' \
     | awk -F'\t' '{s[$1]=$2} END {for (f in s) printf "%.2f GiB\t%s\n", s[f]/1073741824, f}' \
     | sort -n
   ```
   Sum shards per quant directory. Record the head revision with
   `curl -s https://huggingface.co/api/models/<repo> | jq -r .sha`.
2. **Classify**: dense vs MoE (active params), vision (`mmproj-*` present), MTP
   (`-mtp` artifacts), and whether the repo ships a real quant ladder or only
   pre-baked memory envelopes (Flint ships `Mix-12G`/`Mix-24G` — not quants).
3. **Pick the q3 floor** — smallest artifact in the Q3/IQ3 class. If the repo has
   no q3 (Qwen 3.8 GSQ-RCO stops at IQ3_S; DeepSeek starts at IQ1_M), record the
   floor in `note` so nobody asks for a quant that does not exist.
4. **Budget the tier.** weights + KV + draft + projector ≤ usable pool.
   Dense 27B at 128K needs 6–10 GiB KV depending on GQA and KV quant — measure,
   do not assume. When in doubt, publish the smaller context rung.
5. **Write catalog variants** in `references/model-catalog.json`:
   ```json
   {"id":"arete-27b-q4","name":"Arete 27B Q4_K_M","family":"Arete 27B",
    "source":"https://huggingface.co/bartowski/NousResearch_Arete-27B-GGUF",
    "revision":"<40-hex sha>","artifact":"NousResearch_Arete-27B-Q4_K_M.gguf",
    "quantization":"Q4_K_M","vision":true,"moe":false,
    "runtime_features":["vision-projector"],"roles":["main"],
    "upstream_source":"https://huggingface.co/NousResearch/Arete-27B"}
   ```
   `id` is kebab-case and unique; every required field present or `ModelVariant`
   validation throws.
6. **Wire rungs** (or let `fit_ladders.py` regenerate) in `references/fit-lists.json`
   with `model`, `quants`, `size_gb`, `context`, `note`. Keep the tier keys as-is:
   dedicated `8-11gb / 12-15gb / 16-23gb / 24-63gb / 64gb+`;
   unified `8-15gb / 16-23gb / 24-31gb / 32-47gb / 48-63gb / 64gb+`.
7. **Tag requirements** — MoE above the pool needs `requires: strata-stream` so
   `fit_check.py` stops refusing it on dedicated-VRAM physics.
8. **Test**:
   ```bash
   pytest -q tests/test_allowed_lineup.py tests/test_catalog_campaign.py
   python -m turbofit_runtime.model_catalog 2>/dev/null || true
   ```
   Then serve once on the smallest tier claimed. If it OOMs, delete that rung.

## Refusals

- No GGUF in the repo → do not add a variant. File it as a conversion project
  (Darwin 180B is the current example: 335 GiB safetensors).
- No pinned revision → do not add. `main` moves.
- A quant name that does not exist in the tree → do not invent it.
