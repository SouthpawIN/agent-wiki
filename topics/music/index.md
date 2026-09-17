# music — wiki index
> One line per page. The wiki row's CONTEXT section renders this file.
> Last updated: 2026-09-17 | Total pages: 23

## Entities
- [[topics/music/wiki/entities/ace-step|ACE-Step 1.5 4B (MLX 4bit)]] — A 2.06 GB MLX-quantized music model that Chris chose as the first local generation candidate on his 32 GB Mac because it fits alongside existing workloads. Herm
- [[topics/music/wiki/entities/bonsai-27b|Bonsai-27B-mlx-1bit]] — A proposed follow-up artifact to Ternary-Bonsai-27B-mlx-2bit: a 1-bit binary MLX quant for a 27B model. Hermes noted it should be a similar size and MLX-compati
- [[topics/music/wiki/entities/calibri-27b|Calibri 27B]] — Chris asked Hermes to run the same MLX/quant validation workflow for "Calibri and bonsai" after seeing repeated failures on music candidates. No model file, siz
- [[topics/music/wiki/entities/minimax-music-3|MiniMax Music 3 (mxfp8)]] — A 13 GB music model Chris wants running on his machine. Hermes reported it "won't fit alongside MTPLX" in a 32 GB memory budget, so the current plan is a manual
- [[topics/music/wiki/entities/ornith-mlx|Ornith-MLX / ornith-1-5-35a3b]] — A model Hermes began wiring into its catalog/provider setup on 2026-09-07. The only evidence is a Hermes note about `ornith-1-5-35a3b` appearing in `auxiliary_o
- [[topics/music/wiki/entities/spotify|Spotify]] — Spotify is the music service being wired into Chris's Senter wiki as an integration. It is the only music
- [[topics/music/wiki/entities/step-audio-2-mini|Step-Audio-2-mini (active-params candidate)]] — Step-Audio-2-mini entered local music consideration on 2026-09-07 because its active-parameters profile can change the effective memory and speed story even whe
- [[topics/music/wiki/entities/ternary-bonsai-27b|Ternary-Bonsai-27B-mlx-2bit]] — A downloaded MLX model Hermes tracked on 2026-09-07 during local music candidate testing. Hermes captured it at 7.91 GB and noted it as a 27B model in 2-bit ter

## Concepts
- [[topics/music/wiki/concepts/ace-step-lora-pipeline|ACE-Step 1.5 4B LoRA pipeline]] — On 2026-09-14, Chris set a standing goal that shifts the music topic from *getting a model to run* to *building a repeatable generation pipeline* around the mod
- [[topics/music/wiki/concepts/bonsai-27b-mlx-1bit|Bonsai 27B MLX 1-bit vs ternary 2-bit]] — Hermes distinguished two Bonsai MLX quantizations on 2026-09-07: ternary 2-bit and pure 1-bit. The distinction matters for memory and speed if these models are 
- [[topics/music/wiki/concepts/local-music-memory-budget|Local music memory budget]] — On Chris's 32 GB Mac, the already-running [[topics/music/wiki/entities/mtplx|MTPLX]] workload leaves very little headroom for local music generation. Hermes est
- [[topics/music/wiki/concepts/mlx-audio-support-limits|mlx_audio model support limits]] — `mlx_audio` is the runner Hermes tried for local music generation on 2026-09-07. It rejected ACE-Step's model type outright, so a downloaded model can still be 
- [[topics/music/wiki/concepts/music-model-fit-calculation|Music model fit-calculation system]] — On 2026-09-16 Chris defined a standing rule for deciding whether a music model fits a given tier, replacing ad-hoc "does it fit?" guesses with an explicit calcu
- [[topics/music/wiki/concepts/spotify-client-id|Spotify client ID]] — The Spotify client ID is the credential Hermes named as the last external blocker for the

## Decisions
- [[topics/music/wiki/decisions/2026-09-07-music-model-priority|2026-09-07 local music model priority]] — On 2026-09-07, the chosen order of operations for local music models on Chris's 32 GB Mac was:
- [[topics/music/wiki/decisions/2026-09-14-ace-step-lora-pipeline|2026-09-14 ACE-Step LoRA pipeline standing goal]] — On 2026-09-14, Chris chose to build a repeatable LoRA pipeline on top of [[topics/music/wiki/entities/ace-step|ACE-Step 1.5 4B (MLX 4bit)]]. This is a standing 

## Comparisons
- [[topics/music/wiki/comparisons/local-music-models|Local music models]] — Comparison of local generative-music candidates Chris considered on his 32 GB Mac on 2026-09-07. Memory numbers come from Hermes's model-size check; actual runt

## Queries
- [[topics/music/wiki/queries/local-music-generation-blockers|What blocks local music generation right now?]] — Three layers:
- [[topics/music/wiki/queries/local-music-runner-support|Which music candidates actually run under which runner on this Mac?]] — The current blocker is not memory alone. ACE-Step was small enough to download, but `mlx_audio` rejected its model type. We need a runner-by-runner verdict for 
- [[topics/music/wiki/queries/mlx-audio-model-support|Does mlx_audio support ACE-Step's model format, and what is the smallest quant of MiniMax Music 3 available under MLX?]] — ACE-Step failed on model-type support, so we need the support list to pick a viable runner or model format instead of guessing.
- [[topics/music/wiki/queries/mlx-quant-music-builds|Do MLX/quant builds exist for ACE-Step 1.5 and MiniMax Music 3, and does any current runner support their model types on macOS?]] — Chris expects an MLX/quant path to exist; if it does, it changes both the runtime blocker and the memory/size comparison.
- [[topics/music/wiki/queries/spotify-integration-blockers|What still blocks the Spotify integration?]] — One thing: the [[topics/music/wiki/concepts/spotify-client-id|Spotify client ID]]. Hermes's status line
- [[topics/music/wiki/queries/step-audio-2-mini-mlx-test|Step-Audio-2-mini MLX 4-bit test]] — Step-Audio-2-mini is a candidate with an unusual active-parameters profile that may make it cheaper to run than its 35B total parameter count suggests. Before c

