# BRIEF — hermes-agent
_Pre-prompt for the cutter and this topic's agent. Chris edits freely; lines ending `<!-- chris -->` are never rewritten._

## What this topic is
> The agent that grows with you

## Belongs here (scope)
- Anything about: hermes agent, hermes-agent
- Decisions, preferences, pains, tools, people and timelines tied to the above

## Does NOT belong here (anti-scope → route elsewhere)
- General Hermes/fleet coordination → `senter` · the wiki UI itself → `senter-wiki` · video/YouTube → `youtube`
- If a cut mentions another topic by name (music, anser, omnisenter-models, turbofit, legacy-bots, pocket-shop…) more than this one, it goes there

## Aliases (the cutter binds hard on these words)
- hermes agent
- hermes-agent

## Lens — how to read new context for this topic
- What is Chris trying to achieve here, in his words? What changed since the last pass?
- Which statements are DECISIONS (dated, with why), which are PREFERENCES, which are PAINS, which are open QUESTIONS?
- What did he say twice? (repetition = a skill or a rule)

## Standing preferences (apply to every suggestion)
- Root causes, never band-aids. Everything live and visible. Markdown + built-in Hermes over custom code.
- Bots first, then loops; reuse a fleet bot when one fits; skills auto-apply. No pitches about the build process itself.

## What a good suggestion looks like here
- One line, phrased as a question Chris can say yes to, tied to a quote from him, naming the bot that would do it.

## Learned (agent-appended, newest first)
- 2026-09-08 · 131K at 10+ tok/s on M1 32GB is physically impossible regardless of quantization/offloading — 64GB+ Mac is the hardware floor; 65K context is the stable lockpoint.
- 2026-09-08 · Provider locks recorded by Hermes-side tooling are provisional until a verified config write via hermes CLI confirms the exact model variant and throughput target.
- 2026-09-08 · The streaming tok/s measurement rule (separate prompt processing from generation time) is already captured as a wiki concept; no separate skill needed since live-model-evaluation covers the workflow.
- 2026-09-07 · Streaming tok/s is not meaningful unless the measurement script separates prompt processing from generation time; queue an improved script before comparing context lengths.
- 2026-09-07 · Clean-model testing is now a hard pre-test rule on this topic: Maple must be removed and any uncensored variant deleted before testing Qwen 3.8 27B.
- 2026-09-07 · A Hermes-side config-write failure inside a session invalidates recorded provider locks until the Hermes CLI write and restart confirm both the exact model variant and the throughput target.
- 2026-09-07 · Streaming tok/s is not meaningful unless the measurement script separates prompt processing from generation time; queue an improved script before comparing context lengths. <!-- chris -->
- 2026-09-07 · Clean-model testing is now a hard pre-test rule on this topic: Maple must be removed and any uncensored variant deleted before testing Qwen 3.8 27B. <!-- chris -->
- 2026-09-07 · A Hermes-side config-write failure inside a session invalidates recorded provider locks until the Hermes CLI write and restart confirm both the exact model variant and the throughput target. <!-- chris -->
- 2026-09-07 · New raw item `2026-09-07-from-senter.md` is not `hermes-agent` content — it is Hermes-side port-conflict evidence and routing noise, so it belongs in `senter`, not this topic.
- 2026-09-07 · Provider locks recorded by Hermes-side tooling are provisional until a Hermes CLI write and restart confirm them; competing runtime model changes within the same session overwrite recorded locks.
- 2026-09-07 · Leftover `.proposed` query pages should be converted into approved research or explicit not-now decisions so the topic index stays clean.
- 2026-09-07 · On 2026-09-07, active Hermes config writes failed in-session and required switching to the Hermes CLI; the provider lock therefore stayed unsettled.
- 2026-09-07 · On 2026-09-07, Hermes-side provider proposals changed within the same session — Unleashed + DFlash2, Ornith, and unrelated nous free models — so treat recorded locks as provisional until the config write is verifiable.
- 2026-09-07 · Provider locks are provisional until Chris explicitly confirms both the model variant and the throughput target; later hardware evidence can override earlier locks.
- 2026-09-07 · Qwen 3.8 27B + 131K KV cache + DFlash2 on 32GB M1 equals the memory limit exactly; 10+ tok/s at 131K is a hardware ceiling on this host, not a config gap.
- 2026-09-07 · Live model checks on 20260903_001447_7bc70a must start from a clean environment: remove Maple and delete any uncensored variant before testing.
- 2026-09-07 · Provider locks without an explicit model-variant confirmation are provisional; Chris requires Qwen 3.8 27B specifically before accepting a lock.
- 2026-09-07 · After MTPLX config changes, restart Hermes Agent; OOMs during testing may come from stale wrong-flag attempts—verify active server pid before treating as failure.
- 2026-09-07 · M5 Max 58 tok/s is a reference point only; the real acceptance criteria are streaming tok/s plus similarity delta after a clean-environment compression test.
- 2026-09-07 · Chris repeated the Maple/uncensored cleanup precondition three times in quick succession on 2026-09-07; treat it as a mandatory pre-test step, not optional.
- 2026-09-07 · Qwen 3.8 27B Q3_K_XL + 131K KV cache + DFlash2 + macOS/Hermes equals the 32GB limit exactly; the 10+ tok/s target at 131K on this host is a memory-cap ceiling, not a config gap.
- 2026-09-07 · 2026-09-07 · Provider locks without an explicit model-variant confirmation are provisional; Chris requires Qwen 3.8 27B specifically.
- 2026-09-07 · 2026-09-07 · Acceptance criteria for model checks are streaming tok/s + similarity delta, evaluated after a clean-environment compression test.
- 2026-09-07 · M5 Max achieves 58 tok/s on the same model due to faster memory bus and idle system; treat as reference, not target for 32GB M1.
- 2026-09-07 · After MTPLX config changes, restart Hermes Agent to pick them up; OOMs during testing may be stale wrong-flag attempts — verify active server pid before treating as failure.
- 2026-09-07 · 2026-09-07: On 32GB M1, MTPLX Qwen 3.8 27B OOMs at 10K+ tokens with 131K context; 65K context is the stable operating point (~10-12 tok/s, no OOM). Hermes Agent itself reserves ~2-4GB.
- 2026-09-07: For clean model evaluation, Chris explicitly requests deletion of uncensored model variants and removal of Maple before testing the 27B model.
- 2026-09-06: Chris evaluates models via live Hermes compression tests (big essay summarization) followed by an explicit "checking out if this model works" check; capture session id and similarity delta when present.
- 2026-09-07: On 32GB M1, MTPLX Qwen 3.8 27B OOMs at 10K+ tokens with 131K context; 65K context is the stable operating point (~10-12 tok/s, no OOM). Hermes Agent itself reserves ~2-4GB.
