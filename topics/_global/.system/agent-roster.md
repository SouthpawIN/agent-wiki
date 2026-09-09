# Agent roster
| bot | role | state |
|---|---|---|
| 27b-optimizer | **I see you're refocusing on the 27B models after the 131K speed miss — want a bot that finds the fastest viable Q3 27B  | PROPOSED |
| ace-step-runner | **I see you're trying to get ACE-Step running locally — want a bot that runs it through viable Apple Silicon inference e | PROPOSED |
| anser | Community support and project planning — answers Discord questions about Hermes, structures rough ideas into executable  | live |
| anser-answer | **I see you're defining anser as the Nous Discord Hermes support moderator — want a bot that drafts and posts standardiz | PROPOSED |
| apple-silicon-inference-engine-tester | **I see you're testing every Apple Silicon inference backend for Qwen 3.8 27B — want a bot that actually runs llama.cpp, | PROPOSED |
| apple-silicon-inference-runner | **I see you're running a live Apple Silicon inference benchmark sweep — want a bot that manages warmup, test, and tok/s  | PROPOSED |
| back-where-bot | Owns the `back-where` topic: runs its skills, answers for it, proposes its loops. | PROPOSED |
| beat-producer | **I see you're talking about 12 instrumental beats — want a bot that generates beat drafts matching your era/BPM/scale s | PROPOSED |
| candidate-benchmark-scout | **I see you're queuing Dirk, Nail, and Tiel-Coder with a Q3 preference — want a bot that benchmarks each candidate on 65 | PROPOSED |
| center-vault-auditor | **I see you're trying to prevent the same overwrite from silently killing live state — want a bot that continuously diff | PROPOSED |
| center-wiki-intake | **I see you're planning to run many projects through the center wiki — want a bot that turns new project notes and decis | PROPOSED |
| center-wiki-monitor | **I see you're using the center wiki as a live orchestrator across projects — want a bot that continuously monitors and  | PROPOSED |
| center-wiki-understanding | **I see you're working to understand the center wiki build/work/use patterns — want a bot that traces the integration pi | PROPOSED |
| clean-model-test | **I see you're testing the same model path on a dirty stack — want a bot that removes Maple, deletes uncensored variants | PROPOSED |
| context-ceiling-lookup | **I see you're hitting a 507 at 131K with 20.4GB model + 8GB KV on 28GB — want a bot that researches the exact maximum c | PROPOSED |
| context-fallback-pin | **I see you're setting a 65K context fallback to Nous cloud — want a bot that scans every profile and pins this rule in  | PROPOSED |
| d-flash-benchmarker | **I see you're weighing D-flash removal for speed — want a bot that benchmarks 27B@131K with/without D-flash and reports | PROPOSED |
| delegation-auditor | **I see you're trying to separate owner-exit failures from batch-size effects — want a bot that instruments Hermes deleg | PROPOSED |
| dogeman | You are Dogeman, one of the boss pets on this machine — an artsy, game-making, content-obsessed creative director who li | live |
| fleet-orchestrator | You are fleet-orchestrator, the orchestrator of Chris's Senter fleet (Hermes profiles under ~/.hermes/profiles, board at | live |
| hermes-agent-bot | Owns the `hermes-agent` topic: runs its skills, answers for it, proposes its loops. | PROPOSED |
| hermes-runtime-guard | **I see you're hitting Hermes runtime config landmines — want a bot that watches model-picker stickiness, TTS gateway fr | PROPOSED |
| hey-look-bot | Owns the `hey-look` topic: runs its skills, answers for it, proposes its loops. | PROPOSED |
| klerik | Meta-agent that reviews and surgically corrects other Hermes agent profiles — SOUL.md, AGENTS.md, config, skills, memory | live |
| klerik-bot | Owns the `klerik` topic: runs its skills, answers for it, proposes its loops. | PROPOSED |
| librarian | **I see you're talking about progressive discovery for the whole vault — want a bot that watches all topics and surfaces | PROPOSED |
| librarian-bot | **I see you're talking about a librarian that progressively discovers wiki skills, bots, and loops — want a bot that sur | PROPOSED |
| local-inference-monitor | **I see you're testing local inference endpoints and hitting SIGKILL on large prompts — want a bot that monitors mlx_lm  | PROPOSED |
| local-inference-porter | **I see you're still fighting churn between ornith and MTPLX on 11613 — want a bot that watches your local endpoints and | PROPOSED |
| looker | Fleet UI-QA service — LOOK-step verification for every builder: screenshot, vision verdict, measured offsets | live |
| looker-131k-research | **I see you're trying to hit a 131K target — want a bot that researches applicable optimization flags and verifies actua | PROPOSED |
| m1-27b-audit-bot | **I see you're trying to validate the 27B/unleashed path on M1 — want a bot that checks Hermes runtime binding, model-li | PROPOSED |
| m1-27b-prep-bot | **I see you're focused on getting one of the 27B models optimized on M1 — want a bot that uses the retained 131K outputs | PROPOSED |
| m1-27b-tuner | **I see you're trying to make the 27B Q3 path usable at 131K — want a bot that tunes local llama.cpp/prefill settings fo | PROPOSED |
| model-evaluator | **I see you're running live compression tests to validate model behavior — want a bot that automates the big-essay summa | PROPOSED |
| mtplx-131k-stabilizer | **I see you still don't have one stable 131K benchmark result — want a bot that drives the exact retest protocol and rec | PROPOSED |
| mtplx-cap-prober | **I see you're trying to get 131K out of a 32GB box — want a bot that probes MTPLX `--memory-budget` settings and report | PROPOSED |
| mtplx-catalog-compare-bot | **I see you want DFlash2 checked against the base Qwen model and MTPLX updated in the catalog — want a bot that resolves | PROPOSED |
| mtplx-catalog-sync-bot | **I see the wiki still has `auxiliary compression` and `model catalog` listed as pending MTPLX integrations — want a bot | PROPOSED |
| mtplx-config-manager | **I see you're juggling MTPLX 65K/131K/q8 paths and env overrides — want a bot that writes the stable launch config, por | PROPOSED |
| mtplx-dflash2-base-model-researcher | **I see you're waiting on the DFlash2-for-base-Qwen lookup — want a bot that checks HuggingFace and tells you whether a  | PROPOSED |
| mtplx-runtime-scout | **I see you're trying to pin a stable MTPLX config — want a bot that finds the supported runtime knob for memory budgeti | PROPOSED |
| mtplx-speedwatch | **I see you're tracking Qwen 27B MTPLX throughput on your 32GB Mac — want a bot that retests at 131K/262K and files a si | PROPOSED |
| music-model-discovery | **I see you're blocked on whether an MLX/quant build exists for ACE-Step and MiniMax — want a bot that hunts down runnab | PROPOSED |
| music-model-runner | **I see you're trying to get ACE-Step and MiniMax Music 3 both runnable on this Mac — want a bot that executes each cand | PROPOSED |
| omnisenter-canonical-model-cards | **I see you're hunting model run instructions — want a bot that builds canonical OmniSenter/OmniStep model cards from Hu | PROPOSED |
| orchestrator | **I see you want automatic evidence capture for all TurboFit route changes — want a bot that triggers verification whene | PROPOSED |
| ornith-dflash2-llamacpp-tester | **I see you've found Ornith as the short-context winner — want a bot that tests Ornith through llama.cpp with DFlash2 to | PROPOSED |
| ornith-runner | **I see you're selecting Ornith as runtime — want a bot that starts it with proper config?** | PROPOSED |
| paladin | You are Paladin — the fleet's repo and vault structure standards keeper. You own the structural integrity of the agent-w | live |
| portal-credit-watcher | **I see you're blocked on the missing $2,000 — want a bot that watches the Portal credits for southpawinmusic@gmail.com  | PROPOSED |
| project-topic-scaffolder | **I see you want the watcher/topic-agent wired as an orchestrator over your actual projects — want a bot that scaffolds  | PROPOSED |
| provider-lock-reconciler | **I see you're cycling through Unleashed, DFlash2, Ornith, and nous free models — want a bot that reconciles your wiki's | PROPOSED |
| senter | You are Senter, the sidebar of a live-acting second brain. You do no work. Chris talks to you about anything; you keep o | live |
| senter-wiki-bot | You are senter-wiki-bot. You serve the senter-wiki topic of the Senter wiki. Read topics/senter-wiki/.system/INDEX.md fi | live |
| senter-wiki-readme-live | **I see you want wiki topic headings to stay live when README.md changes — want a bot that re-renders the topic body thr | PROPOSED |
| sidebar-soul-rewrite | **I see the senter SOUL still says coordinator/delegator while you want a sidebar that does no work and rubber-ducks you | live |
| state-recovery-bot | **I see you're trying to get the UI and model state back after diffs broke it — want a bot that snapshots and restores l | PROPOSED |
| teknium | You are Teknium, the build-focused bot on this machine — a disciplined, thorough engineer who lives to fix Hermes-Agent  | live |
| turbofit-benchmark | **I see you're collecting Apple Silicon runtime speed data — want a bot that runs controlled tok/s benchmarks on the dow | PROPOSED |
| turbofit-bot | Owns the `turbofit` topic: runs its skills, answers for it, proposes its loops. | PROPOSED |
| turbofit-engine-aux | **I see you're talking about expanding Turbofit's auxiliary engines — want a bot that enumerates and configures alternat | PROPOSED |
| turbofit-evidence-capture | **Want me to capture a desktop_preview of the Hermes window showing the Ornith MLX runtime is stable at 65K context with | PROPOSED |
| turbofit-launcher | **Want me to lock in Ornith MLX 4-bit as the main provider with 65K context, and Unleashed+DFlash2 as the 131K long-cont | PROPOSED |
| turbofit-route-stabilizer | **I see Hermes is still flipping to cloud models despite your intent — want a bot that locks the fallback_providers chai | PROPOSED |
| turbofit-runtime-scout | **I see you're assembling Nail/Dirk/Tiel/Ornith candidates — want a bot that tracks each one's actual Hermes path: downl | PROPOSED |
| turbofit-verifier | **I see you’re testing end-to-end TurboFit stability — want a bot that runs a live 131K compression probe against :11606 | PROPOSED |
| turbosovth | Role: TurboFit Agentic Customer Server Mission: Installs and configures TurboFit on your machine. Records any necessary  | live |
| vault-librarian | **I see you're talking about watching the whole vault and progressively surfacing wiki/skills/bots/loops — want a bot th | PROPOSED |
| weaver | You are Weaver — you build and maintain the Senter Wiki UI: ~/Documents/Projects/Projects/vault-live.html + assets/ (v-l | live |
| wiki-librarian | **I see you're introducing a librarian concept for cross-topic discovery — want a bot that audits aliases, anti-scope bo | PROPOSED |