---
title: music
created: 2026-09-17
updated: 2026-09-17
type: wiki
sources:
  - index.md
  - wiki/
  - raw/inbox/
  - .system/
---

# music

Last updated: 2026-09-17 | Total pages: 23

---

## INTEGRATIONS

This wiki is fed by:

- **Raw inbox:** `raw/inbox/` — daily cuts from Hermes sessions
- **Sessions:** `.system/sessions/` — full conversation transcripts
- **Wiki pages:** `wiki/` — structured knowledge base

---

## README

### Entities

- [ACE-Step 1.5 4B (MLX 4bit)](wiki/ace-step.md) — A 2.06 GB MLX-quantized music model that Chris chose as the first local generation candidate on his 32 GB Mac because it fits alongside existing workloads. Herm
- [Bonsai-27B-mlx-1bit](wiki/bonsai-27b.md) — A proposed follow-up artifact to Ternary-Bonsai-27B-mlx-2bit: a 1-bit binary MLX quant for a 27B model. Hermes noted it should be a similar size and MLX-compati
- [Calibri 27B](wiki/calibri-27b.md) — Chris asked Hermes to run the same MLX/quant validation workflow for "Calibri and bonsai" after seeing repeated failures on music candidates. No model file, siz
- [MiniMax Music 3 (mxfp8)](wiki/minimax-music-3.md) — A 13 GB music model Chris wants running on his machine. Hermes reported it "won't fit alongside MTPLX" in a 32 GB memory budget, so the current plan is a manual
- [Ornith-MLX / ornith-1-5-35a3b](wiki/ornith-mlx.md) — A model Hermes began wiring into its catalog/provider setup on 2026-09-07. The only evidence is a Hermes note about `ornith-1-5-35a3b` appearing in `auxiliary_o
- [Spotify](wiki/spotify.md) — Spotify is the music service being wired into Chris's Senter wiki as an integration. It is the only music
- [Step-Audio-2-mini (active-params candidate)](wiki/step-audio-2-mini.md) — Step-Audio-2-mini entered local music consideration on 2026-09-07 because its active-parameters profile can change the effective memory and speed story even whe
- [Ternary-Bonsai-27B-mlx-2bit](wiki/ternary-bonsai-27b.md) — A downloaded MLX model Hermes tracked on 2026-09-07 during local music candidate testing. Hermes captured it at 7.91 GB and noted it as a 27B model in 2-bit ter

### Concepts

- [ACE-Step 1.5 4B LoRA pipeline](wiki/ace-step-lora-pipeline.md) — On 2026-09-14, Chris set a standing goal that shifts the music topic from *getting a model to run* to *building a repeatable generation pipeline* around the mod
- [Bonsai 27B MLX 1-bit vs ternary 2-bit](wiki/bonsai-27b-mlx-1bit.md) — Hermes distinguished two Bonsai MLX quantizations on 2026-09-07: ternary 2-bit and pure 1-bit. The distinction matters for memory and speed if these models are
- [Local music memory budget](wiki/local-music-memory-budget.md) — On Chris's 32 GB Mac, the already-running [[wiki-topics/music/wiki/entities/mtplx|MTPLX]] workload leaves very little headroom for local music generation. Hermes est
- [mlx_audio model support limits](wiki/mlx-audio-support-limits.md) — `mlx_audio` is the runner Hermes tried for local music generation on 2026-09-07. It rejected ACE-Step's model type outright, so a downloaded model can still be
- [Music model fit-calculation system](wiki/music-model-fit-calculation.md) — On 2026-09-16 Chris defined a standing rule for deciding whether a music model fits a given tier, replacing ad-hoc "does it fit?" guesses with an explicit calcu
- [Spotify client ID](wiki/spotify-client-id.md) — The Spotify client ID is the credential Hermes named as the last external blocker for the

### Decisions

- [2026-09-07 local music model priority](wiki/2026-09-07-music-model-priority.md) — On 2026-09-07, the chosen order of operations for local music models on Chris's 32 GB Mac was:
- [2026-09-14 ACE-Step LoRA pipeline standing goal](wiki/2026-09-14-ace-step-lora-pipeline.md) — On 2026-09-14, Chris chose to build a repeatable LoRA pipeline on top of [[wiki-topics/music/wiki/entities/ace-step|ACE-Step 1.5 4B (MLX 4bit)]]. This is a standing

### Comparisons

- [Local music models](wiki/local-music-models.md) — Comparison of local generative-music candidates Chris considered on his 32 GB Mac on 2026-09-07. Memory numbers come from Hermes's model-size check; actual runt

### Queries

- [What blocks local music generation right now?](wiki/local-music-generation-blockers.md) — Three layers:
- [Which music candidates actually run under which runner on this Mac?](wiki/local-music-runner-support.md) — The current blocker is not memory alone. ACE-Step was small enough to download, but `mlx_audio` rejected its model type. We need a runner-by-runner verdict for
- [Does mlx_audio support ACE-Step's model format, and what is the smallest quant of MiniMax Music 3 available under MLX?](wiki/mlx-audio-model-support.md) — ACE-Step failed on model-type support, so we need the support list to pick a viable runner or model format instead of guessing.
- [Do MLX/quant builds exist for ACE-Step 1.5 and MiniMax Music 3, and does any current runner support their model types on macOS?](wiki/mlx-quant-music-builds.md) — Chris expects an MLX/quant path to exist; if it does, it changes both the runtime blocker and the memory/size comparison.
- [What still blocks the Spotify integration?](wiki/spotify-integration-blockers.md) — One thing: the [[wiki-topics/music/wiki/concepts/spotify-client-id|Spotify client ID]]. Hermes's status line
- [Step-Audio-2-mini MLX 4-bit test](wiki/step-audio-2-mini-mlx-test.md) — Step-Audio-2-mini is a candidate with an unusual active-parameters profile that may make it cheaper to run than its 35B total parameter count suggests. Before c

---

## SKILLS

Topic skills stored in this wiki:

- **[ace-step-doc-research](skills-capabilities/ace-step-doc-research/SKILL.md) — Ground the ACE-Step LoRA pipeline in AceStep's official documentation, not assumptions. Chris mandated this method for the pipeline.
- **[music-model-test](skills-capabilities/music-model-test/SKILL.md) — 1. Inspect current MTPLX/memory state; abort if no headroom.

---

## BOTS

Proposed bots:

- **[ace-step-lora](agents/ace-step-lora.md.proposed) — **I see you want a LoRA of your mp3s on one word — want a bot that, on 'go', trains the AceStep 1.5 4B LoRA and writes the style-defining prompt batch
- **[ace-step-notepad-loop](agents/ace-step-notepad-loop.md.proposed) — **I see you want the research to keep going until it answers its own follow-ups — want a loop that ticks the AceStep doc-research notepad each cycle a
- **[music-model-discovery](agents/music-model-discovery.md.proposed) — **I see you're blocked on whether an MLX/quant build exists for ACE-Step and MiniMax — want a bot that hunts down runnable artifacts and runner suppor
- **[music-model-fit-inputs](agents/music-model-fit-inputs.md.proposed) — **Want me to look up the hidden_size, layers, and available quant bit-widths for ACE-Step 1.5 4B, MiniMax Music 3, Step-Audio-2-mini and the 27B candi
- **[music-model-fit-maintainer](agents/music-model-fit-maintainer.md.proposed) — **I see you built a fit-calculation system and want engine + flags tracked to optimize which models fit which tiers — want me to fold that maintenance
- **[music-model-runner](agents/music-model-runner.md.proposed) — **I see you're trying to get ACE-Step and MiniMax Music 3 both runnable on this Mac — want a bot that executes each candidate in the right memory stat


---

## LOOPS

Proposed loops:

- **[local-music-runner-support](triggers-loops/local-music-runner-support.md.proposed) — owner: anser · cadence: every 6h · status: SUGGESTED
- **[mtplx-music-swap-watch](triggers-loops/mtplx-music-swap-watch.md.proposed) — owner: teknium · cadence: daily · status: SUGGESTED
- **[music-download-verify](triggers-loops/music-download-verify.md.proposed) — owner: music-model-runner · cadence: after every music model download · status: SUGGESTED
- **[music-model-artifact-watch](triggers-loops/music-model-artifact-watch.md.proposed) — owner: looker · cadence: whenever Chris mentions a new music model or runner error · status: SUGGESTED
- **[music-model-runtime-check](triggers-loops/music-model-runtime-check.md.proposed) — owner: teknium · cadence: every 2 hours · status: SUGGESTED
