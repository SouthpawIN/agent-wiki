---
name: model-matrix-add
description: Add a model to the TurboFit catalog and fit ladders across tiers.
version: 1.0.0
author: TurboSouth
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
8. **Wire the recipe** — a catalog variant without a recipe cannot launch.
   `references/model-recipes.json` has one entry per family (binary, port,
   model_root, projector, methods per context) and one per variant (model file,
   draft, methods). Copy the nearest family; give the family a unique port; list a
   method for **every** context the catalog advertises, or the compiler fails with
   `no method recipe for context <n>`.
9. **Register the artifact** — `references/artifact-manifest.json` needs one entry
   per file the recipes reference, with `sha256` taken from Hugging Face's LFS
   `oid` (not computed by downloading) and `size_bytes` from the tree API. The
   manifest set must equal the referenced-file set exactly: extra shard entries
   fail the contract just as missing ones do.
10. **Regenerate the matrix** — it is generated, never hand-edited:
   ```bash
   PYTHONPATH=src python - <<'PY'
   from turbofit_runtime.model_catalog import ModelCatalog, build_configuration_matrix
   import json, pathlib
   cat = ModelCatalog.load(pathlib.Path("references/model-catalog.json"))
   pathlib.Path("references/configuration-matrix.json").write_text(
       json.dumps(build_configuration_matrix(cat), indent=2) + "\n")
   PY
   ```
   If the artifact-manifest test pins the catalog length, bump that number in the
   same commit — it is a deliberate snapshot guard, not an obstacle.
11. **Verify no regressions**, comparing failure lists rather than counts (this
   suite has environment-dependent failures):
   ```bash
   PYTHONPATH=src pytest -q --ignore=tests/test_hermes_fit.py 2>&1 | grep ^FAILED | sort > /tmp/after
   git stash && PYTHONPATH=src pytest -q --ignore=tests/test_hermes_fit.py 2>&1 | grep ^FAILED | sort > /tmp/before && git stash pop
   comm -23 /tmp/after /tmp/before      # must be empty
   ```
12. **Offer, never displace.** A new family is an option in `check_local_options`
   and `ALLOWED_MAIN`; the band default (`local_main_for_vram_gb`,
   `speed_main_for_vram_gb`, `shared_main_for_total_memory_gb`) must not change.
   Promotion to a ladder winner is a benchmark decision, not a catalog edit.

## What "q3 or higher" means per repo

The quant ladder is whatever the uploader published, so map the floor honestly:
Qwen 3.8 27B GSQ-RCO tops out at IQ3_S; Nanbeige's ladder starts at IQ2 and its q3
is IQ3_XS; Flint ships memory envelopes (Mix-12G/Mix-24G), not quants; DeepSeek
starts at IQ1_M. Naming a Q4 that does not exist is the same error as inventing a
size.

## Refusals

- No GGUF in the repo → do not add a variant. File it as a conversion project
  (Darwin 180B is the current example: 335 GiB safetensors).
- No pinned revision → do not add. `main` moves.
- A quant name that does not exist in the tree → do not invent it.
