# faster-without — Brief
> Scope, anti-scope, lens, and standing preferences for this topic.

## Learned
- faster-without refers to removing D-flash to improve speed; Chris previously observed higher speeds earlier.
- Chris’s standing requirement is running the 27B model at a minimum 131K context, even when reconsidering D-flash.
- If raw only references D-flash speed/context, keep in faster-without; broader infra/latency details stay out of scope.
- DFlash2 is engaged as a spec-draft for qwen4 (which supports spec-draft), with D-flash disabled; with D-flash off both MTP and DFlash2 produce full responses at high speed.
- The DFlash2 high-speed result carries no tok/s figure, and the 81 tok/s checkpoint save was requested but unconfirmed — both are open gaps.
- Before any speculative-decode change, save the current fast build as a checkpoint first so it can't be lost (Chris: "I don't want to lose this") — the save-checkpoint-before-experiment rule.
- On 09-15, after resolving the hook-up, the open next move was to research DFlash2's exact setup requirements AND test it — research-then-test, not just hook-up.
- On 09-16 the run reported the enabling conditions improving ("More KV cache room, lower power, faster inference, room for DFlash2 draft") — the speed-up is framed as a continuing trajectory and DFlash2's spec-draft is still pending, not yet engaged or benchmarked.
