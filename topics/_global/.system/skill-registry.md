# Skill registry
| skill | owners | description | state |
|---|---|---|---|
| 131k-llm-tuning-on-m1 | senter | Tune 27B models for 131K context on M1 32GB. | live |
| 27b-m1-tuning-research | topic:back-where | Use when tuning 27B models for M1. Research HF page, test Q3 prefill/batch, emit real tok/s. | live |
| ace-step-doc-research | topic:music | Use when building the ACE-Step 1.5 4B LoRA pipeline and need to ground every step in AceStep's own d | live |
| acestep-lora-pipeline | default | Train LoRA adapters on AceStep 1.5 from audio files. | live |
| agent-oversight | turbosovth | Use when supervising teammate agents doing machine work. | live |
| agent-wiki-vault | default | Use when working in the user's agent-wiki Obsidian vault. | live |
| agent-wiki-vault-ui | looker, senter, weaver | Use when iterating the Senter vault-live dashboard UI. | live |
| agent-wiki-vaults | default | Build agent-wiki (GOOP) Obsidian vaults from GitHub repos. | live |
| airtable | default, anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver | Airtable REST API via curl. Records CRUD, filters, upserts. | live |
| apple-notes | default, anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver | Manage Apple Notes via memo CLI: create, search, edit. | live |
| apple-reminders | default, anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver | Apple Reminders via remindctl: add, list, complete. | live |
| architecture-diagram | default, anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver | Dark-themed SVG architecture/cloud/infra diagrams as HTML. | live |
| arxiv | default, anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver | Search arXiv papers by keyword, author, category, or ID. | live |
| ascii-art | default, anser, dogeman, klerik, looker, paladin, senter, teknium, turbosovth, weaver | ASCII art: pyfiglet, cowsay, boxes, image-to-ascii. | live |
| ascii-video | default, anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver | ASCII video: convert video/audio to colored ASCII MP4/GIF. | live |
| background-job-liveness-check | topic:klerik | Use when a launchd/cron/WatchPaths job is claimed running. Prove it ticked from artifacts, never fro | live |
| baoyu-infographic | default, anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver | Infographics: 21 layouts x 21 styles (信息图, 可视化). | live |
| blocked-page-recovery | default, anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver | Use when a fetch fails: 403/429, paywall, WAF, bot wall. | live |
| blogwatcher | default, anser, dogeman, klerik, looker, paladin, senter, teknium, turbosovth, weaver | Monitor blogs and RSS/Atom feeds via blogwatcher-cli tool. | live |
| bot-card-approval-spawn | klerik, topic:klerik | Use when a bot card is approved in the Senter wiki. Turn the approval into a running Hermes profile  | live |
| bot-verify-loop | default, anser, dogeman, klerik, looker, paladin, senter, teknium, turbosovth, weaver | Builder bot finished a change? LOOK loop + done line. | live |
| box | default, anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver | Box manages cloud files, sharing, search, and metadata. | live |
| browserless-web-debugging | default | Debug single-file HTML/JS pages without a browser. | live |
| candidate-quant-comparison | topic:turbofit | Use when evaluating new local TurboFit candidates. Compare GGUF vs MLX artifacts and prefer Q3 when  | live |
| center-wiki-orchestration | senter, topic:beyond-pissed | Use when working with center wiki as live orchestrator. | live |
| chris-examples-are-illustrations | fleet-orchestrator, topic:senter | Use when Chris describes a wanted workflow via a concrete example. Build the workflow/pipeline, not  | live |
| claude-code | default, anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver | Delegate coding to Claude Code CLI (features, PRs). | live |
| claude-design | default, anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver | Design one-off HTML artifacts (landing, deck, prototype). | live |
| clean-environment-model-evaluation | topic:hermes-agent | Use when evaluating a model in a live Hermes session. Behavior: enforce a clean test environment, us | live |
| codebase-inspection | default, anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver | Inspect codebases w/ pygount: LOC, languages, ratios. | live |
| codex | default, anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver | Delegate coding to OpenAI Codex CLI (features, PRs). | live |
| comfyui | default, anser, dogeman, klerik, looker, paladin, senter, teknium, turbosovth, weaver | Generate images, video, and audio via diffusion workflows. | live |
| competitor-news-monitor | default, anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver | Watch named companies for material news; cited digests. | live |
| computer-use | default, anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver | Drive the desktop background-first; escalate on signal. | live |
| d-flash-131k-benchmark | topic:faster-without | Use when benchmarking D-flash variants for the 27B model at 131K context. | live |
| design-md | default, anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver | Author/validate/export Google's DESIGN.md token spec files. | live |
| device-model-lane-selection | topic:both-smarter | Use when running or choosing a model on Chris's unified-memory MacBook and it is slow, swapping, or  | live |
| dflash2-fork-flag-boundary | topic:turbofit | Use when testing DFlash2 speculative decoding with the dflash2-llama.cpp fork. Record the exact flag | live |
| document-to-action-items | default, anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver | Extract cited obligations, deadlines, tasks from documents. | live |
| docx | default, anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver | Create, read, edit, template, and review Word .docx files. | live |
| dogeman-rant-wiki | dogeman, teknium |  | live |
| dogeman-video-foundry | dogeman, teknium |  | live |
| dogeman-viral-scout | dogeman, teknium |  | live |
| dogfood | default, anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver | Exploratory QA of web apps: find bugs, evidence, reports. | live |
| email-inbox-triage | default, anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver | Triage an inbox: prioritize threads, draft replies safely. | live |
| evaluating-llms-harness | default, anser, dogeman, klerik, looker, paladin, senter, teknium, turbosovth, weaver | lm-eval-harness: benchmark LLMs (MMLU, GSM8K, etc.). | live |
| excalidraw | default, anser, dogeman, klerik, looker, paladin, senter, teknium, turbosovth, weaver | Hand-drawn Excalidraw JSON diagrams (arch, flow, seq). | live |
| findmy | default, anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver | Track Apple devices/AirTags via FindMy.app on macOS. | live |
| flash-raw-linux-iso-to-usb | topic:restore-hdiutil | Use when writing a raw Linux distro ISO (.iso) to a USB so it boots as the right distro on macOS. St | live |
| get-may-omarchy-setup-notes | senter | Use when working inside Chris's get-may topic and he wants the working steps for his Omarchy documen | live |
| gif-search | default, anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver | Search/download GIFs from Tenor via curl + jq. | live |
| github | default, anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver | GitHub via gh CLI: PRs, issues, reviews, repos, auth. | live |
| github-auth | default, anser, dogeman, klerik, looker, paladin, senter, teknium, turbosovth, weaver | GitHub auth setup: HTTPS tokens, SSH keys, gh CLI login. | live |
| github-code-review | default, anser, dogeman, klerik, looker, paladin, senter, teknium, turbosovth, weaver | Review PRs: diffs, inline comments via gh or REST. | live |
| github-issue-to-pr | default, anser, dogeman, klerik, looker, paladin, senter, teknium, turbosovth, weaver | Carry a GitHub issue to a verified PR with honest CI state. | live |
| github-issues | default, anser, dogeman, klerik, looker, paladin, senter, teknium, turbosovth, weaver | Create, triage, label, assign GitHub issues via gh or REST. | live |
| github-pr-workflow | default, anser, dogeman, klerik, looker, paladin, senter, teknium, turbosovth, weaver | GitHub PR lifecycle: branch, commit, open, CI, merge. | live |
| github-repo-management | default, anser, dogeman, klerik, looker, paladin, senter, teknium, turbosovth, weaver | Clone/create/fork repos; manage remotes, releases. | live |
| godmode | klerik | Jailbreak LLMs: Parseltongue, GODMODE, ULTRAPLINIAN. | live |
| google-workspace | default, anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver | Google OAuth2 client credentials (downloaded from Google Cloud Console) | live |
| granular-recovery | topic:need-telling | Use when a rebuild is blocked or state is lost. Backtrack and rebuild from source. | live |
| grounded-citations | default, anser, dogeman, fleet-orchestrator, klerik, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver | Ground answers and documents in cited, verifiable sources. | live |
| grounded-citations.bak | looker | Ground answers and documents in cited, verifiable sources. | live |
| half-made-profile-check | topic:klerik | Use when a bot build/spawn is reported done or 'in progress'. Verify the protected files really chan | live |
| hermes-agent | default, anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver | Use, configure, theme, extend, and orchestrate Hermes Agent. | live |
| hermes-agent-skill-authoring | default, anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver | Author in-repo SKILL.md files: frontmatter and structure. | live |
| hermes-appearance | dogeman, teknium | Use when customizing Hermes pets, bot avatars, or themes. | live |
| hermes-approvals | anser, looker | Use when debugging or auditing Hermes approval flows. | live |
| hermes-bots-and-pets | turbosovth | Use when creating Hermes bot profiles or custom pets. | live |
| hermes-desktop-plugin-authoring | default | Write + verify Hermes desktop plugins with no build step. | live |
| hermes-fleet-ops | default | Use when creating or orchestrating Hermes bot fleets. | live |
| hermes-native-first-backend | senter, topic:senter | Use when a Senter backend piece is custom code. Go native. | live |
| hermes-plugin-ops | teknium | Use when building Hermes plugins or fixing defaults. | live |
| hermes-python-env-isolation | topic:back-where | Use when debugging scan-topics.py or any Hermes tooling change. The execute_code kernel and command- | live |
| hermes-runtime-config-fixes | topic:senter | Use when fixing Hermes runtime config issues for model-picker stickiness, TTS gateway entitlement, o | live |
| hermes-update | default | Use when updating Hermes or diagnosing blocked updates. | live |
| himalaya | default, anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver | Himalaya CLI: IMAP/SMTP email from terminal. | live |
| huggingface-hub | default, anser, dogeman, klerik, looker, paladin, senter, teknium, turbosovth, weaver | HuggingFace hf CLI: search/download/upload models, datasets. | live |
| humanizer | default, anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver | Humanize text: strip AI-isms and add real voice. | live |
| imessage | default, anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver | Send and receive iMessages/SMS via the imsg CLI on macOS. | live |
| inspecting-hermes-desktop-dom | default, anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver | Read the live Hermes desktop DOM/CSS over CDP. | live |
| jupyter-live-kernel | klerik | Iterative Python via live Jupyter kernel (hamelnb). | live |
| knowledge-vault | default | Build an Obsidian vault of project topics from user sources. | live |
| latest-message-wins-task-handling | topic:back-where | Use when a turn resumes from compaction or a Historical Task Snapshot. Treat only the latest user me | live |
| librarian-cross-topic-discovery | topic:senter | Use when the user wants vault-wide progressive discovery across wiki/skills/bots/loops instead of si | live |
| librarian-progressive-discovery | topic:senter | Use when surfacing wiki/skills/bots/loops across topics. Frontmatter-first discovery with one propos | live |
| live-model-evaluation | topic:hermes-agent | Use when running a live Hermes model check. Execute a compression test, measure tok/s and similarity | live |
| llama-cpp | default, anser, dogeman, klerik, looker, paladin, senter, teknium, turbosovth, weaver | llama.cpp local GGUF inference + HF Hub model discovery. | live |
| llm-wiki | default, anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver | Karpathy's LLM Wiki: build/query interlinked markdown KB. | live |
| m1-27b-context-lock | topic:hermes-agent | Use when evaluating Qwen 3.8 27B on 32GB M1 with MTPLX/DFlash2. Apply memory-cap evidence to choose  | live |
| mac-gaming-setup | turbosovth | Use when installing Steam or games on a Mac. | live |
| macos-app-setup | turbosovth | Use when installing or debugging a GUI app on macOS. | live |
| macos-gaming-setup | turbosovth | Use when installing Steam, games, or Wine layers on a Mac. | live |
| macos-sudo-password-test | senter, topic:bl3sst3xas-check | Test a macOS sudo password the agent blocks, manually. | live |
| macos-sudo-recovery | senter | Use when Chris forgot his MacBook sudo password. Recover. | live |
| macos-system-settings | default | Change macOS settings via defaults, restart, verify. | live |
| manim-video | default, anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver | Manim CE animations: 3Blue1Brown math/algo videos. | live |
| maple-mlx-server-runtime | topic:turbofit | Use when running or testing Maple MLX on Apple Silicon for Hermes aux or compression. Use deepgrove- | live |
| maps | default, anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver | Geocode, POIs, routes, timezones via OpenStreetMap/OSRM. | live |
| meeting-action-items | default, anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver | Turn meeting notes into cited decisions, owners, tickets. | live |
| merge-reconciler | default, anser, dogeman, klerik, looker, paladin, senter, teknium, turbosovth, weaver | Neutral third-party resolution of agent merge conflicts. | live |
| minecraft-modpack-server | klerik | Host modded Minecraft servers (CurseForge, Modrinth). | live |
| mlops-inference-serving | anser, looker | ML model inference and serving: local GGUF (llama.cpp) and high-throughput serving (vLLM). | live |
| mlops-model-registry-tracking | anser, looker | ML model registry, experiment tracking, and Hub management: Weights & Biases for experiment tracking | live |
| mlops-training-finetuning | anser, looker | LLM fine-tuning and training: LoRA/QLoRA (Unsloth, Axolotl), preference optimization (DPO, GRPO, KTO | live |
| model-benchmark-sourcing | senter | Use when researching model benchmarks. Use official sources. | live |
| mtplx-131k-q8-swap-runbook | topic:hey-look | Use when testing 131K on the 32GB Mac. Behavior: enforce q8/swap, use fixed prompt pair, record tok/ | live |
| mtplx-131k-retest-protocol | topic:hey-look | Use when retesting MTPLX 131K speed on a 32GB Mac. This skill fixes the prompt-shape/reasoning-mode/ | live |
| mtplx-32gb-macos-tuning | topic:turbofit | Use when tuning MTPLX on 32GB macOS. Check runtime config instead of unsupported CLI flags; validate | live |
| mtplx-memory-budget-override | topic:hey-look | Use when manually sizing MTPLX memory on a memory-constrained Mac. Set session-budget env vars with  | live |
| mtplx-model-setup | senter, topic:hey-look | Use when setting up MTPLX for a local model on Mac. | live |
| mtplx-reasoning-budget-troubleshoot | topic:hey-look | Use when a local-serving model returns empty content or stalls on Mac. Behaviour: diagnose the token | live |
| mtplx-streaming-count | senter, topic:burner-phone | Use when counting MTPLX tokens. Use final chunk usage. | live |
| mtplx-streaming-token-counting | senter | Use when testing MTPLX streaming responses. | live |
| music-model-fit-calc | senter | Use when a music model may or may not fit a tier cap. | live |
| music-model-test | topic:music | Use when setting up or validating a local generative music model on Chris's Mac. Check memory budget | live |
| nano-pdf | default, anser, dogeman, klerik, looker, paladin, senter, teknium, turbosovth, weaver | Edit text in existing PDFs via natural-language prompts. | live |
| native-mcp | klerik | MCP client: connect servers, register tools (stdio/HTTP). | live |
| new-subject-early-trigger | fleet-orchestrator, topic:senter | Use when a chat message introduces a subject with no owning topic. Propose research/scaffold immedia | live |
| node-inspect-debugger | default, anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver | Debug Node.js via --inspect + Chrome DevTools Protocol CLI. | live |
| notion | default, anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver | Notion API + ntn CLI: pages, databases, markdown, Workers. | live |
| obsidian | default, anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver | Read, search, create, and edit notes in the Obsidian vault. | live |
| ocr-and-documents | default, anser, dogeman, klerik, looker, paladin, senter, teknium, turbosovth, weaver | Extract text from PDFs/scans (pymupdf, marker-pdf). | live |
| omarchy-no-shell-diagnosis | senter | Use when an x86 Omarchy-style box is reachable on Tailscale but has no SSH shell and the 443 control | live |
| omarchy-remote-desktop-setup | senter | Use to repair remote desktop/VNC into Chris's Omarchy. | live |
| omarchy-tailscale-setup | senter | Use when configuring remote desktop/VNC + OBS for Chris's Omarchy (arch Linux) over Tailscale from h | live |
| opencode | default, anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver | Delegate coding to OpenCode CLI (features, PR review). | live |
| openhue | default, anser, dogeman, klerik, looker, paladin, senter, teknium, turbosovth, weaver | Control Philips Hue lights, scenes, rooms via OpenHue CLI. | live |
| p5js | default, anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver | p5.js sketches: gen art, shaders, interactive, 3D. | live |
| pdf | default, anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver | PDF files: create, read, merge, fill, OCR, edit text. | live |
| plan | default, anser, dogeman, klerik, looker, paladin, senter, teknium, turbosovth, weaver | Write a markdown plan to .hermes/plans/; no execution. | live |
| pokemon-player | klerik | Play Pokemon via headless emulator + RAM reads. | live |
| popular-web-designs | default, anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver | 54 real design systems (Stripe, Linear, Vercel) as HTML/CSS. | live |
| powerpoint | default, anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver | Create, read, edit .pptx decks with python-pptx. | live |
| preempt-decision-test | fleet-orchestrator, senter, topic:senter | Before carding Chris, answer it from the wiki first. | live |
| pretext | default, anser, dogeman, klerik, looker, paladin, senter, teknium, turbosovth, weaver | Build creative browser demos with DOM-free text layout. | live |
| product-price-monitor | default, anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver | Watch product, flight, or listing prices; alert on target. | live |
| productivity-office-tools | anser, looker | Productivity & office tools: Airtable, Google Workspace, Notion, PowerPoint, Maps, nano-pdf, Obsidia | live |
| profile-surgery | klerik | Spawn or edit a Hermes profile? Checklist + gate pattern. | live |
| progressive-disclosure | senter-wiki-bot, topic:senter-wiki | Use before answering anything about a Senter topic. Read the wiki memory layer INDEX → file → sectio | live |
| proposal-apply-proof | topic:klerik | Use when marking any approved proposal (bot, loop, research, skill) as applied/LIVE. The status flag | live |
| protected-gate-one-click-handoff | topic:klerik | Use when a protected-file guard or security gate blocks a SOUL.md/AGENTS.md write. Stop after the se | live |
| provider-lock-validation | topic:hermes-agent | Use when a provider lock is recorded or proposed. Validate acceptance criteria before treating it as | live |
| python-debugpy | default, anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver | Debug Python: pdb REPL + debugpy remote (DAP). | live |
| qwen-research-first-implementation | topic:back-where | Use when implementing a HuggingFace model variant for local runtime. Research the model page and unl | live |
| recovery-repair-pattern | topic:back-where | Use when fixing Hermes runtime crashes on local M1 hardware. Follow Chris's verification-first repai | live |
| reddit-reading | default, anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver | Read Reddit: subreddits, search, threads, users. No browser. | live |
| remote-linux-ops | default | Use when administering any device on the user's Tailnet (macOS, Linux, Android) — SSH, Tailscale, AD | live |
| remote-os-install | turbosovth | Use when installing an OS on a remote machine over SSH. | live |
| requesting-code-review | default, anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver | Pre-commit review: security scan, quality gates, auto-fix. | live |
| reroute-noise-extraction | topic:memento | Use when a raw item contains duplicated Hermes-state reroute or port-conflict noise. Retain only sub | live |
| research-first-27b-model-implementation | topic:back-where | Use when choosing or switching local LLM artifacts. Always research the model's official/unleashed a | live |
| research-first-hf-model-implementation | senter | Research HuggingFace model pages before implementation. | live |
| research-knowledge-retrieval | anser, looker | Research, knowledge retrieval, and content monitoring: blog/feed monitoring (blogwatcher), ML paper  | live |
| research-paper-writing | default, anser, dogeman, klerik, looker, paladin, senter, teknium, turbosovth, weaver | Write ML papers for NeurIPS/ICML/ICLR: design→submit. | live |
| rss-feeds | default, anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver | Read RSS, Atom, JSON feeds; discover feeds behind a page. | live |
| runtime-python-compat | turbosovth | Use when Python version mismatch breaks a local runtime. | live |
| sdlc-review | default, anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver | Review Kanban handoffs and route verified outcomes. | live |
| senter-fleet-coordination | fleet-orchestrator, senter, weaver | Use when routing fleet ideas, bots, or vault logs. Senter coordinator playbook — kanban-dispatch/ver | live |
| senter-proposal-pipeline | senter-wiki-bot, topic:senter-wiki | Use when a worker/umbrella emits or Chris acts on a wiki proposal. Write `.proposed` artifacts, surf | live |
| senter-watcher | senter-wiki-bot, topic:senter-wiki | Use when the watcher (com.senter.watcher) misfiles, stalls, or needs tuning. Per-message filing of H | live |
| serving-llms-vllm | default, anser, dogeman, klerik, looker, paladin, senter, teknium, turbosovth, weaver | vLLM: high-throughput LLM serving, OpenAI API, quantization. | live |
| session-handoff-latest-message-wins | topic:back-where | Use when a context compaction handoff appears. Only act on the latest message after the summary; dis | live |
| session-librarian | default, anser, dogeman, klerik, looker, paladin, senter, teknium, turbosovth, weaver | Organize sessions by prompt: find, rename, archive, prune. | live |
| sidebar-rubber-duck | fleet-orchestrator, topic:senter | Use when acting as the Senter sidebar chat. Converse only, yes-and, extract ideas; never do tasks; r | live |
| simplify-code | default, anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver | Parallel 4-agent cleanup of recent code changes. | live |
| sketch | default, anser, dogeman, klerik, looker, paladin, senter, teknium, turbosovth, weaver | Throwaway HTML mockups: 2-3 design variants to compare. | live |
| skills | klerik, paladin | Yuanbao (元宝) groups: @mention users, query info/members. | live |
| songsee | default, anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver | Audio spectrograms/features (mel, chroma, MFCC) via CLI. | live |
| songwriting-and-ai-music | default, anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver | Songwriting craft and Suno AI music prompts. | live |
| spike | default, anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver | Throwaway experiments to validate an idea before build. | live |
| stale-process-kill-rescan | topic:self-file | When a watch/scan process overwrites files with stale data after a code update, kill it by PID and r | live |
| systematic-debugging | default, anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver | 4-phase root cause debugging: understand bugs before fixing. | live |
| teams-meeting-pipeline | default, anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver | Teams meeting summaries, job replay, Graph subscriptions. | live |
| termux-workflows | anser, looker | Consolidated umbrella for android skills: termux-tts-voice-fix, ffmpeg-music-video | live |
| test-driven-development | default, anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver | TDD: enforce RED-GREEN-REFACTOR, tests before code. | live |
| topic-agent-bot-first | fleet-orchestrator, topic:senter | Use when a topic worker distils inbox context. One agent per topic rewrites context into the wiki, t | live |
| topic-context-llm-wiki | fleet-orchestrator, topic:senter | Use when writing or refreshing a topic's context section. Build a thorough interlinked LLM wiki from | live |
| topic-flywheel-gepa | fleet-orchestrator, topic:senter | Use when running a topic worker over an inbox. Turn repeated context into skills, cluster skills int | live |
| topic-wiki-compile | senter-wiki-bot, topic:senter-wiki | Use when compiling or reading a topic's two-layer LLM wiki. Raw is immutable, wiki pages are agent-o | live |
| touchdesigner-mcp | default, anser, dogeman, klerik, looker, paladin, senter, teknium, turbosovth, weaver | Control TouchDesigner via twozero MCP. | live |
| tts-fresh-entitlement-retry | topic:back-where | Use when TTS fails after a credit top-up or entitlement error. Retry audio-client resolution with fr | live |
| turbo-artifact-download-spec | topic:turbofit | Use when downloading new TurboFit GGUF/MLX candidate artifacts. Build a reproducible curl-backed dow | live |
| turbo-fit-evidence-capture | topic:turbofit | Use when capturing TurboFit performance or behavior evidence. Capture from Chris's actual Hermes win | live |
| turbo-model-store-cleanup | default, anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver, topic:turbofit | Use when freeing TurboFit storage. Delete only wiki-marked. | live |
| turbofit | default, anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver | Rules for Turbofit Wiki. Use when editing. | live |
| turbofit-runtime-setup | default | Use when setting up or fixing the Turbofit local runtime. | live |
| vault-artifact-staging-procedure | topic:object-important | Use when staging vault files for commit while excluding generated live-state JSON. | live |
| venv-rebuild-as-user | topic:beyond-pissed | Fix a root-owned Python venv that the normal user can't traverse (symlink points into /root). | live |
| wallpaper-compositing | default | Composite line art over dark plates into wallpapers. | live |
| warmup-before-benchmark | topic:try-again | Use when benchmarking local inference on Apple Silicon. Run a warmup prompt before measuring tok/s. | live |
| watcher-per-message-filing | fleet-orchestrator, topic:senter | Use when building or tuning the Senter watcher. File every Hermes message into a topic inbox as it l | live |
| weekly-review-planning | default, anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver | Weekly reset: commitments, stalled work, next-week plan. | live |
| weights-and-biases | default, anser, dogeman, klerik, looker, paladin, senter, teknium, turbosovth, weaver | W&B: log ML experiments, sweeps, model registry, dashboards. | live |
| wiki-approval-apply-proof | topic:senter-wiki | Use when a bot/loop card is approved in the wiki. Prove the apply landed (cron registered, gateway p | live |
| wiki-card-clickoff-contract | senter-wiki-bot, topic:senter-wiki | Use when adding any overlay/card to the Senter wiki. Peek→pin→click-off-saves; the closing press is  | live |
| wiki-demo-video | senter-wiki-bot, topic:senter-wiki | Use when Chris asks for a demo/recording of the Senter wiki. Full-screen with the Hermes sidebar, dr | live |
| wiki-derived-anchors | senter-wiki-bot, topic:senter-wiki | Use when placing or nudging any wiki element by pixels. Measure both reference edges from the DOM an | live |
| wiki-drive-preview | senter-wiki-bot, topic:senter-wiki | Use when you must operate or prove the Senter wiki UI. Drive the real preview pane by selector with  | live |
| wiki-event-performance | senter-wiki-bot, topic:senter-wiki | Use when wiring fleet activity into the Senter wiki UI. Emit `wiki` events from real actions so rows | live |
| wiki-feed-verify | senter-wiki-bot, topic:senter-wiki | Use when checking that fleet posts reach the sidebar feed. Cross-check bridge `/post` arrivals again | live |
| wiki-fix-the-record-not-the-pitch | fleet-orchestrator, senter, topic:senter | Use when an agent re-pitches a rejected item. Fix the page. | live |
| wiki-hand-placement | senter-wiki-bot, topic:senter-wiki | Use when px-by-voice placement stalls after 2–3 rounds. Make the widgets draggable/resizable, let Ch | live |
| wiki-hit-zone-layering | senter-wiki-bot, topic:senter-wiki | Use when adding or changing an invisible click/hover zone in the Senter wiki. Lift real controls abo | live |
| wiki-hover-stays-under-cursor | topic:senter-wiki | Use when a Senter wiki element grows, lifts or expands on hover. The thing under the pointer must st | live |
| wiki-live-activity-visibility | fleet-orchestrator, topic:senter | Use when any worker edits the vault while Chris is watching. Every edit must produce visible UI moti | live |
| wiki-live-music-hookup | fleet-orchestrator, topic:senter | Use when wiring music into the Senter wiki. Play real audio (Spotify/YouTube) and drive the EQ + hea | live |
| wiki-look-verify | looker, senter, senter-wiki-bot, weaver, topic:senter-wiki | Verify Senter Wiki visuals via Chris's real window. | live |
| wiki-media-hud-hitzones | fleet-orchestrator, topic:senter | Use when touching the wiki music HUD volume/mute/transport. Enforces Chris's locked rocker look and  | live |
| wiki-overlay-z-order | fleet-orchestrator, topic:senter | Use when any wiki UI change touches layering. Keep chat + music HUD topmost and hit-test-prove it. | live |
| wiki-page-quality-check | senter, senter-wiki-bot, topic:senter-wiki | Use after a topic-wiki compile. Check one page, scan dupes. | live |
| wiki-player-audio-path | topic:youtube | Use when changing the Senter wiki music player's audio element or source. Apply state on creation, t | live |
| wiki-real-audio-pipeline | senter-wiki-bot, topic:senter-wiki | Use when the wiki player, EQ, or volume misbehaves. Real audio only: yt-dlp proxy → <audio> → analys | live |
| wiki-resume-orientation | senter | Read schema, index, log before editing an existing wiki. | live |
| wiki-safe-edit-contract | topic:senter-wiki | Use when editing vault-live.html. Preserve boot bindings, row geometry, and dot centering. | live |
| wiki-terminology-rename-contract | senter | Use when renaming a UI term across both baked HTML markup and the JS factory + downstream references | live |
| wiki-tone-measure | senter-wiki-bot, topic:senter-wiki | Use when Chris says cream/warm/gray/filter/doesn't match the girl. Measure pixel triples before and  | live |
| wiki-ui-knobs | senter-wiki-bot, topic:senter-wiki | Use when Chris asks to move, resize, recolour or re-time anything in vault-live.html. Every knob, wh | live |
| windows-games-on-mac | turbosovth | Use when installing Windows Steam games on a Mac via Wine. | live |
| xlsx | default, anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver | Create, read, edit Excel .xlsx workbooks and CSVs. | live |
| xurl | default, anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver | X/Twitter via xurl CLI: raw post search, posting, DM, media. | live |
| youtube-content | default, anser, dogeman, fleet-orchestrator, klerik, looker, paladin, senter, senter-wiki-bot, teknium, turbosovth, weaver | YouTube transcripts to summaries, threads, blogs. | live |