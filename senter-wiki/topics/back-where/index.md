# back-where — wiki index
> One line per page. The wiki row's CONTEXT section renders this file.
> Last updated: 2026-09-17 | Total pages: 40

## Entities
- [[topics/back-where/wiki/entities/compaction-handoff-repetition|Context compaction handoff repetition (2026-09-09)]] — The context compaction handoff instruction first appeared in the 2026-09-08 session transition and repeated identically in the 2026-09-09 raw filing. The handof
- [[topics/back-where/wiki/entities/freetoken-rejected-nvidia-only|FreeToken rejected as NVIDIA-only]] — **FreeToken** was investigated and rejected because it supports only NVIDIA RTX 30/40/50 hardware and will not run on Chris's Mac. The decision was made explici
- [[topics/back-where/wiki/entities/gsq-rco-iq3s-and-bonsai-mlx-snapshot|GSQ RCO IQ3S picked and Bonsai MLX snapshot pending]] — On 2026-09-16 Chris selected the **GSQ RCO IQ3S** as the working quant, displacing the earlier Q3K exile preference. His reasoning bundled accuracy, power, cont
- [[topics/back-where/wiki/entities/hardware-headroom-note|Hardware headroom note for M1 32GB]] — Chris treated the 32GB M1 MacBook as available headroom rather than a hard ceiling during recovery. He said the machine should have enough space to run an audit
- [[topics/back-where/wiki/entities/hermes-commit-completion-stub|Hermes commit-completion stub (2026-09-09)]] — The watcher captured a truncated Hermes internal log line after a commit step, ending mid-sentence at a sim score of 0.08.
- [[topics/back-where/wiki/entities/hermes-fallback-causes|Hermes fallback causes]] — The runtime loaded a backup model instead of the explicitly chosen one, and later records showed automatic model changes during the session.
- [[topics/back-where/wiki/entities/hermes-model-download-in-progress|Hermes model download in progress]] — - **01:32**: Download started for a 13GB model file
- [[topics/back-where/wiki/entities/hp-boot-flash-steamplay|HP laptop boot flash and Steam Play setup]] — During mid-September Chris was flashing and booting a new OS onto an **HP laptop** and running into bootloader and Steam setup questions along the way. This is 
- [[topics/back-where/wiki/entities/interrupted-calibri-bonsai-request|Interrupted Calibri and Bonsai request]] — A session turn was interrupted before completion at 11:35. The partial intent had to be examined for follow-up.
- [[topics/back-where/wiki/entities/m1-mac-performance-expectation|M1 Mac performance expectation]] — Chris asserted the host hardware should handle the workload: an M1 MacBook with 32 GB RAM running a model smaller than 27b, with no extra limitations imposed.
- [[topics/back-where/wiki/entities/model-picker-persistence|Model picker persistence until fallback]] — Chris expects a model chosen from the model picker to remain active until it needs to fall back. Selecting a model is treated as a durable binding, not a transi
- [[topics/back-where/wiki/entities/obs-streaming-omarchy-armored-core|OBS streaming from the Omarchy for Armored Core 6]] — On 2026-09-14 Chris described wanting to manage a gaming stream from the MacBook:
- [[topics/back-where/wiki/entities/q3k-xl-double-gpu-gaming-choice|Q3K XL / Unleashed chosen as the game-adjacent model for a double-GPU device]] — On 2026-09-15 Chris clarified *why* he settled on the Q3K XL / Unleashed model rather than it being a pure speed choice: he wants a model that co-runs alongside
- [[topics/back-where/wiki/entities/qwen3-8-27b-unleashed-selection|Qwen3.8 27B unleashed model selection]] — Chris identified the Qwen3.8 27B "unleashed" variant as the preferred model, specifically seeking Q3 quantization for optimal performance. He emphasized researc
- [[topics/back-where/wiki/entities/recovery-background-process|recovery-background-process]] — A background process exited mid-run during recovery, interrupting an in-flight turn. Chris’s note implies some work may already be complete on disk and should b
- [[topics/back-where/wiki/entities/retained-outputs-folder|Retained outputs folder for rejected 131K audition]] — After deciding the 131K Qwen3.8 27B unleashed audition was too slow, Chris explicitly asked for the generated outputs to be saved in a folder rather than delete
- [[topics/back-where/wiki/entities/ssh-credential-sharing|SSH credential sharing (2026-09-13)]] — At 10:09 on 2026-09-13 Chris walked through an SSH password for a machine, spelling out the literal characters ("A's and the ones," L's replaced by 1's, final I
- [[topics/back-where/wiki/entities/token-startup-race|Token startup race condition]] — During UI restoration, a token was being read but the server was still rejecting it. Hermes traced the likely cause to a startup race: the server had not fully 
- [[topics/back-where/wiki/entities/turbofit-options-missing-after-restart|TurboFit options missing after restarting the desktop app]] — On 2026-09-15 Chris restarted the Hermes desktop app on the MacBook and found the **TurboFit** options gone — they did not come back after the restart. ^[raw/in
- [[topics/back-where/wiki/entities/ui-layout-regression|UI layout regression after diff view change]] — Chris asked for a small change — show diffs — and instead elements shifted to the right and then worsened to a black screen. He explicitly stated the UI ended u
- [[topics/back-where/wiki/entities/ui-restoration-verification-check|UI restoration verification check (2026-09-08)]] — A later session turn reported UI restoration complete and moved into verification.

## Concepts
- [[topics/back-where/wiki/concepts/device-embodiment|Device embodiment and identity]] — Chris framed every connected device — the MacBook, his phone, and the Surface Duo 2 — as the *embodiment* of Hermes itself rather than tools he merely operates.
- [[topics/back-where/wiki/concepts/end-to-end-verification|End-to-end verification before declaring done]] — Every fix must be tested through the actual Hermes surface and verified before being called complete. He explicitly rejected claims of success based only on int
- [[topics/back-where/wiki/concepts/model-prefill-fallback|Prefill timeout triggering model fallback]] — Chris observed that the runtime swapped models during the session. He concluded the cause was prefill taking too long, not true incompatibility, and wanted a co
- [[topics/back-where/wiki/concepts/ornith-1-5-goal|Ornith 1.5 as a smarter-model goal]] — Chris stated a goal — that there should be an **Ornith 1.5** on the system that is "actually smarter than the model we are using now." ^[raw/inbox/2026-09-13.md
- [[topics/back-where/wiki/concepts/ornith-startup-priority|Ornith startup priority]] — During recovery, Chris explicitly requested that Ornith be started before addressing Calibri and Bonsai. This appeared as a pre-requisite request when previous 
- [[topics/back-where/wiki/concepts/quantization-by-tier-philosophy|Quantization selection by hardware tier]] — On 2026-09-16 Chris laid out a tier-based rule for choosing quantization: there is no single best quant, only the optimal quant *for each hardware tier*. The jo
- [[topics/back-where/wiki/concepts/recovery-repair-plan|Recovery repair plan]] — The session moved from repeated failure retries to a vault-spec rebuild. The operative rule was to stop touching files until the target was rebuilt from the vau
- [[topics/back-where/wiki/concepts/tts-cache-freshness|TTS cache-freshness failure]] — TTS entitlement checks used stale cached account info or a JWT that was minted before the $2,000 credit top-up, so entitlement remained negative even after paym
- [[topics/back-where/wiki/concepts/tts-credit-outage|TTS failure during credit outage]] — TTS stopped working because the image-analysis model ran out of credits. Chris noted that a $2,000 top-up had been added, so enough balance should exist, yet TT

## Decisions
- [[topics/back-where/wiki/decisions/131k-audition-rejection|131K audition rejection and speed target]] — After running an audition of the 131K unleashed 27B model configuration, Chris explicitly rejected the result as too slow. The generated outputs were retained i
- [[topics/back-where/wiki/decisions/auxiliary-model-binding|Auxiliary model binding with no extra limitations]] — Chris decided that assigning a model as auxiliary should not be blocked by additional constraints. He explicitly said he gave no limitations beyond that role.
- [[topics/back-where/wiki/decisions/completion-criterion-explicit-statement|Explicit completion and block criterion]] — Chris defined an explicit criterion for how Hermes should signal the end of a task: completion must be stated explicitly and then stop, or blockage must be stat
- [[topics/back-where/wiki/decisions/config-editing-permission-authorization|Config-editing and permission authorization]] — On 2026-09-13 Chris explicitly authorized Hermes to edit permission configs and to send permissions his way when a gate is hit, saying this is how every permiss
- [[topics/back-where/wiki/decisions/credit-top-up-tts-restoration|$2,000 credit top-up for TTS restoration]] — Chris added $2,000 in credits to restore TTS functionality, which had failed after the image-analysis model exhausted its allocation. The payment was made, but 
- [[topics/back-where/wiki/decisions/gsq-rco-iq3s-selection-preference|GSQ RCO IQ3S selection preference]] — On 2026-09-16 Chris moved his quantization preference from Q3K exile to the **GSQ RCO IQ3S** quant, pending proof that it is genuinely near task-lossless. ^[raw
- [[topics/back-where/wiki/decisions/qwen3-27b-optimization-priority|Qwen3.8 27B optimization priority]] — After rejecting the 131K speed audition for being too slow, Chris explicitly redirected priority to optimizing one of the 27B models instead of continuing the 1

## Comparisons


## Queries
- [[topics/back-where/wiki/queries/20-8gb-download-completion-verification|20.8GB download completion and loadability verification]] — Multiple download status lines appeared in one topic run: a ~13GB model file reported nearly complete, an IQ3_XXS download later reported incomplete at ~4.7GB o
- [[topics/back-where/wiki/queries/model-performance-on-m1|Model performance on M1]] — What exact batch-size or prefill-capacity change is needed so the chosen model can load at Q3 with 262k contacts and D flash 2 without falling back due to prefi
- [[topics/back-where/wiki/queries/restoration-and-billing|Restoration and billing]] — 1. Where did the $2,000 credit payment go in Portal billing, and why is TTS still unavailable?

