---
name: qwen-research-first-implementation
description: Use when implementing a HuggingFace model variant for local runtime. Research the model page and unleashed page first, then implement.
version: 0.1.0
distilled: 2026-09-07 16:10
topic: back-where
---
# qwen-research-first-implementation
1. Identify the exact model variant and quantization from the HuggingFace model page and the unleashed page.
2. Record the exact artifact filename, deep flash option, and any recommended llama.cpp/MLX settings before changing runtime config.
3. Do not run downloads or edits until the research notes are written and confirmed.
4. Treat missing or mismatched artifacts as a stop condition, not a reason to guess filenames or settings.

## Evidence
> I really want you to get in the habit of First researching and then implementing so you should look at the quen 3.8 27 be unleashed page
> the q3k exiles the most accurate one and it's uncensored and it's smaller And I think they have a deep flash for it
> Remember, the 131K configuration because we're going to audition that again, grab that uncensored one again
