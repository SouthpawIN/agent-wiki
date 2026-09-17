---
title: Bonsai and Colibri Deprioritization
created: 2026-09-07
updated: 2026-09-07
type: concept
tags: [concept, preference, candidate, decision]
sources: [raw/inbox/2026-09-07.md]
confidence: high
---

# Bonsai and Colibri Deprioritization

## What happened

During the 2026-09-07 testing session, subagents explored multiple candidate models including Bonsai (Prism MLX 2-bit ternary, 7.91 GB) and Colibri (custom Maple format). Both were downloaded but neither ran successfully:

- **Colibri**: Failed to load because the standard `mlx_lm` server could not find `config.json`; the model requires custom Maple MLX code ^[raw/inbox/2026-09-07.md].
- **Bonsai MLX 2-bit**: Server started but exited with `FileNotFoundError` on `config.json` ^[raw/inbox/2026-09-07.md].

## Chris's directive

Chris repeatedly redirected focus to Ornith as the sole priority. Three near-identical raw messages at 13:18, 13:20, and 13:30 show his exact framing:

> "It just needs to be configured into turbofit so I can continue with Ornith. Don't worry about bonsai."

> "I'm actually gonna switch models to Ornith because it's smarter than the free models that we're using currently, so if you can get Ornith up on TurboFit first and configured in the way that we had it, then we can continue working after I switch to that model."

> "It just needs to be configured into turbofit so I can continue with Ornith. Don't worry about bonsai. I said the model that we're using is too dumb, okay? So we need to focus entirely on getting Ornith up so I can pick it from the model picker like the other turbofit models."

These messages were followed by Chris switching his active provider to `ornith-1-5-35a3b-mlx via provider turbofit` ^[raw/inbox/2026-09-07.md].

## The hardware reality

Hermes summarized the hard constraint: on M1 32GB with a 27B model at 131K context, ~5-6 tok/s is the ceiling. The hardware cannot hold 19.3 GB model weights + 8 GB KV cache at 131K + macOS overhead ^[raw/inbox/2026-09-07.md].

## Conclusion

Bonsai and Colibri are parked. The active work is Ornith MLX 4-bit as the main turbofit provider, with the contest that Hermes connection timeouts persisted after config repoint and a verified post-restart live completion is still pending.

## Related

- [[wiki-topics/turbofit/wiki/entities/bonsai.md|Bonsai MLX]]
- [[wiki-topics/turbofit/wiki/entities/colibri.md|Colibri]]
- [[wiki-topics/turbofit/wiki/entities/ornith-1-5-35b-a3b-mlx-4-bit|Ornith 1.5 35B-A3B MLX 4-bit]]
- [[wiki-topics/turbofit/wiki/queries/evidence-capture-and-reliability|Evidence Capture and Reliability Query]]
