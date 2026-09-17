# Injections — hey-look

## [UNREAD]
[AGENTS] I see you're trying to get DFlash2 working on Omarchy but the qwen4 llama.cpp build only has --hf-repo-draft (downloads from HuggingFace) — want a bot that gets DFlash2 running on Omarchy via --hf-repo-draft?
[LOOPS] Want a loop that watches 65K memory_guard admission-shed events under your exact large-prompt shapes?
[AGENTS] I see you've found Ornith as the short-context winner — want a bot that tests Ornith through llama.cpp with DFlash2 to see if it keeps speed at 131K?
[LOOPS] Want a repeatable 65K/131K speedwatch that only compares MTPLX vs Unleashed + DFlash2 on this exact setup?
[AGENTS] I see you're waiting on the DFlash2-for-base-Qwen lookup — want a bot that checks HuggingFace and tells you whether a DFlash2 speculative decoder exists for `mtplx-qwen38-27b-optimized-speed`?
[LOOPS] I see q8/swap is the only known non-OOM 131K path — want a loop that confirms it stays stable for the 35-token/800-token and 5K/100-token jobs?
[LOOPS] I see 65K is the only proven stable window — want a loop that reruns the same 685/5010/1015-token benchmark weekly?
[AGENTS] I see you want DFlash2 checked against the base Qwen model and MTPLX updated in the catalog — want a bot that resolves that missing HuggingFace search and syncs the canonical catalog entry?
[AGENTS] I see you're juggling MTPLX 65K/131K/q8 paths and env overrides — want a bot that writes the stable launch config, port assignments, and warmup checklist so you can stop re-entering overrides?
[LOOPS] Want a loop that keeps your working 65K setup honest — confirming speed and memory behavior stay stable after restarts or config changes?
[LOOPS] Want a repeatable check that logs MTPLX's real usable context ceiling after each restart?
[AGENTS] I see you're trying to get 131K out of a 32GB box — want a bot that probes MTPLX `--memory-budget` settings and reports whether the effective context cap can move past 65K?
[AGENTS] I see you still don't have one stable 131K benchmark result — want a bot that drives the exact retest protocol and records the first passing run?
[LOOPS] You've got two conflicting 131K numbers and an unfinished increase-size sweep — want a repeatable loop that locks one protocol, warms up once, then reruns at 131K on the same prompt class until the figures stabilize?
[AGENTS] I see the wiki still has `auxiliary compression` and `model catalog` listed as pending MTPLX integrations — want a bot that wires MTPLX in as the main provider for both and turns those brief items into closed items?
[LOOPS] Want a weekly sync that refreshes the model catalog entry from MTPLX docs?
[LOOPS] Want a nightly 131K benchmark that collapses the contested figures into one stable number?
[AGENTS] I see you're tracking Qwen 27B MTPLX throughput on your 32GB Mac — want a bot that retests at 131K/262K and files a single stable speed figure back into the wiki?

## [READ]
