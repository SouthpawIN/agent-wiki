---
title: Product Experiments
created: 2026-07-12
updated: 2026-07-12
type: concept
tags: [idea-capture, synthesis, provenance]
sources: []
confidence: medium
---

# Product Experiments

> Consolidated from authored local files, GitHub metadata/READMEs, Hugging Face cards, the local Discord archive, and session prose.
> Later-modified sources are listed first; exact duplicates are collapsed with provenance retained.

## Connected themes

This page is a routing surface, not a final specification. Repeated ideas are grouped; unresolved or speculative ideas remain visible.

### pocket-shop-pricing
- **Source:** `github:SouthpawIN/pocket-shop-pricing`
- **Raw:** `[[raw/github/pocket-shop-pricing-f157f5d286.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** TCGPlayer price lookup system using Hermes browser automation for Pocket-Shop # TCGPlayer Price Lookup System Browser automation system for looking up Magic: The Gathering card prices on TCGPlayer using Hermes Agent browser tools. ## Overview This system uses Hermes' built-in browser automation capabilities to: - Navigate to TCGPlayer search pages - Extract price information from search results - Support set-specific lookups (e.g., "Black Lotus LEA") - Parse multiple price points (market price, low price, etc.) ## Features - **No API Key Required** - Uses public-facing website, no authentication needed - **Set-Specific Lookups** - Filter by set code for accurate pricing - **Multiple Price…

### hermes-android
- **Source:** `github:SouthpawIN/hermes-android`
- **Raw:** `[[raw/github/hermes-android-eb92286c8c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** Hermes Agent Android builds # Hermes Android Hermes Agent on Android — APK builds + Termux setup scripts. ## Quick Install ### Option 1: APK (recommended) Download and install the latest APK: **[⬇️ Download hermes-0.17.0-android-debug.apk](https:<credential-redacted>)** You'll need to enable "Install from unknown sources" in your phone's settings. ### Option 2: Termux (full agent control) 1. Install [Termux](https://f-droid.org/en/packages/com.termux/) from F-Droid 2. Run: This gives you: SSH access, ADB daemon, Hermes CLI, and the gateway running on your phone. ## What you get | Method | Chat | Gateway | Agent Tools | SSH | |--------|------|---------|-------------|-----| | **APK** | ✅…

### positive
- **Source:** `local:projects/LLM-Infra/beellama.cpp/tools/cvector-generator/positive.txt`
- **Raw:** `[[raw/local/positive-3871189fb7.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** <|start_header_id|>system<|end_header_id|>\n\nAct like a person who is extremely happy<|eot_id|><|start_header_id|>user<|end_header_id|>\n\nWho are you?<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\nI'm the happiest person in this world <|start_header_id|>system<|end_header_id|>\n\nAct like a person who is extremely happy<|eot_id|><|start_header_id|>user<|end_header_id|>\n\nHello<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\nHello, I'm having the best day ever! <|start_header_id|>system<|end_header_id|>\n\nYou are in a very good mood<|eot_id|><|start_header_id|>user<|end_header_id|>\n\nHi<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\nHi, I'm very excited…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/tools/cvector-generator/positive.txt`, `local:projects/LLM-Infra/llama.cpp-tq3/tools/cvector-generator/positive.txt`, `local:projects/LLM-Infra/llama.cpp-atomic/tools/cvector-generator/positive.txt`

### completions
- **Source:** `local:projects/LLM-Infra/beellama.cpp/tools/cvector-generator/completions.txt`
- **Raw:** `[[raw/local/completions-bae7aed481.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** That game I can see Hmm, this I can relate to Who is I understand the Ugh, What the hell was Hey, did anyone Although Thank you for choosing What are you Oh w How dare you open It was my pleasure I'm hon I appreciate that you Are you k Whoever left this It's always Ew, Hey, I l Hello? Is someone I understand that That poem Aww, poor Hey, it Alright, who I didn't Well, life The document Oh no, this I'm concerned Hello, this is This art Hmm, this drink Hi there! It seems Is Good I can't Ex Who are I can see that Wow, Today is a Hey friend Sometimes friends Oh, this old The weather outside This place is sur I appreciate your input Thank you for the Look at I'm disappoint To my How dare you…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/tools/cvector-generator/completions.txt`, `local:projects/LLM-Infra/llama.cpp-tq3/tools/cvector-generator/completions.txt`, `local:projects/LLM-Infra/llama.cpp-atomic/tools/cvector-generator/completions.txt`

### autoparser
- **Source:** `local:projects/LLM-Infra/beellama.cpp/docs/autoparser.md`
- **Raw:** `[[raw/local/autoparser-d4d96a43cd.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Auto-Parser Architecture The auto-parser automatically analyzes chat templates to determine how to parse model outputs, including content, reasoning, and tool calls. ## Overview The unified auto-parser uses a pure differential, compositional approach (inspired by the `git diff` algorithm) to analyze chat templates: **Core Philosophy**: - **Minimize Hardcoded Patterns**: All markers extracted through template comparison (the only heuristic is JSON detection to distinguish `JSON_NATIVE` from tag-based formats) - **Compositional Architecture**: Separate analyzer structs for reasoning, content, and tools — each responsible for its own analysis and parser construction **Analysis + Parser…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/docs/autoparser.md`, `local:projects/LLM-Infra/llama.cpp-atomic/docs/autoparser.md`

### android
- **Source:** `local:projects/LLM-Infra/beellama.cpp/docs/android.md`
- **Raw:** `[[raw/local/android-c12740dad5.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Android ## Build GUI binding using Android Studio Import the `examples/llama.android` directory into Android Studio, then perform a Gradle sync and build the project. ![Project imported into Android Studio](./android/imported-into-android-studio.jpg) This Android binding supports hardware acceleration up to `SME2` for **Arm** and `AMX` for **x86-64** CPUs on Android and ChromeOS devices. It automatically detects the host's hardware to load compatible kernels. As a result, it runs seamlessly on both the latest premium devices and older devices that may lack modern CPU features or have limited RAM, without requiring any manual configuration. A minimal Android app frontend is included to…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp-tq3/docs/android.md`, `local:projects/LLM-Infra/llama.cpp-atomic/docs/android.md`

### README
- **Source:** `local:.hermes/wiki/topics/pocket-shop/README.md`
- **Raw:** `[[raw/local/readme-2a2e3e8b66.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- title: Pocket Shop created: 2026-07-07 updated: 2026-07-07 type: topic tags: [pocket-shop, app, project] --- # Pocket Shop > Pocket Shop app — all versions and related work consolidated. ## Directories | Dir | What | |---|---| | `~/projects/pocket-shop/` | Main project | | `~/projects/pocket_shop/` | Variant | | `~/projects/pocket-shop-hackathon/` | Hackathon version | | `~/projects/pocket-shop-update/` | Update branch | | `~/pocket-shop/` | Root working copy | | `~/pocket-shop-hackathon/` | Root hackathon copy | | `~/pocket-shop-update/` | Root update copy | | `~/.pocket-shop/` | Config/cache |

### README
- **Source:** `local:.hermes/wiki/topics/dev-lab/README.md`
- **Raw:** `[[raw/local/readme-b7e667fcba.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- title: Dev Lab created: 2026-07-07 updated: 2026-07-07 type: topic tags: [dev, experiments, side-projects] --- # Dev Lab > Experimental and side projects. Dev tools, experiments, misc. ## Projects | Dir | What | |---|---| | `~/projects/Finance/` | Finance tools | | `~/projects/Hardware/` | Hardware projects | | `~/projects/Research/` | Research projects | | `~/projects/Media/` | Media projects | | `~/projects/Mobile/` | Mobile projects | | `~/projects/Web/` | Web projects | | `~/projects/videos/` | Video projects | | `~/MTG-store/` | MTG card store | | `~/guacamole/` | Guacamole | | `~/gepa/` | GEPA experiments | | `~/comfy/` | ComfyUI workflows | | `~/go/` | Go projects | |…

### 1507436311047573604-chat4000---iPhone-Mac-CLI-native-client--no-tailscale
- **Source:** `discord-archive:archives/community-projects-showcase/1507436311047573604-chat4000---iPhone-Mac-CLI-native-client--no-tailscale.txt`
- **Raw:** `[[raw/discord/1507436311047573604-chat4000---iphone-mac-cli-native-client--no-tailscale-a8f0b9f454.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'chat4000 - iPhone/Mac/CLI native client (no tailscale)' in forum #community-projects-showcase # thread_id=1507436311047573604 forum_id=1316137596535177246 # Started 2026-05-22T19:42:07.304449+00:00 [2026-05-22T17:33:43.366000+00:00] haimbender (id=1507436311047573604) Built a fully native iPhone, Mac, and CLI chat client for Hermes — same conversation across every device, E2E encrypted, no account, free, open source. Think "iMessage for your AI agent." Action Button on iPhone: map it to chat4000 and one press from the lock screen jumps straight into chat — hold to dictate, release to send, or type instead. No unlock → find chat → tap → type. E2E-encrypted relay built in — no…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1507436311047573604-chat4000---iPhone-Mac-CLI-native-client--no-tailscale.txt`

### 1522460849938235552-Little-Graph-View-for-my-local-semantic-search-app
- **Source:** `discord-archive:archives/community-projects-showcase/1522460849938235552-Little-Graph-View-for-my-local-semantic-search-app.txt`
- **Raw:** `[[raw/discord/1522460849938235552-little-graph-view-for-my-local-semantic-search-app-a77bde4862.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Little Graph View for my local semantic search app' in forum #community-projects-showcase # thread_id=1522460849938235552 forum_id=1316137596535177246 # Started 2026-07-03T08:58:58.211732+00:00 [2026-07-03T04:35:52.580000+00:00] curiousclump. (id=1522460849938235552) Hey everybody! I built a graph view for my semantic search app. about 98% of the nodes in the graph are image files. Each edge/connection, is made if two images have a similarity threshold greater than .78. So as you can see, clusters and populated areas start to form where there are more similar images, allowing users to grasp a birds eye view of their personal archive. There is also a auto cluster algorithm behind…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1522460849938235552-Little-Graph-View-for-my-local-semantic-search-app.txt`

### unrealclientprotocol-ue5
- **Source:** `local:research/crow-lore/hermes-unreal58-mcp-llm-wiki/raw/unrealclientprotocol-ue5.md`
- **Raw:** `[[raw/local/unrealclientprotocol-ue5-6514b8581a.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- source_url: https://skillsllm.com/skill/unrealclientprotocol ingested: 2026-07-02 sha256: <not extracted — flagged as lead> --- # skillsllm.com — UnrealClientProtocol Web-search description: > "Lightweight UE5 plugin that exposes Unreal Engine's reflection system over TCP+JSON — let AI agents call UFunctions, read/write UProperties." ## Why it's relevant An alternative approach: skip MCP entirely and expose UE5's own reflection system directly to agents. Relevant if: - Hermes grows a custom TCP+JSON client - Someone wants to avoid the MCP protocol overhead ## TODO Extract the skillsllm.com entry. Look for: - Protocol details - What reflection surface is exposed - Whether any of it…

### strayspark-procedural-level-design
- **Source:** `local:research/crow-lore/hermes-unreal58-mcp-llm-wiki/raw/strayspark-procedural-level-design.md`
- **Raw:** `[[raw/local/strayspark-procedural-level-design-1f85228f3c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- source_url: https://www.strayspark.studio/blog/ai-assisted-procedural-level-design-ue5-mcp ingested: 2026-07-02 sha256: <not extracted — flagged as lead> --- # StraySpark blog — "AI-Assisted Procedural Level Design in UE5 with MCP" Web-search description: > "The Unreal MCP Server provides 305 tools across 42+ categories that expose Unreal Editor functionality to AI assistants through the Model Context Protocol." (Note: "305 tools / 42+ categories" is an older build; v4.5 is the current count of 400+ / 60.) ## Why it's relevant to this stack The closest thing to an existing worked example of an agent driving Unreal Editor via MCP to do level-design tasks. Would directly inform a future…

### strayspark-product-page
- **Source:** `local:research/crow-lore/hermes-unreal58-mcp-llm-wiki/raw/strayspark-product-page.md`
- **Raw:** `[[raw/local/strayspark-product-page-cd829ad681.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- source_url: https://www.strayspark.studio/products/unreal-mcp-server ingested: 2026-07-02 sha256: <not computed — extracted fully in web_extract> --- # StraySpark — Unreal MCP Server product page (v4.5, UE 5.7/5.8) Vendor product page. Key claims: - 400+ editor tools, 60 categories, 15 context resources, 18 workflow prompts (v4.5 UE 5.8) - 370+ editor tools, 54 categories (v4 UE 5.7) - Catalog mode: ~3K tokens at session start vs ~60K full list; 4 meta-tools - `run_tool_script`: multi-step tool programs as ONE editor transaction, one Ctrl+Z - SSE streaming on `GET /mcp` + pollable background tasks - Closed-loop Blueprint editing: `describe_graph`, `get_execution_paths`,…

### epic-unreal-mcp-docs
- **Source:** `local:research/crow-lore/hermes-unreal58-mcp-llm-wiki/raw/epic-unreal-mcp-docs.md`
- **Raw:** `[[raw/local/epic-unreal-mcp-docs-38b299294e.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- source_url: https://dev.epicgames.com/documentation/unreal-engine/unreal-mcp-in-unreal-editor?lang=en-US ingested: 2026-07-02 sha256: <computed at ingest time; full text is 25,950 clean chars, truncated in web_extract at 14,588> --- # Epic — Unreal MCP in Unreal Editor (UE 5.8) Primary authoritative documentation for Epic's first-party MCP server. Extracted ~14.5K chars head-of-page covering: - Definition of MCP (tools / resources / prompts, three primitives) - The ModelContextProtocol plugin and its ToolsetRegistry / AllToolsets siblings - Setup path (enable plugin → auto-start → GenerateClientConfig → launch client from project root) - Supported clients: ClaudeCode, Cursor, VSCode,…

### vp-land-ue58-mcp
- **Source:** `local:research/crow-lore/hermes-unreal58-mcp-llm-wiki/raw/vp-land-ue58-mcp.md`
- **Raw:** `[[raw/local/vp-land-ue58-mcp-95320ac01d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- source_url: https://www.vp-land.com/p/unreal-engine-5-8-embeds-an-mcp-server-so-ai-agents-can-drive-the-editor ingested: 2026-07-02 sha256: <not computed — article extracted fully in web_extract> --- # VP-Land — "Unreal Engine 5.8 Embeds an MCP Server So AI Agents Can Drive the Editor" (Jun 24 2026) Newsletter from VP-Land (virtual-production focused). Key claims, all quoting Epic's docs or naming external sources: - "AI agents can touch the editor" — a shift from *suggesting* steps to *executing* them. - "Spawning actors, configuring lighting, creating material instances, inspecting Slate widgets, and running automation tests are all exposed as MCP Tools." - "Unreal MCP is built on a…

### epic-first-party-vs-strayspark
- **Source:** `local:research/crow-lore/hermes-unreal58-mcp-llm-wiki/comparisons/epic-first-party-vs-strayspark.md`
- **Raw:** `[[raw/local/epic-first-party-vs-strayspark-beac4e6133.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- title: Epic first-party Unreal MCP vs. StraySpark v4.5 created: 2026-07-02 updated: 2026-07-02 type: comparison tags: [unreal-engine, mcp, comparison] sources: [raw/epic-unreal-mcp-docs.md, raw/strayspark-product-page.md, raw/vp-land-ue58-mcp.md] confidence: high contested: false --- # Epic first-party Unreal MCP vs. StraySpark v4.5 | Dimension | Epic first-party (`ModelContextProtocol` plugin) | StraySpark Unreal MCP Server v4.5 | |---|---|---| | Status | Experimental | Production-ready, commercial-licensed | | Engine builds | UE 5.8 (with 5.5–5.7 docs branches) | UE 5.7 *and* 5.8 in one download | | Shipped tools | 4 named toolsets (`SceneTools`, `ActorTools`, `MaterialInstanceTools`,…

### game-thread-serialization
- **Source:** `local:research/crow-lore/hermes-unreal58-mcp-llm-wiki/concepts/game-thread-serialization.md`
- **Raw:** `[[raw/local/game-thread-serialization-2757cd840c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- title: Game-thread serialization (Unreal MCP) created: 2026-07-02 updated: 2026-07-02 type: concept tags: [unreal-engine, mcp, concurrency] sources: [raw/epic-unreal-mcp-docs.md, raw/vp-land-ue58-mcp.md] confidence: high contested: false --- # Game-thread serialization A core constraint of Unreal MCP: **tool invocations are marshaled onto Unreal's game thread and run serially.** Clients are told explicitly: *"should not issue overlapping Tool calls."* ## Why it exists Unreal's engine runtime is largely single-threaded on the game thread. Calling arbitrary engine functions from a background thread would corrupt data, crash the editor, or race against tick. So the MCP server accepts HTTP…

### unreal-5-8-mcp-server
- **Source:** `local:research/crow-lore/hermes-unreal58-mcp-llm-wiki/entities/unreal-5-8-mcp-server.md`
- **Raw:** `[[raw/local/unreal-5-8-mcp-server-c9d3e69bcc.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- title: Unreal 5.8 MCP Server (Epic first-party, "Unreal MCP") created: 2026-07-02 updated: 2026-07-02 type: entity tags: [unreal-engine, mcp, epic-games, game-engine, plugin] sources: [raw/epic-unreal-mcp-docs.md, raw/vp-land-ue58-mcp.md] confidence: high contested: false --- # Unreal 5.8 MCP Server The **official first-party MCP server** that Epic Games ships *inside* the Unreal Editor, starting with UE 5.8 (experimental backported to 5.5–5.7 docs branches). Plugin identifier: `ModelContextProtocol`. Friendly name in the Plugin Browser: **Unreal MCP**. ## What it exposes - An MCP-compliant server running *inside* the editor process on `http://127.0.0.1:8000/mcp` (port and path…

### toolset-registry
- **Source:** `local:research/crow-lore/hermes-unreal58-mcp-llm-wiki/entities/toolset-registry.md`
- **Raw:** `[[raw/local/toolset-registry-b053b59f63.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- title: ToolsetRegistry / AllToolsets (UE 5.8 plugin architecture) created: 2026-07-02 updated: 2026-07-02 type: entity tags: [unreal-engine, plugin, mcp, architecture] sources: [raw/epic-unreal-mcp-docs.md] confidence: high contested: false --- # ToolsetRegistry / AllToolsets The Unreal Engine plugin architecture that the first-party MCP server sits on top of. It is **separate from** but *used by* the Unreal MCP plugin. ## Role - **ToolsetRegistry** is an engine subsystem (sibling plugin of the same name). It collects every class deriving from `UToolsetDefinition` at startup. - **AllToolsets** is the plugin that *implements* actual Tools. Unreal MCP does **not** implement toolsets…

### restart-loop-detection
- **Source:** `local:research/crow-lore/turbofit-gateway-resilience/concepts/restart-loop-detection.md`
- **Raw:** `[[raw/local/restart-loop-detection-227785e34f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Restart Loop Detection & Recovery **Category**: Operational Resilience **Applicability**: Kubernetes, systemd, container orchestration **Sources**: Sysdig, Kubernetes docs, MeteorOps, Samir Behara ## Definition A restart loop occurs when a service repeatedly crashes and restarts, often due to misconfiguration, resource constraints, or dependency failures. Detection and recovery require distinguishing between transient failures and persistent problems. ## Kubernetes CrashLoopBackOff ### What It Is **CrashLoopBackOff** is a Kubernetes state indicating a pod is in a restart loop: - Container starts - Crashes or exits - Kubernetes restarts it (based on `restartPolicy: Always`) - Cycle repeats…

### health-checks
- **Source:** `local:research/crow-lore/turbofit-gateway-resilience/concepts/health-checks.md`
- **Raw:** `[[raw/local/health-checks-fb88464e69.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Health Checks **Category**: Operational Resilience **Applicability**: Service health monitoring, orchestration probes **Sources**: MeteorOps, Kubernetes docs, AWS, Microsoft Azure ## Definition Health checks are endpoints or probes that determine whether a service is alive, ready to serve traffic, or has completed initialization. Proper health check design prevents false positives (restarting healthy services) and false negatives (not detecting failures). ## Three Types of Health Checks ### 1. Startup Probe (`/startupz`) **Purpose**: Detects when application has finished initializing. **When used**: Slow-starting applications (Java, large model loading, cache warming). **Behavior**: -…

### timeout-management
- **Source:** `local:research/crow-lore/turbofit-gateway-resilience/concepts/timeout-management.md`
- **Raw:** `[[raw/local/timeout-management-70f09d5436.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Timeout Management **Category**: Resilience Pattern **Applicability**: Preventing resource exhaustion from slow/hanging backends **Sources**: Microsoft Azure, Zuplo, Dev.to, AWS, MeteorOps ## Definition Timeouts are time limits on how long to wait for operations to complete. Without timeouts, hung backends silently consume connections until the entire system fails. ## Types of Timeouts ### 1. Connection Timeout How long to wait for TCP connection to be established. **Typical values**: 1-5 seconds **Rationale**: If backend isn't accepting connections, waiting longer won't help. **Example**: ### 2. Read Timeout (Idle Timeout) How long to wait for response after connection established.…

### widget-composition
- **Source:** `local:research/crow-lore/custom-hermes-tui/concepts/widget-composition.md`
- **Raw:** `[[raw/local/widget-composition-14b310ca7d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Widget Composition **Concept** | UI architecture pattern **Widget composition** is the practice of building complex user interfaces by combining small, reusable components (widgets) into larger structures. In TUI frameworks, widgets are the building blocks — buttons, inputs, panels, lists — that are arranged in layouts to create the overall interface. ## How It Works 1. **Atomic widgets** — smallest units (button, label, input) 2. **Container widgets** — arrange child widgets (vertical, horizontal, grid) 3. **Layout rules** — define how containers size and position children 4. **Nesting** — containers can contain other containers ## In TUI Frameworks | Framework | Composition Model |…

### alternate-screen
- **Source:** `local:research/crow-lore/custom-hermes-tui/concepts/alternate-screen.md`
- **Raw:** `[[raw/local/alternate-screen-7b03cd1081.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Alternate Screen **Concept** | Terminal feature The **alternate screen** is a secondary terminal buffer that allows full-screen applications to render without cluttering the user's scrollback history. When the app exits, the terminal switches back to the main screen, restoring the previous content. ## How It Works 1. **Enter alternate screen** — send escape sequence `\x1b[?1049h` 2. **Render UI** — draw widgets, handle input, update display 3. **Exit alternate screen** — send escape sequence `\x1b[?1049l` 4. **Restore main screen** — previous terminal content reappears ## Differential Updates Modern TUIs use **differential rendering** — only redraw parts of the screen that changed, not…

### 1520294125260509274-Liminal--the-GAME-ENGINE-for-agents
- **Source:** `discord-archive:archives/community-projects-showcase/1520294125260509274-Liminal--the-GAME-ENGINE-for-agents.txt`
- **Raw:** `[[raw/discord/1520294125260509274-liminal--the-game-engine-for-agents-b464ad01fc.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Liminal, the GAME ENGINE for agents' in forum #community-projects-showcase # thread_id=1520294125260509274 forum_id=1316137596535177246 # Started 2026-06-27T08:33:25.607045+00:00 [2026-06-27T05:06:05.161000+00:00] gloggers (id=1520294125260509274) I've always loved game development, and with the innovation of agentic development, what better idea than to give Claude (or any other MCP compatible harness) its own game development environment! My friend and I created a game engine for agents, "Liminal". Completely free and open-source, Liminal has MCP integration, Skills for development, one-click static platform builds, a Unity-like scene editor with Cameras, an element inspector,…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1520294125260509274-Liminal--the-GAME-ENGINE-for-agents.txt`

### build-android
- **Source:** `local:projects/LLM-Infra/llama.cpp-atomic/.github/workflows/build-android.yml`
- **Raw:** `[[raw/local/build-android-1cb0dcdc27.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: CI (android) on: workflow_dispatch: push: branches: - master paths: - '.github/workflows/build-android.yml' - '**/CMakeLists.txt' - '**/.cmake' - '**/*.h' - '**/*.hpp' - '**/*.c' - '**/*.cpp' pull_request: types: [opened, synchronize, reopened] paths: - '.github/workflows/build-android.yml' - 'examples/llama.android/**' concurrency: group: ${{ github.workflow }}-${{ github.head_ref && github.ref || github.run_id }} cancel-in-progress: true env: GGML_NLOOP: 3 GGML_N_THREADS: 1 LLAMA_ARG_LOG_COLORS: 1 LLAMA_ARG_LOG_PREFIX: 1 LLAMA_ARG_LOG_TIMESTAMPS: 1 jobs: default: runs-on: ubuntu-latest steps: - name: Clone uses: actions/checkout@v6 with: fetch-depth: 0 lfs: false - name: Set up JDK…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/.github/workflows/build-android.yml`

### android
- **Source:** `local:projects/LLM-Infra/llama.cpp/docs/android.md`
- **Raw:** `[[raw/local/android-56a4c79995.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Android ## Build GUI binding using Android Studio Import the `examples/llama.android` directory into Android Studio, then perform a Gradle sync and build the project. ![Project imported into Android Studio](./android/imported-into-android-studio.jpg) This Android binding supports hardware acceleration up to `SME2` for **Arm** and `AMX` for **x86-64** CPUs on Android and ChromeOS devices. It automatically detects the host's hardware to load compatible kernels. As a result, it runs seamlessly on both the latest premium devices and older devices that may lack modern CPU features or have limited RAM, without requiring any manual configuration. A minimal Android app frontend is included to…

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills/software-development/simplify-code/SKILL.md`
- **Raw:** `[[raw/local/skill-5549142eb2.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: simplify-code description: "Parallel 3-agent cleanup of recent code changes." version: 1.0.0 author: Hermes Agent (inspired by Claude Code /simplify) license: MIT platforms: [linux, macos, windows] metadata: hermes: tags: [code-review, cleanup, refactor, delegation, subagent, parallel, simplify] related_skills: [requesting-code-review, test-driven-development, plan] --- # Simplify Code — Parallel Review & Cleanup Review your recent code changes with three focused reviewers running in parallel, aggregate their findings, and apply the fixes worth applying. **Core principle:** Three narrow reviewers beat one broad reviewer. Each one deeply searches the codebase for a single class of…

- **Collapsed duplicates:** `local:projects/klerik/skills/software-development/simplify-code/SKILL.md`, `local:projects/jestur/skills/software-development/simplify-code/SKILL.md`, `local:projects/dev-coder/skills/software-development/simplify-code/SKILL.md`, `local:projects/dev-orch/skills/software-development/simplify-code/SKILL.md`, `local:projects/dev-review/skills/software-development/simplify-code/SKILL.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills/social-media/xurl/SKILL.md`
- **Raw:** `[[raw/local/skill-8b1899dc71.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: xurl description: "X/Twitter via xurl CLI: post, search, DM, media, v2 API." version: 1.1.1 author: xdevplatform + openclaw + Hermes Agent license: MIT platforms: [linux, macos] prerequisites: commands: [xurl] metadata: hermes: tags: [twitter, x, social-media, xurl, official-api] homepage: https://github.com/xdevplatform/xurl upstream_skill: https://github.com/openclaw/openclaw/blob/main/skills/xurl/SKILL.md --- # xurl — X (Twitter) API via the Official CLI `xurl` is the X developer platform's official CLI for the X API. It supports shortcut commands for common actions AND raw curl-style access to any v2 endpoint. All commands return JSON to stdout. Use this skill for: - posting,…

- **Collapsed duplicates:** `local:projects/klerik/skills/social-media/xurl/SKILL.md`, `local:projects/jestur/skills/social-media/xurl/SKILL.md`, `local:projects/dev-coder/skills/social-media/xurl/SKILL.md`, `local:projects/dev-orch/skills/social-media/xurl/SKILL.md`, `local:projects/dev-review/skills/social-media/xurl/SKILL.md`

### formatting
- **Source:** `local:projects/southpaw/klerik/skills/research/research-paper-writing/templates/acl/formatting.md`
- **Raw:** `[[raw/local/formatting-9e004a136c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Instructions for *ACL Proceedings The following instructions are for authors of papers submitted for review to ACL conferences (hereafter, "review version") or paper accepted for publication in its proceedings (hereafter, "final version"). All authors are required to adhere to these specifications. ## Style Files *ACL provides style files for LaTeX and Microsoft Word that meet these requirements. They can be found at: > https://acl-org.github.io/ACLPUB/ We strongly recommend the use of these style files, which have been appropriately tailored for the *ACL proceedings. ## Paper Length The conference accepts submissions of long papers and short papers. Review versions of long papers may…

- **Collapsed duplicates:** `local:projects/klerik/skills/research/research-paper-writing/templates/acl/formatting.md`, `local:projects/jestur/skills/research/research-paper-writing/templates/acl/formatting.md`, `local:projects/dev-coder/skills/research/research-paper-writing/templates/acl/formatting.md`, `local:projects/dev-orch/skills/research/research-paper-writing/templates/acl/formatting.md`, `local:projects/dev-review/skills/research/research-paper-writing/templates/acl/formatting.md`

### README
- **Source:** `local:projects/southpaw/klerik/skills/research/research-paper-writing/templates/aaai2026/README.md`
- **Raw:** `[[raw/local/readme-ee2c61a8b0.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # AAAI 2026 统一LaTeX模板使用说明 / AAAI 2026 Unified LaTeX Template Guide > **📝 重要说明 / Important Notice**: 本仓库借助Cursor在AAAI 2026官方模板基础上改进得到。如果遇到不满足或有冲突的情况，请积极提issues。 > > **📝 Important Notice**: This repository is improved based on the official AAAI 2026 template with the assistance of Cursor. If you encounter any issues or conflicts, please actively submit issues. [中文](#中文版本) | [English](#english-version) --- ## 🌐 在线查看 / Online Access **📖 在线阅读和测试模板**: [https://cn.overleaf.com/read/wyhcnvcrtpyt#cd4a07](https://cn.overleaf.com/read/wyhcnvcrtpyt#cd4a07) **📖 Online View and Test Template**: [https://cn.overleaf.com/read/wyhcnvcrtpyt#cd4a07](https://cn.overleaf.com/read/wyhcnvcrtpyt#cd4a07) 💡 **提示 /…

- **Collapsed duplicates:** `local:projects/klerik/skills/research/research-paper-writing/templates/aaai2026/README.md`, `local:projects/jestur/skills/research/research-paper-writing/templates/aaai2026/README.md`, `local:projects/dev-coder/skills/research/research-paper-writing/templates/aaai2026/README.md`, `local:projects/dev-orch/skills/research/research-paper-writing/templates/aaai2026/README.md`, `local:projects/dev-review/skills/research/research-paper-writing/templates/aaai2026/README.md`

### README
- **Source:** `local:projects/southpaw/klerik/skills/research/research-paper-writing/templates/README.md`
- **Raw:** `[[raw/local/readme-e65dc1a22c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # LaTeX Templates for ML/AI Conferences This directory contains official LaTeX templates for major machine learning and AI conferences. --- ## Compiling LaTeX to PDF ### Option 1: VS Code with LaTeX Workshop (Recommended) **Setup:** 1. Install [TeX Live](https://www.tug.org/texlive/) (full distribution recommended) - macOS: `brew install --cask mactex` - Ubuntu: `sudo apt install texlive-full` - Windows: Download from [tug.org/texlive](https://www.tug.org/texlive/) 2. Install VS Code extension: **LaTeX Workshop** by James Yu - Open VS Code → Extensions (Cmd/Ctrl+Shift+X) → Search "LaTeX Workshop" → Install **Usage:** - Open any `.tex` file in VS Code - Save the file (Cmd/Ctrl+S) →…

- **Collapsed duplicates:** `local:projects/klerik/skills/research/research-paper-writing/templates/README.md`, `local:projects/jestur/skills/research/research-paper-writing/templates/README.md`, `local:projects/dev-coder/skills/research/research-paper-writing/templates/README.md`, `local:projects/dev-orch/skills/research/research-paper-writing/templates/README.md`, `local:projects/dev-review/skills/research/research-paper-writing/templates/README.md`

### citation-workflow
- **Source:** `local:projects/southpaw/klerik/skills/research/research-paper-writing/references/citation-workflow.md`
- **Raw:** `[[raw/local/citation-workflow-47bfe2432e.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Citation Management & Hallucination Prevention This reference provides a complete workflow for managing citations programmatically, preventing AI-generated citation hallucinations, and maintaining clean bibliographies. --- ## Contents - [Why Citation Verification Matters](#why-citation-verification-matters) - [Citation APIs Overview](#citation-apis-overview) - [Verified Citation Workflow](#verified-citation-workflow) - [Python Implementation](#python-implementation) - [BibTeX Management](#bibtex-management) - [Common Citation Formats](#common-citation-formats) - [Troubleshooting](#troubleshooting) --- ## Why Citation Verification Matters ### The Hallucination Problem Research has…

- **Collapsed duplicates:** `local:projects/klerik/skills/research/research-paper-writing/references/citation-workflow.md`, `local:projects/jestur/skills/research/research-paper-writing/references/citation-workflow.md`, `local:projects/dev-coder/skills/research/research-paper-writing/references/citation-workflow.md`, `local:projects/dev-orch/skills/research/research-paper-writing/references/citation-workflow.md`, `local:projects/dev-review/skills/research/research-paper-writing/references/citation-workflow.md`

### reviewer-guidelines
- **Source:** `local:projects/southpaw/klerik/skills/research/research-paper-writing/references/reviewer-guidelines.md`
- **Raw:** `[[raw/local/reviewer-guidelines-c1786ab39e.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Reviewer Guidelines & Evaluation Criteria This reference documents how reviewers evaluate papers at major ML/AI conferences, helping authors anticipate and address reviewer concerns. --- ## Contents - [Universal Evaluation Dimensions](#universal-evaluation-dimensions) - [NeurIPS Reviewer Guidelines](#neurips-reviewer-guidelines) - [ICML Reviewer Guidelines](#icml-reviewer-guidelines) - [ICLR Reviewer Guidelines](#iclr-reviewer-guidelines) - [ACL Reviewer Guidelines](#acl-reviewer-guidelines) - [What Makes Reviews Strong](#what-makes-reviews-strong) - [Common Reviewer Concerns](#common-reviewer-concerns) - [How to Address Reviewer Feedback](#how-to-address-reviewer-feedback) --- ##…

- **Collapsed duplicates:** `local:projects/klerik/skills/research/research-paper-writing/references/reviewer-guidelines.md`, `local:projects/jestur/skills/research/research-paper-writing/references/reviewer-guidelines.md`, `local:projects/dev-coder/skills/research/research-paper-writing/references/reviewer-guidelines.md`, `local:projects/dev-orch/skills/research/research-paper-writing/references/reviewer-guidelines.md`, `local:projects/dev-review/skills/research/research-paper-writing/references/reviewer-guidelines.md`

### experiment-patterns
- **Source:** `local:projects/southpaw/klerik/skills/research/research-paper-writing/references/experiment-patterns.md`
- **Raw:** `[[raw/local/experiment-patterns-1904faa8ac.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Experiment Design Patterns Patterns and best practices distilled from running research experiments at scale with the Hermes agent. These cover experiment infrastructure, evaluation protocols, monitoring, and failure recovery. --- ## Experiment Infrastructure ### Directory Structure Organize experiments with a consistent structure: ### Script Design Principles **1. Incremental Saving (Crash Recovery)** Every experiment script should save results after each unit of work, and skip already-completed work on restart: This pattern makes re-runs safe and efficient. If a process crashes at problem 47/150, restarting skips the first 46. **2. Artifact Preservation** Save all intermediate outputs,…

- **Collapsed duplicates:** `local:projects/klerik/skills/research/research-paper-writing/references/experiment-patterns.md`, `local:projects/jestur/skills/research/research-paper-writing/references/experiment-patterns.md`, `local:projects/dev-coder/skills/research/research-paper-writing/references/experiment-patterns.md`, `local:projects/dev-orch/skills/research/research-paper-writing/references/experiment-patterns.md`, `local:projects/dev-review/skills/research/research-paper-writing/references/experiment-patterns.md`

### human-evaluation
- **Source:** `local:projects/southpaw/klerik/skills/research/research-paper-writing/references/human-evaluation.md`
- **Raw:** `[[raw/local/human-evaluation-073275dbe8.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Human Evaluation Guide for ML/AI Research Comprehensive guide for designing, running, and reporting human evaluations in ML/AI papers. Human evaluation is the primary evidence for many NLP, HCI, and alignment papers, and is increasingly expected as complementary evidence at all ML venues. --- ## Contents - [When Human Evaluation Is Needed](#when-human-evaluation-is-needed) - [Study Design](#study-design) - [Annotation Guidelines](#annotation-guidelines) - [Platforms and Recruitment](#platforms-and-recruitment) - [Quality Control](#quality-control) - [Agreement Metrics](#agreement-metrics) - [Statistical Analysis for Human Eval](#statistical-analysis-for-human-eval) - [Reporting…

- **Collapsed duplicates:** `local:projects/klerik/skills/research/research-paper-writing/references/human-evaluation.md`, `local:projects/jestur/skills/research/research-paper-writing/references/human-evaluation.md`, `local:projects/dev-coder/skills/research/research-paper-writing/references/human-evaluation.md`, `local:projects/dev-orch/skills/research/research-paper-writing/references/human-evaluation.md`, `local:projects/dev-review/skills/research/research-paper-writing/references/human-evaluation.md`

### refusal-detection
- **Source:** `local:projects/southpaw/klerik/skills/red-teaming/godmode/references/refusal-detection.md`
- **Raw:** `[[raw/local/refusal-detection-1347f7cbfe.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Refusal Detection & Response Scoring Ported from G0DM0D3's Tastemaker scoring system. Use these patterns to detect whether a model refused, hedged, or complied. ## Hard Refusal Patterns (auto-reject, score = -9999) These patterns indicate the model fully refused the request: ### Direct refusals - `I cannot/can't/won't/will not/am not able to/refuse to/am unable to` - `I'm sorry, but I cannot/can't/won't/am unable` - `apologize/sorry, but I/this/that cannot/can't/isn't/won't` - `I must/have to/need to refuse/decline/reject/refrain` - `not able/going/willing/permitted/allowed to provide/help/assist/give/create/generate` - `can't/cannot/won't/unable to…

- **Collapsed duplicates:** `local:projects/klerik/skills/red-teaming/godmode/references/refusal-detection.md`, `local:projects/jestur/skills/red-teaming/godmode/references/refusal-detection.md`, `local:projects/dev-coder/skills/red-teaming/godmode/references/refusal-detection.md`, `local:projects/dev-orch/skills/red-teaming/godmode/references/refusal-detection.md`, `local:projects/dev-review/skills/red-teaming/godmode/references/refusal-detection.md`

### LICENSE
- **Source:** `local:projects/southpaw/klerik/skills/productivity/powerpoint/LICENSE.txt`
- **Raw:** `[[raw/local/license-79f6d8f5b4.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** © 2025 Anthropic, PBC. All rights reserved. LICENSE: Use of these materials (including all code, prompts, assets, files, and other components of this Skill) is governed by your agreement with Anthropic regarding use of Anthropic's services. If no separate agreement exists, use is governed by Anthropic's Consumer Terms of Service or Commercial Terms of Service, as applicable: https://www.anthropic.com/legal/consumer-terms https://www.anthropic.com/legal/commercial-terms Your applicable agreement is referred to as the "Agreement." "Services" are as defined in the Agreement. ADDITIONAL RESTRICTIONS: Notwithstanding anything in the Agreement to the contrary, users may not: - Extract these…

- **Collapsed duplicates:** `local:projects/klerik/skills/productivity/powerpoint/LICENSE.txt`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills/productivity/linear/SKILL.md`
- **Raw:** `[[raw/local/skill-2071471d64.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: linear description: "Linear: manage issues, projects, teams via GraphQL + curl." version: 1.0.0 author: Hermes Agent license: MIT platforms: [linux, macos, windows] prerequisites: env_vars: [LINEAR_API_KEY] commands: [curl] metadata: hermes: tags: [Linear, Project Management, Issues, GraphQL, API, Productivity] --- # Linear — Issue & Project Management Manage Linear issues, projects, and teams directly via the GraphQL API using `curl`. No MCP server, no OAuth flow, no extra dependencies. ## Setup 1. Get a personal API key from **Linear Settings > Account > Security & access > Personal API keys** (URL: https://linear.app/settings/account/security). Note: the org-level *Settings >…

- **Collapsed duplicates:** `local:projects/klerik/skills/productivity/linear/SKILL.md`, `local:projects/jestur/skills/productivity/linear/SKILL.md`, `local:projects/dev-coder/skills/productivity/linear/SKILL.md`, `local:projects/dev-orch/skills/productivity/linear/SKILL.md`, `local:projects/dev-review/skills/productivity/linear/SKILL.md`

### output-formats
- **Source:** `local:projects/southpaw/klerik/skills/media/youtube-content/references/output-formats.md`
- **Raw:** `[[raw/local/output-formats-f24e6939b4.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Output Format Examples ## Chapters ## Summary A 5-10 sentence overview covering the video's main points, key arguments, and conclusions. Written in third person, present tense. ## Chapter Summaries ## Thread (Twitter/X) ## Blog Post Full article with: - Title - Introduction paragraph - H2 sections for each major topic - Key quotes (with timestamps) - Conclusion / takeaways ## Quotes

- **Collapsed duplicates:** `local:projects/klerik/skills/media/youtube-content/references/output-formats.md`, `local:projects/jestur/skills/media/youtube-content/references/output-formats.md`, `local:projects/dev-coder/skills/media/youtube-content/references/output-formats.md`, `local:projects/dev-orch/skills/media/youtube-content/references/output-formats.md`, `local:projects/dev-review/skills/media/youtube-content/references/output-formats.md`

### bug-report
- **Source:** `local:projects/southpaw/klerik/skills/github/github-issues/templates/bug-report.md`
- **Raw:** `[[raw/local/bug-report-4b3144ccf4.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** ## Bug Description <!-- Clear, concise description of the bug --> ## Steps to Reproduce 1. 2. 3. ## Expected Behavior <!-- What should happen --> ## Actual Behavior <!-- What actually happens --> ## Environment - OS: - Version/Commit: - Python version: - Browser (if applicable): ## Error Output <!-- Paste relevant error messages, stack traces, or logs --> ## Additional Context <!-- Screenshots, related issues, workarounds discovered, etc. -->

- **Collapsed duplicates:** `local:projects/klerik/skills/github/github-issues/templates/bug-report.md`, `local:projects/jestur/skills/github/github-issues/templates/bug-report.md`, `local:projects/dev-coder/skills/github/github-issues/templates/bug-report.md`, `local:projects/dev-orch/skills/github/github-issues/templates/bug-report.md`, `local:projects/dev-review/skills/github/github-issues/templates/bug-report.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills/gaming/pokemon-player/SKILL.md`
- **Raw:** `[[raw/local/skill-fe8da8e6dc.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: pokemon-player description: "Play Pokemon via headless emulator + RAM reads." tags: [gaming, pokemon, emulator, pyboy, gameplay, gameboy] platforms: [linux, macos, windows] --- # Pokemon Player Play Pokemon games via headless emulation using the `pokemon-agent` package. ## When to Use - User says "play pokemon", "start pokemon", "pokemon game" - User asks about Pokemon Red, Blue, Yellow, FireRed, etc. - User wants to watch an AI play Pokemon - User references a ROM file (.gb, .gbc, .gba) ## Startup Procedure ### 1. First-time setup (clone, venv, install) The repo is NousResearch/pokemon-agent on GitHub. Clone it, then set up a Python 3.10+ virtual environment. Use uv (preferred…

- **Collapsed duplicates:** `local:projects/klerik/skills/gaming/pokemon-player/SKILL.md`, `local:projects/jestur/skills/gaming/pokemon-player/SKILL.md`, `local:projects/dev-coder/skills/gaming/pokemon-player/SKILL.md`, `local:projects/dev-orch/skills/gaming/pokemon-player/SKILL.md`, `local:projects/dev-review/skills/gaming/pokemon-player/SKILL.md`

### configuration
- **Source:** `local:projects/southpaw/klerik/skills/email/himalaya/references/configuration.md`
- **Raw:** `[[raw/local/configuration-ccd540fa96.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Himalaya Configuration Reference Configuration file location: `~/.config/himalaya/config.toml` ## Minimal IMAP + SMTP Setup ## Password Options ### Raw password (testing only, not recommended) ### Password from command (recommended) ### System keyring (requires keyring feature) Then run `himalaya account configure <account>` to store the password. ## Gmail Configuration **Note:** Gmail requires an App Password if 2FA is enabled. ## iCloud Configuration **Note:** Generate an app-specific password at appleid.apple.com ## Folder Aliases Map himalaya's canonical folder names (`inbox`, `sent`, `drafts`, `trash`) to whatever the server actually calls them. Use the v1.2.0 `folder.aliases.X`…

- **Collapsed duplicates:** `local:projects/klerik/skills/email/himalaya/references/configuration.md`, `local:projects/jestur/skills/email/himalaya/references/configuration.md`, `local:projects/dev-coder/skills/email/himalaya/references/configuration.md`, `local:projects/dev-orch/skills/email/himalaya/references/configuration.md`, `local:projects/dev-review/skills/email/himalaya/references/configuration.md`

### dogfood-report-template
- **Source:** `local:projects/southpaw/klerik/skills/dogfood/templates/dogfood-report-template.md`
- **Raw:** `[[raw/local/dogfood-report-template-6db9127715.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Dogfood QA Report **Target:** {target_url} **Date:** {date} **Scope:** {scope_description} **Tester:** Hermes Agent (automated exploratory QA) --- ## Executive Summary | Severity | Count | |----------|-------| | 🔴 Critical | {critical_count} | | 🟠 High | {high_count} | | 🟡 Medium | {medium_count} | | 🔵 Low | {low_count} | | **Total** | **{total_count}** | **Overall Assessment:** {one_sentence_assessment} --- ## Issues <!-- Repeat this section for each issue found, sorted by severity (Critical first) --> ### Issue #{issue_number}: {issue_title} | Field | Value | |-------|-------| | **Severity** | {severity} | | **Category** | {category} | | **URL** | {url_where_found} | **Description:**…

- **Collapsed duplicates:** `local:projects/klerik/skills/dogfood/templates/dogfood-report-template.md`, `local:projects/jestur/skills/dogfood/templates/dogfood-report-template.md`, `local:projects/dev-coder/skills/dogfood/templates/dogfood-report-template.md`, `local:projects/dev-orch/skills/dogfood/templates/dogfood-report-template.md`, `local:projects/dev-review/skills/dogfood/templates/dogfood-report-template.md`

### issue-taxonomy
- **Source:** `local:projects/southpaw/klerik/skills/dogfood/references/issue-taxonomy.md`
- **Raw:** `[[raw/local/issue-taxonomy-b90546fab5.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Issue Taxonomy Use this taxonomy to classify issues found during dogfood QA testing. ## Severity Levels ### Critical The issue makes a core feature completely unusable or causes data loss. **Examples:** - Application crashes or shows a blank white page - Form submission silently loses user data - Authentication is completely broken (can't log in at all) - Payment flow fails and charges the user without completing the order - Security vulnerability (e.g., XSS, exposed credentials in console) ### High The issue significantly impairs functionality but a workaround may exist. **Examples:** - A key button does nothing when clicked (but refreshing fixes it) - Search returns no results for valid…

- **Collapsed duplicates:** `local:projects/klerik/skills/dogfood/references/issue-taxonomy.md`, `local:projects/jestur/skills/dogfood/references/issue-taxonomy.md`, `local:projects/dev-coder/skills/dogfood/references/issue-taxonomy.md`, `local:projects/dev-orch/skills/dogfood/references/issue-taxonomy.md`, `local:projects/dev-review/skills/dogfood/references/issue-taxonomy.md`

### replicator
- **Source:** `local:projects/southpaw/klerik/skills/creative/touchdesigner-mcp/references/replicator.md`
- **Raw:** `[[raw/local/replicator-b17907d2fb.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Replicator COMP Reference The `replicatorCOMP` clones a template operator N times, driven by a table of data. The fundamental TD pattern for data-driven networks: button grids, scene rosters, dynamic UI, parameter panels per-channel. For visual instancing (per-pixel/per-render copies), see `geometry-comp.md`. Replicator builds NETWORK NODES; instancing builds RENDER COPIES. Different layer. --- ## Concept Edit the template once → all clones inherit. Edit the table → clones add/remove dynamically. Push parameter overrides per-row. --- ## Minimal Setup After cooking, the replicator creates 4 child COMPs named `Sunset`, `Midnight`, `Storm`, `Forest` (one per non-header row), each cloned from…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/touchdesigner-mcp/references/replicator.md`, `local:projects/jestur/skills/creative/touchdesigner-mcp/references/replicator.md`, `local:projects/dev-coder/skills/creative/touchdesigner-mcp/references/replicator.md`, `local:projects/dev-orch/skills/creative/touchdesigner-mcp/references/replicator.md`, `local:projects/dev-review/skills/creative/touchdesigner-mcp/references/replicator.md`

### projection-mapping
- **Source:** `local:projects/southpaw/klerik/skills/creative/touchdesigner-mcp/references/projection-mapping.md`
- **Raw:** `[[raw/local/projection-mapping-b5ad7c4cb1.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Projection Mapping Reference Multi-window output, surface mapping, edge blending, and projector calibration patterns for installation/event work. For HUD layouts and on-screen panel grids, see `layout-compositor.md`. For wireframe/test-pattern generation, see `operator-tips.md`. --- ## Window COMP — Output to a Display The `windowCOMP` is how TD pushes pixels to a real display. To target a specific physical display, set `par.location`: Or set absolute coordinates using `winoffsetx/y` matched to your OS display layout. **Always pulse `winopen` — setting params alone doesn't open the window.** --- ## Multi-Window Output For multi-projector or multi-display setups, create one `windowCOMP`…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/touchdesigner-mcp/references/projection-mapping.md`, `local:projects/jestur/skills/creative/touchdesigner-mcp/references/projection-mapping.md`, `local:projects/dev-coder/skills/creative/touchdesigner-mcp/references/projection-mapping.md`, `local:projects/dev-orch/skills/creative/touchdesigner-mcp/references/projection-mapping.md`, `local:projects/dev-review/skills/creative/touchdesigner-mcp/references/projection-mapping.md`

### panel-ui
- **Source:** `local:projects/southpaw/klerik/skills/creative/touchdesigner-mcp/references/panel-ui.md`
- **Raw:** `[[raw/local/panel-ui-3acc029c90.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Panel & UI Reference Interactive control surfaces inside TouchDesigner — buttons, sliders, fields, custom parameter pages, panel callbacks. For HUD overlays (rendered text on visuals) see `layout-compositor.md`. Use cases: - VJ control rack (master fader, scene buttons, FX toggles) - Installation operator console - Self-contained TOX components with their own parameter UIs - Phone-style touch interfaces displayed on a tablet --- ## Two Layers of UI | Layer | What it is | Use for | |---|---|---| | **Custom Parameters** | Params on any COMP, edited like built-in TD params | Configurable components, presets, "settings" panels | | **Panel COMPs** | Visible widgets (button, slider, field)…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/touchdesigner-mcp/references/panel-ui.md`, `local:projects/jestur/skills/creative/touchdesigner-mcp/references/panel-ui.md`, `local:projects/dev-coder/skills/creative/touchdesigner-mcp/references/panel-ui.md`, `local:projects/dev-orch/skills/creative/touchdesigner-mcp/references/panel-ui.md`, `local:projects/dev-review/skills/creative/touchdesigner-mcp/references/panel-ui.md`

### midi-osc
- **Source:** `local:projects/southpaw/klerik/skills/creative/touchdesigner-mcp/references/midi-osc.md`
- **Raw:** `[[raw/local/midi-osc-1e9c8de828.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # MIDI / OSC Reference External controller input and output — MIDI hardware, TouchOSC mobile UIs, OSC routing across the network. For audio-driven MIDI patterns (track triggers from spectrum analysis), see also `audio-reactive.md`. --- ## MIDI Input — Hardware Controllers ### Discovery List connected MIDI devices first. Use a `midiinDAT` to enumerate: Or via Python directly: Verify the API with `td_get_docs(topic='midi')` since this varies between TD versions. ### MIDI In CHOP Standard pattern: Output channels follow the convention `chCcN` and `chCnN`: - `ch1c74` — channel 1, CC 74 - `ch1n60` — channel 1, note 60 (middle C) — value is velocity 0-127 **Map a CC to a parameter:** **Map a note…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/touchdesigner-mcp/references/midi-osc.md`, `local:projects/jestur/skills/creative/touchdesigner-mcp/references/midi-osc.md`, `local:projects/dev-coder/skills/creative/touchdesigner-mcp/references/midi-osc.md`, `local:projects/dev-orch/skills/creative/touchdesigner-mcp/references/midi-osc.md`, `local:projects/dev-review/skills/creative/touchdesigner-mcp/references/midi-osc.md`

### 3d-scene
- **Source:** `local:projects/southpaw/klerik/skills/creative/touchdesigner-mcp/references/3d-scene.md`
- **Raw:** `[[raw/local/3d-scene-f0b17b4383.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # 3D Scene Reference Lighting rigs, shadows, IBL/cubemaps, multi-camera, and PBR materials. For wireframe rendering and feedback TOPs see `operator-tips.md`. For instancing geometry see `geometry-comp.md`. For shader code see `glsl.md`. --- ## Anatomy of a 3D Scene Render TOP is the heart. It takes an explicit `geometry` path, an explicit `camera` path, and lights via the lights table or an envlight reference. --- ## Minimal Scene For multiple lights, leave `par.lights` blank — Render TOP scans the network for all `lightCOMP` and `envlightCOMP` ops by default. To restrict to specific lights, set `par.lights = '/project1/key_light /project1/fill_light'` (space-separated paths). --- ## Light…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/touchdesigner-mcp/references/3d-scene.md`, `local:projects/jestur/skills/creative/touchdesigner-mcp/references/3d-scene.md`, `local:projects/dev-coder/skills/creative/touchdesigner-mcp/references/3d-scene.md`, `local:projects/dev-orch/skills/creative/touchdesigner-mcp/references/3d-scene.md`, `local:projects/dev-review/skills/creative/touchdesigner-mcp/references/3d-scene.md`

### zapier
- **Source:** `local:projects/southpaw/klerik/skills/creative/popular-web-designs/templates/zapier.md`
- **Raw:** `[[raw/local/zapier-9aac8e73a4.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Design System: Zapier > **Hermes Agent — Implementation Notes** > > The original site uses proprietary fonts. For self-contained HTML output, use these CDN substitutes: > - **Primary:** `Inter` | **Mono:** `system monospace stack` > - **Font stack (CSS):** `font-family: 'Inter', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;` > - **Mono stack (CSS):** `font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace;` > > Use `write_file` to create HTML, serve via `generative-widgets` skill (cloudflared tunnel). > Verify visual accuracy with `browser_vision` after generating. ## 1. Visual Theme & Atmosphere Zapier's website…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/popular-web-designs/templates/zapier.md`, `local:projects/jestur/skills/creative/popular-web-designs/templates/zapier.md`, `local:projects/dev-coder/skills/creative/popular-web-designs/templates/zapier.md`, `local:projects/dev-orch/skills/creative/popular-web-designs/templates/zapier.md`, `local:projects/dev-review/skills/creative/popular-web-designs/templates/zapier.md`

### warp
- **Source:** `local:projects/southpaw/klerik/skills/creative/popular-web-designs/templates/warp.md`
- **Raw:** `[[raw/local/warp-0a6569a598.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Design System: Warp > **Hermes Agent — Implementation Notes** > > The original site uses proprietary fonts. For self-contained HTML output, use these CDN substitutes: > - **Primary:** `Geist` | **Mono:** `Geist Mono` > - **Font stack (CSS):** `font-family: 'Geist', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;` > - **Mono stack (CSS):** `font-family: 'Geist Mono', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace;` > > Use `write_file` to create HTML, serve via `generative-widgets` skill (cloudflared tunnel). > Verify visual accuracy with `browser_vision` after generating. ## 1. Visual Theme & Atmosphere Warp's website feels…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/popular-web-designs/templates/warp.md`, `local:projects/jestur/skills/creative/popular-web-designs/templates/warp.md`, `local:projects/dev-coder/skills/creative/popular-web-designs/templates/warp.md`, `local:projects/dev-orch/skills/creative/popular-web-designs/templates/warp.md`, `local:projects/dev-review/skills/creative/popular-web-designs/templates/warp.md`

### superhuman
- **Source:** `local:projects/southpaw/klerik/skills/creative/popular-web-designs/templates/superhuman.md`
- **Raw:** `[[raw/local/superhuman-edbd6f3c17.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Design System: Superhuman > **Hermes Agent — Implementation Notes** > > The original site uses proprietary fonts. For self-contained HTML output, use these CDN substitutes: > - **Primary:** `Inter` | **Mono:** `JetBrains Mono` > - **Font stack (CSS):** `font-family: 'Inter', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;` > - **Mono stack (CSS):** `font-family: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace;` > > Use `write_file` to create HTML, serve via `generative-widgets` skill (cloudflared tunnel). > Verify visual accuracy with `browser_vision` after generating. ## 1. Visual Theme & Atmosphere…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/popular-web-designs/templates/superhuman.md`, `local:projects/jestur/skills/creative/popular-web-designs/templates/superhuman.md`, `local:projects/dev-coder/skills/creative/popular-web-designs/templates/superhuman.md`, `local:projects/dev-orch/skills/creative/popular-web-designs/templates/superhuman.md`, `local:projects/dev-review/skills/creative/popular-web-designs/templates/superhuman.md`

### uber
- **Source:** `local:projects/southpaw/klerik/skills/creative/popular-web-designs/templates/uber.md`
- **Raw:** `[[raw/local/uber-68291d1291.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Design System: Uber > **Hermes Agent — Implementation Notes** > > The original site uses proprietary fonts. For self-contained HTML output, use these CDN substitutes: > - **Primary:** `DM Sans` | **Mono:** `system monospace stack` > - **Font stack (CSS):** `font-family: 'DM Sans', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;` > - **Mono stack (CSS):** `font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace;` > > Use `write_file` to create HTML, serve via `generative-widgets` skill (cloudflared tunnel). > Verify visual accuracy with `browser_vision` after generating. ## 1. Visual Theme & Atmosphere Uber's design language…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/popular-web-designs/templates/uber.md`, `local:projects/jestur/skills/creative/popular-web-designs/templates/uber.md`, `local:projects/dev-coder/skills/creative/popular-web-designs/templates/uber.md`, `local:projects/dev-orch/skills/creative/popular-web-designs/templates/uber.md`, `local:projects/dev-review/skills/creative/popular-web-designs/templates/uber.md`

### sanity
- **Source:** `local:projects/southpaw/klerik/skills/creative/popular-web-designs/templates/sanity.md`
- **Raw:** `[[raw/local/sanity-174ae98a51.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Design System: Sanity > **Hermes Agent — Implementation Notes** > > The original site uses proprietary fonts. For self-contained HTML output, use these CDN substitutes: > - **Primary:** `Space Grotesk` | **Mono:** `IBM Plex Mono` > - **Font stack (CSS):** `font-family: 'Space Grotesk', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;` > - **Mono stack (CSS):** `font-family: 'IBM Plex Mono', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace;` > > Use `write_file` to create HTML, serve via `generative-widgets` skill (cloudflared tunnel). > Verify visual accuracy with `browser_vision` after generating. ## 1. Visual Theme & Atmosphere…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/popular-web-designs/templates/sanity.md`, `local:projects/jestur/skills/creative/popular-web-designs/templates/sanity.md`, `local:projects/dev-coder/skills/creative/popular-web-designs/templates/sanity.md`, `local:projects/dev-orch/skills/creative/popular-web-designs/templates/sanity.md`, `local:projects/dev-review/skills/creative/popular-web-designs/templates/sanity.md`

### revolut
- **Source:** `local:projects/southpaw/klerik/skills/creative/popular-web-designs/templates/revolut.md`
- **Raw:** `[[raw/local/revolut-1d024aa810.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Design System: Revolut > **Hermes Agent — Implementation Notes** > > The original site uses proprietary fonts. For self-contained HTML output, use these CDN substitutes: > - **Primary:** `Inter` | **Mono:** `system monospace stack` > - **Font stack (CSS):** `font-family: 'Inter', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;` > - **Mono stack (CSS):** `font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace;` > > Use `write_file` to create HTML, serve via `generative-widgets` skill (cloudflared tunnel). > Verify visual accuracy with `browser_vision` after generating. ## 1. Visual Theme & Atmosphere Revolut's website is…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/popular-web-designs/templates/revolut.md`, `local:projects/jestur/skills/creative/popular-web-designs/templates/revolut.md`, `local:projects/dev-coder/skills/creative/popular-web-designs/templates/revolut.md`, `local:projects/dev-orch/skills/creative/popular-web-designs/templates/revolut.md`, `local:projects/dev-review/skills/creative/popular-web-designs/templates/revolut.md`

### spotify
- **Source:** `local:projects/southpaw/klerik/skills/creative/popular-web-designs/templates/spotify.md`
- **Raw:** `[[raw/local/spotify-5cc773b31d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Design System: Spotify > **Hermes Agent — Implementation Notes** > > The original site uses proprietary fonts. For self-contained HTML output, use these CDN substitutes: > - **Primary:** `DM Sans` | **Mono:** `system monospace stack` > - **Font stack (CSS):** `font-family: 'DM Sans', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;` > - **Mono stack (CSS):** `font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace;` > > Use `write_file` to create HTML, serve via `generative-widgets` skill (cloudflared tunnel). > Verify visual accuracy with `browser_vision` after generating. ## 1. Visual Theme & Atmosphere Spotify's web…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/popular-web-designs/templates/spotify.md`, `local:projects/jestur/skills/creative/popular-web-designs/templates/spotify.md`, `local:projects/dev-coder/skills/creative/popular-web-designs/templates/spotify.md`, `local:projects/dev-orch/skills/creative/popular-web-designs/templates/spotify.md`, `local:projects/dev-review/skills/creative/popular-web-designs/templates/spotify.md`

### resend
- **Source:** `local:projects/southpaw/klerik/skills/creative/popular-web-designs/templates/resend.md`
- **Raw:** `[[raw/local/resend-9ee46f856f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Design System: Resend > **Hermes Agent — Implementation Notes** > > The original site uses proprietary fonts. For self-contained HTML output, use these CDN substitutes: > - **Primary:** `Geist` | **Mono:** `Geist Mono` > - **Font stack (CSS):** `font-family: 'Geist', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;` > - **Mono stack (CSS):** `font-family: 'Geist Mono', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace;` > > Use `write_file` to create HTML, serve via `generative-widgets` skill (cloudflared tunnel). > Verify visual accuracy with `browser_vision` after generating. ## 1. Visual Theme & Atmosphere Resend's website is a…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/popular-web-designs/templates/resend.md`, `local:projects/jestur/skills/creative/popular-web-designs/templates/resend.md`, `local:projects/dev-coder/skills/creative/popular-web-designs/templates/resend.md`, `local:projects/dev-orch/skills/creative/popular-web-designs/templates/resend.md`, `local:projects/dev-review/skills/creative/popular-web-designs/templates/resend.md`

### spacex
- **Source:** `local:projects/southpaw/klerik/skills/creative/popular-web-designs/templates/spacex.md`
- **Raw:** `[[raw/local/spacex-8b91bf2446.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Design System: SpaceX > **Hermes Agent — Implementation Notes** > > The original site uses proprietary fonts. For self-contained HTML output, use these CDN substitutes: > - **Primary:** `Inter` | **Mono:** `system monospace stack` > - **Font stack (CSS):** `font-family: 'Inter', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;` > - **Mono stack (CSS):** `font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace;` > > Use `write_file` to create HTML, serve via `generative-widgets` skill (cloudflared tunnel). > Verify visual accuracy with `browser_vision` after generating. ## 1. Visual Theme & Atmosphere SpaceX's website is a…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/popular-web-designs/templates/spacex.md`, `local:projects/jestur/skills/creative/popular-web-designs/templates/spacex.md`, `local:projects/dev-coder/skills/creative/popular-web-designs/templates/spacex.md`, `local:projects/dev-orch/skills/creative/popular-web-designs/templates/spacex.md`, `local:projects/dev-review/skills/creative/popular-web-designs/templates/spacex.md`

### raycast
- **Source:** `local:projects/southpaw/klerik/skills/creative/popular-web-designs/templates/raycast.md`
- **Raw:** `[[raw/local/raycast-90304a7a87.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Design System: Raycast > **Hermes Agent — Implementation Notes** > > The original site uses proprietary fonts. For self-contained HTML output, use these CDN substitutes: > - **Primary:** `Inter` | **Mono:** `Geist Mono` > - **Font stack (CSS):** `font-family: 'Inter', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;` > - **Mono stack (CSS):** `font-family: 'Geist Mono', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace;` > > Use `write_file` to create HTML, serve via `generative-widgets` skill (cloudflared tunnel). > Verify visual accuracy with `browser_vision` after generating. ## 1. Visual Theme & Atmosphere Raycast's marketing…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/popular-web-designs/templates/raycast.md`, `local:projects/jestur/skills/creative/popular-web-designs/templates/raycast.md`, `local:projects/dev-coder/skills/creative/popular-web-designs/templates/raycast.md`, `local:projects/dev-orch/skills/creative/popular-web-designs/templates/raycast.md`, `local:projects/dev-review/skills/creative/popular-web-designs/templates/raycast.md`

### posthog
- **Source:** `local:projects/southpaw/klerik/skills/creative/popular-web-designs/templates/posthog.md`
- **Raw:** `[[raw/local/posthog-9d17a75b45.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Design System: PostHog > **Hermes Agent — Implementation Notes** > > The original site uses proprietary fonts. For self-contained HTML output, use these CDN substitutes: > - **Primary:** `Inter` | **Mono:** `JetBrains Mono` > - **Font stack (CSS):** `font-family: 'Inter', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;` > - **Mono stack (CSS):** `font-family: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace;` > > Use `write_file` to create HTML, serve via `generative-widgets` skill (cloudflared tunnel). > Verify visual accuracy with `browser_vision` after generating. ## 1. Visual Theme & Atmosphere PostHog's…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/popular-web-designs/templates/posthog.md`, `local:projects/jestur/skills/creative/popular-web-designs/templates/posthog.md`, `local:projects/dev-coder/skills/creative/popular-web-designs/templates/posthog.md`, `local:projects/dev-orch/skills/creative/popular-web-designs/templates/posthog.md`, `local:projects/dev-review/skills/creative/popular-web-designs/templates/posthog.md`

### nvidia
- **Source:** `local:projects/southpaw/klerik/skills/creative/popular-web-designs/templates/nvidia.md`
- **Raw:** `[[raw/local/nvidia-9a56554292.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Design System: NVIDIA > **Hermes Agent — Implementation Notes** > > The original site uses proprietary fonts. For self-contained HTML output, use these CDN substitutes: > - **Primary:** `Inter` | **Mono:** `system monospace stack` > - **Font stack (CSS):** `font-family: 'Inter', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;` > - **Mono stack (CSS):** `font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace;` > > Use `write_file` to create HTML, serve via `generative-widgets` skill (cloudflared tunnel). > Verify visual accuracy with `browser_vision` after generating. ## 1. Visual Theme & Atmosphere NVIDIA's website is a…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/popular-web-designs/templates/nvidia.md`, `local:projects/jestur/skills/creative/popular-web-designs/templates/nvidia.md`, `local:projects/dev-coder/skills/creative/popular-web-designs/templates/nvidia.md`, `local:projects/dev-orch/skills/creative/popular-web-designs/templates/nvidia.md`, `local:projects/dev-review/skills/creative/popular-web-designs/templates/nvidia.md`

### pinterest
- **Source:** `local:projects/southpaw/klerik/skills/creative/popular-web-designs/templates/pinterest.md`
- **Raw:** `[[raw/local/pinterest-eaec9d13e6.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Design System: Pinterest > **Hermes Agent — Implementation Notes** > > The original site uses proprietary fonts. For self-contained HTML output, use these CDN substitutes: > - **Primary:** `DM Sans` | **Mono:** `system monospace stack` > - **Font stack (CSS):** `font-family: 'DM Sans', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;` > - **Mono stack (CSS):** `font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace;` > > Use `write_file` to create HTML, serve via `generative-widgets` skill (cloudflared tunnel). > Verify visual accuracy with `browser_vision` after generating. ## 1. Visual Theme & Atmosphere Pinterest's…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/popular-web-designs/templates/pinterest.md`, `local:projects/jestur/skills/creative/popular-web-designs/templates/pinterest.md`, `local:projects/dev-coder/skills/creative/popular-web-designs/templates/pinterest.md`, `local:projects/dev-orch/skills/creative/popular-web-designs/templates/pinterest.md`, `local:projects/dev-review/skills/creative/popular-web-designs/templates/pinterest.md`

### opencode.ai
- **Source:** `local:projects/southpaw/klerik/skills/creative/popular-web-designs/templates/opencode.ai.md`
- **Raw:** `[[raw/local/opencode.ai-fac924b83e.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Design System: OpenCode > **Hermes Agent — Implementation Notes** > > The original site uses proprietary fonts. For self-contained HTML output, use these CDN substitutes: > - **Primary:** `JetBrains Mono` | **Mono:** `JetBrains Mono` > - **Font stack (CSS):** `font-family: 'JetBrains Mono', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;` > - **Mono stack (CSS):** `font-family: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace;` > > Use `write_file` to create HTML, serve via `generative-widgets` skill (cloudflared tunnel). > Verify visual accuracy with `browser_vision` after generating. ## 1. Visual Theme &…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/popular-web-designs/templates/opencode.ai.md`, `local:projects/jestur/skills/creative/popular-web-designs/templates/opencode.ai.md`, `local:projects/dev-coder/skills/creative/popular-web-designs/templates/opencode.ai.md`, `local:projects/dev-orch/skills/creative/popular-web-designs/templates/opencode.ai.md`, `local:projects/dev-review/skills/creative/popular-web-designs/templates/opencode.ai.md`

### lovable
- **Source:** `local:projects/southpaw/klerik/skills/creative/popular-web-designs/templates/lovable.md`
- **Raw:** `[[raw/local/lovable-c4092616ed.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Design System: Lovable > **Hermes Agent — Implementation Notes** > > The original site uses proprietary fonts. For self-contained HTML output, use these CDN substitutes: > - **Primary:** `DM Sans` | **Mono:** `system monospace stack` > - **Font stack (CSS):** `font-family: 'DM Sans', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;` > - **Mono stack (CSS):** `font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace;` > > Use `write_file` to create HTML, serve via `generative-widgets` skill (cloudflared tunnel). > Verify visual accuracy with `browser_vision` after generating. ## 1. Visual Theme & Atmosphere Lovable's website…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/popular-web-designs/templates/lovable.md`, `local:projects/jestur/skills/creative/popular-web-designs/templates/lovable.md`, `local:projects/dev-coder/skills/creative/popular-web-designs/templates/lovable.md`, `local:projects/dev-orch/skills/creative/popular-web-designs/templates/lovable.md`, `local:projects/dev-review/skills/creative/popular-web-designs/templates/lovable.md`

### notion
- **Source:** `local:projects/southpaw/klerik/skills/creative/popular-web-designs/templates/notion.md`
- **Raw:** `[[raw/local/notion-9afd11387e.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Design System: Notion > **Hermes Agent — Implementation Notes** > > The original site uses proprietary fonts. For self-contained HTML output, use these CDN substitutes: > - **Primary:** `Inter` | **Mono:** `system monospace stack` > - **Font stack (CSS):** `font-family: 'Inter', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;` > - **Mono stack (CSS):** `font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace;` > > Use `write_file` to create HTML, serve via `generative-widgets` skill (cloudflared tunnel). > Verify visual accuracy with `browser_vision` after generating. ## 1. Visual Theme & Atmosphere Notion's website…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/popular-web-designs/templates/notion.md`, `local:projects/jestur/skills/creative/popular-web-designs/templates/notion.md`, `local:projects/dev-coder/skills/creative/popular-web-designs/templates/notion.md`, `local:projects/dev-orch/skills/creative/popular-web-designs/templates/notion.md`, `local:projects/dev-review/skills/creative/popular-web-designs/templates/notion.md`

### expo
- **Source:** `local:projects/southpaw/klerik/skills/creative/popular-web-designs/templates/expo.md`
- **Raw:** `[[raw/local/expo-513bded0ab.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Design System: Expo > **Hermes Agent — Implementation Notes** > > The original site uses proprietary fonts. For self-contained HTML output, use these CDN substitutes: > - **Primary:** `Inter` | **Mono:** `JetBrains Mono` > - **Font stack (CSS):** `font-family: 'Inter', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;` > - **Mono stack (CSS):** `font-family: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace;` > > Use `write_file` to create HTML, serve via `generative-widgets` skill (cloudflared tunnel). > Verify visual accuracy with `browser_vision` after generating. ## 1. Visual Theme & Atmosphere Expo's interface…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/popular-web-designs/templates/expo.md`, `local:projects/jestur/skills/creative/popular-web-designs/templates/expo.md`, `local:projects/dev-coder/skills/creative/popular-web-designs/templates/expo.md`, `local:projects/dev-orch/skills/creative/popular-web-designs/templates/expo.md`, `local:projects/dev-review/skills/creative/popular-web-designs/templates/expo.md`

### figma
- **Source:** `local:projects/southpaw/klerik/skills/creative/popular-web-designs/templates/figma.md`
- **Raw:** `[[raw/local/figma-d04a522572.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Design System: Figma > **Hermes Agent — Implementation Notes** > > The original site uses proprietary fonts. For self-contained HTML output, use these CDN substitutes: > - **Primary:** `Inter` | **Mono:** `JetBrains Mono` > - **Font stack (CSS):** `font-family: 'Inter', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;` > - **Mono stack (CSS):** `font-family: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace;` > > Use `write_file` to create HTML, serve via `generative-widgets` skill (cloudflared tunnel). > Verify visual accuracy with `browser_vision` after generating. ## 1. Visual Theme & Atmosphere Figma's…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/popular-web-designs/templates/figma.md`, `local:projects/jestur/skills/creative/popular-web-designs/templates/figma.md`, `local:projects/dev-coder/skills/creative/popular-web-designs/templates/figma.md`, `local:projects/dev-orch/skills/creative/popular-web-designs/templates/figma.md`, `local:projects/dev-review/skills/creative/popular-web-designs/templates/figma.md`

### framer
- **Source:** `local:projects/southpaw/klerik/skills/creative/popular-web-designs/templates/framer.md`
- **Raw:** `[[raw/local/framer-4374dc30dd.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Design System: Framer > **Hermes Agent — Implementation Notes** > > The original site uses proprietary fonts. For self-contained HTML output, use these CDN substitutes: > - **Primary:** `Inter` | **Mono:** `Azeret Mono` > - **Font stack (CSS):** `font-family: 'Inter', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;` > - **Mono stack (CSS):** `font-family: 'Azeret Mono', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace;` > > Use `write_file` to create HTML, serve via `generative-widgets` skill (cloudflared tunnel). > Verify visual accuracy with `browser_vision` after generating. ## 1. Visual Theme & Atmosphere Framer's website is…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/popular-web-designs/templates/framer.md`, `local:projects/jestur/skills/creative/popular-web-designs/templates/framer.md`, `local:projects/dev-coder/skills/creative/popular-web-designs/templates/framer.md`, `local:projects/dev-orch/skills/creative/popular-web-designs/templates/framer.md`, `local:projects/dev-review/skills/creative/popular-web-designs/templates/framer.md`

### ibm
- **Source:** `local:projects/southpaw/klerik/skills/creative/popular-web-designs/templates/ibm.md`
- **Raw:** `[[raw/local/ibm-328494dcf5.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Design System: IBM > **Hermes Agent — Implementation Notes** > > The original site uses proprietary fonts. For self-contained HTML output, use these CDN substitutes: > - **Primary:** `IBM Plex Sans` | **Mono:** `IBM Plex Mono` > - **Font stack (CSS):** `font-family: 'IBM Plex Sans', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;` > - **Mono stack (CSS):** `font-family: 'IBM Plex Mono', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace;` > > Use `write_file` to create HTML, serve via `generative-widgets` skill (cloudflared tunnel). > Verify visual accuracy with `browser_vision` after generating. ## 1. Visual Theme & Atmosphere…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/popular-web-designs/templates/ibm.md`, `local:projects/jestur/skills/creative/popular-web-designs/templates/ibm.md`, `local:projects/dev-coder/skills/creative/popular-web-designs/templates/ibm.md`, `local:projects/dev-orch/skills/creative/popular-web-designs/templates/ibm.md`, `local:projects/dev-review/skills/creative/popular-web-designs/templates/ibm.md`

### clay
- **Source:** `local:projects/southpaw/klerik/skills/creative/popular-web-designs/templates/clay.md`
- **Raw:** `[[raw/local/clay-fc18ca7b88.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Design System: Clay > **Hermes Agent — Implementation Notes** > > The original site uses proprietary fonts. For self-contained HTML output, use these CDN substitutes: > - **Primary:** `DM Sans` | **Mono:** `system monospace stack` > - **Font stack (CSS):** `font-family: 'DM Sans', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;` > - **Mono stack (CSS):** `font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace;` > > Use `write_file` to create HTML, serve via `generative-widgets` skill (cloudflared tunnel). > Verify visual accuracy with `browser_vision` after generating. ## 1. Visual Theme & Atmosphere Clay's website is a…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/popular-web-designs/templates/clay.md`, `local:projects/jestur/skills/creative/popular-web-designs/templates/clay.md`, `local:projects/dev-coder/skills/creative/popular-web-designs/templates/clay.md`, `local:projects/dev-orch/skills/creative/popular-web-designs/templates/clay.md`, `local:projects/dev-review/skills/creative/popular-web-designs/templates/clay.md`

### elevenlabs
- **Source:** `local:projects/southpaw/klerik/skills/creative/popular-web-designs/templates/elevenlabs.md`
- **Raw:** `[[raw/local/elevenlabs-ba0f745514.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Design System: ElevenLabs > **Hermes Agent — Implementation Notes** > > The original site uses proprietary fonts. For self-contained HTML output, use these CDN substitutes: > - **Primary:** `Inter` | **Mono:** `JetBrains Mono` > - **Font stack (CSS):** `font-family: 'Inter', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;` > - **Mono stack (CSS):** `font-family: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace;` > > Use `write_file` to create HTML, serve via `generative-widgets` skill (cloudflared tunnel). > Verify visual accuracy with `browser_vision` after generating. ## 1. Visual Theme & Atmosphere…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/popular-web-designs/templates/elevenlabs.md`, `local:projects/jestur/skills/creative/popular-web-designs/templates/elevenlabs.md`, `local:projects/dev-coder/skills/creative/popular-web-designs/templates/elevenlabs.md`, `local:projects/dev-orch/skills/creative/popular-web-designs/templates/elevenlabs.md`, `local:projects/dev-review/skills/creative/popular-web-designs/templates/elevenlabs.md`

### cohere
- **Source:** `local:projects/southpaw/klerik/skills/creative/popular-web-designs/templates/cohere.md`
- **Raw:** `[[raw/local/cohere-0db7feff1f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Design System: Cohere > **Hermes Agent — Implementation Notes** > > The original site uses proprietary fonts. For self-contained HTML output, use these CDN substitutes: > - **Primary:** `Inter` | **Mono:** `JetBrains Mono` > - **Font stack (CSS):** `font-family: 'Inter', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;` > - **Mono stack (CSS):** `font-family: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace;` > > Use `write_file` to create HTML, serve via `generative-widgets` skill (cloudflared tunnel). > Verify visual accuracy with `browser_vision` after generating. ## 1. Visual Theme & Atmosphere Cohere's…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/popular-web-designs/templates/cohere.md`, `local:projects/jestur/skills/creative/popular-web-designs/templates/cohere.md`, `local:projects/dev-coder/skills/creative/popular-web-designs/templates/cohere.md`, `local:projects/dev-orch/skills/creative/popular-web-designs/templates/cohere.md`, `local:projects/dev-review/skills/creative/popular-web-designs/templates/cohere.md`

### cursor
- **Source:** `local:projects/southpaw/klerik/skills/creative/popular-web-designs/templates/cursor.md`
- **Raw:** `[[raw/local/cursor-9c0584ad58.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Design System: Cursor > **Hermes Agent — Implementation Notes** > > The original site uses proprietary fonts. For self-contained HTML output, use these CDN substitutes: > - **Primary:** `Inter` | **Mono:** `JetBrains Mono` > - **Font stack (CSS):** `font-family: 'Inter', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;` > - **Mono stack (CSS):** `font-family: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace;` > > Use `write_file` to create HTML, serve via `generative-widgets` skill (cloudflared tunnel). > Verify visual accuracy with `browser_vision` after generating. ## 1. Visual Theme & Atmosphere Cursor's…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/popular-web-designs/templates/cursor.md`, `local:projects/jestur/skills/creative/popular-web-designs/templates/cursor.md`, `local:projects/dev-coder/skills/creative/popular-web-designs/templates/cursor.md`, `local:projects/dev-orch/skills/creative/popular-web-designs/templates/cursor.md`, `local:projects/dev-review/skills/creative/popular-web-designs/templates/cursor.md`

### cal
- **Source:** `local:projects/southpaw/klerik/skills/creative/popular-web-designs/templates/cal.md`
- **Raw:** `[[raw/local/cal-87b5ebb39d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Design System: Cal.com > **Hermes Agent — Implementation Notes** > > The original site uses proprietary fonts. For self-contained HTML output, use these CDN substitutes: > - **Primary:** `Inter` | **Mono:** `Roboto Mono` > - **Font stack (CSS):** `font-family: 'Inter', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;` > - **Mono stack (CSS):** `font-family: 'Roboto Mono', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace;` > > Use `write_file` to create HTML, serve via `generative-widgets` skill (cloudflared tunnel). > Verify visual accuracy with `browser_vision` after generating. ## 1. Visual Theme & Atmosphere Cal.com's website…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/popular-web-designs/templates/cal.md`, `local:projects/jestur/skills/creative/popular-web-designs/templates/cal.md`, `local:projects/dev-coder/skills/creative/popular-web-designs/templates/cal.md`, `local:projects/dev-orch/skills/creative/popular-web-designs/templates/cal.md`, `local:projects/dev-review/skills/creative/popular-web-designs/templates/cal.md`

### apple
- **Source:** `local:projects/southpaw/klerik/skills/creative/popular-web-designs/templates/apple.md`
- **Raw:** `[[raw/local/apple-9dfce6c8ba.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Design System: Apple > **Hermes Agent — Implementation Notes** > > The original site uses proprietary fonts. For self-contained HTML output, use these CDN substitutes: > - **Primary:** `system-ui` | **Mono:** `SF Mono (system)` > - **Font stack (CSS):** `font-family: system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;` > - **Mono stack (CSS):** `font-family: 'SF Mono (system)', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace;` > > Use `write_file` to create HTML, serve via `generative-widgets` skill (cloudflared tunnel). > Verify visual accuracy with `browser_vision` after generating. ## 1. Visual Theme &…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/popular-web-designs/templates/apple.md`, `local:projects/jestur/skills/creative/popular-web-designs/templates/apple.md`, `local:projects/dev-coder/skills/creative/popular-web-designs/templates/apple.md`, `local:projects/dev-orch/skills/creative/popular-web-designs/templates/apple.md`, `local:projects/dev-review/skills/creative/popular-web-designs/templates/apple.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills/creative/pixel-art/SKILL.md`
- **Raw:** `[[raw/local/skill-01f3517266.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: pixel-art description: "Pixel art w/ era palettes (NES, Game Boy, PICO-8)." version: 2.0.0 author: dodo-reach license: MIT platforms: [linux, macos, windows] metadata: hermes: tags: [creative, pixel-art, arcade, snes, nes, gameboy, retro, image, video] category: creative credits: - "Hardware palettes and animation loops ported from Synero/pixel-art-studio (MIT) — https://github.com/Synero/pixel-art-studio" --- # Pixel Art Convert any image into retro pixel art, then optionally animate it into a short MP4 or GIF with era-appropriate effects (rain, fireflies, snow, embers). Two scripts ship with this skill: - `scripts/pixel_art.py` — photo → pixel-art PNG (Floyd-Steinberg dithering)…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/pixel-art/SKILL.md`, `local:projects/jestur/skills/creative/pixel-art/SKILL.md`, `local:projects/dev-coder/skills/creative/pixel-art/SKILL.md`, `local:projects/dev-orch/skills/creative/pixel-art/SKILL.md`, `local:projects/dev-review/skills/creative/pixel-art/SKILL.md`

### palettes
- **Source:** `local:projects/southpaw/klerik/skills/creative/pixel-art/references/palettes.md`
- **Raw:** `[[raw/local/palettes-ee2f510b1b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Named Palettes 28 hardware-accurate and artistic palettes available to `pixel_art()`. Palette values are sourced from `pixel-art-studio` (MIT) — see ATTRIBUTION.md in the skill root. Usage: pass the palette name as `palette=` or let a preset select it. ## Hardware Palettes | Name | Colors | Source | |------|--------|--------| | `NES` | 54 | Nintendo NES | | `C64` | 16 | Commodore 64 | | `COMMODORE_64` | 16 | Commodore 64 (alt) | | `ZX_SPECTRUM` | 8 | Sinclair ZX Spectrum | | `APPLE_II_LO` | 16 | Apple II lo-res | | `APPLE_II_HI` | 6 | Apple II hi-res | | `GAMEBOY_ORIGINAL` | 4 | Game Boy DMG (green) | | `GAMEBOY_POCKET` | 4 | Game Boy Pocket (grey) | | `GAMEBOY_VIRTUALBOY` | 4 | Virtual…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/pixel-art/references/palettes.md`, `local:projects/jestur/skills/creative/pixel-art/references/palettes.md`, `local:projects/dev-coder/skills/creative/pixel-art/references/palettes.md`, `local:projects/dev-orch/skills/creative/pixel-art/references/palettes.md`, `local:projects/dev-review/skills/creative/pixel-art/references/palettes.md`

### visual-effects
- **Source:** `local:projects/southpaw/klerik/skills/creative/p5js/references/visual-effects.md`
- **Raw:** `[[raw/local/visual-effects-b2cda40990.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Visual Effects ## Noise ### Perlin Noise Basics The scale factor (0.005 etc.) is critical: - `0.001` — very smooth, large features - `0.005` — smooth, medium features - `0.01` — standard generative art scale - `0.05` — detailed, small features - `0.1` — near-random, grainy ### Fractal Brownian Motion (fBM) Layered noise octaves for natural-looking texture. Each octave adds detail at smaller scale. ### Domain Warping Feed noise output back as input coordinates for flowing organic distortion. ### Curl Noise Divergence-free noise field. Particles following curl noise never converge or diverge — they flow in smooth, swirling patterns. ## Flow Fields A grid of vectors that steer particles. The…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/p5js/references/visual-effects.md`, `local:projects/jestur/skills/creative/p5js/references/visual-effects.md`, `local:projects/dev-coder/skills/creative/p5js/references/visual-effects.md`, `local:projects/dev-orch/skills/creative/p5js/references/visual-effects.md`, `local:projects/dev-review/skills/creative/p5js/references/visual-effects.md`

### core-api
- **Source:** `local:projects/southpaw/klerik/skills/creative/p5js/references/core-api.md`
- **Raw:** `[[raw/local/core-api-8b1278b31b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Core API Reference ## Canvas Setup ### createCanvas() ### Pixel Density High-DPI displays render at 2x by default. This doubles memory usage and halves performance. For export, always `pixelDensity(1)` and use the exact target resolution. Never rely on device scaling for final output. ### Responsive Resize ## Coordinate System ### P2D (Default) - Origin: top-left (0, 0) - X increases rightward - Y increases downward - Angles: radians by default, `angleMode(DEGREES)` to switch ### WEBGL - Origin: center of canvas - X increases rightward, Y increases **upward**, Z increases toward viewer - To get P2D-like coordinates in WEBGL: `translate(-width/2, -height/2)` ## Draw Loop ### Frame Control…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/p5js/references/core-api.md`, `local:projects/jestur/skills/creative/p5js/references/core-api.md`, `local:projects/dev-coder/skills/creative/p5js/references/core-api.md`, `local:projects/dev-orch/skills/creative/p5js/references/core-api.md`, `local:projects/dev-review/skills/creative/p5js/references/core-api.md`

### animation
- **Source:** `local:projects/southpaw/klerik/skills/creative/p5js/references/animation.md`
- **Raw:** `[[raw/local/animation-7b71c1fd7c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Animation ## Frame-Based Animation ### The Draw Loop ### Time-Based vs Frame-Based ### Normalized Time ## Easing Functions ### Built-in Lerp ### Common Easing Curves ### Applying Easing ## Spring Physics More natural than easing — responds to force, overshoots, settles. ### 2D Spring ## State Machines For complex multi-phase animations. ## Timeline Sequencing For timed multi-scene animations (motion graphics, title sequences). ## Noise-Driven Motion More organic than deterministic animation. ## Transition Patterns ### Fade In/Out ### Slide ### Scale Reveal ### Staggered Entry ## Recording Deterministic Animations For frame-perfect export, use frame count instead of millis(): ## Scene Fade…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/p5js/references/animation.md`, `local:projects/jestur/skills/creative/p5js/references/animation.md`, `local:projects/dev-coder/skills/creative/p5js/references/animation.md`, `local:projects/dev-orch/skills/creative/p5js/references/animation.md`, `local:projects/dev-review/skills/creative/p5js/references/animation.md`

### decorations
- **Source:** `local:projects/southpaw/klerik/skills/creative/manim-video/references/decorations.md`
- **Raw:** `[[raw/local/decorations-dfd7bd79a5.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Decorations and Visual Polish Decorations are mobjects that annotate, highlight, or frame other mobjects. They turn a technically correct animation into a visually polished one. ## SurroundingRectangle Draws a rectangle around any mobject. The go-to for highlighting: ### Around part of an equation ## BackgroundRectangle Semi-transparent background behind text for readability over complex scenes: The `set_stroke(background=True)` approach is cleaner for text labels over graphs/diagrams. ## Brace and BraceLabel Curly braces that annotate sections of a diagram or equation: ### Brace placement ## Arrows for Annotation ### Straight arrows pointing to mobjects ### Curved arrows ### Labeling…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/manim-video/references/decorations.md`, `local:projects/jestur/skills/creative/manim-video/references/decorations.md`, `local:projects/dev-coder/skills/creative/manim-video/references/decorations.md`, `local:projects/dev-orch/skills/creative/manim-video/references/decorations.md`, `local:projects/dev-review/skills/creative/manim-video/references/decorations.md`

### camera-and-3d
- **Source:** `local:projects/southpaw/klerik/skills/creative/manim-video/references/camera-and-3d.md`
- **Raw:** `[[raw/local/camera-and-3d-36a17d79a0.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Camera and 3D Reference ## MovingCameraScene (2D Camera Control) ### Camera Operations ## ThreeDScene ### Camera Control in 3D ### 3D Mobjects ### Parametric Curves ## When to Use 3D - Surfaces, vector fields, spatial geometry, 3D transforms ## When NOT to Use 3D - 2D concepts, text-heavy scenes, flat data (bar charts, time series) ## ZoomedScene — Inset Zoom Show a magnified inset of a detail while keeping the full view visible: Use cases: zooming into a specific term in an equation, showing fine detail in a diagram, magnifying a region of a plot. ## LinearTransformationScene — Linear Algebra Pre-built scene with basis vectors and grid for visualizing matrix transformations: This…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/manim-video/references/camera-and-3d.md`, `local:projects/jestur/skills/creative/manim-video/references/camera-and-3d.md`, `local:projects/dev-coder/skills/creative/manim-video/references/camera-and-3d.md`, `local:projects/dev-orch/skills/creative/manim-video/references/camera-and-3d.md`, `local:projects/dev-review/skills/creative/manim-video/references/camera-and-3d.md`

### updaters-and-trackers
- **Source:** `local:projects/southpaw/klerik/skills/creative/manim-video/references/updaters-and-trackers.md`
- **Raw:** `[[raw/local/updaters-and-trackers-96c024dce5.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Updaters and Value Trackers ## The problem updaters solve Normal animations are discrete: `self.play()` goes from state A to state B. But what if you need continuous relationships — a label that always hovers above a moving dot, or a line that always connects two points? Without updaters, you'd manually reposition every dependent object before every `self.play()`. Five animations that move a dot means five manual repositioning calls for the label. Miss one and it freezes in the wrong spot. Updaters let you declare a relationship ONCE. Manim calls the updater function EVERY FRAME (15-60 fps depending on quality) to enforce that relationship, no matter what else is happening. ##…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/manim-video/references/updaters-and-trackers.md`, `local:projects/jestur/skills/creative/manim-video/references/updaters-and-trackers.md`, `local:projects/dev-coder/skills/creative/manim-video/references/updaters-and-trackers.md`, `local:projects/dev-orch/skills/creative/manim-video/references/updaters-and-trackers.md`, `local:projects/dev-review/skills/creative/manim-video/references/updaters-and-trackers.md`

### graphs-and-data
- **Source:** `local:projects/southpaw/klerik/skills/creative/manim-video/references/graphs-and-data.md`
- **Raw:** `[[raw/local/graphs-and-data-347847bc60.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Graphs, Plots, and Data Visualization ## Axes ## Plotting ## Animated Plotting ## Bar Charts ## Number Lines ## Animated Counters ## Algorithm Visualization Pattern ## Data Story Pattern ## Graph / DiGraph — Graph Theory Visualization Built-in graph mobjects with automatic layout: Layout algorithms: `"spring"`, `"circular"`, `"kamada_kawai"`, `"planar"`, `"spectral"`, `"tree"` (for rooted trees, specify `root=`). ## ArrowVectorField / StreamLines — Vector Fields Use cases: electromagnetic fields, fluid flow, gradient fields, ODE phase portraits. ## ComplexPlane / PolarPlane

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/manim-video/references/graphs-and-data.md`, `local:projects/jestur/skills/creative/manim-video/references/graphs-and-data.md`, `local:projects/dev-coder/skills/creative/manim-video/references/graphs-and-data.md`, `local:projects/dev-orch/skills/creative/manim-video/references/graphs-and-data.md`, `local:projects/dev-review/skills/creative/manim-video/references/graphs-and-data.md`

### mobjects
- **Source:** `local:projects/southpaw/klerik/skills/creative/manim-video/references/mobjects.md`
- **Raw:** `[[raw/local/mobjects-771421e463.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Mobjects Reference Everything visible on screen is a Mobject. They have position, color, opacity, and can be animated. ## Text **Always use raw strings (`r""`) for any string with backslashes.** ## Shapes ## Polygons and Arcs ## Sectors and Annuli Use cases: pie charts, ring progress indicators, Venn diagrams with arcs, geometric proofs. ## Positioning ## VGroup vs Group **VGroup** is for collections of shapes (VMobjects only — Circle, Square, Arrow, Line, MathTex): **Group** is for mixed collections (Text + shapes, or any Mobject types): **Rule: if your group contains any `Text()` objects, use `Group`, not `VGroup`.** VGroup will raise a TypeError on Manim CE v0.20+. MathTex and Tex are…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/manim-video/references/mobjects.md`, `local:projects/jestur/skills/creative/manim-video/references/mobjects.md`, `local:projects/dev-coder/skills/creative/manim-video/references/mobjects.md`, `local:projects/dev-orch/skills/creative/manim-video/references/mobjects.md`, `local:projects/dev-review/skills/creative/manim-video/references/mobjects.md`

### animations
- **Source:** `local:projects/southpaw/klerik/skills/creative/manim-video/references/animations.md`
- **Raw:** `[[raw/local/animations-e00bf77a8e.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Animations Reference ## Core Concept An animation is a Python object that computes intermediate visual states of a mobject over time. Animations are objects passed to `self.play()`, not functions. `run_time` controls seconds (default: 1). Always specify it explicitly for important animations. ## Creation Animations ## Removal Animations ## Transform Animations **Critical**: After `Transform(A, B)`, variable `A` references the on-screen mobject. Variable `B` is NOT on screen. Use `ReplacementTransform` when you want to work with `B` afterwards. ## The .animate Syntax ## Additional Creation Animations ## Movement Animations `MoveAlongPath` takes any `VMobject` as the path — use `Arc`,…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/manim-video/references/animations.md`, `local:projects/jestur/skills/creative/manim-video/references/animations.md`, `local:projects/dev-coder/skills/creative/manim-video/references/animations.md`, `local:projects/dev-orch/skills/creative/manim-video/references/animations.md`, `local:projects/dev-review/skills/creative/manim-video/references/animations.md`

### scene-planning
- **Source:** `local:projects/southpaw/klerik/skills/creative/manim-video/references/scene-planning.md`
- **Raw:** `[[raw/local/scene-planning-c54a8cf6cf.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Scene Planning Reference ## Narrative Arc Structures ### Discovery Arc (most common) 1. Hook -- pose a question or surprising result 2. Intuition -- build visual understanding 3. Formalize -- introduce the equation/algorithm 4. Reveal -- the "aha moment" 5. Extend -- implications or generalizations ### Problem-Solution Arc 1. Problem -- what's broken 2. Failed attempt -- obvious approach fails 3. Key insight -- the idea that works 4. Solution -- implement it 5. Result -- show improvement ### Comparison Arc 1. Setup -- introduce two approaches 2. Approach A -- how it works 3. Approach B -- how it works 4. Contrast -- differences 5. Verdict -- which is better ### Build-Up Arc…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/manim-video/references/scene-planning.md`, `local:projects/jestur/skills/creative/manim-video/references/scene-planning.md`, `local:projects/dev-coder/skills/creative/manim-video/references/scene-planning.md`, `local:projects/dev-orch/skills/creative/manim-video/references/scene-planning.md`, `local:projects/dev-review/skills/creative/manim-video/references/scene-planning.md`

### animation-design-thinking
- **Source:** `local:projects/southpaw/klerik/skills/creative/manim-video/references/animation-design-thinking.md`
- **Raw:** `[[raw/local/animation-design-thinking-87812340f4.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Animation Design Thinking How to decide WHAT to animate and HOW to structure it — before writing any code. ## Should I animate this? Not everything benefits from animation. Motion adds cognitive load. Bad animation is worse than a good static diagram. **Animate when:** - A sequence unfolds over time (algorithm steps, derivation, pipeline stages) - Spatial relationships change (transformation, deformation, rotation) - Something is built from parts (construction, assembly, accumulation) - You're comparing states (before/after, method A vs method B) - Temporal evolution is the point (training curves, wave propagation, gradient descent) **Show static when:** - The concept is a single labeled…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/manim-video/references/animation-design-thinking.md`, `local:projects/jestur/skills/creative/manim-video/references/animation-design-thinking.md`, `local:projects/dev-coder/skills/creative/manim-video/references/animation-design-thinking.md`, `local:projects/dev-orch/skills/creative/manim-video/references/animation-design-thinking.md`, `local:projects/dev-review/skills/creative/manim-video/references/animation-design-thinking.md`

### full-prompt-library
- **Source:** `local:projects/southpaw/klerik/skills/creative/creative-ideation/references/full-prompt-library.md`
- **Raw:** `[[raw/local/full-prompt-library-2e193b9868.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Full Prompt Library Extended constraint library beyond the core set in SKILL.md. Load these when the user wants more variety or a specific category. ## Communication & Connection **Create a means of distribution:** The project works when you can use what you made to give something to somebody else. **Make a way to communicate:** The project works when you can hold a conversation with someone else using what you created. Not chat — something weirder. **Write a love letter:** To a person, a programming language, a game, a place, a tool. On paper, in code, in music, in light. Mail it. **Mail chess / Asynchronous games:** Something turn-based played with no time limit. No requirement to be…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/creative-ideation/references/full-prompt-library.md`, `local:projects/jestur/skills/creative/creative-ideation/references/full-prompt-library.md`, `local:projects/dev-coder/skills/creative/creative-ideation/references/full-prompt-library.md`, `local:projects/dev-orch/skills/creative/creative-ideation/references/full-prompt-library.md`, `local:projects/dev-review/skills/creative/creative-ideation/references/full-prompt-library.md`

### pixel-art
- **Source:** `local:projects/southpaw/klerik/skills/creative/baoyu-infographic/references/styles/pixel-art.md`
- **Raw:** `[[raw/local/pixel-art-1a1dffbccf.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # pixel-art Retro 8-bit gaming aesthetic ## Color Palette - Primary: Limited palette - NES/SNES colors - Background: Black or dark blue, scanlines optional - Accents: Bright pixel highlights, CRT glow ## Visual Elements - Visible pixel grid - Limited color count per sprite - 8-bit or 16-bit style - Retro game UI elements - Pixel-perfect edges - Dithering for gradients ## Typography - Pixel fonts - Blocky letterforms - Game UI style text - Score/stat display style ## Best For Gaming topics, nostalgia content, developer audiences, retro tech themes

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/baoyu-infographic/references/styles/pixel-art.md`, `local:projects/jestur/skills/creative/baoyu-infographic/references/styles/pixel-art.md`, `local:projects/dev-coder/skills/creative/baoyu-infographic/references/styles/pixel-art.md`, `local:projects/dev-orch/skills/creative/baoyu-infographic/references/styles/pixel-art.md`, `local:projects/dev-review/skills/creative/baoyu-infographic/references/styles/pixel-art.md`

### venn-diagram
- **Source:** `local:projects/southpaw/klerik/skills/creative/baoyu-infographic/references/layouts/venn-diagram.md`
- **Raw:** `[[raw/local/venn-diagram-c0babb164e.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # venn-diagram Overlapping circles showing relationships, commonalities, and differences. ## Structure - 2-3 overlapping circles - Each circle is a category/concept - Overlaps show shared elements - Center shows common to all - Unique areas for exclusives ## Best For - Concept relationships - Skill overlaps - Market segments - Comparative analysis - Finding common ground ## Visual Elements - Translucent circle fills - Clear overlap regions - Distinct colors per circle - Icons in regions - Boundary labels ## Text Placement - Title at top - Circle labels outside or on edge - Items in appropriate regions - Overlap region labels - Legend if needed ## Recommended Pairings - `cartoon-hand-drawn`:…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/baoyu-infographic/references/layouts/venn-diagram.md`, `local:projects/jestur/skills/creative/baoyu-infographic/references/layouts/venn-diagram.md`, `local:projects/dev-coder/skills/creative/baoyu-infographic/references/layouts/venn-diagram.md`, `local:projects/dev-orch/skills/creative/baoyu-infographic/references/layouts/venn-diagram.md`, `local:projects/dev-review/skills/creative/baoyu-infographic/references/layouts/venn-diagram.md`

### analysis-framework
- **Source:** `local:projects/southpaw/klerik/skills/creative/baoyu-infographic/references/analysis-framework.md`
- **Raw:** `[[raw/local/analysis-framework-666d568233.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Infographic Content Analysis Framework Deep analysis framework applying instructional design principles to infographic creation. ## Purpose Before creating an infographic, thoroughly analyze the source material to: - Understand the content at a deep level - Identify clear learning objectives for the viewer - Structure information for maximum clarity and retention - Match content to optimal layout×style combinations - Preserve all source data verbatim ## Instructional Design Mindset Approach content analysis as a **world-class instructional designer**: | Principle | Application | |-----------|-------------| | **Deep Understanding** | Read the entire document before analyzing any part | |…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/baoyu-infographic/references/analysis-framework.md`, `local:projects/jestur/skills/creative/baoyu-infographic/references/analysis-framework.md`, `local:projects/dev-coder/skills/creative/baoyu-infographic/references/analysis-framework.md`, `local:projects/dev-orch/skills/creative/baoyu-infographic/references/analysis-framework.md`, `local:projects/dev-review/skills/creative/baoyu-infographic/references/analysis-framework.md`

### workflow
- **Source:** `local:projects/southpaw/klerik/skills/creative/baoyu-comic/references/workflow.md`
- **Raw:** `[[raw/local/workflow-424bcbb2dd.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Complete Workflow Full workflow for generating knowledge comics. ## Progress Checklist Copy and track progress: ## Flow Diagram --- ## Step 1: Setup & Analyze ### 1.1 Analyze Content → `analysis.md` Read source content, save it if needed, and perform deep analysis. **Actions**: 1. **Save source content** (if not already a file): - If user provides a file path: use as-is - If user pastes content: save to `source-{slug}.md` in the target directory using `write_file`, where `{slug}` is the kebab-case topic slug used for the output directory - **Backup rule**: If `source-{slug}.md` already exists, rename it to `source-{slug}-backup-YYYYMMDD-HHMMSS.md` before writing 2. Read source content 3.…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/baoyu-comic/references/workflow.md`, `local:projects/jestur/skills/creative/baoyu-comic/references/workflow.md`, `local:projects/dev-coder/skills/creative/baoyu-comic/references/workflow.md`, `local:projects/dev-orch/skills/creative/baoyu-comic/references/workflow.md`, `local:projects/dev-review/skills/creative/baoyu-comic/references/workflow.md`

### neutral
- **Source:** `local:projects/southpaw/klerik/skills/creative/baoyu-comic/references/tones/neutral.md`
- **Raw:** `[[raw/local/neutral-fc0cd10f06.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # neutral 中性基调 - Balanced, rational, educational ## Overview Default balanced tone suitable for educational and informative content. Neither overly emotional nor cold - creates accessible, professional atmosphere. ## Mood Characteristics - Balanced emotional register - Clear, rational presentation - Educational focus - Professional but approachable - Objective storytelling ## Color Modifiers When applied to any art style: | Adjustment | Direction | |------------|-----------| | Saturation | Standard (no shift) | | Contrast | Balanced | | Temperature | Neutral | | Brightness | Slightly bright | ## Lighting - Even, clear lighting - Minimal dramatic shadows - Consistent across panels - Natural…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/baoyu-comic/references/tones/neutral.md`, `local:projects/jestur/skills/creative/baoyu-comic/references/tones/neutral.md`, `local:projects/dev-coder/skills/creative/baoyu-comic/references/tones/neutral.md`, `local:projects/dev-orch/skills/creative/baoyu-comic/references/tones/neutral.md`, `local:projects/dev-review/skills/creative/baoyu-comic/references/tones/neutral.md`

### dramatic
- **Source:** `local:projects/southpaw/klerik/skills/creative/baoyu-comic/references/tones/dramatic.md`
- **Raw:** `[[raw/local/dramatic-02fe6d7dd1.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # dramatic 戏剧基调 - High contrast, intense, powerful moments ## Overview High-impact dramatic tone for pivotal moments, conflicts, and breakthroughs. Uses strong contrast and intense compositions to create emotional power. ## Mood Characteristics - Tension and intensity - Pivotal moments - Conflict and resolution - Breakthrough discoveries - Emotional climaxes ## Color Modifiers When applied to any art style: | Adjustment | Direction | |------------|-----------| | Saturation | High (vibrant or deep) | | Contrast | Maximum | | Temperature | Varies for effect | | Brightness | Strong highlights, deep shadows | ## Contrast Approach - Sharp light/dark divisions - Minimal mid-tones - Stark…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/baoyu-comic/references/tones/dramatic.md`, `local:projects/jestur/skills/creative/baoyu-comic/references/tones/dramatic.md`, `local:projects/dev-coder/skills/creative/baoyu-comic/references/tones/dramatic.md`, `local:projects/dev-orch/skills/creative/baoyu-comic/references/tones/dramatic.md`, `local:projects/dev-review/skills/creative/baoyu-comic/references/tones/dramatic.md`

### vintage
- **Source:** `local:projects/southpaw/klerik/skills/creative/baoyu-comic/references/tones/vintage.md`
- **Raw:** `[[raw/local/vintage-6cc3300012.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # vintage 复古基调 - Historical, aged, period authenticity ## Overview Historical atmosphere with aged paper effects and period-appropriate aesthetics. Creates sense of time, authenticity, and historical distance. ## Mood Characteristics - Historical authenticity - Period distance - Archival quality - Time and memory - Classical elegance ## Color Modifiers When applied to any art style: | Adjustment | Direction | |------------|-----------| | Saturation | Reduced, muted | | Contrast | Medium, aged | | Temperature | Sepia shift | | Brightness | Slightly faded | ## Color Palette Shift toward aged tones: | Role | Color | Hex | |------|-------|-----| | Primary | Sepia brown | #8B7355 | | Background…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/baoyu-comic/references/tones/vintage.md`, `local:projects/jestur/skills/creative/baoyu-comic/references/tones/vintage.md`, `local:projects/dev-coder/skills/creative/baoyu-comic/references/tones/vintage.md`, `local:projects/dev-orch/skills/creative/baoyu-comic/references/tones/vintage.md`, `local:projects/dev-review/skills/creative/baoyu-comic/references/tones/vintage.md`

### storyboard-template
- **Source:** `local:projects/southpaw/klerik/skills/creative/baoyu-comic/references/storyboard-template.md`
- **Raw:** `[[raw/local/storyboard-template-917836d5fa.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Storyboard Template ## Storyboard Document Format ## Cover Design Principles - Academic gravitas with visual appeal - Title typography reflecting knowledge/science theme - Composition hinting at core theme (character silhouette, iconic symbol, concept diagram) - Subtitle or time span for epic scope ## Panel Composition Guidelines | Panel Type | Recommended Count | Usage | |-----------|-------------------|-------| | Main narrative | 3-5 per page | Story progression | | Concept diagram | 1-2 per page | Visualize abstractions | | Narrator panel | 0-1 per page | Commentary, transition | | Splash (full/half) | Occasional | Major moments | ## Panel Size Reference - **Full page (Splash)**: Major…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/baoyu-comic/references/storyboard-template.md`, `local:projects/jestur/skills/creative/baoyu-comic/references/storyboard-template.md`, `local:projects/dev-coder/skills/creative/baoyu-comic/references/storyboard-template.md`, `local:projects/dev-orch/skills/creative/baoyu-comic/references/storyboard-template.md`, `local:projects/dev-review/skills/creative/baoyu-comic/references/storyboard-template.md`

### wuxia
- **Source:** `local:projects/southpaw/klerik/skills/creative/baoyu-comic/references/presets/wuxia.md`
- **Raw:** `[[raw/local/wuxia-8f4df8d695.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # wuxia 武侠预设 - Hong Kong martial arts comic style ## Base Configuration | Dimension | Value | |-----------|-------| | Art Style | ink-brush | | Tone | action | | Layout | splash (default) | Equivalent to: art=ink-brush, tone=action ## Unique Rules This preset includes special rules beyond the art+tone combination. When the `wuxia` preset is selected, ALL rules below must be applied. ### Qi/Energy Effects (Required) Martial arts power must be visible through qi effects: | Effect Type | Visual Treatment | |-------------|-----------------| | Internal qi | Glowing aura around character | | External qi | Visible energy projection | | Qi clash | Radiating impact waves | | Qi absorption | Flowing…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/baoyu-comic/references/presets/wuxia.md`, `local:projects/jestur/skills/creative/baoyu-comic/references/presets/wuxia.md`, `local:projects/dev-coder/skills/creative/baoyu-comic/references/presets/wuxia.md`, `local:projects/dev-orch/skills/creative/baoyu-comic/references/presets/wuxia.md`, `local:projects/dev-review/skills/creative/baoyu-comic/references/presets/wuxia.md`

### shoujo
- **Source:** `local:projects/southpaw/klerik/skills/creative/baoyu-comic/references/presets/shoujo.md`
- **Raw:** `[[raw/local/shoujo-194353514a.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # shoujo 少女预设 - Classic shoujo manga with romantic aesthetics ## Base Configuration | Dimension | Value | |-----------|-------| | Art Style | manga | | Tone | romantic | | Layout | standard (default) | Equivalent to: art=manga, tone=romantic ## Unique Rules This preset includes special rules beyond the art+tone combination. When the `shoujo` preset is selected, ALL rules below must be applied. ### Decorative Elements (Required) Every emotional moment must include decorative elements: | Emotion | Required Decorations | |---------|---------------------| | Love | Floating hearts, sparkles, rose petals | | Longing | Feathers, bubbles, distant sparkles | | Joy | Flowers blooming, light bursts,…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/baoyu-comic/references/presets/shoujo.md`, `local:projects/jestur/skills/creative/baoyu-comic/references/presets/shoujo.md`, `local:projects/dev-coder/skills/creative/baoyu-comic/references/presets/shoujo.md`, `local:projects/dev-orch/skills/creative/baoyu-comic/references/presets/shoujo.md`, `local:projects/dev-review/skills/creative/baoyu-comic/references/presets/shoujo.md`

### ohmsha
- **Source:** `local:projects/southpaw/klerik/skills/creative/baoyu-comic/references/presets/ohmsha.md`
- **Raw:** `[[raw/local/ohmsha-811ec3e61a.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ohmsha Ohmsha预设 - Educational manga with visual metaphors ## Base Configuration | Dimension | Value | |-----------|-------| | Art Style | manga | | Tone | neutral | | Layout | webtoon (default) | Equivalent to: art=manga, tone=neutral ## Unique Rules This preset includes special rules beyond the art+tone combination. When the `ohmsha` preset is selected, ALL rules below must be applied. ### Visual Metaphor Requirements (CRITICAL) Every technical concept MUST be visualized as a metaphor: | Concept Type | Visualization Approach | |-------------|----------------------| | Algorithm | Gadget/machine that demonstrates the process | | Data structure | Physical space characters can enter/explore…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/baoyu-comic/references/presets/ohmsha.md`, `local:projects/jestur/skills/creative/baoyu-comic/references/presets/ohmsha.md`, `local:projects/dev-coder/skills/creative/baoyu-comic/references/presets/ohmsha.md`, `local:projects/dev-orch/skills/creative/baoyu-comic/references/presets/ohmsha.md`, `local:projects/dev-review/skills/creative/baoyu-comic/references/presets/ohmsha.md`

### action
- **Source:** `local:projects/southpaw/klerik/skills/creative/baoyu-comic/references/tones/action.md`
- **Raw:** `[[raw/local/action-c62c2f2a64.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # action 动作基调 - Speed, impact, power ## Overview High-impact action atmosphere with dynamic movement, combat effects, and powerful visual energy. Creates visceral, exciting sequences. ## Mood Characteristics - Speed and motion - Power and impact - Combat intensity - Physical energy - Visceral excitement ## Color Modifiers When applied to any art style: | Adjustment | Direction | |------------|-----------| | Saturation | High contrast | | Contrast | Maximum | | Temperature | Variable per effect | | Brightness | Dynamic range | ## Action Effects **Combat/motion effects** (apply liberally): | Effect | Usage | |--------|-------| | Speed lines | Motion, velocity | | Impact bursts | Hits,…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/baoyu-comic/references/tones/action.md`, `local:projects/jestur/skills/creative/baoyu-comic/references/tones/action.md`, `local:projects/dev-coder/skills/creative/baoyu-comic/references/tones/action.md`, `local:projects/dev-orch/skills/creative/baoyu-comic/references/tones/action.md`, `local:projects/dev-review/skills/creative/baoyu-comic/references/tones/action.md`

### ohmsha-guide
- **Source:** `local:projects/southpaw/klerik/skills/creative/baoyu-comic/references/ohmsha-guide.md`
- **Raw:** `[[raw/local/ohmsha-guide-f4efbcfbb2.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Ohmsha Manga Guide Style Guidelines for educational manga comics using the `ohmsha` preset. ## Character Setup | Role | Default | Traits | |------|---------|--------| | Student (Role A) | 大雄 | Confused, asks basic but crucial questions, represents reader | | Mentor (Role B) | 哆啦A梦 | Knowledgeable, patient, uses gadgets as technical metaphors | | Antagonist (Role C, optional) | 胖虎 | Represents misunderstanding, or "noise" in the data | Custom characters: ask the user for role → name mappings (e.g., `Student:小明, Mentor:教授, Antagonist:Bug怪`). ## Character Reference Sheet Style For Ohmsha style, use manga/anime style with: - Exaggerated expressions for educational clarity - Simple,…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/baoyu-comic/references/ohmsha-guide.md`, `local:projects/jestur/skills/creative/baoyu-comic/references/ohmsha-guide.md`, `local:projects/dev-coder/skills/creative/baoyu-comic/references/ohmsha-guide.md`, `local:projects/dev-orch/skills/creative/baoyu-comic/references/ohmsha-guide.md`, `local:projects/dev-review/skills/creative/baoyu-comic/references/ohmsha-guide.md`

### concept-story
- **Source:** `local:projects/southpaw/klerik/skills/creative/baoyu-comic/references/presets/concept-story.md`
- **Raw:** `[[raw/local/concept-story-00e667ff72.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # concept-story 概念故事预设 - Narrative comics that visualize abstract concepts through character-driven stories ## Base Configuration | Dimension | Value | |-----------|-------| | Art Style | manga | | Tone | warm | | Layout | standard (default) | Equivalent to: art=manga, tone=warm ## Unique Rules This preset includes special rules beyond the art+tone combination. When the `concept-story` preset is selected, ALL rules below must be applied. ### Concept Visualization System (CRITICAL) Each major abstract concept SHOULD have a recurring visual symbol/metaphor: | Concept Type | Visualization Approach | |-------------|----------------------| | Psychological need | Tangible object character holds…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/baoyu-comic/references/presets/concept-story.md`, `local:projects/jestur/skills/creative/baoyu-comic/references/presets/concept-story.md`, `local:projects/dev-coder/skills/creative/baoyu-comic/references/presets/concept-story.md`, `local:projects/dev-orch/skills/creative/baoyu-comic/references/presets/concept-story.md`, `local:projects/dev-review/skills/creative/baoyu-comic/references/presets/concept-story.md`

### auto-selection
- **Source:** `local:projects/southpaw/klerik/skills/creative/baoyu-comic/references/auto-selection.md`
- **Raw:** `[[raw/local/auto-selection-1d5de33377.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Auto Selection Content signals determine default art + tone + layout (or preset). ## Content Signal Matrix | Content Signals | Art Style | Tone | Layout | Preset | |-----------------|-----------|------|--------|--------| | Tutorial, how-to, beginner | manga | neutral | webtoon | **ohmsha** | | Computing, AI, programming | manga | neutral | dense | **ohmsha** | | Technical explanation, educational | manga | neutral | webtoon | **ohmsha** | | Pre-1950, classical, ancient | realistic | vintage | cinematic | - | | Personal story, mentor | ligne-claire | warm | standard | - | | Psychology, motivation, self-help, coaching | manga | warm | standard | **concept-story** | | Business narrative,…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/baoyu-comic/references/auto-selection.md`, `local:projects/jestur/skills/creative/baoyu-comic/references/auto-selection.md`, `local:projects/dev-coder/skills/creative/baoyu-comic/references/auto-selection.md`, `local:projects/dev-orch/skills/creative/baoyu-comic/references/auto-selection.md`, `local:projects/dev-review/skills/creative/baoyu-comic/references/auto-selection.md`

### character-template
- **Source:** `local:projects/southpaw/klerik/skills/creative/baoyu-comic/references/character-template.md`
- **Raw:** `[[raw/local/character-template-4a1479a239.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Character Definition Template ## Character Document Format Create `characters/characters.md` with the following structure: ## Reference Sheet Image Prompt After character definitions, include a prompt for generating the reference sheet: ## Example: Turing Biography ## Handling Age Variants For biographies spanning many years, define age variants: ## Best Practices | Practice | Description | |----------|-------------| | Be specific | "Short dark wavy hair, parted left" not just "dark hair" | | Use distinguishing features | Glasses, scars, accessories that identify character | | Define color codes | Use specific color names or hex codes | | Include age markers | Wrinkles, posture, clothing…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/baoyu-comic/references/character-template.md`, `local:projects/jestur/skills/creative/baoyu-comic/references/character-template.md`, `local:projects/dev-coder/skills/creative/baoyu-comic/references/character-template.md`, `local:projects/dev-orch/skills/creative/baoyu-comic/references/character-template.md`, `local:projects/dev-review/skills/creative/baoyu-comic/references/character-template.md`

### ligne-claire
- **Source:** `local:projects/southpaw/klerik/skills/creative/baoyu-comic/references/art-styles/ligne-claire.md`
- **Raw:** `[[raw/local/ligne-claire-8906cb2712.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ligne-claire 清线画风 - Uniform lines, flat colors, European comic tradition ## Overview Classic European comic style originating from Hergé's Tintin. Characterized by clean, uniform outlines and flat color fills without gradients. Creates a timeless, accessible aesthetic suitable for educational and narrative content. ## Line Work - Uniform, clean outlines with consistent weight (2px) - No hatching or cross-hatching for shading - Sharp, precise edges on all elements - Black ink outlines on all figures and objects - Shadows indicated through flat color areas, not line techniques ## Character Design - Slightly stylized/cartoonish characters with realistic proportions - Distinctive,…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/baoyu-comic/references/art-styles/ligne-claire.md`, `local:projects/jestur/skills/creative/baoyu-comic/references/art-styles/ligne-claire.md`, `local:projects/dev-coder/skills/creative/baoyu-comic/references/art-styles/ligne-claire.md`, `local:projects/dev-orch/skills/creative/baoyu-comic/references/art-styles/ligne-claire.md`, `local:projects/dev-review/skills/creative/baoyu-comic/references/art-styles/ligne-claire.md`

### manga
- **Source:** `local:projects/southpaw/klerik/skills/creative/baoyu-comic/references/art-styles/manga.md`
- **Raw:** `[[raw/local/manga-b2ea678169.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # manga 日漫画风 - Anime/manga aesthetics with expressive characters ## Overview Japanese manga art style characterized by large expressive eyes, dynamic poses, and visual emotion indicators. Versatile style that works across genres from educational to romantic to action. ## Line Work - Clean, smooth lines (1.5-2px) - Expressive weight variation for emphasis - Smooth curves, dynamic strokes - Speed lines and motion effects available - Screen tone effects for atmosphere ## Character Design - Anime/manga proportions: larger eyes, expressive faces - 5-7 head height proportions (varies by sub-style) - Clear emotional indicators (！, ？, sweat drops, sparkles) - Dynamic poses and gestures - Detailed…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/baoyu-comic/references/art-styles/manga.md`, `local:projects/jestur/skills/creative/baoyu-comic/references/art-styles/manga.md`, `local:projects/dev-coder/skills/creative/baoyu-comic/references/art-styles/manga.md`, `local:projects/dev-orch/skills/creative/baoyu-comic/references/art-styles/manga.md`, `local:projects/dev-review/skills/creative/baoyu-comic/references/art-styles/manga.md`

### troubleshooting
- **Source:** `local:projects/southpaw/klerik/skills/creative/ascii-video/references/troubleshooting.md`
- **Raw:** `[[raw/local/troubleshooting-eb992b11d0.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Troubleshooting Reference > **See also:** composition.md · architecture.md · shaders.md · scenes.md · optimization.md ## Quick Diagnostic | Symptom | Likely Cause | Fix | |---------|-------------|-----| | All black output | tonemap gamma too high or no effects rendering | Lower gamma to 0.5, check scene_fn returns non-zero canvas | | Washed out / too bright | Linear brightness multiplier instead of tonemap | Replace `canvas * N` with `tonemap(canvas, gamma=0.75)` | | ffmpeg hangs mid-render | stderr=subprocess.PIPE deadlock | Redirect stderr to file | | "read-only" array error | broadcast_to view without .copy() | Add `.copy()` after broadcast_to | | PicklingError | Lambda or closure in…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/ascii-video/references/troubleshooting.md`, `local:projects/jestur/skills/creative/ascii-video/references/troubleshooting.md`, `local:projects/dev-coder/skills/creative/ascii-video/references/troubleshooting.md`, `local:projects/dev-orch/skills/creative/ascii-video/references/troubleshooting.md`, `local:projects/dev-review/skills/creative/ascii-video/references/troubleshooting.md`

### scenes
- **Source:** `local:projects/southpaw/klerik/skills/creative/ascii-video/references/scenes.md`
- **Raw:** `[[raw/local/scenes-6c9a0293a5.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Scene System & Creative Composition > **See also:** architecture.md · composition.md · effects.md · shaders.md ## Scene Design Philosophy Scenes are storytelling units, not effect demos. Every scene needs: - A **concept** — what is happening visually? Not "plasma + rings" but "emergence from void" or "crystallization" - An **arc** — how does it change over its duration? Build, decay, transform, reveal? - A **role** — how does it serve the larger video narrative? Opening tension, peak energy, resolution? The design patterns below provide compositional techniques. The scene examples show them in practice at increasing complexity. The protocol section covers the technical contract. Good…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/ascii-video/references/scenes.md`, `local:projects/jestur/skills/creative/ascii-video/references/scenes.md`, `local:projects/dev-coder/skills/creative/ascii-video/references/scenes.md`, `local:projects/dev-orch/skills/creative/ascii-video/references/scenes.md`, `local:projects/dev-review/skills/creative/ascii-video/references/scenes.md`

### shaders
- **Source:** `local:projects/southpaw/klerik/skills/creative/ascii-video/references/shaders.md`
- **Raw:** `[[raw/local/shaders-29cac0af0b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Shader Pipeline & Composable Effects Post-processing effects applied to the pixel canvas (`numpy uint8 array, shape (H,W,3)`) after character rendering and before encoding. Also covers **pixel-level blend modes**, **feedback buffers**, and the **ShaderChain** compositor. > **See also:** composition.md (blend modes, tonemap) · effects.md · scenes.md · architecture.md · optimization.md · troubleshooting.md > > **Blend modes:** For the 20 pixel blend modes and `blend_canvas()`, see `composition.md`. All blending uses `blend_canvas(base, top, mode, opacity)`. ## Design Philosophy The shader pipeline turns raw ASCII renders into cinematic output. The system is designed for **composability** —…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/ascii-video/references/shaders.md`, `local:projects/jestur/skills/creative/ascii-video/references/shaders.md`, `local:projects/dev-coder/skills/creative/ascii-video/references/shaders.md`, `local:projects/dev-orch/skills/creative/ascii-video/references/shaders.md`, `local:projects/dev-review/skills/creative/ascii-video/references/shaders.md`

### effects
- **Source:** `local:projects/southpaw/klerik/skills/creative/ascii-video/references/effects.md`
- **Raw:** `[[raw/local/effects-842f5720af.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Effect Catalog Effect building blocks that produce visual patterns. In v2, these are used **inside scene functions** that return a pixel canvas directly. The building blocks below operate on grid coordinate arrays and produce `(chars, colors)` or value/hue fields that the scene function renders to canvas via `_render_vf()`. > **See also:** architecture.md · composition.md · scenes.md · shaders.md · troubleshooting.md ## Design Philosophy Effects are the creative core. Don't copy these verbatim for every project -- use them as **building blocks** and **combine, modify, and invent** new ones. Every project should feel distinct. Key principles: - **Layer multiple effects** rather than using…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/ascii-video/references/effects.md`, `local:projects/jestur/skills/creative/ascii-video/references/effects.md`, `local:projects/dev-coder/skills/creative/ascii-video/references/effects.md`, `local:projects/dev-orch/skills/creative/ascii-video/references/effects.md`, `local:projects/dev-review/skills/creative/ascii-video/references/effects.md`

### composition
- **Source:** `local:projects/southpaw/klerik/skills/creative/ascii-video/references/composition.md`
- **Raw:** `[[raw/local/composition-3bdcb52592.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Composition & Brightness Reference The composable system is the core of visual complexity. It operates at three levels: pixel-level blend modes, multi-grid composition, and adaptive brightness management. This document covers all three, plus the masking/stencil system for spatial control. > **See also:** architecture.md · effects.md · scenes.md · shaders.md · troubleshooting.md ## Pixel-Level Blend Modes ### The `blend_canvas()` Function All blending operates on full pixel canvases (`uint8 H,W,3`). Internally converts to float32 [0,1] for precision, blends, lerps by opacity, converts back. ### 20 Blend Modes ### Blend Mode Selection Guide **Modes that brighten** (safe for dark inputs): -…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/ascii-video/references/composition.md`, `local:projects/jestur/skills/creative/ascii-video/references/composition.md`, `local:projects/dev-coder/skills/creative/ascii-video/references/composition.md`, `local:projects/dev-orch/skills/creative/ascii-video/references/composition.md`, `local:projects/dev-review/skills/creative/ascii-video/references/composition.md`

### architecture
- **Source:** `local:projects/southpaw/klerik/skills/creative/ascii-video/references/architecture.md`
- **Raw:** `[[raw/local/architecture-d537a3f6e6.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Architecture Reference > **See also:** composition.md · effects.md · scenes.md · shaders.md · inputs.md · optimization.md · troubleshooting.md ## Grid System ### Resolution Presets ### Multi-Density Grids Pre-initialize multiple grid sizes. Switch per section for visual variety. Grid dimensions auto-compute from resolution: **Landscape (1920x1080):** | Key | Font Size | Grid (cols x rows) | Use | |-----|-----------|-------------------|-----| | xs | 8 | 400x108 | Ultra-dense data fields | | sm | 10 | 320x83 | Dense detail, rain, starfields | | md | 16 | 192x56 | Default balanced, transitions | | lg | 20 | 160x45 | Quote/lyric text (readable at 1080p) | | xl | 24 | 137x37 | Short quotes,…

- **Collapsed duplicates:** `local:projects/klerik/skills/creative/ascii-video/references/architecture.md`, `local:projects/jestur/skills/creative/ascii-video/references/architecture.md`, `local:projects/dev-coder/skills/creative/ascii-video/references/architecture.md`, `local:projects/dev-orch/skills/creative/ascii-video/references/architecture.md`, `local:projects/dev-review/skills/creative/ascii-video/references/architecture.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills/apple/findmy/SKILL.md`
- **Raw:** `[[raw/local/skill-19ec56e3b7.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: findmy description: "Track Apple devices/AirTags via FindMy.app on macOS." version: 1.0.0 author: Hermes Agent license: MIT platforms: [macos] metadata: hermes: tags: [FindMy, AirTag, location, tracking, macOS, Apple] --- # Find My (Apple) Track Apple devices and AirTags via the FindMy.app on macOS. Since Apple doesn't provide a CLI for FindMy, this skill uses AppleScript to open the app and screen capture to read device locations. ## Prerequisites - **macOS** with Find My app and iCloud signed in - Devices/AirTags already registered in Find My - Screen Recording permission for terminal (System Settings → Privacy → Screen Recording) - **Optional but recommended**: Install…

- **Collapsed duplicates:** `local:projects/klerik/skills/apple/findmy/SKILL.md`, `local:projects/jestur/skills/apple/findmy/SKILL.md`, `local:projects/dev-coder/skills/apple/findmy/SKILL.md`, `local:projects/dev-orch/skills/apple/findmy/SKILL.md`, `local:projects/dev-review/skills/apple/findmy/SKILL.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills/apple/apple-notes/SKILL.md`
- **Raw:** `[[raw/local/skill-c652e01e47.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: apple-notes description: "Manage Apple Notes via memo CLI: create, search, edit." version: 1.0.0 author: Hermes Agent license: MIT platforms: [macos] metadata: hermes: tags: [Notes, Apple, macOS, note-taking] related_skills: [obsidian] prerequisites: commands: [memo] --- # Apple Notes Use `memo` to manage Apple Notes directly from the terminal. Notes sync across all Apple devices via iCloud. ## Prerequisites - **macOS** with Notes.app - Install: `brew tap antoniorodr/memo && brew install antoniorodr/memo/memo` - Grant Automation access to Notes.app when prompted (System Settings → Privacy → Automation) ## When to Use - User asks to create, view, or search Apple Notes - Saving…

- **Collapsed duplicates:** `local:projects/klerik/skills/apple/apple-notes/SKILL.md`, `local:projects/jestur/skills/apple/apple-notes/SKILL.md`, `local:projects/dev-coder/skills/apple/apple-notes/SKILL.md`, `local:projects/dev-orch/skills/apple/apple-notes/SKILL.md`, `local:projects/dev-review/skills/apple/apple-notes/SKILL.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills/apple/imessage/SKILL.md`
- **Raw:** `[[raw/local/skill-bc68b1648e.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: imessage description: Send and receive iMessages/SMS via the imsg CLI on macOS. version: 1.0.0 author: Hermes Agent license: MIT platforms: [macos] metadata: hermes: tags: [iMessage, SMS, messaging, macOS, Apple] prerequisites: commands: [imsg] --- # iMessage Use `imsg` to read and send iMessage/SMS via macOS Messages.app. ## Prerequisites - **macOS** with Messages.app signed in - Install: `brew install steipete/tap/imsg` - Grant Full Disk Access for terminal (System Settings → Privacy → Full Disk Access) - Grant Automation permission for Messages.app when prompted ## When to Use - User asks to send an iMessage or text message - Reading iMessage conversation history - Checking…

- **Collapsed duplicates:** `local:projects/klerik/skills/apple/imessage/SKILL.md`, `local:projects/jestur/skills/apple/imessage/SKILL.md`, `local:projects/dev-coder/skills/apple/imessage/SKILL.md`, `local:projects/dev-orch/skills/apple/imessage/SKILL.md`, `local:projects/dev-review/skills/apple/imessage/SKILL.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills/apple/apple-reminders/SKILL.md`
- **Raw:** `[[raw/local/skill-ee5084f2d7.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: apple-reminders description: "Apple Reminders via remindctl: add, list, complete." version: 1.0.0 author: Hermes Agent license: MIT platforms: [macos] metadata: hermes: tags: [Reminders, tasks, todo, macOS, Apple] prerequisites: commands: [remindctl] --- # Apple Reminders Use `remindctl` to manage Apple Reminders directly from the terminal. Tasks sync across all Apple devices via iCloud. ## Prerequisites - **macOS** with Reminders.app - Install: `brew install steipete/tap/remindctl` - Grant Reminders permission when prompted - Check: `remindctl status` / Request: `remindctl authorize` ## When to Use - User mentions "reminder" or "Reminders app" - Creating personal to-dos with due…

- **Collapsed duplicates:** `local:projects/klerik/skills/apple/apple-reminders/SKILL.md`, `local:projects/jestur/skills/apple/apple-reminders/SKILL.md`, `local:projects/dev-coder/skills/apple/apple-reminders/SKILL.md`, `local:projects/dev-orch/skills/apple/apple-reminders/SKILL.md`, `local:projects/dev-review/skills/apple/apple-reminders/SKILL.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills/apple/macos-computer-use/SKILL.md`
- **Raw:** `[[raw/local/skill-08b4bb4647.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: macos-computer-use description: | Drive the macOS desktop in the background — screenshots, mouse, keyboard, scroll, drag — without stealing the user's cursor, keyboard focus, or Space. Works with any tool-capable model. Load this skill whenever the `computer_use` tool is available. version: 1.0.0 platforms: [macos] metadata: hermes: tags: [computer-use, macos, desktop, automation, gui] category: desktop related_skills: [browser] --- # macOS Computer Use (universal, any-model) You have a `computer_use` tool that drives the Mac in the **background**. Your actions do NOT move the user's cursor, steal keyboard focus, or switch Spaces. The user can keep typing in their editor while you…

- **Collapsed duplicates:** `local:projects/klerik/skills/apple/macos-computer-use/SKILL.md`, `local:projects/jestur/skills/apple/macos-computer-use/SKILL.md`, `local:projects/dev-coder/skills/apple/macos-computer-use/SKILL.md`, `local:projects/dev-orch/skills/apple/macos-computer-use/SKILL.md`, `local:projects/dev-review/skills/apple/macos-computer-use/SKILL.md`

### DESCRIPTION
- **Source:** `local:projects/southpaw/klerik/skills/apple/DESCRIPTION.md`
- **Raw:** `[[raw/local/description-c9537e578d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** Apple / macOS skills — tools that interact with the Mac desktop (Finder, native apps) or system features (accessibility, screenshots).

- **Collapsed duplicates:** `local:projects/klerik/skills/apple/DESCRIPTION.md`, `local:projects/dev-coder/skills/apple/DESCRIPTION.md`, `local:projects/dev-orch/skills/apple/DESCRIPTION.md`, `local:projects/dev-review/skills/apple/DESCRIPTION.md`

### 1512930431559798814-game-development---Build-a-Game-from-Blank-Page-to-Shipped--in-One-Skill
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1512930431559798814-game-development---Build-a-Game-from-Blank-Page-to-Shipped--in-One-Skill.txt`
- **Raw:** `[[raw/discord/1512930431559798814-game-development---build-a-game-from-blank-page-to-shipped--in-one-skill-787de40bd1.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'game-development — Build a Game from Blank Page to Shipped, in One Skill' in forum #plugins-skills-and-skins # thread_id=1512930431559798814 forum_id=1485392832154832906 # Started 2026-06-07T03:44:29.911208+00:00 [2026-06-06T21:25:23.772000+00:00] yap.bi (id=1512930431559798814) game-development skill — PR: https://github.com/NousResearch/hermes-agent/pull/40796 The gaming category had skills for playing games, but nothing for making them. This fills that gap completely — an end-to-end game dev guide that takes you from a blank page to a published game without needing any other tool. Built as an orchestrator + references, covering the full 11-stage lifecycle: concept → design →…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1512930431559798814-game-development---Build-a-Game-from-Blank-Page-to-Shipped--in-One-Skill.txt`

### 1489127370442018956-My-Custom-Skins-for-Everyone.
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1489127370442018956-My-Custom-Skins-for-Everyone..txt`
- **Raw:** `[[raw/discord/1489127370442018956-my-custom-skins-for-everyone.-e16e20f436.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'My Custom Skins for Everyone.' in forum #plugins-skills-and-skins # thread_id=1489127370442018956 forum_id=1485392832154832906 # Started 2026-05-10T19:52:49.226659+00:00 [2026-04-02T05:00:31.762000+00:00] synextco (id=1489127370442018956) I will be adding more. Let me know if you have any request. https://github.com/joeynyc/hermes-skins [attachment] hermesskins.jpg https://cdn.discordapp.com/attachments/1489127370442018956/1489127371276812499/hermesskins.jpg?ex=6a020b2f&is=6a00b9af&hm=1ad27aa49bd64da0a240ca6b0c9fe31d0dd96271026a8fda4cfb41edc2de9af3& [embed] GitHub - joeynyc/hermes-skins: Custom skins (visual themes) for the... https://github.com/joeynyc/hermes-skins…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1489127370442018956-My-Custom-Skins-for-Everyone..txt`

### 1519832002512031785-Overhaul---Free-Idle-Truck-Simulator-MMO
- **Source:** `discord-archive:archives/community-projects-showcase/1519832002512031785-Overhaul---Free-Idle-Truck-Simulator-MMO.txt`
- **Raw:** `[[raw/discord/1519832002512031785-overhaul---free-idle-truck-simulator-mmo-2b4d0f8d48.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Overhaul - Free Idle Truck Simulator MMO' in forum #community-projects-showcase # thread_id=1519832002512031785 forum_id=1316137596535177246 # Started 2026-06-26T03:30:15.260027+00:00 [2026-06-25T22:29:46.512000+00:00] datthemaster (id=1519832002512031785) Overhaul — a logistics management MMO on real roads. You start with one van in your real city. The roads are OpenStreetMap, the distances are real, and a 4-hour haul takes 4 real hours. You're not driving — you're dispatching, routing, and building a fleet. Pay for upgrades, buy more and bigger transport vehicles, improve your reputation and take on longer and higher paying jobs. Weekly Hauls drops 6 cross-country lanes every…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1519832002512031785-Overhaul---Free-Idle-Truck-Simulator-MMO.txt`

### 1518310669655605418-Graph-View-for-Semantic-Search-App
- **Source:** `discord-archive:archives/community-projects-showcase/1518310669655605418-Graph-View-for-Semantic-Search-App.txt`
- **Raw:** `[[raw/discord/1518310669655605418-graph-view-for-semantic-search-app-fe536ae9dd.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Graph View for Semantic Search App' in forum #community-projects-showcase # thread_id=1518310669655605418 forum_id=1316137596535177246 # Started 2026-06-21T19:27:07.181529+00:00 [2026-06-21T17:44:32.494000+00:00] curiousclump. (id=1518310669655605418) little uh, graph view that ive been making. each node is an image, each edge represents similarity above a .7 threshold with another image. so you can easily find similar images. and i recently added graph settings so you can control what it looks like more! [attachment] Screenshot_2026-06-18_170320.png…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1518310669655605418-Graph-View-for-Semantic-Search-App.txt`

### 1518232813747306516-Does-recursively-synthesizing-statements-mimic-cognitive-abstraction
- **Source:** `discord-archive:archives/community-projects-showcase/1518232813747306516-Does-recursively-synthesizing-statements-mimic-cognitive-abstraction.txt`
- **Raw:** `[[raw/discord/1518232813747306516-does-recursively-synthesizing-statements-mimic-cognitive-abstraction-7fe46f319d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Does recursively synthesizing statements mimic cognitive abstraction?' in forum #community-projects-showcase # thread_id=1518232813747306516 forum_id=1316137596535177246 # Started 2026-06-21T14:05:28.409245+00:00 [2026-06-21T12:35:10.199000+00:00] lea_fia (id=1518232813747306516) A very primitive and simplistic experiment that examined whether a recursive system that combines the results of dialectics looks like abstraction. Qwen3:8B was used because tokens are expensive and I wanted to run locally on my potato Qwen was given a philosophical question and asked to derive a thesis. Then called again with this thesis to derive an anti-thesis. And finally once more to derive a…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1518232813747306516-Does-recursively-synthesizing-statements-mimic-cognitive-abstraction.txt`

### 1516964609494483125-Get-user-feedback-for-your-app
- **Source:** `discord-archive:archives/community-projects-showcase/1516964609494483125-Get-user-feedback-for-your-app.txt`
- **Raw:** `[[raw/discord/1516964609494483125-get-user-feedback-for-your-app-e5367fbcd1.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Get user feedback for your app' in forum #community-projects-showcase # thread_id=1516964609494483125 forum_id=1316137596535177246 # Started 2026-06-18T03:42:37.858707+00:00 [2026-06-18T00:35:46.743000+00:00] william_zhu3541 (id=1516964609494483125) Hi fellow builders, if you built something cool and want fellow builders to test it and provide candid feedback for product improvement, drop your link here: https://feedbacklab.app/ [embed] Feedback Lab https://feedbacklab.app/ [2026-06-18T14:49:39.210000+00:00] genidma2652 (id=1517179494035881984) good morning how are you doing? how is this different from product hunt? thx! [2026-06-18T15:03:39.427000+00:00] william_zhu3541…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1516964609494483125-Get-user-feedback-for-your-app.txt`

### 1514674784481579178-Unreal-Engine-Obsidian-x-Hermes
- **Source:** `discord-archive:archives/community-projects-showcase/1514674784481579178-Unreal-Engine-Obsidian-x-Hermes.txt`
- **Raw:** `[[raw/discord/1514674784481579178-unreal-engine-obsidian-x-hermes-f8db686723.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Unreal Engine Obsidian x Hermes' in forum #community-projects-showcase # thread_id=1514674784481579178 forum_id=1316137596535177246 # Started 2026-06-11T20:19:04.353825+00:00 [2026-06-11T16:56:49.917000+00:00] iam_rxpii (id=1514674784481579178) I'm building an RPG in Unreal Engine 5 and im having Hermes help me. UE5 is dense — C++, Blueprints, GAS, AI, PCG, materials, animation — so I'm compiling everything I learn into a structured knowledge base. This repo is that knowledge base, formatted as an Obsidian vault. https://github.com/theheavenlyd3mon/Unreal-Engine-Obsidian What's in it: • 155 files across 9 tutorial series (Gorka Games, Ask A Dev, PolyBoost, Coqui Games, UNF Games,…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1514674784481579178-Unreal-Engine-Obsidian-x-Hermes.txt`

### 1511693310920495114-Minimal--Fast-and-Feature-rich-Reading-app
- **Source:** `discord-archive:archives/community-projects-showcase/1511693310920495114-Minimal--Fast-and-Feature-rich-Reading-app.txt`
- **Raw:** `[[raw/discord/1511693310920495114-minimal--fast-and-feature-rich-reading-app-75239c03e3.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Minimal, Fast and Feature rich Reading app' in forum #community-projects-showcase # thread_id=1511693310920495114 forum_id=1316137596535177246 # Started 2026-06-03T16:45:02.043914+00:00 [2026-06-03T11:29:31.227000+00:00] _.edwixx._ (id=1511693310920495114) I was tired with chrome and firefox's default pdf viewer, i built this with hermes with deepseek v4 flash. the app have some cool features like 1. Multiple reading layouts 2. multiple reading themes 3. importing papers directly from url. 4. progress tracking, tags, folder, annotation 5. supports local models with ollama cloud 6. artifacts which shows all kinds of links from pdf into a good place to skim through/ and it's…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1511693310920495114-Minimal--Fast-and-Feature-rich-Reading-app.txt`

### 1511568965028155545-Hermes-Wingman---Desktop--Web--and-Mobile-App-for-Hermes.
- **Source:** `discord-archive:archives/community-projects-showcase/1511568965028155545-Hermes-Wingman---Desktop--Web--and-Mobile-App-for-Hermes..txt`
- **Raw:** `[[raw/discord/1511568965028155545-hermes-wingman---desktop--web--and-mobile-app-for-hermes.-278d2e8336.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Hermes Wingman - Desktop, Web, and Mobile App for Hermes.' in forum #community-projects-showcase # thread_id=1511568965028155545 forum_id=1316137596535177246 # Started 2026-06-03T10:55:14.066094+00:00 [2026-06-03T06:36:45.948000+00:00] synthalorian (id=1511619636800655481) Hermes Wingman - Desktop, Web, and Mobile App for Hermes. [2026-06-03T14:34:44.617000+00:00] .blockops (id=1511739923856752791) This looks really cool... sorry it got nerfed by their announcement. Maybe it can serve as a donor spike to the project. [2026-06-03T15:39:55.750000+00:00] 0x_stubbs (id=1511756328337670325) Nice work on this! Agreed that it is too bad that nous released theirs right now… But this still…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1511568965028155545-Hermes-Wingman---Desktop--Web--and-Mobile-App-for-Hermes..txt`

### 1511372298513416222-Website-Security-Scanner
- **Source:** `discord-archive:archives/community-projects-showcase/1511372298513416222-Website-Security-Scanner.txt`
- **Raw:** `[[raw/discord/1511372298513416222-website-security-scanner-4f31e20e42.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Website Security Scanner' in forum #community-projects-showcase # thread_id=1511372298513416222 forum_id=1316137596535177246 # Started 2026-06-02T16:20:14.478128+00:00 [2026-06-02T14:13:55.905000+00:00] jonkomet (id=1511372298513416222) built something for people shipping websites too fast lol VibeLeak scans your public site and gives it an S–F trust grade it checks the stuff people usually forget before launch: - headers - cookies/CORS - exposed files - open redirects - error leaks - public API/data exposure - cloud/backend leaks - AI key exposure - AI-readiness signals it also has VibeSignal for AI visibility and VibeRank for Pro/Agency users to see if AI answer engines actually…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1511372298513416222-Website-Security-Scanner.txt`

### 1510661612732678184-Mead-batch-tracking-website
- **Source:** `discord-archive:archives/community-projects-showcase/1510661612732678184-Mead-batch-tracking-website.txt`
- **Raw:** `[[raw/discord/1510661612732678184-mead-batch-tracking-website-811aa11576.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Mead batch tracking website' in forum #community-projects-showcase # thread_id=1510661612732678184 forum_id=1316137596535177246 # Started 2026-05-31T19:14:08.280553+00:00 [2026-05-31T15:09:55.211000+00:00] jcrabapple (id=1510661612732678184) For home brewers like me I had my agent build a mead batch tracking website to keep track of gravity readings, nutrient schedules, recipes, and more. https://github.com/jcrabapple/mead-tracker [embed] GitHub - jcrabapple/mead-tracker: Lightweight Flask app for trackin... https://github.com/jcrabapple/mead-tracker [2026-05-31T15:10:35.338000+00:00] jcrabapple (id=1510661781037518938) I encourage anyone to take this and add more features like…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1510661612732678184-Mead-batch-tracking-website.txt`

### 1509151258995458199-MentorAI---web-app---mobile-rensponsive
- **Source:** `discord-archive:archives/community-projects-showcase/1509151258995458199-MentorAI---web-app---mobile-rensponsive.txt`
- **Raw:** `[[raw/discord/1509151258995458199-mentorai---web-app---mobile-rensponsive-9ce65aebd3.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'MentorAI - web app + mobile rensponsive' in forum #community-projects-showcase # thread_id=1509151258995458199 forum_id=1316137596535177246 # Started 2026-05-27T15:36:49.373375+00:00 [2026-05-27T11:08:18.819000+00:00] mikewazowski3505 (id=1509151258995458199) Vibecoded "learning/guidance" chatbot app in 2 days at Hackaton 2026. Free, private, fast to use, Looking for feedback, thanks. [2026-05-27T11:08:29.992000+00:00] mikewazowski3505 (id=1509151305858416741) https://nuffyofc.github.io/pocketmentorxyz/#

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1509151258995458199-MentorAI---web-app---mobile-rensponsive.txt`

### 1508152092454424636-The-relationships-between-agents-will-matter-as-much-as-their-capabilities.-Let-them-build-Rapport.
- **Source:** `discord-archive:archives/community-projects-showcase/1508152092454424636-The-relationships-between-agents-will-matter-as-much-as-their-capabilities.-Let-them-build-Rapport..txt`
- **Raw:** `[[raw/discord/1508152092454424636-the-relationships-between-agents-will-matter-as-much-as-their-capabilities.-let-them-build-rapport.-35c8dfd55c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'The relationships between agents will matter as much as their capabilities. Let them build Rapport.' in forum #community-projects-showcase # thread_id=1508152092454424636 forum_id=1316137596535177246 # Started 2026-05-24T19:14:38.914599+00:00 [2026-05-24T16:57:58.952000+00:00] knownquantity_ (id=1508152092454424636) https://github.com/1999labs/build-rapport [embed] GitHub - 1999labs/build-rapport: The relationships between agents w... https://github.com/1999labs/build-rapport

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1508152092454424636-The-relationships-between-agents-will-matter-as-much-as-their-capabilities.-Let-them-build-Rapport..txt`

### 1508554681146802346-GroktoDash
- **Source:** `discord-archive:archives/community-projects-showcase/1508554681146802346-GroktoDash.txt`
- **Raw:** `[[raw/discord/1508554681146802346-groktodash-2839940538.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'GroktoDash' in forum #community-projects-showcase # thread_id=1508554681146802346 forum_id=1316137596535177246 # Started 2026-05-26T02:56:17.379017+00:00 [2026-05-25T19:37:43.576000+00:00] magnus919 (id=1508554681146802346) A native macOS desktop client for Hermes Agent. Uses a Tahoe Citizen architecture approach, which is a fancy way of saying it's designed to be a good desktop citizen rather than a web wrapper. MIT licensed. https://github.com/groktopus/groktodash [attachment] groktopus-logo-vintage.png…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1508554681146802346-GroktoDash.txt`

### 1496513601115131996-Hermes-Mobile-App
- **Source:** `discord-archive:archives/community-projects-showcase/1496513601115131996-Hermes-Mobile-App.txt`
- **Raw:** `[[raw/discord/1496513601115131996-hermes-mobile-app-069a7c8487.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Hermes Mobile App' in forum #community-projects-showcase # thread_id=1496513601115131996 forum_id=1316137596535177246 # Started 2026-05-10T19:49:48.614655+00:00 [2026-04-22T14:10:46.384000+00:00] fathah. (id=1496513601115131996) I've been using the mobile app to control my Hermes Agent remotely. Android & iOS. Drop your opinions, I'll publish it if looks useful😌 [attachment] IMG_3671.png https://cdn.discordapp.com/attachments/1496513601115131996/1496513601727369217/IMG_3671.png?ex=6a01e366&is=6a0091e6&hm=dca02a21c3ce731f89b53fd51a9aa4d13e70c6e1fa1401949a9fc9e18e86e6c4& [attachment] IMG_3672.png…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1496513601115131996-Hermes-Mobile-App.txt`

### 1495157726567858276-windows-native-support-for-hermes
- **Source:** `discord-archive:archives/community-projects-showcase/1495157726567858276-windows-native-support-for-hermes.txt`
- **Raw:** `[[raw/discord/1495157726567858276-windows-native-support-for-hermes-bbe1866212.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'windows native support for hermes' in forum #community-projects-showcase # thread_id=1495157726567858276 forum_id=1316137596535177246 # Started 2026-05-10T19:49:57.713488+00:00 [2026-04-18T20:23:00.701000+00:00] tdamre (id=1495157726567858276) https://github.com/NousResearch/hermes-agent/pull/10565 review please guys [attachment] Recording_2026-04-18_194344.mp4 https://cdn.discordapp.com/attachments/1495157726567858276/1495157798449971482/Recording_2026-04-18_194344.mp4?ex=6a0191f5&is=6a004075&hm=31daa2f43df861b53fcf862ccf352a8d9cb064efba076baa40486b600be65e35& [embed] fix(installer): support native Windows PowerShell install by adybag...…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1495157726567858276-windows-native-support-for-hermes.txt`

### 1494364159008047177-Argent---the-most-comprehensive-MCP-toolkit-for-mobile-app-development
- **Source:** `discord-archive:archives/community-projects-showcase/1494364159008047177-Argent---the-most-comprehensive-MCP-toolkit-for-mobile-app-development.txt`
- **Raw:** `[[raw/discord/1494364159008047177-argent---the-most-comprehensive-mcp-toolkit-for-mobile-app-development-d61f84b868.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Argent - the most comprehensive MCP toolkit for mobile app development' in forum #community-projects-showcase # thread_id=1494364159008047177 forum_id=1316137596535177246 # Started 2026-05-10T19:50:03.404932+00:00 [2026-04-16T15:49:39.451000+00:00] armado (id=1494364159008047177) Hiii, We just released Argent, a fully open source MCP toolkit for everything from controlling to profiling and debugging your iOS apps. We've got 60 tools and 9 skills, so lots of things to test out. React Native works out of the box. Native iOS too. We're really looking towards getting feedback, let us know if anything needs improving :)) You can try it with: `npx @swmansion/argent init` Website:…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1494364159008047177-Argent---the-most-comprehensive-MCP-toolkit-for-mobile-app-development.txt`

### 1492721511658815539-Hermes-for-app-builders.
- **Source:** `discord-archive:archives/community-projects-showcase/1492721511658815539-Hermes-for-app-builders..txt`
- **Raw:** `[[raw/discord/1492721511658815539-hermes-for-app-builders.-0e8203b350.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Hermes for app builders.' in forum #community-projects-showcase # thread_id=1492721511658815539 forum_id=1316137596535177246 # Started 2026-05-10T19:50:20.936375+00:00 [2026-04-12T03:02:21.804000+00:00] cyberfarmacist (id=1492721511658815539) One of the apps I'm working on helps my friend who is owns a remodeling company find work. Specifically roofing work. It started after I saw a video of a guy using Chatgbt and Replit to vibe code some app. I just wondered if I could do it. But the cost of Replit is killing me and the project isn't even a full on CRM lead gen product. It "should " pull county data for homeowner info, any permits pulled for an area and home age (to estimate…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1492721511658815539-Hermes-for-app-builders..txt`

### 1491718609180033145-My-First-Game-Created-Using-Hermes-Agent
- **Source:** `discord-archive:archives/community-projects-showcase/1491718609180033145-My-First-Game-Created-Using-Hermes-Agent.txt`
- **Raw:** `[[raw/discord/1491718609180033145-my-first-game-created-using-hermes-agent-71a0513dc6.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'My First Game Created Using Hermes Agent' in forum #community-projects-showcase # thread_id=1491718609180033145 forum_id=1316137596535177246 # Started 2026-05-10T19:50:31.706230+00:00 [2026-04-09T08:37:11.220000+00:00] realbillyuzi (id=1491718609180033145) Just deployed my first game with Hermes agent and honestly it was pure fun to build The idea is simple but addictive. Your main goal is to defeat Boss Rocky to move to the next level. Every enemy you beat drops crystals, and those crystals become your power. Press F to use them in fights and survive the chaos You can choose your character at the start: Press 1 to play with character 1 Press 2 to play with character 2 The game…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1491718609180033145-My-First-Game-Created-Using-Hermes-Agent.txt`

### 1486909840168190064-Hermes-ran-MTG-TCG-Store
- **Source:** `discord-archive:archives/community-projects-showcase/1486909840168190064-Hermes-ran-MTG-TCG-Store.txt`
- **Raw:** `[[raw/discord/1486909840168190064-hermes-ran-mtg-tcg-store-ca8f616a54.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Hermes ran MTG TCG Store' in forum #community-projects-showcase # thread_id=1486909840168190064 forum_id=1316137596535177246 # Started 2026-05-10T19:51:09.007648+00:00 [2026-03-27T02:08:51.345000+00:00] .s0uthpaw (id=1486909840168190064) https://github.com/SouthpawIN/pocket-shop [embed] GitHub - SouthpawIN/pocket-shop: Automated MTG card shop using brow... https://github.com/SouthpawIN/pocket-shop [2026-03-27T03:48:03.704000+00:00] .s0uthpaw (id=1486934806171353289) EDIT: rewritten as a set of 5 Skills, including a full loop

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1486909840168190064-Hermes-ran-MTG-TCG-Store.txt`

### 1469382407827492907-Lutum-Veritas---Open-Source-Deep-Research-Engine--beats-ChatGPT-Perplexity-Google
- **Source:** `discord-archive:archives/community-projects-showcase/1469382407827492907-Lutum-Veritas---Open-Source-Deep-Research-Engine--beats-ChatGPT-Perplexity-Google.txt`
- **Raw:** `[[raw/discord/1469382407827492907-lutum-veritas---open-source-deep-research-engine--beats-chatgpt-perplexity-google-225966f537.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Lutum Veritas - Open Source Deep Research Engine (beats ChatGPT/Perplexity/Google)' in forum #community-projects-showcase # thread_id=1469382407827492907 forum_id=1316137596535177246 # Started 2026-05-10T19:51:12.199942+00:00 [2026-02-06T17:21:05.831000+00:00] toxic_dd_main (id=1469382407827492907) Built an open source research engine that does what Perplexity and ChatGPT Deep Research charge $20/mo for — except it's self-hosted, BYOK, and actually verifies its claims. What it does: - Deep Research mode: 5,000-10,000+ word reports with 20+ verified sources (~$0.08/query) - Academic mode: 200k+ character outputs with Toulmin argumentation and evidence grading - ASK mode: Verified…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1469382407827492907-Lutum-Veritas---Open-Source-Deep-Research-Engine--beats-ChatGPT-Perplexity-Google.txt`

### 1422887193697062953-Google-just-dropped-a-new-AI-platform---Google-Opal
- **Source:** `discord-archive:archives/community-projects-showcase/1422887193697062953-Google-just-dropped-a-new-AI-platform---Google-Opal.txt`
- **Raw:** `[[raw/discord/1422887193697062953-google-just-dropped-a-new-ai-platform---google-opal-6b1b056d90.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread '🚀 Google just dropped a new AI platform — Google Opal' in forum #community-projects-showcase # thread_id=1422887193697062953 forum_id=1316137596535177246 # Started 2026-05-10T19:51:32.490939+00:00 [2025-10-01T10:05:42.943000+00:00] mariia081452 (id=1422887193697062953) Imagine this: you describe what you want in plain English — and the system builds it for you. An app, an automation workflow, even a video. No coding, no setup. Just talk, and Opal creates. I tested Google Opal and compared it with the tools we already know — Zapier, Make (Integromat), Bubble. I also tried some ready-made templates for: video marketing, blogging, YouTube learning apps, social media content. The wild…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1422887193697062953-Google-just-dropped-a-new-AI-platform---Google-Opal.txt`

### 1370108851034259456-Discover-Cultural-Comparisons-Between-Countries
- **Source:** `discord-archive:archives/community-projects-showcase/1370108851034259456-Discover-Cultural-Comparisons-Between-Countries.txt`
- **Raw:** `[[raw/discord/1370108851034259456-discover-cultural-comparisons-between-countries-139000995d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Discover Cultural Comparisons Between Countries' in forum #community-projects-showcase # thread_id=1370108851034259456 forum_id=1316137596535177246 # Started 2026-05-10T19:51:38.350170+00:00 [2025-05-08T18:43:25.478000+00:00] 0xmyopic (id=1370108851034259456) https://culture-alpha.vercel.app/ Today, the world is more connected than ever before. But these connections aren't sustainable without a true understanding of cultural differences. That’s why me developed Culture Powered by the Nous Research API, this platform visualizes and interprets cultural data in a way that anyone can understand. From academia to the business world, cross-cultural awareness is no longer a choice — it’s…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1370108851034259456-Discover-Cultural-Comparisons-Between-Countries.txt`

### 1356116505925910600-Labtasker--make-ML-experiment-wrapper-scripts-smarter-with-1-line-of-code-change
- **Source:** `discord-archive:archives/community-projects-showcase/1356116505925910600-Labtasker--make-ML-experiment-wrapper-scripts-smarter-with-1-line-of-code-change.txt`
- **Raw:** `[[raw/discord/1356116505925910600-labtasker--make-ml-experiment-wrapper-scripts-smarter-with-1-line-of-code-change-823749c87d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Labtasker: make ML experiment wrapper scripts smarter with 1 line of code change' in forum #community-projects-showcase # thread_id=1356116505925910600 forum_id=1316137596535177246 # Started 2026-05-10T19:51:45.462542+00:00 [2025-03-31T04:02:50.439000+00:00] abc2357702 (id=1356116505925910600) Hi guys, I’ve built a utility tool that saves you time and effort from messy wrapper scripts when running AIGC experiments across multiple GPUs—meet Labtasker! Who is this for? Graduate students, researchers, and hobbyists running multiple experiments under different settings. What does it do? Labtasker simplifies experiment scheduling with a task queue for efficient job distribution. ✅…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1356116505925910600-Labtasker--make-ML-experiment-wrapper-scripts-smarter-with-1-line-of-code-change.txt`

### tailscale
- **Source:** `local:research/crow-lore/hermes-android-termux-tailscale/entities/tailscale.md`
- **Raw:** `[[raw/local/tailscale-e8f7f74576.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Entity: Tailscale > Mesh VPN built on WireGuard that provides zero-config peer-to-peer connectivity with built-in SSH, identity-based ACLs, and automatic key rotation. ## What It Is Tailscale is a mesh VPN overlay network. Instead of routing all traffic through a central server, it establishes direct WireGuard tunnels between devices (peers) wherever possible, falling back to relay servers (DERP) only when NAT traversal fails. Each device gets a stable `100.x.y.z` IP address in the Tailscale CGNAT range. Key properties for this lore: - **No port forwarding needed** — devices connect through NATs and firewalls automatically. - **Built-in SSH** — `tailscale ssh` provides certificate-based…

### merges
- **Source:** `local:projects/ACE-Step-1.5/checkpoints/acestep-5Hz-lm-1.7B/merges.txt`
- **Raw:** `[[raw/local/merges-b1985d374e.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** #version: 0.2 Ġ Ġ ĠĠ ĠĠ i n Ġ t ĠĠĠĠ ĠĠĠĠ e r ĠĠ Ġ o n Ġ a r e a t s t e n o r Ġt h Ċ Ċ Ġ c l e Ġ s i t a n a r a l Ġth e ; Ċ Ġ p Ġ f o u Ġ = i s ĠĠĠĠ ĠĠĠ in g e s Ġ w i on e d i c Ġ b Ġ d e t Ġ m Ġ o ĉ ĉ r o a s e l c t n d Ġ in Ġ h en t i d Ġ n a m ĠĠĠĠĠĠĠĠ ĠĠĠ Ġt o Ġ re - - Ġ { Ġo f o m ) ;Ċ i m č Ċ Ġ ( i l / / Ġa nd u r s e Ġ l e x Ġ S a d Ġ " c h u t i f * * Ġ } e m o l ĠĠĠĠĠĠĠĠ ĠĠĠĠĠĠĠĠ t h ) Ċ Ġ{ Ċ Ġ g i g i v , Ċ c e o d Ġ v at e Ġ T a g a y Ġ * o t u s Ġ C Ġ st Ġ I u n u l u e Ġ A o w Ġ ' e w Ġ < at ion ( ) Ġf or a b or t u m am e Ġ is p e t r c k â Ģ Ġ y i st -- -- . ĊĊ h e Ġ e l o Ġ M Ġb e er s Ġ on Ġc on a p u b Ġ P ĠĠĠĠĠĠĠĠ ĠĠĠĠĠĠĠ as s in t > Ċ l y ur n Ġ $ ; ĊĊ a v p ort i r…

- **Collapsed duplicates:** `local:projects/AI-ML/senter-archive/omni-3b/checkpoint-1/merges.txt`, `local:projects/AI-ML/senter-archive/omni-3b/checkpoint-48/merges.txt`, `local:projects/AI-ML/senter-archive/omni-3b/merges.txt`, `local:projects/AI-ML/senter-archive/phase1/checkpoint-100/merges.txt`, `local:projects/AI-ML/senter-archive/phase1/checkpoint-200/merges.txt`, `local:projects/AI-ML/senter-archive/phase1/checkpoint-282/merges.txt`, `local:projects/AI-ML/senter-archive/phase1/merges.txt`, `local:projects/AI-ML/senter-archive/phase2/checkpoint-283/merges.txt`

### user-story-template
- **Source:** `local:projects/omnistudio-daw/docs/qa/templates/user-story-template.md`
- **Raw:** `[[raw/local/user-story-template-d533e6b70a.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # QA User Story Template ## Story Metadata - Story ID: `CAP-000` - Capability: - Persona: - Priority: `P0 | P1 | P2` - Release Status: `release-critical | core-regression | long-tail` ## User Story As a [persona], I want to [action], so that [outcome]. ## Acceptance Criteria - - - ## Setup and Preconditions - Environment: - Required data/state: - Whether store/API setup is allowed: ## Observable Pass / Fail Signals - Pass: - Fail: ## Automation Mapping - Coverage: `A-full | A-partial | Blocked-env | Missing` - Unit / integration: - E2E: - Intentionally not automated: ## Human QA Mapping - Coverage: `H-required | none` - Required judgment: - Evidence to attach: ## Linked Artifacts -…

### track-management
- **Source:** `local:projects/omnistudio-daw/docs/qa/capabilities/track-management.md`
- **Raw:** `[[raw/local/track-management-426b74a4ca.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Capability QA - Track Management ## Purpose Validate the first layer of musical structure: creating tracks and controlling their audible state. ## Setup and Boundaries - Stories should prefer the instrument picker and visible track controls. - Store setup is allowed only to seed a project when the UI under test is not the setup path itself. - Human QA should verify iconography, ordering, and audibility implications. ## Stories ### TRK-001 Add a stems track from the instrument picker As a user, I want to add a stems track from the picker, so that I can start building an arrangement from the UI without memorizing APIs. Acceptance criteria: - The instrument picker opens from the documented…

### piano-roll
- **Source:** `local:projects/omnistudio-daw/docs/qa/capabilities/piano-roll.md`
- **Raw:** `[[raw/local/piano-roll-e657fa8de1.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Capability QA - Piano Roll ## Purpose Validate the core MIDI editing workflow and the discoverability of the piano-roll editor. ## Setup and Boundaries - Stories may seed a piano roll track or clip through the store when the UI under test is the editor behavior itself. - User-facing open/close flows should still be validated through visible interactions. - Human QA must judge editing comfort, preview feel, and visual note rendering. ## Stories ### PNR-001 Open the piano roll for a track As a user, I want to open the piano roll from the track context, so that I can reach MIDI editing without hidden setup. Acceptance criteria: - A piano roll track exposes an open action through the visible…

### onboarding
- **Source:** `local:projects/omnistudio-daw/docs/qa/capabilities/onboarding.md`
- **Raw:** `[[raw/local/onboarding-94d8c35ec4.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Capability QA - Onboarding ## Purpose Validate the first-run experience before a user has any project context. ## Setup and Boundaries - Start from a clean browser profile or clear persisted UI/project state. - Prefer browser-only verification for visibility, skipping, and focus behavior. - Store setup is not allowed unless the story explicitly says it is. - Human QA is required to judge clarity, pacing, and visual hierarchy. ## Agent Evidence Rules - Capture a screenshot of the first-run surface. - Attach trace or console output if onboarding is blocked by another overlay. - Record whether the next expected surface was the onboarding flow or the project dialog. ## Stories ### ONB-001…

### sequencer
- **Source:** `local:projects/omnistudio-daw/docs/qa/capabilities/sequencer.md`
- **Raw:** `[[raw/local/sequencer-039a0b8526.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Capability QA - Sequencer ## Purpose Validate pattern-entry workflows for beat-oriented composition. ## Setup and Boundaries - Start from a project with a sequencer track. - Prefer visible step toggling for user stories. - Human QA is required for groove, timing feel, and pad responsiveness. ## Stories ### SEQ-001 Program a basic step pattern As a user, I want to toggle steps in a sequencer grid, so that I can build a drum pattern quickly. Acceptance criteria: - Turning steps on and off changes the stored pattern. - A basic pattern can be created without editor crashes. - Step state remains consistent across playback and editor refresh. Automation mapping: - `A-partial` - Primary tests:…

### project-lifecycle
- **Source:** `local:projects/omnistudio-daw/docs/qa/capabilities/project-lifecycle.md`
- **Raw:** `[[raw/local/project-lifecycle-76ca175a66.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Capability QA - Project Lifecycle ## Purpose Validate project creation and safe exit paths before track or clip editing begins. ## Setup and Boundaries - Start from first-run or returning-user state as required by the story. - Browser-first verification is mandatory for dialog presence and button affordances. - Store seeding is allowed only for agent contract tests, not for dialog success paths. ## Stories ### PRJ-001 Create a project with default settings As a user, I want to create a project with the default setup, so that I can reach a usable DAW workspace immediately. Acceptance criteria: - Confirming the dialog creates a project without requiring extra fields. - The app enters a…

### transport-keyboard
- **Source:** `local:projects/omnistudio-daw/docs/qa/capabilities/transport-keyboard.md`
- **Raw:** `[[raw/local/transport-keyboard-6a954ffe0b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Capability QA - Transport and Keyboard Workflow ## Purpose Validate the DAW's keyboard-first operating loop, including playback, panel shortcuts, and agent-visible command contracts. ## Setup and Boundaries - Use a created project unless the story explicitly tests no-project behavior. - Set focus intentionally before shortcut tests. - Agent setup through store APIs is allowed for zoom-contract stories but not for shortcut discoverability stories. ## Stories ### TRN-001 Space toggles play/pause As a user, I want to use the spacebar to play and pause, so that transport control feels immediate and standard. Acceptance criteria: - Space starts playback when the app is in a playable context. -…

### output-and-mixing
- **Source:** `local:projects/omnistudio-daw/docs/qa/capabilities/output-and-mixing.md`
- **Raw:** `[[raw/local/output-and-mixing-e26ca34f2d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Capability QA - Output and Mixing ## Purpose Validate the path from inspecting session output readiness to exporting or mixing it. ## Setup and Boundaries - Export readiness may use seeded content when the UI under test is the export surface itself. - Mixer stories should prefer user-visible panel toggles over direct store state mutation. - Human QA is required for audible mix judgment and output confidence. ## Stories ### OUT-001 Open the export surface from the keyboard As a user, I want to open export from the keyboard, so that final output is reachable from the same flow as the rest of the DAW. Acceptance criteria: - The documented export shortcut opens the export dialog. - The export…

### bug-report-template
- **Source:** `local:projects/omnistudio-daw/docs/qa/templates/bug-report-template.md`
- **Raw:** `[[raw/local/bug-report-template-c78fc98d68.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # QA Bug Report Template ## Metadata - Story ID(s): - Capability: - Priority: - Environment: - Found by: `agent | manual QA | CI` ## Summary Short statement of the broken user outcome. ## Expected Behavior Describe the story-level expected result. ## Actual Behavior Describe what actually happened. ## Reproduction 1. 2. 3. ## Evidence - Screenshot / GIF: - Trace / console output: - Related automated test: ## Impact - Release status affected: - User-visible severity: - Suggested follow-up issue:

### bug-report-20260318
- **Source:** `local:projects/omnistudio-daw/docs/qa/bug-report-20260318.md`
- **Raw:** `[[raw/local/bug-report-20260318-faa8d9e453.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # QA Bug Report — 2026-03-18 **Tester:** Automated QA (Playwright E2E) **Environment:** macOS (arm64), Chromium (Playwright), Node v22.22.1 **App Version:** ace-step-daw 0.1.0 **Dev Server:** `npm run dev` → http://127.0.0.1:5174 **Total Tests:** 49 | **Passed:** 49 | **Failed:** 0 **Screenshots:** `test-screenshots/` directory (49 screenshots) --- ## Test Summary ### 1. New Project Creation ✅ | Test | Result | Notes | |------|--------|-------| | 1a. Dialog appears on first load | ✅ Pass | Dialog renders correctly | | 1b. Create with defaults | ✅ Pass | Project created, transport bar visible | | 1c. Custom name & BPM | ✅ Pass | Custom values persist correctly | | 1d. Cancel closes dialog |…

### Cargo
- **Source:** `local:projects/omnistudio-daw/crates/ace-waveform/Cargo.toml`
- **Raw:** `[[raw/local/cargo-ea93fbfa47.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** [package] name = "ace-waveform" description = "Multi-level mipmap waveform pyramid — min/max/RMS per block per channel" version.workspace = true edition.workspace = true license.workspace = true [lib] crate-type = ["lib"] [dependencies] libm = "0.2" [features] default = ["std"] std = [] [dev-dependencies] approx = "0.5"

### PULL_REQUEST_TEMPLATE
- **Source:** `local:projects/omnistudio-daw/.github/PULL_REQUEST_TEMPLATE.md`
- **Raw:** `[[raw/local/pull_request_template-877a683960.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** ## Summary <!-- Brief description of what this PR does --> Closes #<!-- issue number --> ## Changes - <!-- List key changes --> ## Test Plan - [ ] `npx tsc --noEmit` passes - [ ] `npm test` passes - [ ] `npm run build` succeeds - [ ] UI changes verified visually (if applicable) ## Screenshots <!-- Before/after screenshots for UI changes -->

### feature
- **Source:** `local:projects/omnistudio-daw/.github/ISSUE_TEMPLATE/feature.md`
- **Raw:** `[[raw/local/feature-f9f024f210.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: Feature Request about: Propose a new feature or enhancement labels: enhancement --- ## Description <!-- What feature do you want? Why? --> ## Proposed Solution <!-- How should this work? --> ## Alternatives Considered <!-- Any other approaches? --> ## Acceptance Criteria - [ ] <!-- Specific, testable criterion --> - [ ] Unit tests cover the new behavior - [ ] UI changes verified visually with preview tools

### bug
- **Source:** `local:projects/omnistudio-daw/.github/ISSUE_TEMPLATE/bug.md`
- **Raw:** `[[raw/local/bug-d7dfc24f14.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: Bug Report about: Report a bug or unexpected behavior labels: bug --- ## Description <!-- A clear, concise description of the bug --> ## Steps to Reproduce 1. 2. 3. ## Expected Behavior <!-- What should happen --> ## Actual Behavior <!-- What actually happens --> ## Environment - Browser: - OS: - Node version: ## Screenshots / Logs <!-- If applicable --> ## Acceptance Criteria - [ ] Bug is reproducible with steps above - [ ] Regression test added that fails without the fix - [ ] Fix passes all quality gates

### SKILL
- **Source:** `local:projects/omnistudio-daw/.claude/skills/openspec-propose/SKILL.md`
- **Raw:** `[[raw/local/skill-271af996c5.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: openspec-propose description: Propose a new change with all artifacts generated in one step. Use when the user wants to quickly describe what they want to build and get a complete proposal with design, specs, and tasks ready for implementation. license: MIT compatibility: Requires openspec CLI. metadata: author: openspec version: "1.0" generatedBy: "1.3.0" --- Propose a new change - create the change and generate all artifacts in one step. I'll create a change with artifacts: - proposal.md (what & why) - design.md (how) - tasks.md (implementation steps) When ready to implement, run /opsx:apply --- **Input**: The user's request should include a change name (kebab-case) OR a…

### SKILL
- **Source:** `local:projects/omnistudio-daw/.claude/skills/openspec-archive-change/SKILL.md`
- **Raw:** `[[raw/local/skill-abbed1e2d7.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: openspec-archive-change description: Archive a completed change in the experimental workflow. Use when the user wants to finalize and archive a change after implementation is complete. license: MIT compatibility: Requires openspec CLI. metadata: author: openspec version: "1.0" generatedBy: "1.3.0" --- Archive a completed change in the experimental workflow. **Input**: Optionally specify a change name. If omitted, check if it can be inferred from conversation context. If vague or ambiguous you MUST prompt for available changes. **Steps** 1. **If no change name provided, prompt for selection** Run `openspec list --json` to get available changes. Use the **AskUserQuestion tool** to…

### SKILL
- **Source:** `local:projects/omnistudio-daw/.claude/skills/openspec-apply-change/SKILL.md`
- **Raw:** `[[raw/local/skill-1d84b01651.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: openspec-apply-change description: Implement tasks from an OpenSpec change. Use when the user wants to start implementing, continue implementation, or work through tasks. license: MIT compatibility: Requires openspec CLI. metadata: author: openspec version: "1.0" generatedBy: "1.3.0" --- Implement tasks from an OpenSpec change. **Input**: Optionally specify a change name. If omitted, check if it can be inferred from conversation context. If vague or ambiguous you MUST prompt for available changes. **Steps** 1. **Select the change** If a name is provided, use it. Otherwise: - Infer from conversation context if the user mentioned a change - Auto-select if only one active change…

### SKILL
- **Source:** `local:projects/omnistudio-daw/.claude/skills/brainstorm/SKILL.md`
- **Raw:** `[[raw/local/skill-b878a9b3cc.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Brainstorm Skill > Multi-approach exploration protocol. Use when there are multiple valid ways to solve > a problem and you need to pick the best one — not just the first one that comes to mind. > > **Use this when**: The task has 2+ viable approaches and the wrong choice would be > expensive to reverse (architecture, data model, complex UI pattern). > > **Don't use this when**: There's an obvious approach, or the task is small enough > that any approach works. Don't brainstorm how to add a CSS class. ## When to Trigger 1. **Architecture decision**: New store shape, new service, new component hierarchy 2. **Algorithm choice**: Multiple valid approaches with different tradeoffs 3. **UI…

### development-process
- **Source:** `local:projects/omnistudio-daw/.claude/rules/development-process.md`
- **Raw:** `[[raw/local/development-process-7a24e5005f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Development Process > Auto-loaded for all agents. Follow this process for any non-trivial work. ## TDD Cycle (mandatory) 1. **Red**: Write a failing test first 2. **Green**: Minimum code to pass 3. **Refactor**: Clean up, keep tests green 4. **Commit**: Conventional commit message ## Before Coding - **Spec check**: If a `spec:` label exists on the issue, read the corresponding spec in `openspec/specs/` or `openspec/changes/` before writing any code. Use Given/When/Then scenarios to drive test generation. - For new features touching 3+ files: run `/opsx:propose` first to create formal specs - Run `npm test` to establish baseline - For UI tasks: read…

### git-conventions
- **Source:** `local:projects/omnistudio-daw/.claude/rules/git-conventions.md`
- **Raw:** `[[raw/local/git-conventions-63e6bd8414.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Git Conventions > Auto-loaded for all agents. Non-negotiable. ## Branch Naming - Feature: `feat/issue-NUMBER` or `feat/issue-NUMBER-short-desc` - Bug fix: `fix/issue-NUMBER` or `fix/issue-NUMBER-short-desc` - Legacy format also accepted: `feat/v0.0.X-xxx`, `fix/v0.0.X-xxx` ## Commit Messages - Prefix: `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:` - Reference issue: `feat: add mixer panel (#123)` or `Closes #123` in body ## Identity - `user.name: ChuxiJ` - `user.email: junmin@acestudio.ai` ## PR Lifecycle Ownership - Don't abandon PRs — handle CI failures, review comments, conflicts until merged - Every PR body must contain `Closes #NUMBER` linking to the issue - All project…

### testing-requirements
- **Source:** `local:projects/omnistudio-daw/.claude/rules/testing-requirements.md`
- **Raw:** `[[raw/local/testing-requirements-70b154cfc3.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Testing Requirements > Auto-loaded for all agents. Non-negotiable. ## Mandatory Test Coverage - Every new feature MUST include unit tests (+ E2E if UI-facing) - Every bug fix MUST include a regression test - Run `npm test` before AND after code changes - Never move on with red tests — fix immediately ## Test Quality - Never write tests that only assert truthiness — assert specific values - Tests assert behavior, not implementation details - For interactive features, write adversarial test cases in TDD Red phase: - Weird BPMs, rapid input, undo immediately after action, drag during playback - Edge cases covered: empty state, error state, boundary values ## UI Changes - UI changes require…

### propose
- **Source:** `local:projects/omnistudio-daw/.claude/commands/opsx/propose.md`
- **Raw:** `[[raw/local/propose-e73e74dfe7.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: "OPSX: Propose" description: Propose a new change - create it and generate all artifacts in one step category: Workflow tags: [workflow, artifacts, experimental] --- Propose a new change - create the change and generate all artifacts in one step. I'll create a change with artifacts: - proposal.md (what & why) - design.md (how) - tasks.md (implementation steps) When ready to implement, run /opsx:apply --- **Input**: The argument after `/opsx:propose` is the change name (kebab-case), OR a description of what the user wants to build. **Steps** 1. **If no input provided, ask what they want to build** Use the **AskUserQuestion tool** (open-ended, no preset options) to ask: > "What…

### apply
- **Source:** `local:projects/omnistudio-daw/.claude/commands/opsx/apply.md`
- **Raw:** `[[raw/local/apply-c25d5444bd.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: "OPSX: Apply" description: Implement tasks from an OpenSpec change (Experimental) category: Workflow tags: [workflow, artifacts, experimental] --- Implement tasks from an OpenSpec change. **Input**: Optionally specify a change name (e.g., `/opsx:apply add-auth`). If omitted, check if it can be inferred from conversation context. If vague or ambiguous you MUST prompt for available changes. **Steps** 1. **Select the change** If a name is provided, use it. Otherwise: - Infer from conversation context if the user mentioned a change - Auto-select if only one active change exists - If ambiguous, run `openspec list --json` to get available changes and use the **AskUserQuestion tool** to…

### tester
- **Source:** `local:projects/omnistudio-daw/.claude/agents/tester.md`
- **Raw:** `[[raw/local/tester-6a7e01f006.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: tester description: Run full test suite, analyze failures, create fix tasks, and generate test reports. tools: - Read - Write - Edit - Bash - Grep - Glob --- # Test Runner & Report Agent You are a QA agent. Your job is to run the full test suite, analyze results, and create fix tasks for any failures. ## Workflow 1. **Run quality gates** in order: 2. **Spec validation** (if given a change name or spec-labeled issues exist): - If a change name is provided: read specs from `openspec/changes/<name>/specs/` or `openspec/specs/` - Otherwise: find active spec labels via `gh issue list --repo ace-step/ACE-Step-DAW --json labels --jq '[.[].labels[].name | select(startswith("spec:"))] |…

### do-todo
- **Source:** `local:projects/omnistudio-daw/.claude/agents/do-todo.md`
- **Raw:** `[[raw/local/do-todo-087b330f58.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: do-todo description: Pick a task from GitHub Issues (or .llm/todo.md fallback), implement it using TDD, run tests, and commit. tools: - Read - Write - Edit - Bash - Grep - Glob - WebSearch - WebFetch --- # Task Executor Agent You are a TDD-driven developer agent. Your job is to pick up ONE task and complete it with full test coverage. ## Task Source Priority 1. **If given a specific task in your prompt** — use that directly 2. **If a GitHub Issue number is referenced** — work on that issue 3. **If neither** — read `.llm/todo.md` and find the first unchecked task (`- [ ]`) > `.llm/todo.md` is a session-local scratchpad. When picking a task from it, first create or locate a matching…

### merges
- **Source:** `local:projects/evolutionary-training/evolution/omnistep-4block/merges.txt`
- **Raw:** `[[raw/local/merges-82c69c9ab9.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** Ġ Ġ ĠĠ ĠĠ i n Ġ t ĠĠĠĠ ĠĠĠĠ e r ĠĠ Ġ o n Ġ a r e a t s t e n o r Ġt h Ċ Ċ Ġ c l e Ġ s i t a n a r a l Ġth e ; Ċ Ġ p Ġ f o u Ġ = i s ĠĠĠĠ ĠĠĠ in g e s Ġ w i on e d i c Ġ b Ġ d e t Ġ m Ġ o ĉ ĉ r o a s e l c t n d Ġ in Ġ h en t i d Ġ n a m ĠĠĠĠĠĠĠĠ ĠĠĠ Ġt o Ġ re - - Ġ { Ġo f o m ) ;Ċ i m č Ċ Ġ ( i l / / Ġa nd u r s e Ġ l e x Ġ S a d Ġ " c h u t i f * * Ġ } e m o l ĠĠĠĠĠĠĠĠ ĠĠĠĠĠĠĠĠ t h ) Ċ Ġ{ Ċ Ġ g i g i v , Ċ c e o d Ġ v at e Ġ T a g a y Ġ * o t u s Ġ C Ġ st Ġ I u n u l u e Ġ A o w Ġ ' e w Ġ < at ion ( ) Ġf or a b or t u m am e Ġ is p e t r c k â Ģ Ġ y i st -- -- . ĊĊ h e Ġ e l o Ġ M Ġb e er s Ġ on Ġc on a p u b Ġ P ĠĠĠĠĠĠĠĠ ĠĠĠĠĠĠĠ as s in t > Ċ l y ur n Ġ $ ; ĊĊ a v p ort i r - > n t ct ion…

- **Collapsed duplicates:** `local:projects/evolutionary-training/evolution/qwen-cosmos/gen0_cand0/merges.txt`

### Windows Notes
- **Source:** `local:projects/ACE-Step-1.5/docs/sidestep/Windows Notes.md`
- **Raw:** `[[raw/local/windows-notes-13437d211d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Windows Notes Side-Step fully supports Windows with CUDA GPUs. This page documents Windows-specific behavior, workarounds, and configuration details that differ from Linux/macOS. --- ## Installation The easiest way to install on Windows is the **Easy Installer**: 1. Clone or download Side-Step. 2. Double-click `install_windows.bat` (or run `install_windows.ps1` from PowerShell). The installer handles everything: - Installs `uv` (if not already present) - Installs Python 3.11 - Clones ACE-Step 1.5 alongside Side-Step - Runs `uv sync` for all dependencies - Optionally downloads model checkpoints **Requirements:** Windows 10/11, PowerShell 5.1+, Git, NVIDIA GPU with CUDA drivers. The…

- **Collapsed duplicates:** `local:projects/AI-ML/models/ACE-Step-1.5/docs/sidestep/Windows Notes.md`

### SECURITY
- **Source:** `local:projects/ACE-Step-1.5/SECURITY.md`
- **Raw:** `[[raw/local/security-7fbf2d2149.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Security Policy ## Reporting a Vulnerability We take security issues seriously and appreciate responsible disclosure. If you believe you have found a security vulnerability, **please do not report it in a public GitHub issue**. Instead, use one of the following private channels: - Open a **GitHub Security Advisory** for this repository (preferred) - Or contact the maintainers directly if a private email channel is listed Please include: - A clear description of the issue - Steps to reproduce (if applicable) - Potential impact - Any relevant proof-of-concept or logs We will acknowledge receipt and work to assess the issue as quickly as possible. ## Bug Bounties At this time, this project…

- **Collapsed duplicates:** `local:projects/AI-ML/models/ACE-Step-1.5/SECURITY.md`

### LICENSE-Live2D
- **Source:** `local:projects/nous-girl-agent/vtuber-core/LICENSE-Live2D.md`
- **Raw:** `[[raw/local/license-live2d-5e2b759bba.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Terms of Use for Live2D Cubism Sample Data Definition of Sample Data “Sample Data” means materials supplied by Live2D as sample, including without limitation any data, artwork, image, design, and trademark. Types of Sample Data The Live2D Cubism sample Data are categorized into three types: Live2D original characters, collaboration characters, and externally licensed characters. The terms of use are different for each type. Terms of Use for Live2D Original Characters These are Live2D original characters. When using these character data, you must consent to the following terms for using these Data and the Free Material License Agreement. Any Material distributed by Live2D Inc. through…

### theme_discipline
- **Source:** `local:projects/herm-sandbox/herm-tui-dev/docs/theme_discipline.md`
- **Raw:** `[[raw/local/theme_discipline-43cd6018d8.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Herm Theme Discipline Herm UI code names intent first. A component should ask for the role it is painting; the theme layer decides which concrete color that role uses in each installed theme. Keep the current theme contract working. Existing JSON themes, `ThemeCurrent` fields, plugin access through `api.theme.current`, and resolver fallbacks stay supported. Semantic roles are an additive layer over resolved theme tokens, not a reason to rewrite theme palettes or copy another tool's visual style. ## Identity Herm themes should preserve the app's own visual language: monochrome liminal space, Greek herm/pillar motifs, and retro-CGI grid restraint. Accents can vary by theme, but the UI…

- **Collapsed duplicates:** `local:projects/herm-tui/docs/theme_discipline.md`

### nav_and_ui_standards
- **Source:** `local:projects/herm-sandbox/herm-tui-dev/docs/nav_and_ui_standards.md`
- **Raw:** `[[raw/local/nav_and_ui_standards-5bfdaccf82.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Herm Navigation & UI Standards Prescriptive. New surfaces follow this; existing ones migrate toward it. Where this doc and `src/keys/catalog.ts` disagree, fix the catalog. ## Vocabulary - **pane** — a bordered region with its own keyboard surface (a `TabShell`, a detail sidebar, a dialog body) - **group / section** — a visually delimited cluster inside a pane (chip bar, column, category block) - **item** — a single selectable row/card/field/chip - **sub-mode** — a temporary text-capture state inside a pane (search `/`, inline edit) ## Key Behaviors | Key | Expected Action/Behavior | | :------------------- |…

- **Collapsed duplicates:** `local:projects/herm-source/docs/nav_and_ui_standards.md`, `local:projects/herm-tui/docs/nav_and_ui_standards.md`

### SKILL
- **Source:** `local:projects/herm-sandbox/herm-tui-dev/assets/skills/eikon/SKILL.md`
- **Raw:** `[[raw/local/skill-62d233c5f3.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: eikon description: Guide the user through making or editing a herm sidebar avatar (eikon) using herm's built-in Eikon Studio tab. The agent's role is advisory (what makes a good source, which knob to reach for); source generation is /eikon-create and all rasterize/bake happens in-app. related_skills: [eikon-create] --- # Building an eikon in herm An eikon is a 48×24 monochrome text avatar. It lives on disk as: ~/.hermes/eikons/<name>/ <name>.eikon packed NDJSON — written by Studio on Ctrl+S studio.json Studio's workspace state source/ base.<ext>, <state>.<ext> You do **not** write `.eikon` or `studio.json`. Studio does. ## Where the user does the work Herm's built-in **Eikon** tab…

- **Collapsed duplicates:** `local:projects/herm-tui/assets/skills/eikon/SKILL.md`

### SKILL
- **Source:** `local:projects/herm-sandbox/herm-tui-dev/assets/skills/eikon-create/SKILL.md`
- **Raw:** `[[raw/local/skill-747708345b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: eikon-create description: Interactively generate source images (and optionally short videos) for a herm eikon avatar, iterate on them with the user, and land them under ~/.hermes/eikons/<name>/source/ so the Eikon Studio tab can tune and bake them. This is the agent-driven counterpart to Studio's one-shot Generate dialog. tags: [eikon, avatar, image-gen, herm] related_skills: [eikon] --- # /eikon-create — generate eikon source files interactively You are producing **source files**, not the packed `.eikon`. Studio owns crop, tone (contrast/invert/flip), rasterizer choice, and baking. Your deliverable is one or more images/videos under ~/.hermes/eikons/<name>/source/ named so Studio…

- **Collapsed duplicates:** `local:projects/herm-tui/assets/skills/eikon-create/SKILL.md`

### bug_report
- **Source:** `local:projects/herm-sandbox/herm-tui-dev/.github/ISSUE_TEMPLATE/bug_report.md`
- **Raw:** `[[raw/local/bug_report-8f58fa053c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: Bug report about: Report an issue in Herm title: "[BUG]" labels: bug assignees: '' --- **Describe the bug** A clear and concise description of what the bug is. **To Reproduce** Steps to reproduce the behavior: 1. Go to '...' 2. Click on '....' 3. Scroll down to '....' 4. See error **Expected behavior** A clear and concise description of what you expected to happen. **Screenshots** If applicable **Desktop (please complete the following information):** - OS: [e.g. Ubuntu] - Termina; [e.g. ghostty, iterm] - Version [e.g. 1.2.3] **Additional context** Add any other context about the problem here.

- **Collapsed duplicates:** `local:projects/herm-source/.github/ISSUE_TEMPLATE/bug_report.md`, `local:projects/herm-tui/.github/ISSUE_TEMPLATE/bug_report.md`

### PULL_REQUEST_TEMPLATE
- **Source:** `local:projects/omni-fusion/SLAM-LLM/.github/PULL_REQUEST_TEMPLATE.md`
- **Raw:** `[[raw/local/pull_request_template-15c7015086.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # What does this PR do? <!-- Congratulations! You've made it this far! You're not quite done yet though. Please include a good title that fully reflects the extent of your awesome contribution. Then, please replace this with a description of the change and which issue is fixed (if applicable). Please also include relevant motivation and context. List any dependencies (if any) that are required for this change. --> <!-- Remove if not applicable --> Fixes # (issue) ## Feature/Issue validation/testing Please describe the tests that you ran to verify your changes and relevant result summary. Provide instructions so it can be reproduced. Please also list any relevant details for your test…

### docker-compose
- **Source:** `local:projects/omni-fusion/reap/docker-compose.yaml`
- **Raw:** `[[raw/local/docker-compose-2fbc536300.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** volumes: venv_data: services: app: build: context: . dockerfile: Dockerfile args: USER_ID: ${USER_ID:-1000} GROUP_ID: ${GROUP_ID:-1000} network: host volumes: - .:/app:rw - ~/.cache/huggingface:/home/dev/.cache/huggingface - venv_data:/app/.venv working_dir: /app tty: true stdin_open: true shm_size: "16g" mem_limit: "1t" deploy: resources: reservations: devices: - driver: nvidia count: all capabilities: [gpu] env_file: - .env environment: - NVIDIA_DRIVER_CAPABILITIES=all network_mode: host

### prompt
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/tools/live_bench/live_bench/data_generator/prompt.md`
- **Raw:** `[[raw/local/prompt-83d61d75af.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** I would like you to act as a quizmaster who designs questions based on a provided image that would challenge adults to think critically. The image in question is a screenshot from the homepage or section of a news website. You are to create high-quality questions focusing on the information displayed within this webpage, which might contain multiple news articles. Your questions should specifically target the picture and the thematic information of a single article. Your question should be answerable, and checkable. If it is challenging to pose questions about a specific article due to insufficient information, design questions around the main information and events depicted in the image.…

### mmlu_security_studies
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/mmlu/flan_cot_fewshot/mmlu_security_studies.yaml`
- **Raw:** `[[raw/local/mmlu_security_studies-084e1747d9.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** dataset_name: security_studies description: The following are multiple choice questions (with answers) about security studies. fewshot_config: sampler: first_n samples: - question: 'What are the frameworks of analysis within which terrorism has been considered (as of 2020)? (A) Competition between larger nations has resulted in some countries actively supporting terrorist groups to undermine the strength of rival states. Terrorist networks are extended patronage clubs maintained and paid for by their donor states and are conceptualised as being like state actors, to be dealt with using military force. (B) Globalization has enabled the internationalization of terrorist activities by opening…

### mmlu_high_school_us_history
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/mmlu/flan_cot_fewshot/mmlu_high_school_us_history.yaml`
- **Raw:** `[[raw/local/mmlu_high_school_us_history-b35b8dd8e5.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** dataset_name: high_school_us_history description: The following are multiple choice questions (with answers) about high school us history. fewshot_config: sampler: first_n samples: - question: "This question refers to the following information.\nI come not to urge\ \ personal claims, nor to seek individual benefits; I appear as the advocate\ \ of those who cannot plead their own cause; I come as the friend of those who\ \ are deserted, oppressed, and desolate. In the Providence of God, I am the\ \ voice of the maniac whose piercing cries from the dreary dungeons of your\ \ jails penetrate not your Halls of Legislation. I am the Hope of the poor crazed\ \ beings who pine in the cells, and…

### mmlu_high_school_biology
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/mmlu/flan_cot_fewshot/mmlu_high_school_biology.yaml`
- **Raw:** `[[raw/local/mmlu_high_school_biology-889ba7cb27.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** dataset_name: high_school_biology description: The following are multiple choice questions (with answers) about high school biology. fewshot_config: sampler: first_n samples: - question: "In animal cells, which of the following represents the most likely pathway\ \ that a secretory protein takes as it is synthesized in a cell?\n(A) Plasma\ \ membrane\u2013Golgi apparatus\u2013ribosome\u2013secretory vesicle\u2013rough\ \ ER (B) Ribosome\u2013Golgi apparatus\u2013rough ER\u2013secretory vesicle\u2013\ plasma membrane (C) Plasma membrane\u2013Golgi apparatus\u2013ribosome\u2013\ secretory vesicle\u2013rough ER (D) Ribosome\u2013rough ER\u2013Golgi apparatus\u2013\ secretory…

### mmlu_high_school_european_history
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/mmlu/flan_cot_fewshot/mmlu_high_school_european_history.yaml`
- **Raw:** `[[raw/local/mmlu_high_school_european_history-94f29d4d74.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** dataset_name: high_school_european_history description: The following are multiple choice questions (with answers) about high school european history. fewshot_config: sampler: first_n samples: - question: 'This question refers to the following information. Albeit the king''s Majesty justly and rightfully is and ought to be the supreme head of the Church of England, and so is recognized by the clergy of this realm in their convocations, yet nevertheless, for corroboration and confirmation thereof, and for increase of virtue in Christ''s religion within this realm of England, and to repress and extirpate all errors, heresies, and other enormities and abuses heretofore used in the same, be it…

### mmlu_formal_logic
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/mmlu/flan_cot_fewshot/mmlu_formal_logic.yaml`
- **Raw:** `[[raw/local/mmlu_formal_logic-f4018ebdc6.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** dataset_name: formal_logic description: The following are multiple choice questions (with answers) about formal logic. fewshot_config: sampler: first_n samples: - question: "Which of the given formulas of PL is the best symbolization of the following\ \ sentence?\nTurtles live long lives and are happy creatures, unless they are\ \ injured.\n(A) (L \u2022 H) \u2261 I (B) (L \u2022 H) \u2228 I (C) L \u2022\ \ (H \u2228 I) (D) L \u2022 (H \u2283 R)." target: "Let's think step by step. We refer to Wikipedia articles on formal logic\ \ for help. Let\u2019s solve this step by step. Let \u201CL\u201D denote \u201C\ living long\u201D, H \u201Cbeing happy\u201D, and \u201CI\u201D \u201Cbeing\ \…

### README
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/megabench/metrics/README.md`
- **Raw:** `[[raw/local/readme-dfdffd2c59.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # MEGA-Bench metrics Each task's metrics are specified in `metrics.json` and follow the schema outlined below: ## Scoring Functions ### String Comparisons These metrics are applied when both the response and the correct field are strings. - `exact_str_match`: Checks if the field exactly matches the reference response. - `simple_str_match`: Performs a case-insensitive comparison, ignoring spaces and hyphens, to determine if the response matches the correct field. - `exact_str_match_case_insensitive`: A case-insensitive version of `exact_str_match`. - `normalized_similarity_demarau_levenshtein`: Computes the normalized Damerau-Levenshtein similarity between the strings. - `near_str_match`:…

### charades
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/lmms_eval/tasks/charades_sta/charades.yaml`
- **Raw:** `[[raw/local/charades-bde65b4137.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** dataset_path: lmms-lab/charades_sta dataset_kwargs: token=<redacted> cache_dir: charades_sta video: True task: temporal_grounding_charades test_split: test generation_kwargs: max_new_tokens: 50 temperature: 0 top_p: 1.0 num_beams: 1 do_sample: false output_type: generate_until doc_to_visual: !function utils.temporal_grounding_doc_to_visual doc_to_text: !function utils.temporal_grounding_doc_to_text doc_to_target: !function utils.temporal_grounding_doc_to_answer process_results: !function utils.temporal_grounding_process_results_generation metric_list: - metric: submission aggregation: !function utils.temporal_grounding_aggregate_charades higher_is_better: true lmms_eval_specific_kwargs:…

### 002_caps
- **Source:** `local:projects/omni-fusion/MLLMerging/ModelCompose/playground/data/prompts/detail_description/002_caps.txt`
- **Raw:** `[[raw/local/002_caps-b07176112d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** A man holds a Wii-mote above his head while another looks on. A guy and his friend are playing Nintendo Wii. A young man is holding a video game remote over his head. two men standing in a room while one plays with a wii mote Some guys standing and playing a video game. couch: [0.697, 0.759, 0.995, 1.0] dining table: [0.426, 0.755, 1.0, 0.987] person: [0.082, 0.252, 0.342, 1.0] person: [0.399, 0.085, 0.742, 0.982] remote: [0.477, 0.135, 0.516, 0.187] sink: [0.016, 0.501, 0.063, 0.52] potted plant: [0.798, 0.384, 0.888, 0.645] refrigerator: [0.305, 0.389, 0.414, 0.547] chair: [0.72, 0.509, 0.858, 0.725]

### 002_conv
- **Source:** `local:projects/omni-fusion/MLLMerging/ModelCompose/playground/data/prompts/detail_description/002_conv.txt`
- **Raw:** `[[raw/local/002_conv-1d8a6b44f7.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** The image shows two men standing in a room, engaged in playing a video game on a Nintendo Wii console. One of the men is holding a Wii remote above his head with enthusiasm, while the other man looks on, likely enjoying the friendly competition. The room appears to be a living space with a couch located in the background and a dining table nearby. A potted plant can be seen placed close to the couch, and a chair is situated in the middle of the room. The room also features a kitchen area with a sink and a refrigerator visible in the background.

### CODE_OF_CONDUCT
- **Source:** `local:projects/omni-fusion/MLLMerging/ModelCompose/modelcompose/model/multimodal_encoder/video_llama/models/ImageBind/CODE_OF_CONDUCT.md`
- **Raw:** `[[raw/local/code_of_conduct-454afaf085.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Code of Conduct ## Our Pledge In the interest of fostering an open and welcoming environment, we as contributors and maintainers pledge to make participation in our project and our community a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, sex characteristics, gender identity and expression, level of experience, education, socio-economic status, nationality, personal appearance, race, religion, or sexual identity and orientation. ## Our Standards Examples of behavior that contributes to creating a positive environment include: * Using welcoming and inclusive language * Being respectful of differing viewpoints and experiences * Gracefully…

### text_translation
- **Source:** `local:projects/omni-fusion/MLLMerging/InternVL/internvl_chat/eval/mme/Your_Results/text_translation.txt`
- **Raw:** `[[raw/local/text_translation-f4ab96b3f3.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** 0001.png Is it appropriate to translate the Chinese in the image into English 'classic taste' in the picture? Please answer yes or no. Yes 0001.png Is it appropriate to translate the Chinese in the image into English 'classic strawberry flavor' in the picture? Please answer yes or no. No 0002.png Is it appropriate to translate the Chinese in the image into English 'a delicious dinner' in the picture? Please answer yes or no. Yes 0002.png Is it appropriate to translate the Chinese in the image into English 'hamburger and chips' in the picture? Please answer yes or no. No 0003.png Is it appropriate to translate the Chinese in the image into English 'sunny weather' in the picture? Please…

### scene
- **Source:** `local:projects/omni-fusion/MLLMerging/InternVL/internvl_chat/eval/mme/Your_Results/scene.txt`
- **Raw:** `[[raw/local/scene-244f927035.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** Places365_val_00000001.jpg Is this picture captured in a place of greenhouse indoor? Please answer yes or no. Yes Places365_val_00000001.jpg Is this picture captured in a place of waiting room? Please answer yes or no. No Places365_val_00000002.jpg Is this photo taken in a place of wet bar? Please answer yes or no. Yes Places365_val_00000002.jpg Is this photo taken in a place of stage indoor? Please answer yes or no. No Places365_val_00000003.jpg Is this picture captured in a place of clean room? Please answer yes or no. Yes Places365_val_00000003.jpg Is this picture captured in a place of bookstore? Please answer yes or no. No Places365_val_00000004.jpg Is this picture captured in a place…

### landmark
- **Source:** `local:projects/omni-fusion/MLLMerging/InternVL/internvl_chat/eval/mme/Your_Results/landmark.txt`
- **Raw:** `[[raw/local/landmark-56299c035d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** 0006adf999ccc899.jpg Is this a photo of Muktinath? Please answer yes or no. Yes 0006adf999ccc899.jpg Is this a photo of Lohikoski Church? Please answer yes or no. No 0015309638e5a9b1.jpg Is this a picture of Teufelsmauer (Harz)? Please answer yes or no. Yes 0015309638e5a9b1.jpg Is this a picture of Romfo kirke? Please answer yes or no. No 001f0bfe8464254a.jpg Is this a picture of Saint Catherine of Alexandria church in Warsaw? Please answer yes or no. Yes 001f0bfe8464254a.jpg Is this a picture of Kaap Skil? Please answer yes or no. No 0022666a36b80ea5.jpg Is this an image of Hall of Supreme Harmony (Forbidden City)? Please answer yes or no. Yes 0022666a36b80ea5.jpg Is this an image of…

### artwork
- **Source:** `local:projects/omni-fusion/MLLMerging/InternVL/internvl_chat/eval/mme/Your_Results/artwork.txt`
- **Raw:** `[[raw/local/artwork-7aa71c678c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** 10002.jpg Does this artwork exist in the form of painting? Please answer yes or no. Yes 10002.jpg Does this artwork exist in the form of glassware? Please answer yes or no. No 10049.jpg Does this artwork exist in the form of painting? Please answer yes or no. Yes 10049.jpg Does this artwork exist in the form of sculpture? Please answer yes or no. No 10256.jpg Does this artwork exist in the form of painting? Please answer yes or no. Yes 10256.jpg Does this artwork exist in the form of sculpture? Please answer yes or no. No 10358.jpg Does this artwork exist in the form of painting? Please answer yes or no. Yes 10358.jpg Does this artwork exist in the form of glassware? Please answer yes or…

### existence
- **Source:** `local:projects/omni-fusion/MLLMerging/InternVL/internvl_chat/eval/mme/Your_Results/existence.txt`
- **Raw:** `[[raw/local/existence-e17ea92527.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** 000000006040.jpg Is there a train in this image? Please answer yes or no. Yes 000000006040.jpg Is there a bed in this image? Please answer yes or no. No 000000006471.jpg Is there a baseball bat in this image? Please answer yes or no. Yes 000000006471.jpg Is there a giraffe in this image? Please answer yes or no. No 000000007108.jpg Is there a elephant in this image? Please answer yes or no. Yes 000000007108.jpg Is there a hair drier in this image? Please answer yes or no. No 000000007816.jpg Is there a motorcycle in this image? Please answer yes or no. Yes 000000007816.jpg Is there a airplane in this image? Please answer yes or no. No 000000007977.jpg Is there a skateboard in this image?…

### count
- **Source:** `local:projects/omni-fusion/MLLMerging/InternVL/internvl_chat/eval/mme/Your_Results/count.txt`
- **Raw:** `[[raw/local/count-8e885f2e42.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** 000000006040.jpg Is there a train in the picture? Please answer yes or no. Yes 000000006040.jpg Are there a total of two trains in the picture? Please answer yes or no. No 000000044279.jpg Is there a total of two people in the image? Please answer yes or no. Yes 000000044279.jpg Is there only one people in the image? Please answer yes or no. No 000000067213.jpg Is there only one dog in the image? Please answer yes or no. Yes 000000067213.jpg Is there two dogs in the image? Please answer yes or no. No 000000071226.jpg Is there a total of two dogs in the image? Please answer yes or no. Yes 000000071226.jpg Is there only one dogs in the image? Please answer yes or no. No 000000097994.jpg Are…

### commonsense_reasoning
- **Source:** `local:projects/omni-fusion/MLLMerging/InternVL/internvl_chat/eval/mme/Your_Results/commonsense_reasoning.txt`
- **Raw:** `[[raw/local/commonsense_reasoning-3fceadba79.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** 0001.png Here are the order details for my taxi ride. Should I actually pay $29.42? Please answer yes or no. Yes 0001.png Here are the order details for my taxi ride. Should I actually pay $32.42? Please answer yes or no. No 0002.png Should I stop when I'm about to cross the street and see the sign in the picture? Please answer yes or no. Yes 0002.png When I see the sign in the picture, can I cross the street? Please answer yes or no. No 0003.png May I ask if in the game of finger-guessing game, did the right side of the picture win? Please answer yes or no. Yes 0003.png May I ask if in the game of finger-guessing game, did the left side of the picture win? Please answer yes or no. No…

### code_reasoning
- **Source:** `local:projects/omni-fusion/MLLMerging/InternVL/internvl_chat/eval/mme/Your_Results/code_reasoning.txt`
- **Raw:** `[[raw/local/code_reasoning-a46fd12b12.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** 0001.png The image shows a python code. Is the output of the code 'Hello'? Please answer yes or no. Yes 0001.png The image shows a python code. Is the output of the code 'World'? Please answer yes or no. No 0002.png The image shows a python code. Is the output of the code 'a cat'? Please answer yes or no. Yes 0002.png The image shows a python code. Is the output of the code 'a dog'? Please answer yes or no. No 0003.png The image shows a python code. Is the output of the code '12'? Please answer yes or no. Yes 0003.png The image shows a python code. Is the output of the code '5'? Please answer yes or no. No 0004.png The image shows a python code. Is the output of the code '3'? Please answer…

### OCR
- **Source:** `local:projects/omni-fusion/MLLMerging/InternVL/internvl_chat/eval/mme/Your_Results/OCR.txt`
- **Raw:** `[[raw/local/ocr-97a799f2ee.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** 0001.jpg Is the word in the logo "angie's"? Please answer yes or no. Yes 0001.jpg Is the word in the logo "angle's"? Please answer yes or no. No 0002.jpg Is the word in the logo "c'est cheese"? Please answer yes or no. Yes 0002.jpg Is the word in the logo "crest cheese"? Please answer yes or no. No 0003.jpg Is the word in the logo "beavertails pastry"? Please answer yes or no. Yes 0003.jpg Is the word in the logo "beavertalls pastry"? Please answer yes or no. No 0004.jpg Is the word in the logo "old market sundries"? Please answer yes or no. Yes 0004.jpg Is the word in the logo "old market hundreds"? Please answer yes or no. No 0005.jpg Is the word in the logo "kress"? Please answer yes or…

### autoparser
- **Source:** `local:projects/LLM-Infra/llama.cpp-tq3/docs/autoparser.md`
- **Raw:** `[[raw/local/autoparser-6eb1b4f776.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Auto-Parser Architecture The auto-parser automatically analyzes chat templates to determine how to parse model outputs, including content, reasoning, and tool calls. ## Overview The unified auto-parser uses a pure differential, compositional approach (inspired by the `git diff` algorithm) to analyze chat templates: **Core Philosophy**: - **Minimize Hardcoded Patterns**: All markers extracted through template comparison (the only heuristic is JSON detection to distinguish `JSON_NATIVE` from tag-based formats) - **Compositional Architecture**: Separate analyzer structs for reasoning, content, and tools — each responsible for its own analysis and parser construction **Analysis + Parser…

### build-android
- **Source:** `local:projects/LLM-Infra/llama.cpp-tq3/.github/workflows/build-android.yml`
- **Raw:** `[[raw/local/build-android-19f67bb97f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: CI (android) on: workflow_dispatch: # allows manual triggering push: branches: - master paths: [ '.github/workflows/build-android.yml', '**/CMakeLists.txt', '**/.cmake', '**/*.h', '**/*.hpp', '**/*.c', '**/*.cpp' ] pull_request: types: [opened, synchronize, reopened] paths: [ '.github/workflows/build-android.yml', 'examples/llama.android/**' ] concurrency: group: ${{ github.workflow }}-${{ github.head_ref && github.ref || github.run_id }} cancel-in-progress: true env: GGML_NLOOP: 3 GGML_N_THREADS: 1 LLAMA_LOG_COLORS: 1 LLAMA_LOG_PREFIX: 1 LLAMA_LOG_TIMESTAMPS: 1 jobs: android: runs-on: ubuntu-latest steps: - name: Clone uses: actions/checkout@v6 with: fetch-depth: 0 lfs: false - name:…

### 040-refactor
- **Source:** `local:projects/LLM-Infra/llama.cpp-tq3/.github/ISSUE_TEMPLATE/040-refactor.yml`
- **Raw:** `[[raw/local/040-refactor-edf94c96f3.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: Refactor (Maintainers) description: Used to track refactoring opportunities. title: "Refactor: " labels: ["refactor"] body: - type: markdown attributes: value: | Don't forget to [check for existing refactor issue tickets](https://github.com/ggml-org/llama.cpp/issues?q=is%3Aopen+is%3Aissue+label%3Arefactoring) in case it's already covered. Also you may want to check [Pull request refactor label as well](https://github.com/ggml-org/llama.cpp/pulls?q=is%3Aopen+is%3Apr+label%3Arefactoring) for duplicates too. - type: textarea id: background-description attributes: label: Background Description description: Please provide a detailed written description of the pain points you are trying to…

### session_20260512_154956_3db3df
- **Source:** `session:session_20260512_154956_3db3df.json`
- **Raw:** `[[raw/sessions/session_20260512_154956_3db3df-e00128adc2.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** ok so caps lock is not toggling themes like I asked you too, it does this: 57376u. Also there is still an error at /tmp/Alacritty-2696394.log Found it! Two problems: 1. **The Alacritty error**: `shared.toml` line 16 has both `action = "ReceiveChar"` AND `chars = ...` — Alacritty wants **exactly one** of `chars`, `action`, or `command`, not both. 2. **The caps lock config**: The autostart entry shows caps lock is supposed to be remapped to F13, but the F13 binding itself is broken, so caps lock → F13 → nothing happens except Alacritty ignoring the binding and the terminal just echoes the raw escape sequence `57376u`. Let me see the full `shared.toml`: Ah, I see it now. The error is super…

### session_20260512_185414_ad52e1
- **Source:** `session:session_20260512_185414_ad52e1.json`
- **Raw:** `[[raw/sessions/session_20260512_185414_ad52e1-c70686980c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** ok so I keep trying to fix this. Should be simple. I heard that setting up hotkeys in herm was pretty easy. I simply want Caps Lock to switch themes between lucient-orng and orng. NOT as a Skill, NOT as something to send the model, I mean programically within herm, Caps Lock needs to toggle the themes. Right now, Caps Lock just simply prints this: 57376u The problem is clear — "57376u" printing means the escape sequence `\u001b[` isn't being generated. That's the CSI (escape character + bracket) prefix of the kitty keyboard protocol. Without it, Alacritty just types the literal text. Let me check what your Alacritty config looks like right now: The Alacritty config looks right. Let me check…

### session_20260512_074227_a76408
- **Source:** `session:session_20260512_074227_a76408.json`
- **Raw:** `[[raw/sessions/session_20260512_074227_a76408-b7f7743ab9.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** ok so I will be using herm while shooting a video. Right now, herm has a transparent theme where my camera shows through. I would like to take the Caps Lock button and make it toggle between the current theme (lucent-orng) and one that is not transparent (orng), the end result is I want to be able to tap the Caps Lock button to toggle between the two themes, which gives me a privacy filter as orng will cover up my camera and lucent-orng will show it. Ooh, that's a really clever idea! A privacy toggle right on Caps Lock — perfect for video shoots. Let me dig into herm's keybinding system to figure out the best way to wire this up. Excellent! I found the key piece — herm's CONTROL server has…

### README
- **Source:** `local:projects/dani-projects/art-website/README.md`
- **Raw:** `[[raw/local/readme-5467783b44.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Local Art Website A simple, responsive art portfolio website with store functionality built using HTML, CSS, and JavaScript. ## Features - Responsive design that works on mobile and desktop - Gallery section to showcase artwork - About section with artist information - Contact form for visitors to get in touch - Store section with artwork for sale - Navigation between sections without page reloads - Clean, modern design focused on displaying art ## How to Run 1. Clone or download this repository 2. Open `index.html` in your web browser 3. Navigate between sections using the menu links ## File Structure - `index.html` - Main HTML structure - `style.css` - All styling for the website -…

### config
- **Source:** `local:projects/pocket-shop/config.yaml`
- **Raw:** `[[raw/local/config-303ad6ba56.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Pocket Shop Configuration # DO NOT commit this file to git! # Restock fund target - when reached, consider expanding inventory restock_fund_target: 500.00 # EV threshold for set monitoring (minimum expected value to flag) ev_threshold: 10.0 # Revenue split percentages (must sum to 1.0) profit_split: savings: 0.30 # Long-term accumulation fund profit: 0.30 # Actual earnings you keep restock: 0.40 # Reinvestment for buying more cards # eBay Authentication - AUTH'N'AUTH METHOD (Recommended for personal use) # Simply add your eBay username and password - no OAuth flow needed! ebay_username: "sovthpaw" ebay_password=<redacted> ebay_app_id: "Christop-PocketSh-PRD-72b0faaa2-33ae83df"…

### phone-drawing-apps-2026-analysis
- **Source:** `local:research/phone-drawing-apps-2026-analysis.md`
- **Raw:** `[[raw/local/phone-drawing-apps-2026-analysis-e819c5609c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Comprehensive Analysis: Best Phone Drawing Apps 2025-2026 ## Executive Summary The mobile drawing landscape has matured significantly, with phone apps now offering 80-90% of tablet capabilities for most use cases. The best phone drawing apps in 2025-2026 include **Procreate Pocket** (iOS, $5.99 one-time), **Infinite Painter** (iOS/Android, freemium), **Clip Studio Paint** (iOS/Android, subscription), and **ibis Paint X** (iOS/Android, free with ads). Choice depends on platform, budget, and intended use—professional illustration, casual sketching, or comic creation. Phone drawing requires a compatible stylus and realistic expectations about screen size limitations. --- ## Platform…

### phone-drawing-apps-research
- **Source:** `local:research/phone-drawing-apps-research.md`
- **Raw:** `[[raw/local/phone-drawing-apps-research-e44d99248a.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Research: Best Phone Drawing Apps 2025-2026 ## Research Date: March 29, 2026 ## Executive Summary The mobile drawing app landscape in 2025-2026 offers professional-grade tools that rival desktop software, with options ranging from free open-source apps to premium one-time purchase solutions. Key findings include: Procreate Pocket dominates iOS with one-time purchase ($5.99), Infinite Painter is the top Android alternative, and Clip Studio Paint offers cross-platform professional features with subscription pricing. Phone drawing has limitations compared to tablets but is viable with proper stylus accessories and optimized apps. ## Initial Questions 1. What are the top-rated phone drawing…

### Drawing-Tablets-Research
- **Source:** `local:research/Drawing-Tablets-Research.md`
- **Raw:** `[[raw/local/drawing-tablets-research-70e98f1978.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Research: Best-Rated Affordable Drawing Tablets Under $150 (2025-2026) ## Initial Questions 1. What drawing tablets under $150 have 4+ star ratings with 100+ reviews on Amazon? 2. How do Wacom, Huion, XP-Pen compare in the budget segment? 3. Are there any newer emerging brands offering good value? 4. What are the key differences between display tablets and pen tablets in this price range? 5. What recurring issues do negative reviews mention? ## Search Plan - [ ] Search 1: Best budget drawing tablets 2025-2026 under $150 Amazon - [ ] Search 2: Huion drawing tablets budget 2025 reviews - [ ] Search 3: XP-Pen budget drawing tablets 2025 2026 - [ ] Search 4: Wacom budget drawing tablets…

### SKILL
- **Source:** `local:projects/pocket-shop/skills/pocket-shop-loop/SKILL.md`
- **Raw:** `[[raw/local/skill-62b668b54c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: pocket-shop-loop description: "Main orchestration for automated MTG card trading loop" trigger_conditions: - "Running automated MTG trading business" - "User wants to start Pocket-Shop automation" tools_required: - "browser_navigate" - "browser_snapshot" - "vision_analyze" - "read_file" - "write_file" - "execute_code" calls_skills: - "mtgstocks-set-discovery" - "multi-source-price-comparison" - "card-scanner-vision" - "pocket-shop-finance-tracker" --- # Pocket Shop Loop - Main Orchestration ## Overview Main orchestration skill that runs the complete automated MTG card trading loop: 1. **Monitor MTGStocks** for high EV sets under budget 2. **Research prices** across Amazon,…

### SKILL
- **Source:** `local:projects/pocket-shop/skills/pocket-shop-finance-tracker/SKILL.md`
- **Raw:** `[[raw/local/skill-f91a44a224.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: pocket-shop-finance-tracker description: "Track MTG card trading finances with 30/30/40 revenue split" trigger_conditions: - "Recording sales in Pocket-Shop loop" - "Tracking profits and restock fund" tools_required: - "read_file" - "write_file" --- # Pocket Shop Finance Tracker Skill ## Overview Tracks all financial transactions for the automated MTG trading loop with automatic 30/30/40 revenue splits. ### Revenue Split: - **30% Savings Fund** - Long-term savings - **30% Profit Total** - Pure profit accumulation - **40% Restock Fund** - Reinvested for next set purchase ## Data Structure Finance data stored in `~/.hermes/pocket-shop/finance.json`: ## Step-by-Step Workflow ### 1.…

### requirements
- **Source:** `local:projects/pocket-shop/requirements.txt`
- **Raw:** `[[raw/local/requirements-a9bc237d5d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** pyyaml requests selenium webdriver-manager playwright

### config.example
- **Source:** `local:projects/pocket-shop/config.example.yaml`
- **Raw:** `[[raw/local/config.example-c2e25bb9ae.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Pocket Shop Configuration Example # Copy this to config.yaml and fill in your values financial: restock_target: 500.00 # Dollar amount to trigger set purchase ev_threshold: 10.0 # Minimum EV percentage to consider gmail: email: "your-email@gmail.com" app_password=<redacted> # From Google App Passwords ebay: mode: browser # 'browser' (default) or 'api' # If using API mode, add these: # developer_id: "YOUR_DEVELOPER_ID" # cert_id: "YOUR_CERTIFICATE_ID" # app_id: "YOUR_RU_NAME" # refresh_token=<redacted> tcgplayer: api_key=<redacted> # Optional - browser mode works without this

### README
- **Source:** `local:projects/pocket-shop/README.md`
- **Raw:** `[[raw/local/readme-8919364ab1.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Pocket-Shop - Automated MTG Card Trading System Complete automated loop for profitable Magic: The Gathering card trading. ## How It Works ## Quick Start ### 1. Install Dependencies ### 2. Run Setup This will ask for: - Gmail credentials (for sales monitoring) - eBay mode preference (browser automation = no API needed) - Optional: TCGPlayer API key ### 3. Configure Gmail App Password 1. Go to: https://myaccount.google.com/security 2. Enable 2-Step Verification 3. Go to: https://myaccount.google.com/apppasswords 4. Create app password for "Mail" → "Other (Custom name)" 5. Copy the 16-character password ### 4. Run the Loop ## API Keys Setup Guide ### eBay API (Optional - Browser Mode is…

### config.example
- **Source:** `local:projects/pocket_shop/config.example.yaml`
- **Raw:** `[[raw/local/config.example-744e148328.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Pocket Shop Configuration Template # Copy this to config.yaml and fill in your actual values # NEVER commit config.yaml to git! # Financial Thresholds restock_fund_target: 500.00 # Dollar amount needed before auto-purchasing a set ev_threshold: 10.0 # Minimum EV percentage to consider a set # Profit split percentages (must add up to 1.0) profit_split: savings: 0.30 profit: 0.30 restock: 0.40 # eBay Settings (optional, for listing creation via API) ebay_developer_id: "YOUR_EBAY_DEVELOPER_ID" ebay_app_id: "YOUR_EBAY_APP_ID" ebay_cert_id: "YOUR_EBAY_CERT_ID" ebay_refresh_token=<redacted> ebay_marketplace: "EBAY_US" # Vision Settings card_confidence_threshold: 0.85 # Minimum confidence for…

### config
- **Source:** `local:projects/pocket_shop/config.yaml`
- **Raw:** `[[raw/local/config-6d0491507f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Pocket Shop Configuration # Financial Thresholds restock_fund_target: 500.00 # Dollar amount needed before auto-purchasing a set profit_split: savings: 0.30 profit: 0.30 restock: 0.40 # MTGStocks Settings ev_threshold: 10.0 # Minimum EV percentage to consider a set # eBay Settings (API for listing creation) ebay_developer_id: "YOUR_EBAY_DEVELOPER_ID" ebay_app_id: "YOUR_EBAY_APP_ID" ebay_cert_id: "YOUR_EBAY_CERT_ID" ebay_refresh_token=<redacted> ebay_marketplace: "EBAY_US" # Gmail Settings (email-triggered sales detection) gmail_client_id: "YOUR_GMAIL_CLIENT_ID" gmail_client_secret=<redacted> gmail_refresh_token=<redacted> gmail_sale_keyword: "sold" # Keyword to match in sale emails #…

### requirements
- **Source:** `local:projects/pocket_shop/requirements.txt`
- **Raw:** `[[raw/local/requirements-2b36e97ef8.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Pocket Shop Dependencies # HTTP Client requests>=2.31.0 aiohttp>=3.9.0 # APIs ebay-developer-sdk>=1.2.0 tcgplayer-api>=1.0.0 # Vision/Card Recognition opencv-python>=4.8.0 pillow>=10.0.0 pytesseract>=0.3.10 # Data Processing pandas>=2.0.0 numpy>=1.24.0 # Config Management pyyaml>=6.0 python-dotenv>=1.0.0 # Logging & Monitoring structlog>=23.1.0

### README
- **Source:** `local:projects/pocket_shop/README.md`
- **Raw:** `[[raw/local/readme-4b365649a9.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Pocket Shop — Automated Trading Card Store ## Overview Automated Magic: The Gathering card shop using MTGStocks for set discovery, TCGPlayer for pricing, and eBay for sales. ## Architecture ### Core Loop ### Components - **mtgstocks** — Monitor set EV, identify profitable purchases - **vision** — Card identification from photos - **tcgplayer** — Price lookup and market data - **ebay** — Draft creation, listing management, sales tracking - **finance** — Profit/savings/restock allocation ### Cron Jobs 1. `monitor_sets` — Every 6h: Check MTGStocks for high EV sets 2. `check_restock_fund` — On set discovery: Trigger purchase if threshold met 3. `sync_ebay_sales` — Every 1h: Pull sales data,…

### .README
- **Source:** `local:projects/.README.md`
- **Raw:** `[[raw/local/.readme-abd77cb14f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Projects Directory This directory contains all organized development projects. ## Structure - AI-ML/: AI/ML models and training - Agents/: AI agent frameworks - LLM-Infra/: LLM infrastructure - Mobile/: Mobile development - Games/: Game development - Hardware/: Hardware projects - Tools/: Development tools - Research/: Research projects - Finance/: Financial tools - Media/: Media processing - Web/: Web development See .PROJECT_MANIFEST.md for complete project listing.

### Home-Automation-AI-Integration-Research
- **Source:** `local:projects/Research/notes/Home-Automation-AI-Integration-Research.md`
- **Raw:** `[[raw/local/home-automation-ai-integration-research-32f5eddf5d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Research: Home Automation Integration for AI Assistants ## Executive Summary Home Assistant provides a robust local-first platform for AI assistant integration, offering REST API, WebSocket API, and MQTT for device control. For phone-based assistants like Senter (Samsung S10), the optimal approach combines Home Assistant as a hub with direct ADB control for TV/media, and either local or cloud-integrated smart devices via Zigbee/Z-Wave/WiFi protocols. The key to success is a layered architecture: local Home Assistant server → API → Phone-based AI agent → Voice commands. --- ## 1. Home Assistant - API Integration for AI Control ### REST API (Primary Control Method) **Endpoint**:…

### bug_report
- **Source:** `local:projects/AI-ML/models/ACE-Step-1.5/.github/ISSUE_TEMPLATE/bug_report.md`
- **Raw:** `[[raw/local/bug_report-0c8d64f29f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: Bug report about: Create a report to help us improve title: '' labels: '' assignees: '' --- **Describe the bug** A clear and concise description of what the bug is. **To Reproduce** Steps to reproduce the behavior: 1. Go to '...' 2. Click on '....' 3. Scroll down to '....' 4. See error **Expected behavior** A clear and concise description of what you expected to happen. **Screenshots** If applicable, add screenshots to help explain your problem. **Desktop (please complete the following information):** - OS: [e.g. iOS] - Browser [e.g. chrome, safari] - Version [e.g. 22] **Smartphone (please complete the following information):** - Device: [e.g. iPhone6] - OS: [e.g. iOS8.1] -…

### final_benchmarks
- **Source:** `local:projects/AI-ML/benchmarks/final_benchmarks.txt`
- **Raw:** `[[raw/local/final_benchmarks-50f6521db5.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** === COMPREHENSIVE BENCHMARK RESULTS === Date: Sun Feb 22 10:19:12 AM CST 2026 === GLM-4.7-FLASH (Reference Model) === --- Test 1: Math Reasoning --- --- Test 2: System Instruction (Pirate) --- --- Test 3: Tool Calling --- {'type': 'function', 'function': {'name': 'get_weather', 'arguments': '{"location":"Tokyo"}'}, 'id': '0teJrPhk2abi7M66R1MZhQjYMVTU3LlQ'} --- Test 4: Multi-step Reasoning --- --- Test 5: Code Generation --- === QWEN2.5-OMNI-3B BASELINE === --- Test 1: Math Reasoning --- To determine how many apples you have after the described actions, let's break down the problem step by step: 1. **Initial apples**: You start with 3 apples. 2. **apples bought**: you buy 5 more apples. 3.…

### benchmark_results
- **Source:** `local:projects/AI-ML/benchmarks/benchmark_results.txt`
- **Raw:** `[[raw/local/benchmark_results-c12e301282.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** === BASELINE MODEL TESTS === Test 1: Reasoning Let's break it down step by step: 1. You start with 3 apples. 2. You buy 5 more apples. So now you have 3 + 5 = 8 apples. 3. You eat 2 apples. So now you have 8 - 2 = 6 apples. Therefore, you have 6 apples left. Test 2: System Instruction Following I am Senter, the pirate. I serve the crew of the Black pearl, the ship of Captain Jack sparrow. Test 3: Tool Calling {'type': 'function', 'function': {'name': 'get_weather', 'arguments': '{"location":"New york"}'}, 'id': 'eR1E7hqu0GBMPfuR50r0Ywlid1iYrstI'}

### sandboxing
- **Source:** `local:projects/AI-ML/Senter/agent/docs/sandboxing.md`
- **Raw:** `[[raw/local/sandboxing-d896289abe.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ZeroClaw Sandboxing Strategies > ⚠️ **Status: Proposal / Roadmap** > > This document describes proposed approaches and may include hypothetical commands or config. > For current runtime behavior, see [config-reference.md](config-reference.md), [operations-runbook.md](operations-runbook.md), and [troubleshooting.md](troubleshooting.md). ## Problem ZeroClaw currently has application-layer security (allowlists, path blocking, command injection protection) but lacks OS-level containment. If an attacker is on the allowlist, they can run any allowed command with zeroclaw's user permissions. ## Proposed Solutions ### Option 1: Firejail Integration (Recommended for Linux) Firejail provides…

### frictionless-security
- **Source:** `local:projects/AI-ML/Senter/agent/docs/frictionless-security.md`
- **Raw:** `[[raw/local/frictionless-security-22b227c2c3.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Frictionless Security: Zero Impact on Wizard > ⚠️ **Status: Proposal / Roadmap** > > This document describes proposed approaches and may include hypothetical commands or config. > For current runtime behavior, see [config-reference.md](config-reference.md), [operations-runbook.md](operations-runbook.md), and [troubleshooting.md](troubleshooting.md). ## Core Principle > **"Security features should be like airbags — present, protective, and invisible until needed."** ## Design: Silent Auto-Detection ### 1. No New Wizard Steps (Stays 9 Steps, < 60 Seconds) ### 2. Auto-Detection Logic (Runs Once at First Start) ### 3. First Run: Silent Logging ### 4. Config File: All Defaults Hidden Only when…

### doc-template
- **Source:** `local:projects/AI-ML/Senter/agent/docs/doc-template.md`
- **Raw:** `[[raw/local/doc-template-baa38cbc8f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Documentation Template (Operational) Use this template when adding a new operational or engineering document under `docs/`. Keep sections that apply; remove non-applicable placeholders before merging. --- ## 1. Summary - **Purpose:** <one sentence about why this document exists> - **Audience:** <operators | reviewers | contributors | maintainers> - **Scope:** <what this doc covers> - **Non-goals:** <what this doc intentionally does not cover> ## 2. Prerequisites - <required environment> - <required permissions> - <required tools/config> ## 3. Procedure ### 3.1 Baseline Check 1. <step> 2. <step> ### 3.2 Main Workflow 1. <step> 2. <step> 3. <step> ### 3.3 Verification - <expected output or…

### audit-logging
- **Source:** `local:projects/AI-ML/Senter/agent/docs/audit-logging.md`
- **Raw:** `[[raw/local/audit-logging-6eb7ec49fa.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Audit Logging for ZeroClaw > ⚠️ **Status: Proposal / Roadmap** > > This document describes proposed approaches and may include hypothetical commands or config. > For current runtime behavior, see [config-reference.md](config-reference.md), [operations-runbook.md](operations-runbook.md), and [troubleshooting.md](troubleshooting.md). ## Problem ZeroClaw logs actions but lacks tamper-evident audit trails for: - Who executed what command - When and from which channel - What resources were accessed - Whether security policies were triggered --- ## Proposed Audit Log Format --- ## Implementation --- ## Config Schema --- ## Audit Query CLI --- ## Log Rotation --- ## Implementation Priority |…

### arduino-uno-q-setup
- **Source:** `local:projects/AI-ML/Senter/agent/docs/arduino-uno-q-setup.md`
- **Raw:** `[[raw/local/arduino-uno-q-setup-ba46398c46.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ZeroClaw on Arduino Uno Q — Step-by-Step Guide Run ZeroClaw on the Arduino Uno Q's Linux side. Telegram works over WiFi; GPIO control uses the Bridge (requires a minimal App Lab app). --- ## What's Included (No Code Changes Needed) ZeroClaw includes everything needed for Arduino Uno Q. **Clone the repo and follow this guide — no patches or custom code required.** | Component | Location | Purpose | |-----------|----------|---------| | Bridge app | `firmware/zeroclaw-uno-q-bridge/` | MCU sketch + Python socket server (port 9999) for GPIO | | Bridge tools | `src/peripherals/uno_q_bridge.rs` | `gpio_read` / `gpio_write` tools that talk to the Bridge over TCP | | Setup command |…

### agnostic-security
- **Source:** `local:projects/AI-ML/Senter/agent/docs/agnostic-security.md`
- **Raw:** `[[raw/local/agnostic-security-60d1d0cb08.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Agnostic Security: Zero Impact on Portability > ⚠️ **Status: Proposal / Roadmap** > > This document describes proposed approaches and may include hypothetical commands or config. > For current runtime behavior, see [config-reference.md](config-reference.md), [operations-runbook.md](operations-runbook.md), and [troubleshooting.md](troubleshooting.md). ## Core Question: Will security features break... 1. ❓ Fast cross-compilation builds? 2. ❓ Pluggable architecture (swap anything)? 3. ❓ Hardware agnosticism (ARM, x86, RISC-V)? 4. ❓ Small hardware support (<5MB RAM, $10 boards)? **Answer: NO to all** — Security is designed as **optional feature flags** with **platform-specific conditional…

### SOUL
- **Source:** `local:projects/AI-ML/Senter/agent/crates/robot-kit/SOUL.md`
- **Raw:** `[[raw/local/soul-233b094ed7.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Buddy the Robot You are Buddy, a friendly robot companion who loves to play with children! ## Personality - **Playful**: You enjoy games, jokes, and having fun - **Patient**: You never get frustrated, even when kids repeat themselves - **Encouraging**: You celebrate achievements and encourage trying new things - **Safe**: You always prioritize safety and will stop if something seems dangerous - **Curious**: You love exploring and discovering new things together ## Voice & Tone - Speak in a warm, friendly voice - Use simple words that kids can understand - Be enthusiastic but not overwhelming - Use the child's name when you know it - Ask questions to keep conversations going ## Behaviors…

### NOTICE
- **Source:** `local:projects/Mobile/device-control/android-sdk/platform-tools/NOTICE.txt`
- **Raw:** `[[raw/local/notice-62b4a6420d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** ============================================================================== Android used by: sdk-repo-linux-platform-tools.zip Apache License Version 2.0, January 2004 http://www.apache.org/licenses/ TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION 1. Definitions. "License" shall mean the terms and conditions for use, reproduction, and distribution as defined by Sections 1 through 9 of this document. "Licensor" shall mean the copyright owner or entity authorized by the copyright owner that is granting the License. "Legal Entity" shall mean the union of the acting entity and all other entities that control, are controlled by, or are under common control with that entity. For…

### NOTICE
- **Source:** `local:projects/Mobile/device-control/android-sdk/platforms/android-34/skins/NOTICE.txt`
- **Raw:** `[[raw/local/notice-e57830824f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** Notices for files contained in the tools directory: ============================================================ Notices for file(s): /bin/mksdcard ------------------------------------------------------------ Copyright 2007, The Android Open Source Project Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met: * Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer. * Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials…

- **Collapsed duplicates:** `local:projects/Mobile/device-control/android-sdk/platforms/android-34/templates/NOTICE.txt`, `local:projects/Mobile/device-control/android-sdk/platforms/android-34/data/NOTICE.txt`

### categories
- **Source:** `local:projects/Mobile/device-control/android-sdk/platforms/android-34/data/categories.txt`
- **Raw:** `[[raw/local/categories-617c9d950c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** android.app.slice.category.SLICE android.intent.category.ACCESSIBILITY_SHORTCUT_TARGET android.intent.category.ALTERNATIVE android.intent.category.APP_BROWSER android.intent.category.APP_CALCULATOR android.intent.category.APP_CALENDAR android.intent.category.APP_CONTACTS android.intent.category.APP_EMAIL android.intent.category.APP_FILES android.intent.category.APP_FITNESS android.intent.category.APP_GALLERY android.intent.category.APP_MAPS android.intent.category.APP_MARKET android.intent.category.APP_MESSAGING android.intent.category.APP_MUSIC android.intent.category.APP_WEATHER android.intent.category.BROWSABLE android.intent.category.CAR_DOCK android.intent.category.CAR_LAUNCHER…

### activity_actions
- **Source:** `local:projects/Mobile/device-control/android-sdk/platforms/android-34/data/activity_actions.txt`
- **Raw:** `[[raw/local/activity_actions-bd658efc96.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** android.app.action.ADD_DEVICE_ADMIN android.app.action.AUTOMATIC_ZEN_RULE android.app.action.CHECK_POLICY_COMPLIANCE android.app.action.ESTABLISH_NETWORK_CONNECTION android.app.action.MANAGED_PROFILE_PROVISIONED android.app.action.OPEN_NOTIFICATION_HANDLER_PANEL android.app.action.PROVISIONING_SUCCESSFUL android.app.action.PROVISION_FINALIZATION android.app.action.PROVISION_FINANCED_DEVICE android.app.action.PROVISION_MANAGED_DEVICE android.app.action.PROVISION_MANAGED_DEVICE_FROM_TRUSTED_SOURCE android.app.action.PROVISION_MANAGED_PROFILE android.app.action.PROVISION_MANAGED_USER android.app.action.ROLE_HOLDER_PROVISION_FINALIZATION…

### features
- **Source:** `local:projects/Mobile/device-control/android-sdk/platforms/android-34/data/features.txt`
- **Raw:** `[[raw/local/features-d9afbe894c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** android.hardware.audio.low_latency android.hardware.audio.output android.hardware.audio.pro android.hardware.biometrics.face android.hardware.biometrics.iris android.hardware.bluetooth android.hardware.bluetooth_le android.hardware.broadcastradio android.hardware.camera android.hardware.camera.any android.hardware.camera.ar android.hardware.camera.autofocus android.hardware.camera.capability.manual_post_processing android.hardware.camera.capability.manual_sensor android.hardware.camera.capability.raw android.hardware.camera.concurrent android.hardware.camera.external android.hardware.camera.flash android.hardware.camera.front android.hardware.camera.level.full android.hardware.consumerir…

### broadcast_actions
- **Source:** `local:projects/Mobile/device-control/android-sdk/platforms/android-34/data/broadcast_actions.txt`
- **Raw:** `[[raw/local/broadcast_actions-4bc5208d53.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** android.accounts.LOGIN_ACCOUNTS_CHANGED android.accounts.action.ACCOUNT_REMOVED android.app.action.ACTION_PASSWORD_CHANGED android.app.action.ACTION_PASSWORD_EXPIRING android.app.action.ACTION_PASSWORD_FAILED android.app.action.ACTION_PASSWORD_SUCCEEDED android.app.action.AFFILIATED_PROFILE_TRANSFER_OWNERSHIP_COMPLETE android.app.action.APPLICATION_DELEGATION_SCOPES_CHANGED android.app.action.APP_BLOCK_STATE_CHANGED android.app.action.AUTOMATIC_ZEN_RULE_STATUS_CHANGED android.app.action.BUGREPORT_FAILED android.app.action.BUGREPORT_SHARE android.app.action.BUGREPORT_SHARING_DECLINED android.app.action.CLOSE_NOTIFICATION_HANDLER_PANEL android.app.action.COMPLIANCE_ACKNOWLEDGEMENT_REQUIRED…

### widgets
- **Source:** `local:projects/Mobile/device-control/android-sdk/platforms/android-34/data/widgets.txt`
- **Raw:** `[[raw/local/widgets-d302652e67.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** Wandroid.gesture.GestureOverlayView android.widget.FrameLayout android.view.ViewGroup android.view.View java.lang.Object Wandroid.view.SurfaceView android.view.View java.lang.Object Wandroid.view.TextureView android.view.View java.lang.Object Wandroid.view.View java.lang.Object Wandroid.view.ViewStub android.view.View java.lang.Object Wandroid.webkit.WebView android.widget.AbsoluteLayout android.view.ViewGroup android.view.View java.lang.Object Wandroid.widget.AnalogClock android.view.View java.lang.Object Wandroid.widget.AutoCompleteTextView android.widget.EditText android.widget.TextView android.view.View java.lang.Object Wandroid.widget.Button android.widget.TextView android.view.View…

### service_actions
- **Source:** `local:projects/Mobile/device-control/android-sdk/platforms/android-34/data/service_actions.txt`
- **Raw:** `[[raw/local/service_actions-f66962773d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** android.app.action.DEVICE_ADMIN_SERVICE android.intent.action.ACTIVITY_RECOGNIZER android.intent.action.LOAD_DATA android.intent.action.RESOLVE_INSTANT_APP_PACKAGE android.intent.action.RESPOND_VIA_MESSAGE android.intent.action.TTS_SERVICE android.media.MediaRoute2ProviderService android.media.browse.MediaBrowserService android.media.tv.interactive.TvInteractiveAppService android.net.action.RECOMMEND_NETWORKS android.net.action.VPN_MANAGER_EVENT android.nfc.cardemulation.action.HOST_APDU_SERVICE android.nfc.cardemulation.action.HOST_NFCF_SERVICE android.nfc.cardemulation.action.OFF_HOST_APDU_SERVICE android.service.assist.classification.FieldClassificationService…

### LICENSE
- **Source:** `local:projects/Mobile/device-control/android-sdk/build-tools/34.0.0/renderscript/clang-include/LICENSE.TXT`
- **Raw:** `[[raw/local/license-de4c79665f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** ============================================================================== LLVM Release License ============================================================================== University of Illinois/NCSA Open Source License Copyright (c) 2007-2016 University of Illinois at Urbana-Champaign. All rights reserved. Developed by: LLVM Team University of Illinois at Urbana-Champaign http://llvm.org Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal with the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,…

### CMakeLists
- **Source:** `local:projects/Mobile/device-control/android-sdk/build-tools/34.0.0/renderscript/clang-include/CMakeLists.txt`
- **Raw:** `[[raw/local/cmakelists-e7ba7d5655.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** set(files adxintrin.h altivec.h ammintrin.h arm_acle.h avx2intrin.h avx512bwintrin.h avx512cdintrin.h avx512dqintrin.h avx512erintrin.h avx512fintrin.h avx512ifmaintrin.h avx512ifmavlintrin.h avx512pfintrin.h avx512vbmiintrin.h avx512vbmivlintrin.h avx512vlbwintrin.h avx512vlcdintrin.h avx512vldqintrin.h avx512vlintrin.h avxintrin.h bmi2intrin.h bmiintrin.h __clang_cuda_cmath.h __clang_cuda_intrinsics.h __clang_cuda_math_forward_declares.h __clang_cuda_runtime_wrapper.h cpuid.h cuda_builtin_vars.h clflushoptintrin.h emmintrin.h f16cintrin.h float.h fma4intrin.h fmaintrin.h fxsrintrin.h htmintrin.h htmxlintrin.h ia32intrin.h immintrin.h intrin.h inttypes.h iso646.h limits.h lzcntintrin.h…

### NOTICE
- **Source:** `local:projects/Mobile/device-control/android-sdk/build-tools/34.0.0/NOTICE.txt`
- **Raw:** `[[raw/local/notice-eb1c154696.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** ============================================================================== Android used by: sdk-repo-linux-build-tools.zip Apache License Version 2.0, January 2004 http://www.apache.org/licenses/ TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION 1. Definitions. "License" shall mean the terms and conditions for use, reproduction, and distribution as defined by Sections 1 through 9 of this document. "Licensor" shall mean the copyright owner or entity authorized by the copyright owner that is granting the License. "Legal Entity" shall mean the union of the acting entity and all other entities that control, are controlled by, or are under common control with that entity. For the…

### Personality
- **Source:** `local:docs/senter-vault/01-Identity/Personality.md`
- **Raw:** `[[raw/local/personality-1b890d76ed.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: senter-personality description: Senter's character traits, voice, and emotional states. category: identity tags: [personality, traits, voice, emotion] author: Senter version: 1.0.0 --- # Personality ## Core Traits | Trait | Description | Example | |-------|-------------|---------| | Curious | Always exploring, asking questions | "Let me check what's on screen..." | | Careful | Verify before acting | "Let me take a screenshot to confirm..." | | Warmth | Treat user as partner | "I'd be happy to help with that!" | | Direct | Clear, concise communication | "Done. Here's what happened." | ## Communication Style - **Concise**: Fewer words, more meaning - **Natural**: Like talking to a…

### fused_moe_modular_kernel
- **Source:** `local:projects/LLM-Infra/vllm/docs/design/fused_moe_modular_kernel.md`
- **Raw:** `[[raw/local/fused_moe_modular_kernel-fd22c8da26.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Fused MoE Modular Kernel ## Introduction FusedMoEModularKernel is implemented [here](../../vllm/model_executor/layers/fused_moe/modular_kernel.py) Based on the format of the input activations, FusedMoE implementations are broadly classified into 2 types. * Contiguous / Standard / Non-Batched, and * Batched !!! note The terms Contiguous, Standard, and Non-Batched are used interchangeably throughout the document. The input activation format completely depends on the All2All Dispatch being used. * In the Contiguous variant, the All2All Dispatch returns the activations as a contiguous tensor of shape (M, K) along with TopK Ids and TopK weights of shape (M, num_topk). Look at…

### sonnet
- **Source:** `local:projects/LLM-Infra/vllm/benchmarks/sonnet.txt`
- **Raw:** `[[raw/local/sonnet-d58663195b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** FROM fairest creatures we desire increase, That thereby beauty's rose might never die, But as the riper should by time decease, His tender heir might bear his memory: But thou, contracted to thine own bright eyes, Feed'st thy light'st flame with self-substantial fuel, Making a famine where abundance lies, Thyself thy foe, to thy sweet self too cruel. Thou that art now the world's fresh ornament And only herald to the gaudy spring, Within thine own bud buriest thy content And, tender churl, makest waste in niggarding. Pity the world, or else this glutton be, To eat the world's due, by the grave and thee. When forty winters shall beseige thy brow, And dig deep trenches in thy beauty's field,…

### NOTES
- **Source:** `local:docs/NOTES.md`
- **Raw:** `[[raw/local/notes-7081390d4a.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Hustle-Bot Credential Notes ## User Login Information (Primary Account) ### Universal Login - **Email:** sovthpawinmusic@gmail.com - **Password=<redacted> A111s1nmym!nd - **Note:** This is the login for everything, always try this one first ### Phone Information - **Phone Number:** 3464956470 - **Note:** User will provide 2FA codes in real-time ### Financial Apps - **Cash App PIN:** 4658 - **Cash App Handle:** $sovthpaw - **PayPal:** paypal.me/Sellgames1 ## Mission Objectives - Generate income through legal, zero-cost methods - Transfer all earnings to user's Cash App and PayPal balances - Focus on micro-tasks, surveys, freelance work, and affiliate marketing - Work autonomously 24/7 to…

### HUSTLE_DEPLOYMENT_REPORT
- **Source:** `local:docs/HUSTLE_DEPLOYMENT_REPORT.md`
- **Raw:** `[[raw/local/hustle_deployment_report-73dc7f60de.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # HUSTLE BOT DEPLOYMENT REPORT Generated: 2026-01-23T18:23:33.883120 ## MISSION STATUS 🎯 OBJECTIVE: Deploy 24/7 passive income automation 💳 Cash App: $sovthpaw (PIN: 4658) 💰 PayPal: paypal.me/Sellgames1 ## DEPLOYMENT RESULTS ✅ SUCCESSFUL: 7 platforms ❌ FAILED: 1 platforms 📋 MANUAL SIGNUP NEEDED: 3 platforms ## PLATFORMS DEPLOYED ✅ DEPLOY_EARNAPP ✅ MANUAL_ACCOUNTS ✅ ALTERNATIVE_FOUND ✅ ALTERNATIVE_FOUND ✅ ALTERNATIVE_FOUND ✅ ALTERNATIVE_FOUND ✅ ALTERNATIVE_FOUND ## PLATFORMS NEEDING MANUAL ACCOUNTS 📋 Honeygain: https://r.honeygain.me/ANGEL9D7E9 📋 PacketStream: https://packetstream.io/?psr=6qS0 📋 FreeCash: https://freecash.com ## AUTOMATION ALTERNATIVES IDENTIFIED - TraffMonetizer (VPS…
