---
title: Cyber-Tiel-Coder Confirmed Running through Hermes (2026-09-15)
created: 2026-09-15
updated: 2026-09-15
type: decision
tags: [decision, tool, timeline]
sources: [raw/inbox/2026-09-15.md]
confidence: high
---

On 2026-09-15 Hermes confirmed two models actually running through Hermes on Chris's machine, resolving the earlier model-search query. ^[raw/inbox/2026-09-15.md]

**What:** Two models verified live through Hermes:
- **Omarchy Unleashed 27B** — responded "4" in ~18s. ^[raw/inbox/2026-09-15.md]
- **Mac Cyber Tiel Coder 35B** (a variant of **Ornith-1.5-35B-A3B**) — responded "Hello from Cyber-Tiel-Coder." in ~1m25s. ^[raw/inbox/2026-09-15.md]

**Why:** These were the candidates from Chris's voice clues ("Horneth" / "Cyber Teal Coder" / "Killier Ragdoll"). The "Cyber Tiel Coder" was initially too slow on M1 32GB (22GB model + 65K context = swapping); Hermes retried with a smaller context window and it worked. ^[raw/inbox/2026-09-15.md]

> "Both models confirmed through Hermes. Ready for whatever's next." ^[raw/inbox/2026-09-15.md]

**When:** 13:14–13:20 on 2026-09-15. ^[raw/inbox/2026-09-15.md]

**Constraint (measured):** the Cyber Tiel Coder fits only at a reduced context window on the M1 32GB device — it does not fit at 65K. ^[raw/inbox/2026-09-15.md]

## Verification notes (2026-09-15)
A 13:15 "Reply in 1 sentence" request ended on a **context-overflow error after partial delivery** — the request no longer fit the model's context window (the streaming reply was cut off mid-delivery). ^[raw/inbox/2026-09-15.md]

At 15:44 and 16:19 Chris asked the model to "Say hello in 5 words"; it answered with generic greetings rather than a constrained five-word line ("Hello there, how are you?", "Hello there, my friend.", "Hello, how are you today?"). ^[raw/inbox/2026-09-15.md]

## Related
- [[model-candidates|Model Candidates on Hugging Face]]
- [[ornith|Ornith]]
- [[device-specific-model-lanes|Device-Specific Model Lanes]]
