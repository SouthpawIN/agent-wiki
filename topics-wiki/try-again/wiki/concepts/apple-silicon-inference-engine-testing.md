---
title: Apple Silicon Inference Engine Testing
created: 2026-09-07
updated: 2026-09-07
type: concept
tags: [inference, apple-silicon, qwen, engine, research, decision]
sources: [raw/inbox/2026-09-07.md]
confidence: medium
---

# Apple Silicon Inference Engine Testing

Chris wants to research and test all available Apple Silicon inference engines for Qwen 3.8 27B, with the goal of making larger models runnable locally on this computer. ^[raw/inbox/2026-09-07.md]

## Requested scope
On 2026-09-07 at 05:36, Chris asked for: "Research ALL possible ways to run Qwen 3.8 27B on Apple Silicon M1 32GB at 131K context with maximum speed. Find FreeToken, OMLX, MLX, and any other backends. Report specific model IDs, commands, and expected tok/s for each approach." ^[raw/inbox/2026-09-07.md]

## Intended methodology
- Test llama.cpp with different quants, KV cache types, and speculative decoding. ^[raw/inbox/2026-09-07.md]
- Test MLX via the deepgrove fork. ^[raw/inbox/2026-09-07.md]
- Test OMLX. ^[raw/inbox/2026-09-07.md]
- Test FreeToken. ^[raw/inbox/2026-09-07.md]
- Test any other engines found during research. ^[raw/inbox/2026-09-07.md]
- Start with parallel research and system checks. ^[raw/inbox/2026-09-07.md]

## Dispatch record
- Dispatched at 2026-09-07 03:06:01 as a leaf role task. ^[raw/inbox/2026-09-07.md]
- Total duration: 3400.47s. ^[raw/inbox/2026-09-07.md]
- Task result: failed. "Research and test ALL available Apple Silicon inference engines for Qwen 3.8 27B to find the fastest configuration." ^[raw/inbox/2026-09-07.md]
- Required later reporting: "Report tok/s for each test." ^[raw/inbox/2026-09-07.md]

## Target criteria
- Hardware: Apple Silicon M1 with 32 GB RAM. ^[raw/inbox/2026-09-07.md]
- Model: Qwen 3.8 27B. ^[raw/inbox/2026-09-07.md]
- Context: 131K context. ^[raw/inbox/2026-09-07.md]
- Priority: maximum speed. ^[raw/inbox/2026-09-07.md]

## Scope revision, 2026-09-07 05:36
- Early framing: research and test all available Apple Silicon inference engines for Qwen 3.8 27B. ^[raw/inbox/2026-09-07.md]
- Revised framing: deliver per-engine artifacts, not just a recommendation: specific model IDs, commands, and expected tok/s. ^[raw/inbox/2026-09-07.md]
- This revision broadened the deliverable set while narrowing the acceptability criterion: named commands plus tok/s became mandatory. ^[raw/inbox/2026-09-07.md]

## Benchmark expansion, 2026-09-07 08:17
- Chris asked to test Tiel Coder and Dirk 27B in addition to Qwen 3.8 27B. ^[raw/inbox/2026-09-07.md]
- Quote: "Try Tiel Coder and Dirk 27B as well." ^[raw/inbox/2026-09-07.md]

## Model-specific instructions
- Tiel Coder: latest build, quant Q4 K XL. ^[raw/inbox/2026-09-07.md]
- Dirk 27B: Dirk 3.8 27B with MTP, tested with and without, quant Q3. ^[raw/inbox/2026-09-07.md]
- Quote for Dirk: "Q4 K XL for Tiel Coder and that Q3 I mentioned for Dirk. Make sure to grab Dirk 3.8 27B with the MTP, test with and without, and grab the latest Tiel Coder." ^[raw/inbox/2026-09-07.md]

## Warmup requirement
- Chris said to warm each model before measuring: "Remember to let each model do a warmup prompt and then test their speed while it's warm." ^[raw/inbox/2026-09-07.md]
- This affects all models in this sweep: Qwen 3.8 27B, Tiel Coder, and Dirk 27B. ^[raw/inbox/2026-09-07.md]
- ACE-Step is also covered if tested. ^[raw/inbox/2026-09-07.md]

## Reporting requirement
- After the sweep, Chris wants tok/s reported for each test: "Report tok/s for each test." ^[raw/inbox/2026-09-07.md]

## Benchmark protocol, 2026-09-07 10:39
- Finalized ordered sequence: warmup, then short prompt, then 5K prompt. ^[raw/inbox/2026-09-07.md]
- Quote: "Run warmup, then short prompt (500 tokens), then 5K prompt (100 tokens). Report tok/s for each." ^[raw/inbox/2026-09-07.md]
- Housekeeping: "Make sure to clear the old model off before testing the new one." ^[raw/inbox/2026-09-07.md]

## Candidate narrowing, 2026-09-07 10:37
- Active scope narrowed from open Qwen engine sweep plus Tiel Coder and Dirk 27B to Bonsai, Maple Colibri, and Ornith 1.5 35A3B. ^[raw/inbox/2026-09-07.md]
- Quote: "cut Nail, Tiel Coder, and every. 27B besides Bonsai. Bonsai vs Maple Colibri vs Ornith 1.5 35A3B is where I am at." ^[raw/inbox/2026-09-07.md]
- This creates a contested intermediate state: Tiel Coder and Dirk 27B have recorded partial results and specific instructions, but those candidates are now deprioritized. ^[raw/inbox/2026-09-07.md]

## Operational note
- A 2026-09-07 sweep task was interrupted after 1944.94s with 50 API calls; full transcript is at `/Users/sovthpaw/.hermes/cache/delegation/live/deleg_dc36df32/task-1.log`. ^[raw/inbox/2026-09-07.md]
- System config edits were blocked at 2026-09-07 12:01 and 13:50; the operative notes say "use the hermes command or another approach" and then "try with the write_file tool instead." These are operational evidence only; they do not change the benchmark requirements. ^[raw/inbox/2026-09-07.md]
- Recurring pattern confirmed by 2026-09-09 working notes: "The tool is blocking on shell commands that modify files. Let me use the patch tool instead to make these changes:" and "Good - the lines still have the old values. The shell sed command got blocked. Let me use Python to make these patches:" ^[raw/inbox/2026-09-09.md]
- Pattern extended to 2026-09-10: shell tool showing "Shell tool is not available in this mode" and timing out during git push/commit operations, with shifts to `terminal` and `commit` commands as alternatives. On 2026-09-10 14:30, an additional sub-issue appeared: the venv Python is 3.11.16 but the source code uses Python 3.10+ union syntax (`str | object`). Full record at [[topics-wiki/try-again/wiki/queries/2026-09-10-tool-blocking-continued|2026-09-10 Tool Invocation Blocking (Continued)]]. ^[raw/inbox/2026-09-10.md]
- Operative guidance for this topic: the shell tool is not a reliable path for file mutation or git operations; native tools (`patch`, `write_file`, `terminal`) or Python file APIs are the operative path. ^[raw/inbox/2026-09-09.md]
- [[topics-wiki/try-again/wiki/queries/2026-09-10-tool-blocking-continued|2026-09-10 Tool Invocation Blocking (Continued)]]
- [[topics-wiki/try-again/wiki/queries/2026-09-09-tool-blocking|2026-09-09 Tool Invocation Blocking]]
- [[topics-wiki/try-again/wiki/concepts/curl-timeouts-and-python-fallback|Curl Timeouts and Python Fallback]]

## Related
- [[topics-wiki/try-again/wiki/entities/ace-step|ACE-Step]] is a separately downloaded local model Chris also wants to get running, but it is not part of the Qwen benchmark sweep. ^[raw/inbox/2026-09-07.md]
- [[topics-wiki/try-again/wiki/entities/qwen-3-8-27b|Qwen 3.8 27B]]
- [[topics-wiki/try-again/wiki/entities/tiel-coder|Tiel Coder]]
- [[topics-wiki/try-again/wiki/entities/dirk-27b|Dirk 27B]]
- [[topics-wiki/try-again/wiki/concepts/turbofit-engine-options|Turbofit Engine Options]]
- [[topics-wiki/try-again/wiki/concepts/restore-retry|Restore / Retry]]
- [[topics-wiki/try-again/wiki/decisions/warmup-before-speed-test|Warmup Before Speed Test]]
- [[topics-wiki/try-again/wiki/decisions/benchmark-protocol|Benchmark Protocol]]
- [[topics-wiki/try-again/wiki/comparisons/2026-09-07-candidate-narrowing|2026-09-07 Candidate Narrowing]]
