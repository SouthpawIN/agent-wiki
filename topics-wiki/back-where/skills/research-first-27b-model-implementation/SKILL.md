---
name: research-first-27b-model-implementation
description: Use when choosing or switching local LLM artifacts. Always research the model's official/unleashed and HuggingFace pages before implementation.
version: 0.1.0
distilled: 2026-09-07 05:22
topic: back-where
---
# research-first-27b-model-implementation
1. Identify the exact model variant and quantization family Chris named.
2. Read the model's official/unleashed page, then HuggingFace model page, before any download or config change.
3. Note artifact names, quantization levels, flash-attention/deepflash support, and platform availability.
4. Propose one runnable artifact/config for Chris to approve; do not download or modify Hermes/runtime files without explicit approval.
5. Preserve any generated outputs from speed/audition runs in a saved folder for later reuse.
6. If a run is too slow, do not rerun the same test; shift to the next optimization target Chris stated.

## Evidence
> I really want you to get in the habit of First researching and then implementing so you should look at the quen 3.8 27 be unleashed page the q3k exiles the most accurate one and it's uncensored and it's smaller And I think they have a deep flash for it.
> Let me research these models and check what'll fit on this box.
