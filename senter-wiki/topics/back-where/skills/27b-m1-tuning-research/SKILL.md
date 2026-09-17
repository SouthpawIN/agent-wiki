---
name: 27b-m1-tuning-research
description: Use when tuning 27B models for M1. Research HF page, test Q3 prefill/batch, emit real tok/s.
version: 0.1.0
distilled: 2026-09-07 06:44
topic: back-where
---
# 27b-m1-tuning-research
1. Read the HuggingFace/Unleashed page for the Qwen3.8 27B variant before touching settings.
2. Load at Q3 with 262k contacts and D flash 2.
3. Sweep batch-size and prefill-capacity; record real tok/s per tick.
4. Reject any run that falls back silently — evidence only.
5. Append winning config + tok/s figure to wiki/queries/model-performance-on-m1.md.
Pitfall: don't reuse the rejected 131K baseline speeds; the audition was already too slow.

## Evidence
> "I really want you to get in the habit of First researching and then implementing..."
> "All right, never mind. We didn't go fast enough..."
