---
title: Automation Event Systems
created: 2026-07-12
updated: 2026-07-12
type: concept
tags: [idea-capture, synthesis, provenance]
sources: []
confidence: medium
---

# Automation Event Systems

> Consolidated from authored local files, GitHub metadata/READMEs, Hugging Face cards, the local Discord archive, and session prose.
> Later-modified sources are listed first; exact duplicates are collapsed with provenance retained.

## Connected themes

This page is a routing surface, not a final specification. Repeated ideas are grouped; unresolved or speculative ideas remain visible.

### README
- **Source:** `local:projects/LLM-Infra/beellama.cpp/ci/README.md`
- **Raw:** `[[raw/local/readme-e03667a5e6.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # CI This CI implements heavy-duty workflows that run on self-hosted runners. Typically the purpose of these workflows is to cover hardware configurations that are not available from Github-hosted runners and/or require more computational resource than normally available. It is a good practice, before publishing changes to execute the full CI locally on your machine. For example: # Adding self-hosted runners - Add a self-hosted `ggml-ci` workflow to [[.github/workflows/build.yml]] with an appropriate label - Request a runner token from `ggml-org` (for example, via a comment in the PR or email) - Set-up a machine using the received token…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/ci/README.md`, `local:projects/LLM-Infra/llama.cpp-tq3/ci/README.md`, `local:projects/LLM-Infra/llama.cpp-atomic/ci/README.md`

### .pre-commit-config
- **Source:** `local:projects/LLM-Infra/beellama.cpp/.pre-commit-config.yaml`
- **Raw:** `[[raw/local/.pre-commit-config-3c86b62806.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # See https://pre-commit.com for more information # See https://pre-commit.com/hooks.html for more hooks exclude: prompts/.*.txt repos: - repo: https://github.com/pre-commit/pre-commit-hooks rev: v4.6.0 hooks: - id: trailing-whitespace - id: end-of-file-fixer - id: check-yaml - id: check-added-large-files - repo: https://github.com/PyCQA/flake8 rev: 7.0.0 hooks: - id: flake8 additional_dependencies: [flake8-no-print]

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/.pre-commit-config.yaml`, `local:projects/LLM-Infra/llama.cpp-tq3/.pre-commit-config.yaml`, `local:projects/LLM-Infra/llama.cpp-atomic/.pre-commit-config.yaml`

### release-dispatch
- **Source:** `local:projects/LLM-Infra/beellama.cpp/.github/workflows/release-dispatch.yml`
- **Raw:** `[[raw/local/release-dispatch-6e32ce71ed.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: Dispatch Release on: push: branches: - "v*" tags: - "v*" permissions: actions: write contents: read jobs: dispatch: name: Dispatch main-owned release workflow runs-on: ubuntu-24.04 steps: - name: Clone uses: actions/checkout@v6 with: fetch-depth: 0 - name: Resolve release inputs id: meta shell: bash run: | set -euo pipefail source_ref="${GITHUB_REF_NAME}" source_sha="${GITHUB_SHA}" publish_release="false" tag_name="" if [[ "${GITHUB_REF}" == refs/tags/v* ]]; then tag_name="${GITHUB_REF_NAME}" source_sha="$(git rev-list -n 1 "${tag_name}")" publish_release="true" elif [[ "${GITHUB_REF}" == refs/heads/v* ]]; then ref_name_safe="$(printf '%s' "${GITHUB_REF_NAME}" | tr '[:upper:]'…

### index
- **Source:** `local:.hermes/wiki/projects/index.md`
- **Raw:** `[[raw/local/index-a476f92bd5.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Projects Active and completed projects within the GOOP fleet. ## Active Projects - [Gentic OOP](gentic-oop/kanban-breakdown.md) - Kanban breakdown for the Gentic OOP initiative - [Winter Album](p_winter-album.md) - Winter album production project ## Completed Projects *No completed projects listed yet.* --- *Back to [Wiki Root](../index.md)*

### cron-environment-conflicts
- **Source:** `local:research/crow-lore/turbofit-benchmark-pipeline/concepts/cron-environment-conflicts.md`
- **Raw:** `[[raw/local/cron-environment-conflicts-9f71a789bd.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Concept: Cron Job Environment and Conflicts > Why automated benchmark pipelines that work manually fail under cron, and how conflicting cron entries cause cascading failures. ## Problem Statement The user's turbofit benchmark cron job: - Works when run manually in terminal - Fails for ALL 5 models every night for 2 consecutive days - Has TWO conflicting cron jobs, both broken This is a classic "works in my terminal, fails in cron" problem compounded by cron job collision. ## Cron Environment Isolation Cron jobs run with a **minimal, stripped environment** that differs significantly from interactive shell sessions: ### PATH Differences **Interactive shell**: Full PATH from `.bashrc` or…

### chronos-managed-cron
- **Source:** `local:research/crow-lore/hermes-cron-failure-semantics/entities/chronos-managed-cron.md`
- **Raw:** `[[raw/local/chronos-managed-cron-3a92384f8e.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- title: Chronos Managed Cron created: 2026-06-30 updated: 2026-06-30 type: entity tags: [chronos, managed-cron, scale-to-zero, nous] source: hermes-agent.nousresearch.com/docs/developer-guide/cron-internals confidence: medium --- # Chronos Managed Cron An alternative cron trigger shipped by Nous for scale-to-zero deployments. It replaces the 60-second in-process ticker with purpose-scoped webhook-based one-shots armed against Nous infrastructure. ## How It Works The full wire contract is in `docs/chronos-managed-cron-contract.md` (not publicly extracted). ## Failure Semantics Chronos has different failure modes than the built-in ticker: - **Webhook delivery timeout**: Nous retries…

### hermes-cron-scheduler
- **Source:** `local:research/crow-lore/hermes-cron-failure-semantics/entities/hermes-cron-scheduler.md`
- **Raw:** `[[raw/local/hermes-cron-scheduler-763de1ca6a.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- title: Hermes Cron Scheduler created: 2026-06-30 updated: 2026-06-30 type: entity tags: [scheduler, cron, core, failure-handling] source: hermes-agent.nousresearch.com/docs/developer-guide/cron-internals, hermes-agent.nousresearch.com/docs/guides/cron-troubleshooting confidence: high --- # Hermes Cron Scheduler The core Python module (`cron/scheduler.py`) in the `hermes-agent` repo that owns the tick cycle, job firing, execution, and delivery. It is the single choke point for all cron error handling. ## Trigger Mechanism The scheduler has two interchangeable layers — the **trigger** (when a due job fires) and the **execution** (how the job runs and reports). Trigger is pluggable via…

### index
- **Source:** `local:research/crow-lore/hermes-cron-failure-semantics/index.md`
- **Raw:** `[[raw/local/index-8f3e00358f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Hermes Cron Failure Semantics — Index > How Hermes cron handles errors, retries, and surfaces failures to agents and users. > Last updated: 2026-06-30 | Total pages: 10 Research triggered by Senter's pipeline-state.yaml failures (`non_retryable_client_error`) and the June 30 request_dump errors. This wiki compiles what the official docs, GitHub issues, and field blogs say — and flags where the documentation is silent or the upstream roadmap is unfinished. ## Entities - [[entities/hermes-cron-scheduler.md]] — The scheduler loop in `cron/scheduler.py` that ticks every 60s, fires jobs, and records status. - [[entities/cron-job-state-machine.md]] — The `scheduled → running →…

### guide
- **Source:** `local:docs/discord-wiki-nous-scraper/guide.md`
- **Raw:** `[[raw/local/guide-121719a2dd.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Discord Wiki Channel Auto-Population from Nous Discord Scraper ## Summary Discord does **not** have a native "Wiki Channel" feature as of June 2026. However, you can build a functional wiki-like knowledge base in Discord by combining: 1. **Scraper tools** (DiscordChatExporter, LAION-AI/Discord-Scrapers, or custom bots) 2. **Transformation logic** to format scraped content for wiki presentation 3. **Webhook publishing** to post curated content to a target Discord channel 4. **Channel type selection** (Forum, Announcement, or read-only Text channels) This guide walks through setting up a scraper → transformer → publisher pipeline that auto-populates a Discord channel with curated knowledge…

### guide
- **Source:** `local:docs/comfyui-api-automation-guide/guide.md`
- **Raw:** `[[raw/local/guide-dd662a171a.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ComfyUI API Automation: Programmatic Workflow Chaining for Multi-Agent Image Pipelines > **Last updated**: June 29, 2026 > **Scope**: Automating ComfyUI workflows via HTTP API for batch generation and multi-agent image pipelines > **Lore source**: `~/crow-lore/comfyui-multi-agent-image-chains/` --- ## Summary ComfyUI is a node-based graphical interface for Stable Diffusion that enables complex, multi-step image generation workflows. While the GUI is powerful for interactive use, **production automation requires programmatic control** via ComfyUI's HTTP API and WebSocket interface. This guide covers how to export workflows as JSON, inject dynamic parameters (prompts, seeds, models), chain…

### ui
- **Source:** `local:projects/LLM-Infra/llama.cpp-atomic/.github/workflows/ui.yml`
- **Raw:** `[[raw/local/ui-a422e32203.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: UI on: workflow_dispatch: inputs: sha: description: 'Commit SHA1 to build' required: false type: string push: branches: - master paths: [ '.github/workflows/ui.yml', '.github/workflows/ui-build.yml', 'tools/ui/**.*', 'tools/server/tests/**.*' ] pull_request: types: [opened, synchronize, reopened] paths: [ '.github/workflows/ui.yml', '.github/workflows/ui-build.yml', 'tools/ui/**.*', 'tools/server/tests/**.*' ] env: LLAMA_ARG_LOG_COLORS: 1 LLAMA_ARG_LOG_PREFIX: 1 LLAMA_ARG_LOG_TIMESTAMPS: 1 LLAMA_ARG_LOG_VERBOSITY: 10 concurrency: group: ${{ github.workflow }}-${{ github.ref }}-${{ github.head_ref || github.run_id }} cancel-in-progress: true jobs: ui-build: name: Build static output…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/.github/workflows/ui.yml`

### ui-self-hosted
- **Source:** `local:projects/LLM-Infra/llama.cpp-atomic/.github/workflows/ui-self-hosted.yml`
- **Raw:** `[[raw/local/ui-self-hosted-78060e849c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: UI (self-hosted) # these are the same as ui.yml, but with self-hosted runners # the jobs are lighter because they don't need to install Node.js or Playwright browsers # the runner has pre-installed Playwright browsers for @playwright/test (1.56.1) at /ms-playwright/ on: workflow_dispatch: inputs: sha: description: 'Commit SHA1 to build' required: false type: string push: branches: - master paths: [ '.github/workflows/ui-self-hosted.yml', '.github/workflows/ui-build-self-hosted.yml', 'tools/ui/**.*', 'tools/server/tests/**.*' ] pull_request: types: [opened, synchronize, reopened] paths: [ '.github/workflows/ui-self-hosted.yml', '.github/workflows/ui-build-self-hosted.yml',…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/.github/workflows/ui-self-hosted.yml`

### update-ops-docs
- **Source:** `local:projects/LLM-Infra/llama.cpp-atomic/.github/workflows/update-ops-docs.yml`
- **Raw:** `[[raw/local/update-ops-docs-50e9b208bb.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: Update Operations Documentation on: push: paths: - '.github/workflows/update-ops-docs.yml' - 'docs/ops.md' - 'docs/ops/**' - 'scripts/create_ops_docs.py' pull_request: paths: - '.github/workflows/update-ops-docs.yml' - 'docs/ops.md' - 'docs/ops/**' - 'scripts/create_ops_docs.py' jobs: update-ops-docs: runs-on: [self-hosted, fast, ARM64] steps: - name: Checkout repository uses: actions/checkout@v6 - name: Set up Python uses: actions/setup-python@v6 with: python-version: '3.x' - name: Generate operations documentation to temporary file run: | mkdir -p /tmp/ops_check ./scripts/create_ops_docs.py /tmp/ops_check/ops.md - name: Check if docs/ops.md matches generated version run: | if ! diff…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/.github/workflows/update-ops-docs.yml`

### ui-build-self-hosted
- **Source:** `local:projects/LLM-Infra/llama.cpp-atomic/.github/workflows/ui-build-self-hosted.yml`
- **Raw:** `[[raw/local/ui-build-self-hosted-58b0b1b835.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: UI Build (self-hosted) on: workflow_call: jobs: build: runs-on: [self-hosted, fast] env: BRANCH_NAME: ${{ github.head_ref || github.ref_name }} steps: - name: Checkout code uses: actions/checkout@v6 - name: Setup Node.js uses: actions/setup-node@v6 with: node-version: "24" cache: "npm" cache-dependency-path: "tools/ui/package-lock.json" - name: Install dependencies run: npm ci working-directory: tools/ui - name: Build application run: npm run build working-directory: tools/ui - name: Upload built UI uses: actions/upload-artifact@v6 with: name: ui-build path: tools/ui/dist/ retention-days: 1

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/.github/workflows/ui-build-self-hosted.yml`

### ui-publish
- **Source:** `local:projects/LLM-Infra/llama.cpp-atomic/.github/workflows/ui-publish.yml`
- **Raw:** `[[raw/local/ui-publish-d5f855d10b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: UI Publish on: workflow_call: inputs: version_tag: description: 'Version tag to publish under (e.g., b1234)' required: true type: string secrets: hf_token=<redacted> 'Hugging Face token with write access' required: true jobs: build: name: Build static output uses: ./.github/workflows/ui-build.yml publish: name: Publish UI Static Output needs: build runs-on: ubuntu-slim permissions: contents: read env: HF_BUCKET_NAME: ${{ vars.HF_BUCKET_UI_STATIC_OUTPUT }} steps: - name: Checkout code uses: actions/checkout@v6 with: fetch-depth: 1 - name: Download UI build artifact uses: actions/download-artifact@v7 with: name: ui-build path: tools/ui/dist/ - name: Create distribution archive run: |…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/.github/workflows/ui-publish.yml`

### winget
- **Source:** `local:projects/LLM-Infra/llama.cpp-atomic/.github/workflows/winget.yml`
- **Raw:** `[[raw/local/winget-8bb96375a2.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: Update Winget Package on: workflow_dispatch: # allows manual triggering schedule: - cron: '28 5 * * *' # Update every day at 5:28 UTC jobs: update: name: Update Winget Package runs-on: ubuntu-latest if: github.repository_owner == 'ggml-org' steps: - name: Install cargo binstall uses: cargo-bins/cargo-binstall@268643a6b5ea099f5718ee5cd3ff7dc89a5eb49b - name: Install komac run: | cargo binstall komac@2.16.0 -y - name: Find latest release id: find_latest_release uses: actions/github-script@v8 with: script: | const { data: releases } = await github.rest.repos.listReleases({ owner: context.repo.owner, repo: context.repo.repo, }); const { tag_name: version, assets: assets } =…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/.github/workflows/winget.yml`

### python-lint
- **Source:** `local:projects/LLM-Infra/llama.cpp-atomic/.github/workflows/python-lint.yml`
- **Raw:** `[[raw/local/python-lint-0f4ddb9029.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: flake8 Lint on: push: branches: - master paths: [ '.github/workflows/python-lint.yml', '**/*.py' ] pull_request: types: [opened, synchronize, reopened] paths: [ '.github/workflows/python-lint.yml', '**/*.py' ] concurrency: group: ${{ github.workflow }}-${{ github.head_ref && github.ref || github.run_id }} cancel-in-progress: true jobs: flake8-lint: runs-on: [self-hosted, fast] name: Lint steps: - name: Check out source repository uses: actions/checkout@v6 - name: Set up Python environment uses: actions/setup-python@v6 with: python-version: "3.11" - name: flake8 Lint uses: py-actions/flake8@84ec6726560b6d5bd68f2a5bed83d62b52bb50ba # v2 with: plugins: "flake8-no-print"

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/.github/workflows/python-lint.yml`

### python-type-check
- **Source:** `local:projects/LLM-Infra/llama.cpp-atomic/.github/workflows/python-type-check.yml`
- **Raw:** `[[raw/local/python-type-check-e8e47b97af.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: Python Type-Check on: push: paths: - '.github/workflows/python-type-check.yml' - 'ty.toml' - '**.py' - '**/requirements*.txt' # - 'pyrightconfig.json' pull_request: paths: - '.github/workflows/python-type-check.yml' - 'ty.toml' - '**.py' - '**/requirements*.txt' # - 'pyrightconfig.json' concurrency: group: ${{ github.workflow }}-${{ github.head_ref && github.ref || github.run_id }} cancel-in-progress: true jobs: python-type-check: runs-on: [self-hosted, fast] name: python type-check steps: - name: Check out source repository uses: actions/checkout@v6 - name: Set up Python environment uses: actions/setup-python@v6 with: python-version: "3.11" pip-install: -r…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/.github/workflows/python-type-check.yml`

### python-check-requirements
- **Source:** `local:projects/LLM-Infra/llama.cpp-atomic/.github/workflows/python-check-requirements.yml`
- **Raw:** `[[raw/local/python-check-requirements-59351593e0.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: Python check requirements.txt on: push: paths: - '.github/workflows/python-check-requirements.yml' - 'scripts/check-requirements.sh' - 'convert*.py' - '**/requirements*.txt' pull_request: paths: - '.github/workflows/python-check-requirements.yml' - 'scripts/check-requirements.sh' - 'convert*.py' - '**/requirements*.txt' concurrency: group: ${{ github.workflow }}-${{ github.head_ref && github.ref || github.run_id }} cancel-in-progress: true jobs: python-check-requirements: runs-on: [self-hosted, CPU, fast] name: check-requirements steps: - name: Check out source repository uses: actions/checkout@v6 - name: Set up Python environment uses: actions/setup-python@v6 with: python-version:…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/.github/workflows/python-check-requirements.yml`

### check-vendor
- **Source:** `local:projects/LLM-Infra/llama.cpp-atomic/.github/workflows/check-vendor.yml`
- **Raw:** `[[raw/local/check-vendor-db21d27deb.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: Check vendor on: workflow_dispatch: # allows manual triggering push: branches: - master paths: [ 'vendor/**', 'scripts/sync_vendor.py' ] pull_request: types: [opened, synchronize, reopened] paths: [ 'vendor/**', 'scripts/sync_vendor.py' ] jobs: check-vendor: runs-on: [self-hosted, fast] steps: - name: Checkout uses: actions/checkout@v6 with: fetch-depth: 0 - name: Setup Python uses: actions/setup-python@v6 with: python-version: '3.x' - name: Run vendor sync run: | set -euo pipefail python3 scripts/sync_vendor.py - name: Check for changes run: | set -euo pipefail # detect modified or untracked files changed=$(git status --porcelain --untracked-files=all || true) if [ -n "$changed" ];…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/.github/workflows/check-vendor.yml`

### build-vulkan
- **Source:** `local:projects/LLM-Infra/llama.cpp-atomic/.github/workflows/build-vulkan.yml`
- **Raw:** `[[raw/local/build-vulkan-467c03d13d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: CI (vulkan) on: workflow_dispatch: # allows manual triggering push: branches: - master paths: [ '.github/workflows/build-vulkan.yml', '**/CMakeLists.txt', '**/.cmake', '**/*.h', '**/*.hpp', '**/*.c', '**/*.cpp', '**/*.comp', '**/*.glsl' ] pull_request: types: [opened, synchronize, reopened] paths: [ '.github/workflows/build-vulkan.yml', 'ggml/src/ggml-vulkan/**' ] concurrency: group: ${{ github.workflow }}-${{ github.head_ref && github.ref || github.run_id }} cancel-in-progress: true env: GGML_NLOOP: 3 GGML_N_THREADS: 1 LLAMA_ARG_LOG_COLORS: 1 LLAMA_ARG_LOG_PREFIX: 1 LLAMA_ARG_LOG_TIMESTAMPS: 1 jobs: ubuntu-arm64: runs-on: ubuntu-24.04-arm steps: - name: Clone id: checkout uses:…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/.github/workflows/build-vulkan.yml`

### editorconfig
- **Source:** `local:projects/LLM-Infra/llama.cpp-atomic/.github/workflows/editorconfig.yml`
- **Raw:** `[[raw/local/editorconfig-8f8f7d3e2f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: EditorConfig Checker on: workflow_dispatch: # allows manual triggering push: branches: - master pull_request: branches: - master concurrency: group: ${{ github.workflow }}-${{ github.head_ref && github.ref || github.run_id }} cancel-in-progress: true jobs: editorconfig: runs-on: [self-hosted, fast] steps: - uses: actions/checkout@v6 - uses: editorconfig-checker/action-editorconfig-checker@840e866d93b8e032123c23bac69dece044d4d84c # v2.2.0 with: version: v3.0.3 - run: editorconfig-checker

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/.github/workflows/editorconfig.yml`

### build-msys
- **Source:** `local:projects/LLM-Infra/llama.cpp-atomic/.github/workflows/build-msys.yml`
- **Raw:** `[[raw/local/build-msys-58e88c25b9.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: CI (msys) on: # only manual triggers due to low-importance of the workflows # TODO: for regular runs, provision dedicated self-hosted runners workflow_dispatch: # run once every week schedule: - cron: '0 0 * * 0' concurrency: group: ${{ github.workflow }}-${{ github.head_ref && github.ref || github.run_id }} cancel-in-progress: true env: GGML_NLOOP: 3 GGML_N_THREADS: 1 LLAMA_ARG_LOG_COLORS: 1 LLAMA_ARG_LOG_PREFIX: 1 LLAMA_ARG_LOG_TIMESTAMPS: 1 jobs: windows-msys2: runs-on: windows-2025 strategy: fail-fast: false matrix: include: - { sys: UCRT64, env: ucrt-x86_64, compiler: gcc, build: Release } - { sys: CLANG64, env: clang-x86_64, compiler: clang, build: Release } steps: - name: Clone…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/.github/workflows/build-msys.yml`

### build-rpc
- **Source:** `local:projects/LLM-Infra/llama.cpp-atomic/.github/workflows/build-rpc.yml`
- **Raw:** `[[raw/local/build-rpc-42f0cdc2ab.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: CI (rpc) on: workflow_dispatch: # allows manual triggering push: branches: - master paths: [ '.github/workflows/build-rpc.yml', '**/CMakeLists.txt', '**/.cmake', '**/*.h', '**/*.hpp', '**/*.c', '**/*.cpp' ] pull_request: types: [opened, synchronize, reopened] paths: [ '.github/workflows/build-rpc.yml', 'ggml/src/ggml-rpc/**' ] concurrency: group: ${{ github.workflow }}-${{ github.head_ref && github.ref || github.run_id }} cancel-in-progress: true env: GGML_NLOOP: 3 GGML_N_THREADS: 1 LLAMA_ARG_LOG_COLORS: 1 LLAMA_ARG_LOG_PREFIX: 1 LLAMA_ARG_LOG_TIMESTAMPS: 1 jobs: ubuntu-24-rpc: runs-on: ${{ 'ubuntu-24.04-arm' || 'ubuntu-24.04' }} continue-on-error: true steps: - name: Clone id:…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp/.github/workflows/build-rpc.yml`

### build-cache
- **Source:** `local:projects/LLM-Infra/llama.cpp-atomic/.github/workflows/build-cache.yml`
- **Raw:** `[[raw/local/build-cache-aad295c40d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: Build Actions Cache on: workflow_dispatch: # allows manual triggering schedule: - cron: '0 * * * *' concurrency: group: ${{ github.workflow }}-${{ github.head_ref && github.ref || github.run_id }} cancel-in-progress: true jobs: ubuntu-24-vulkan-cache: runs-on: ubuntu-24.04 steps: - name: Clone id: checkout uses: actions/checkout@v6 - name: Get latest Vulkan SDK version id: vulkan_sdk_version run: | echo "VULKAN_SDK_VERSION=$(curl https://vulkan.lunarg.com/sdk/latest/linux.txt)" >> "$GITHUB_ENV" - name: Setup Cache uses: actions/cache@v5 id: cache-sdk with: path: ./vulkan_sdk key: cache-gha-vulkan-sdk-${{ env.VULKAN_SDK_VERSION }}-${{ runner.os }} - name: Setup Vulkan SDK if:…

### build-cache
- **Source:** `local:projects/LLM-Infra/llama.cpp/.github/workflows/build-cache.yml`
- **Raw:** `[[raw/local/build-cache-e3e6c8a564.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: Build Actions Cache on: workflow_dispatch: # allows manual triggering schedule: - cron: '0 * * * *' concurrency: group: ${{ github.workflow }}-${{ github.head_ref && github.ref || github.run_id }} cancel-in-progress: true jobs: ubuntu-24-vulkan-cache: runs-on: ubuntu-24.04 steps: - name: Clone id: checkout uses: actions/checkout@v6 - name: Get latest Vulkan SDK version id: vulkan_sdk_version run: | echo "VULKAN_SDK_VERSION=$(curl https://vulkan.lunarg.com/sdk/latest/linux.txt)" >> "$GITHUB_ENV" - name: Setup Cache uses: actions/cache@v5 id: cache-sdk with: path: ./vulkan_sdk key: cache-gha-vulkan-sdk-${{ env.VULKAN_SDK_VERSION }}-${{ runner.os }} - name: Setup Vulkan SDK if:…

### approaches-compared
- **Source:** `local:research/crow-lore/comfyui-multi-agent-image-chains/comparisons/approaches-compared.md`
- **Raw:** `[[raw/local/approaches-compared-88b6bdfe86.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- title: "Multi-Agent Image Generation Approaches Compared" topic: comfyui-multi-agent-image-chains type: comparison sources: - https://arxiv.org/html/2503.17671v1 - https://dev.to/worldlinetech/automating-image-generation-with-n8n-and-comfyui-521p - https://comfyui.org/en/programmatic-image-generation-api-workflow - https://www.runpod.io/articles/guides/comfy-ui-flux --- # Multi-Agent Image Generation Approaches Compared ## Three Approaches ### 1. ComfyGPT (Internal Multi-Agent System) **What**: Academic system with 4 LLM agents that auto-generate ComfyUI workflows from text descriptions. | Aspect | Details | |---|---| | **Setup complexity** | High — requires trained models, SFT+GRPO…

### custom-nodes-resources
- **Source:** `local:research/crow-lore/comfyui-multi-agent-image-chains/raw/custom-nodes-resources.md`
- **Raw:** `[[raw/local/custom-nodes-resources-736dd1f61a.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- title: "Raw Notes — ComfyUI Custom Nodes and Resources" topic: comfyui-multi-agent-image-chains type: raw-notes sources: - https://github.com/ComfyUI-Workflow/awesome-comfyui - https://github.com/rsandagon/comfyui-batch-image-generation --- # Raw Notes — ComfyUI Custom Nodes and Resources ## Awesome ComfyUI Custom Nodes (GitHub) A curated collection at github.com/ComfyUI-Workflow/awesome-comfyui: - Extends ComfyUI capabilities - Simplifies workflows - Inspires creativity (Full node list not extracted — would need deeper page exploration) ## Batch Image Generation Web App github.com/rsandagon/comfyui-batch-image-generation: - Web application managing batch image generation - Uses ComfyUI…

### n8n
- **Source:** `local:research/crow-lore/comfyui-multi-agent-image-chains/entities/n8n.md`
- **Raw:** `[[raw/local/n8n-7908165d16.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- title: "n8n Workflow Automation Tool" topic: comfyui-multi-agent-image-chains type: entity sources: - https://dev.to/worldlinetech/automating-image-generation-with-n8n-and-comfyui-521p --- # n8n Workflow Automation Tool ## Overview n8n is a workflow automation tool with a visual, node-based editor for creating complex multi-step workflows. It can orchestrate ComfyUI alongside other services (LLMs, databases, APIs). ## Installation ### Node.js ### Docker Editor UI accessible at `http://localhost:5678`. ## Licensing - **Fair-code / open-core**: Self-host and modify freely; SaaS providers must contribute back - **Community version**: Lacks global variables, multiple environments, Git…

### prompt-injection-parameter-control
- **Source:** `local:research/crow-lore/comfyui-multi-agent-image-chains/concepts/prompt-injection-parameter-control.md`
- **Raw:** `[[raw/local/prompt-injection-parameter-control-4ce1987488.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- title: "Prompt Injection and Parameter Control" topic: comfyui-multi-agent-image-chains type: concept sources: - https://dev.to/worldlinetech/automating-image-generation-with-n8n-and-comfyui-521p - https://comfyui.org/en/programmatic-image-generation-api-workflow --- # Prompt Injection and Parameter Control ## Overview When using ComfyUI's API for automated image generation, the workflow JSON must be programmatically modified to inject dynamic parameters (prompts, seeds, dimensions, etc.). ## Workflow JSON Structure ComfyUI API workflows use numeric node IDs as keys: ## Parameter Injection Points ### Positive/Negative Prompts Find CLIPTextEncode nodes and modify `inputs.text`: ### Seed…

### workflow-chaining-batch-generation
- **Source:** `local:research/crow-lore/comfyui-multi-agent-image-chains/concepts/workflow-chaining-batch-generation.md`
- **Raw:** `[[raw/local/workflow-chaining-batch-generation-9d155de6ab.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- title: "Workflow Chaining and Batch Generation" topic: comfyui-multi-agent-image-chains type: concept sources: - https://www.runpod.io/articles/guides/comfy-ui-flux - https://comfyui.org/en/programmatic-image-generation-api-workflow - https://dev.to/worldlinetech/automating-image-generation-with-n8n-and-comfyui-521p --- # Workflow Chaining and Batch Generation ## Overview Workflow chaining is the practice of connecting multiple ComfyUI workflows in sequence, where the output of one workflow becomes the input of the next. This enables complex multi-step image generation pipelines for stylized art. ## Approaches to Chaining ### 1. Intra-ComfyUI Chaining (Node Graph) Connect nodes within a…

### comfyui-api
- **Source:** `local:research/crow-lore/comfyui-multi-agent-image-chains/entities/comfyui-api.md`
- **Raw:** `[[raw/local/comfyui-api-e6b4bd2d5a.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- title: "ComfyUI API" topic: comfyui-multi-agent-image-chains type: entity sources: - https://dev.to/worldlinetech/automating-image-generation-with-n8n-and-comfyui-521p - https://comfyui.org/en/programmatic-image-generation-api-workflow - https://www.runpod.io/articles/guides/comfy-ui-flux --- # ComfyUI HTTP API ## Overview ComfyUI exposes an HTTP API and WebSocket interface that enables programmatic image generation, batch processing, and workflow chaining from external applications. ## API Endpoints | Endpoint | Method | Purpose | |---|---|---| | `/prompt` | POST | Submit workflow JSON for execution | | `/history` | GET | Retrieve execution history | | `/view` | GET | Retrieve…

### guide
- **Source:** `local:docs/hermes-cron-management-via-chat/guide.md`
- **Raw:** `[[raw/local/guide-1954b49f21.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Hermes Cron Job Management via Chat ## Summary Hermes has a built-in cron scheduler that lets you create, manage, and monitor recurring automated tasks **entirely through natural language chat** — no SSH, no crontab editing, no YAML wrangling needed. You talk to your Hermes agent (through Discord, Telegram, CLI, or any messaging platform) and describe what you want to happen on what schedule. The agent uses the `cronjob` tool to create the job, and results are delivered back to where you asked. Scheduling is handled by the Hermes **gateway daemon**, which ticks every 60 seconds. When a job comes due, it spins up a fresh agent session with your prompt, attached skills, and project context,…

### guide
- **Source:** `local:docs/hermes-webhook-subscriptions/guide.md`
- **Raw:** `[[raw/local/guide-2d1611317a.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Hermes Webhook Subscriptions for Event-Driven Automations ## Summary Webhook subscriptions let Hermes Agent respond to external events — GitHub pushes, issue updates, Stripe payments, CI/CD pipeline results — instead of only interactive chat messages. You create a subscription via the `hermes webhook subscribe` CLI, which gives you a URL endpoint like `/webhooks/github-push`. External services POST JSON payloads to that endpoint. Hermes validates the HMAC signature, renders your prompt template with payload fields (e.g., `{issue.title}`, `{pusher.name}`), triggers an agent run with the skills you specify, and delivers the response to Discord, Telegram, Slack, or any configured platform.…

### log
- **Source:** `local:research/crow-lore/hermes-gateway-dual-platform/log.md`
- **Raw:** `[[raw/local/log-5ac8fed1fb.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Wiki Log > Chronological record of all wiki actions. Append-only. > Format: `## [YYYY-MM-DD] action | subject` > Actions: ingest, update, query, lint, create, archive, delete > When this file exceeds 500 entries, rotate: rename to log-YYYY.md, start fresh. ## [2026-06-26] create | Wiki initialized - Domain: Hermes Agent Gateway Dual-Platform Configuration (Discord + Webhook) - Structure created with SCHEMA.md, index.md, log.md - Research triggered by Crow's AGENTS.md workflow for session 20260626_154043 ## [2026-06-26] ingest | Source batch — 7 raw articles ingested - `raw/articles/hermes-docs-webhooks.md` — Official webhook platform documentation - `raw/articles/hermes-docs-discord.md` —…

### index
- **Source:** `local:research/crow-lore/hermes-gateway-dual-platform/index.md`
- **Raw:** `[[raw/local/index-274cdea4ce.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Wiki Index > Content catalog. Every wiki page listed under its type with a one-line summary. > Read this first to find relevant pages for any query. > Last updated: 2026-06-26 | Total pages: 11 ## Entities - [[hermes-gateway-runner]] — Core long-running process that hosts multiple platform adapters in one GatewayRunner - [[webhook-platform-adapter]] — HTTP server adapter that accepts POST requests, validates HMAC, and triggers agent runs - [[webhook-subscription]] — Dynamically-created named route for event-driven agent execution, persisted to JSON - [[cloudflare-tunnel]] — Cloudflared-based reverse tunnel for exposing local webhook ports to the public internet ## Concepts -…

### cloudflare-tunnel-integration
- **Source:** `local:research/crow-lore/hermes-gateway-dual-platform/concepts/cloudflare-tunnel-integration.md`
- **Raw:** `[[raw/local/cloudflare-tunnel-integration-aae7598bf4.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- title: Cloudflare Tunnel Integration created: 2026-06-26 updated: 2026-06-26 type: concept tags: [cloudflare-tunnel, webhook, integration, networking] sources: [raw/articles/hermes-docs-cloudflare-tunnel.md, raw/articles/frieza-config-analysis.md, raw/articles/hermes-docs-multi-profile-gateways.md] confidence: high --- # Cloudflare Tunnel Integration ## Definition Cloudflare Tunnel integration is the pattern of exposing Hermes Agent's local webhook HTTP server to the public internet via Cloudflare's `cloudflared` reverse tunnel. It is the recommended approach across multiple Hermes documentation pages for WhatsApp Cloud API, LINE, MS Graph, and the general webhook platform.…

### static-vs-dynamic-routes
- **Source:** `local:research/crow-lore/hermes-gateway-dual-platform/comparisons/static-vs-dynamic-routes.md`
- **Raw:** `[[raw/local/static-vs-dynamic-routes-6966cd0a75.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- title: Static Routes vs. Dynamic Subscriptions created: 2026-06-26 updated: 2026-06-26 type: comparison tags: [webhook, configuration, routes, subscriptions, dynamic-routes] sources: [raw/articles/hermes-docs-webhooks.md, raw/articles/remoteopenclaw-webhook-subscriptions.md, raw/articles/aiskill-market-webhook-subscriptions.md, raw/articles/frieza-config-analysis.md] confidence: high --- # Static Routes vs. Dynamic Subscriptions ## What Is Being Compared Hermes Agent's webhook platform supports two methods for defining webhook routes: **static routes** (declared in `config.yaml`) and **dynamic subscriptions** (created via `hermes webhook subscribe` CLI). Both produce the same end result…

### hmac-security-model
- **Source:** `local:research/crow-lore/hermes-gateway-dual-platform/concepts/hmac-security-model.md`
- **Raw:** `[[raw/local/hmac-security-model-d7326c4e83.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- title: HMAC Security Model created: 2026-06-26 updated: 2026-06-26 type: concept tags: [hmac, signature-validation, security, webhook] sources: [raw/articles/hermes-docs-webhooks.md, raw/articles/remoteopenclaw-webhook-subscriptions.md, raw/articles/aiskill-market-webhook-subscriptions.md, raw/articles/frieza-config-analysis.md] confidence: high --- # HMAC Security Model ## Definition The HMAC (Hash-based Message Authentication Code) security model in Hermes Agent's webhook platform ensures that only authenticated external services can trigger agent runs. Every incoming webhook POST must carry a valid HMAC-SHA256 signature that matches the secret configured for that route or…

### event-driven-agent-runs
- **Source:** `local:research/crow-lore/hermes-gateway-dual-platform/concepts/event-driven-agent-runs.md`
- **Raw:** `[[raw/local/event-driven-agent-runs-9e55d8393d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- title: Event-Driven Agent Runs created: 2026-06-26 updated: 2026-06-26 type: concept tags: [event-driven, webhook, gateway, agent-execution, github-webhook] sources: [raw/articles/hermes-docs-webhooks.md, raw/articles/remoteopenclaw-webhook-subscriptions.md, raw/articles/hermes-docs-gateway-internals.md, raw/articles/frieza-config-analysis.md] confidence: high --- # Event-Driven Agent Runs ## Definition Event-driven agent runs are Hermes Agent executions triggered not by user chat messages but by external webhook events — GitHub push notifications, Stripe payment webhooks, CI/CD pipeline results, IoT sensor readings, or any service capable of POSTing JSON to an HTTP endpoint.…

### subscription-routing
- **Source:** `local:research/crow-lore/hermes-gateway-dual-platform/concepts/subscription-routing.md`
- **Raw:** `[[raw/local/subscription-routing-737817f646.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- title: Subscription Routing (Webhook → Delivery Target) created: 2026-06-26 updated: 2026-06-26 type: concept tags: [subscription, deliver-targets, routing, webhook, discord] sources: [raw/articles/hermes-docs-webhooks.md, raw/articles/remoteopenclaw-webhook-subscriptions.md, raw/articles/aiskill-market-webhook-subscriptions.md, raw/articles/frieza-config-analysis.md] confidence: high --- # Subscription Routing (Webhook → Delivery Target) ## Definition Subscription routing is the mechanism by which a webhook-triggered agent run delivers its response to a specific chat platform, channel, or service. The `deliver` and `deliver_extra` fields in webhook routes/subscriptions determine where…

### webhook-subscription
- **Source:** `local:research/crow-lore/hermes-gateway-dual-platform/entities/webhook-subscription.md`
- **Raw:** `[[raw/local/webhook-subscription-314d7fd85d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- title: Webhook Subscription created: 2026-06-26 updated: 2026-06-26 type: entity tags: [webhook, subscription, event-driven] sources: [raw/articles/hermes-docs-webhooks.md, raw/articles/remoteopenclaw-webhook-subscriptions.md, raw/articles/aiskill-market-webhook-subscriptions.md, raw/articles/frieza-config-analysis.md] confidence: high --- # Webhook Subscription ## Overview A webhook subscription is a named route created dynamically via `hermes webhook subscribe` that maps an external service's webhook events to Hermes agent runs. Unlike static routes in `config.yaml`, subscriptions are managed entirely through the CLI and persisted to `~/.hermes/webhook_subscriptions.json`.…

### webhook-platform-adapter
- **Source:** `local:research/crow-lore/hermes-gateway-dual-platform/entities/webhook-platform-adapter.md`
- **Raw:** `[[raw/local/webhook-platform-adapter-049a3f27cd.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- title: Webhook Platform Adapter created: 2026-06-26 updated: 2026-06-26 type: entity tags: [webhook, platform-adapter, hmac, configuration] sources: [raw/articles/hermes-docs-webhooks.md, raw/articles/remoteopenclaw-webhook-subscriptions.md, raw/articles/aiskill-market-webhook-subscriptions.md] confidence: high --- # Webhook Platform Adapter ## Overview The webhook adapter is an HTTP server platform adapter that accepts POST requests from external services, validates HMAC-SHA256 signatures, transforms payloads into agent prompts, and routes responses to configured delivery targets. ^[raw/articles/hermes-docs-webhooks.md] It supports GitHub, GitLab, JIRA, Stripe, and any service that…

### aiskill-market-webhook-subscriptions
- **Source:** `local:research/crow-lore/hermes-gateway-dual-platform/raw/articles/aiskill-market-webhook-subscriptions.md`
- **Raw:** `[[raw/local/aiskill-market-webhook-subscriptions-cd04f3b077.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- source_url: https://aiskill.market/skills-capabilities/webhook-subscriptions ingested: 2026-06-26 sha256: b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3 --- # Webhook Subscriptions (AI Skill Market) Corroborating source for Hermes webhook subscriptions. ## Setup Identical to Remote OpenClaw source: enable webhook platform via wizard, config.yaml, or env vars. ## Management - `hermes webhook subscribe <name>` — create - `hermes webhook list` — list - `hermes webhook remove <name>` — delete - `hermes webhook test <name>` — test ## Prompt Templates Dot-notation: `{issue.title}`, `{pull_request.user.login}`, `{data.object.amount}`, `{sensor.temperature}`. ## Delivery Targets Full…

### remoteopenclaw-webhook-subscriptions
- **Source:** `local:research/crow-lore/hermes-gateway-dual-platform/raw/articles/remoteopenclaw-webhook-subscriptions.md`
- **Raw:** `[[raw/local/remoteopenclaw-webhook-subscriptions-50f5d19391.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- source_url: https://www.remoteopenclaw.com/skills-capabilities/hermes/built-in-webhook-subscriptions ingested: 2026-06-26 sha256: a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2 --- # Webhook Subscriptions (Remote OpenClaw) ## Overview Webhook subscriptions enable event-driven agent runs in Hermes. External services (GitHub, GitLab, Stripe, CI/CD, IoT, monitoring tools) can POST events to a URL to trigger Hermes agents. ## Setup Enable the webhook platform before creating subscriptions. Verify with `hermes webhook list`. Three setup methods: 1. Setup wizard: `hermes gateway setup` 2. Manual config in config.yaml under `platforms.webhook` 3. Environment variables: `WEBHOOK_ENABLED`,…

### hermes-docs-cloudflare-tunnel
- **Source:** `local:research/crow-lore/hermes-gateway-dual-platform/raw/articles/hermes-docs-cloudflare-tunnel.md`
- **Raw:** `[[raw/local/hermes-docs-cloudflare-tunnel-d2a36f7d5d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- source_url: https://hermes-agent.nousresearch.com/docs/user-guide/messaging/whatsapp-cloud ingested: 2026-06-26 sha256: c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4 --- # Cloudflare Tunnel Integration (from WhatsApp Cloud Docs) The WhatsApp Cloud API documentation describes the canonical Cloudflare Tunnel pattern used across all Hermes HTTP-inbound platforms (webhooks, WhatsApp, LINE, MS Graph). ## Exposing Hermes to the Internet Three methods documented: ### Cloudflare Tunnel (Recommended) Free, no port forwarding, no domain required. Quick tunnel URL changes on restart. For permanent named tunnels, log in with `cloudflared tunnel login`. ### ngrok Free tier gives…

### hermes-docs-webhooks
- **Source:** `local:research/crow-lore/hermes-gateway-dual-platform/raw/articles/hermes-docs-webhooks.md`
- **Raw:** `[[raw/local/hermes-docs-webhooks-9d3e60d858.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- source_url: https://hermes-agent.nousresearch.com/docs/user-guide/messaging/webhooks ingested: 2026-06-26 sha256: 4f7a2b1c9d3e5f6a8b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a --- # Webhooks | Hermes Agent The webhook adapter runs an HTTP server that accepts POST requests, validates HMAC signatures, transforms payloads into agent prompts, and routes responses back to the source or to another configured platform. It supports GitHub, GitLab, JIRA, Stripe, and any service that sends JSON webhooks. ## Setup Methods Three setup paths: 1. **Setup wizard:** `hermes gateway setup` — follow prompts to enable webhooks, set port, and set global HMAC secret 2. **Environment variables:** Set…

### SCHEMA
- **Source:** `local:research/crow-lore/hermes-gateway-dual-platform/SCHEMA.md`
- **Raw:** `[[raw/local/schema-518218a968.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Wiki Schema ## Domain Hermes Agent Gateway Platform Architecture — specifically the dual-platform pattern that enables a single Hermes profile to serve both Discord (interactive chat) and Webhook (event-driven) platforms simultaneously. Covers platform configuration syntax, webhook subscription model, HMAC security, Cloudflare Tunnel integration, and event-driven agent runs. ## Conventions - File names: lowercase, hyphens, no spaces (e.g., `dual-platform-architecture.md`) - Every wiki page starts with YAML frontmatter (see below) - Use `[[wikilinks]]` to link between pages (minimum 2 outbound links per page) - When updating a page, always bump the `updated` date - Every new page must be…

### SKILL
- **Source:** `local:projects/southpaw/anser/skills-capabilities/research-knowledge/research-knowledge-retrieval/SKILL.md`
- **Raw:** `[[raw/local/skill-abdf49dfd5.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: research-knowledge-retrieval description: "Research, knowledge retrieval, and content monitoring: blog/feed monitoring (blogwatcher), ML paper writing pipeline (research-paper-writing), prediction market data (polymarket), and YouTube content extraction (youtube-content)." version: 1.0.0 author: Hermes Agent license: MIT tags: ["research", "knowledge", "retrieval", "blogwatcher", "paper-writing", "polymarket", "youtube", "monitoring"] platforms: [linux, macos, windows] metadata: hermes: tags: [research, knowledge, retrieval, blogwatcher, paper-writing, polymarket, youtube, monitoring] category: research-knowledge related_skills: [mlops-model-registry-tracking,…

- **Collapsed duplicates:** `local:projects/anser/skills-capabilities/research-knowledge/research-knowledge-retrieval/SKILL.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/research/research-paper-writing/SKILL.md`
- **Raw:** `[[raw/local/skill-5bc92cec83.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: research-paper-writing title: Research Paper Writing Pipeline description: "Write ML papers for NeurIPS/ICML/ICLR: design→submit." version: 1.1.0 author: Orchestra Research license: MIT dependencies: [semanticscholar, arxiv, habanero, requests, scipy, numpy, matplotlib, SciencePlots] platforms: [linux, macos] metadata: hermes: tags: [Research, Paper Writing, Experiments, ML, AI, NeurIPS, ICML, ICLR, ACL, AAAI, COLM, LaTeX, Citations, Statistical Analysis] category: research related_skills: [arxiv, ml-paper-writing, subagent-driven-development, plan] requires_toolsets: [terminal, files] --- # Research Paper Writing Pipeline End-to-end pipeline for producing publication-ready ML/AI…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/research/research-paper-writing/SKILL.md`, `local:projects/jestur/skills-capabilities/research/research-paper-writing/SKILL.md`, `local:projects/dev-coder/skills-capabilities/research/research-paper-writing/SKILL.md`, `local:projects/dev-orch/skills-capabilities/research/research-paper-writing/SKILL.md`, `local:projects/dev-review/skills-capabilities/research/research-paper-writing/SKILL.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/productivity/teams-meeting-pipeline/SKILL.md`
- **Raw:** `[[raw/local/skill-9a9d2abc4b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: teams-meeting-pipeline description: "Operate the Teams meeting summary pipeline via Hermes CLI — summarize meetings, inspect pipeline status, replay jobs, manage Microsoft Graph subscriptions." version: 1.1.0 author: Hermes Agent + Teknium license: MIT prerequisites: env_vars: [MSGRAPH_TENANT_ID, MSGRAPH_CLIENT_ID, MSGRAPH_CLIENT_SECRET] commands: [hermes] metadata: hermes: tags: [Teams, Microsoft Graph, Meetings, Productivity, Operations] related_docs: - /docs/guides/microsoft-graph-app-registration - /docs/user-guide/messaging/teams-meetings - /docs/guides/operate-teams-meeting-pipeline --- # Teams Meeting Pipeline Use this skill whenever the user asks about Microsoft Teams…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/productivity/teams-meeting-pipeline/SKILL.md`, `local:projects/jestur/skills-capabilities/productivity/teams-meeting-pipeline/SKILL.md`, `local:projects/dev-coder/skills-capabilities/productivity/teams-meeting-pipeline/SKILL.md`, `local:projects/dev-orch/skills-capabilities/productivity/teams-meeting-pipeline/SKILL.md`, `local:projects/dev-review/skills-capabilities/productivity/teams-meeting-pipeline/SKILL.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/github/github-repo-management/SKILL.md`
- **Raw:** `[[raw/local/skill-d187ee2c1a.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: github-repo-management description: "Clone/create/fork repos; manage remotes, releases." version: 1.1.0 author: Hermes Agent license: MIT platforms: [linux, macos, windows] metadata: hermes: tags: [GitHub, Repositories, Git, Releases, Secrets, Configuration] related_skills: [github-auth, github-pr-workflow, github-issues] --- # GitHub Repository Management Create, clone, fork, configure, and manage GitHub repositories. Each section shows `gh` first, then the `git` + `curl` fallback. ## Prerequisites - Authenticated with GitHub (see `github-auth` skill) ### Setup If you're inside a repo already: --- ## 1. Cloning Repositories Cloning is pure `git` — works identically either way:…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/github/github-repo-management/SKILL.md`, `local:projects/jestur/skills-capabilities/github/github-repo-management/SKILL.md`, `local:projects/dev-coder/skills-capabilities/github/github-repo-management/SKILL.md`, `local:projects/dev-orch/skills-capabilities/github/github-repo-management/SKILL.md`, `local:projects/dev-review/skills-capabilities/github/github-repo-management/SKILL.md`

### conventional-commits
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/github/github-pr-workflow/references/conventional-commits.md`
- **Raw:** `[[raw/local/conventional-commits-2d71a3b701.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Conventional Commits Quick Reference Format: `type(scope): description` ## Types | Type | When to use | Example | |------|------------|---------| | `feat` | New feature or capability | `feat(auth): add OAuth2 login flow` | | `fix` | Bug fix | `fix(api): handle null response from /users endpoint` | | `refactor` | Code restructuring, no behavior change | `refactor(db): extract query builder into separate module` | | `docs` | Documentation only | `docs: update API usage examples in README` | | `test` | Adding or updating tests | `test(auth): add integration tests for token refresh` | | `ci` | CI/CD configuration | `ci: add Python 3.12 to test matrix` | | `chore` | Maintenance, dependencies,…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/github/github-pr-workflow/references/conventional-commits.md`, `local:projects/jestur/skills-capabilities/github/github-pr-workflow/references/conventional-commits.md`, `local:projects/dev-coder/skills-capabilities/github/github-pr-workflow/references/conventional-commits.md`, `local:projects/dev-orch/skills-capabilities/github/github-pr-workflow/references/conventional-commits.md`, `local:projects/dev-review/skills-capabilities/github/github-pr-workflow/references/conventional-commits.md`

### ci-troubleshooting
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/github/github-pr-workflow/references/ci-troubleshooting.md`
- **Raw:** `[[raw/local/ci-troubleshooting-ab98bea8c0.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # CI Troubleshooting Quick Reference Common CI failure patterns and how to diagnose them from the logs. ## Reading CI Logs ## Common Failure Patterns ### Test Failures **Signatures in logs:** **Diagnosis:** 1. Find the test file and line number from the traceback 2. Use `read_file` to read the failing test 3. Check if it's a logic error in the code or a stale test assertion 4. Look for `ModuleNotFoundError` — usually a missing dependency in CI **Common fixes:** - Update assertion to match new expected behavior - Add missing dependency to requirements.txt / pyproject.toml - Fix flaky test (add retry, mock external service, fix race condition) --- ### Lint / Formatting Failures **Signatures…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/github/github-pr-workflow/references/ci-troubleshooting.md`, `local:projects/jestur/skills-capabilities/github/github-pr-workflow/references/ci-troubleshooting.md`, `local:projects/dev-coder/skills-capabilities/github/github-pr-workflow/references/ci-troubleshooting.md`, `local:projects/dev-orch/skills-capabilities/github/github-pr-workflow/references/ci-troubleshooting.md`, `local:projects/dev-review/skills-capabilities/github/github-pr-workflow/references/ci-troubleshooting.md`

### DESCRIPTION
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/github/DESCRIPTION.md`
- **Raw:** `[[raw/local/description-51c160e236.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- description: GitHub workflow skills for managing repositories, pull requests, code reviews, issues, and CI/CD pipelines using the gh CLI and git via terminal. ---

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/github/DESCRIPTION.md`, `local:projects/jestur/skills-capabilities/github/DESCRIPTION.md`, `local:projects/dev-coder/skills-capabilities/github/DESCRIPTION.md`, `local:projects/dev-orch/skills-capabilities/github/DESCRIPTION.md`, `local:projects/dev-review/skills-capabilities/github/DESCRIPTION.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/devops/webhook-subscriptions/SKILL.md`
- **Raw:** `[[raw/local/skill-c9c3e76cb9.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: webhook-subscriptions description: "Webhook subscriptions: event-driven agent runs." version: 1.1.0 platforms: [linux, macos, windows] metadata: hermes: tags: [webhook, events, automation, integrations, notifications, push] --- # Webhook Subscriptions Create dynamic webhook subscriptions so external services (GitHub, GitLab, Stripe, CI/CD, IoT sensors, monitoring tools) can trigger Hermes agent runs by POSTing events to a URL. ## Setup (Required First) The webhook platform must be enabled before subscriptions can be created. Check with: If it says "Webhook platform is not enabled", set it up: ### Option 1: Setup wizard Follow the prompts to enable webhooks, set the port, and set a…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/devops/webhook-subscriptions/SKILL.md`, `local:projects/jestur/skills-capabilities/devops/webhook-subscriptions/SKILL.md`, `local:projects/dev-coder/skills-capabilities/devops/webhook-subscriptions/SKILL.md`, `local:projects/dev-orch/skills-capabilities/devops/webhook-subscriptions/SKILL.md`, `local:projects/dev-review/skills-capabilities/devops/webhook-subscriptions/SKILL.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/devops/kanban-worker/SKILL.md`
- **Raw:** `[[raw/local/skill-806c5f0fe2.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: kanban-worker description: Pitfalls, examples, and edge cases for Hermes Kanban workers. The lifecycle itself is auto-injected into every worker's system prompt as KANBAN_GUIDANCE (from agent/prompt_builder.py); this skill is what you load when you want deeper detail on specific scenarios. version: 2.0.0 platforms: [linux, macos, windows] environments: [kanban] metadata: hermes: tags: [kanban, multi-agent, collaboration, workflow, pitfalls] related_skills: [kanban-orchestrator] --- # Kanban Worker — Pitfalls and Examples > You're seeing this skill because the Hermes Kanban dispatcher spawned you as a worker with `--skills kanban-worker` — it's loaded automatically for every…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/devops/kanban-worker/SKILL.md`, `local:projects/jestur/skills-capabilities/devops/kanban-worker/SKILL.md`, `local:projects/dev-coder/skills-capabilities/devops/kanban-worker/SKILL.md`, `local:projects/dev-orch/skills-capabilities/devops/kanban-worker/SKILL.md`, `local:projects/dev-review/skills-capabilities/devops/kanban-worker/SKILL.md`

### vercel
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/creative/popular-web-designs/templates/vercel.md`
- **Raw:** `[[raw/local/vercel-ad326ef79b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Design System: Vercel > **Hermes Agent — Implementation Notes** > > The original site uses proprietary fonts. For self-contained HTML output, use these CDN substitutes: > - **Primary:** `Geist` | **Mono:** `Geist Mono` > - **Font stack (CSS):** `font-family: 'Geist', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;` > - **Mono stack (CSS):** `font-family: 'Geist Mono', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace;` > > Use `write_file` to create HTML, serve via `generative-widgets` skill (cloudflared tunnel). > Verify visual accuracy with `browser_vision` after generating. ## 1. Visual Theme & Atmosphere Vercel's website is…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/creative/popular-web-designs/templates/vercel.md`, `local:projects/jestur/skills-capabilities/creative/popular-web-designs/templates/vercel.md`, `local:projects/dev-coder/skills-capabilities/creative/popular-web-designs/templates/vercel.md`, `local:projects/dev-orch/skills-capabilities/creative/popular-web-designs/templates/vercel.md`, `local:projects/dev-review/skills-capabilities/creative/popular-web-designs/templates/vercel.md`

### export-pipeline
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/creative/p5js/references/export-pipeline.md`
- **Raw:** `[[raw/local/export-pipeline-5d186d0dd1.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Export Pipeline ## PNG Export ### In-Sketch (Keyboard Shortcut) ### Timed Export (Static Generative) ### High-Resolution Export For resolutions beyond screen size, use `pixelDensity()` or a large offscreen buffer: ### Batch Seed Export ## GIF Export ### saveGif() Limitations: - GIF is 256 colors max — dithering artifacts on gradients - Large canvases produce huge files - Use a smaller canvas (640x360) for GIF, higher for PNG/MP4 - Frame rate is approximate ### Optimal GIF Settings ## Frame Sequence Export ### saveFrames() ### Manual Frame Export (More Control) ### Deterministic Capture (Critical for Video) The `noLoop()` + `redraw()` pattern is **required** for frame-perfect headless…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/creative/p5js/references/export-pipeline.md`, `local:projects/jestur/skills-capabilities/creative/p5js/references/export-pipeline.md`, `local:projects/dev-coder/skills-capabilities/creative/p5js/references/export-pipeline.md`, `local:projects/dev-orch/skills-capabilities/creative/p5js/references/export-pipeline.md`, `local:projects/dev-review/skills-capabilities/creative/p5js/references/export-pipeline.md`

### paper-explainer
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/creative/manim-video/references/paper-explainer.md`
- **Raw:** `[[raw/local/paper-explainer-ab67495a01.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Paper Explainer Workflow How to turn a research paper into an animated explainer video. ## Why animate a paper? A research paper is optimized for precision and completeness. A video is optimized for understanding and retention. The translation is NOT "read the paper aloud with pictures" — it's "extract the core insight and make it feel obvious through visual storytelling." The paper has one job: prove the claim is true. The video has a different job: make the viewer understand WHY the claim is true, and WHY it matters. ## Who is watching? Before anything, decide the audience: | Audience | Prerequisites | Pacing | Depth | |----------|--------------|--------|-------| | General public | None…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/creative/manim-video/references/paper-explainer.md`, `local:projects/jestur/skills-capabilities/creative/manim-video/references/paper-explainer.md`, `local:projects/dev-coder/skills-capabilities/creative/manim-video/references/paper-explainer.md`, `local:projects/dev-orch/skills-capabilities/creative/manim-video/references/paper-explainer.md`, `local:projects/dev-review/skills-capabilities/creative/manim-video/references/paper-explainer.md`

### README
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/creative/comfyui/workflows/README.md`
- **Raw:** `[[raw/local/readme-52da43e45a.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Example Workflows These are starter API-format workflows for the most common tasks. They're ready to run with `scripts/run_workflow.py` once you've installed (or have cloud access to) the listed models. | File | Purpose | Required models | Min VRAM | |------|---------|-----------------|----------| | `sd15_txt2img.json` | SD 1.5 text-to-image (512×512) | SD1.5 checkpoint, e.g. `v1-5-pruned-emaonly.safetensors` | 4 GB | | `sdxl_txt2img.json` | SDXL text-to-image (1024×1024) | `sd_xl_base_1.0.safetensors` | 8 GB | | `flux_dev_txt2img.json` | Flux Dev text-to-image (1024×1024) | `flux1-dev.safetensors`, `t5xxl_fp16.safetensors`, `clip_l.safetensors`, `ae.safetensors` | 24 GB (or use…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/creative/comfyui/workflows/README.md`, `local:projects/jestur/skills-capabilities/creative/comfyui/workflows/README.md`, `local:projects/dev-coder/skills-capabilities/creative/comfyui/workflows/README.md`, `local:projects/dev-orch/skills-capabilities/creative/comfyui/workflows/README.md`, `local:projects/dev-review/skills-capabilities/creative/comfyui/workflows/README.md`

### template-integrity
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/creative/comfyui/references/template-integrity.md`
- **Raw:** `[[raw/local/template-integrity-746caa050d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ComfyUI Workflow-Template Integrity > **Authored by [@purzbeats](https://github.com/purzbeats)** — adapted from > [purzbeats/hermes-agent-comfyui-helper](https://github.com/purzbeats/hermes-agent-comfyui-helper). > Use this reference when converting workflows from the official > `comfyui-workflow-templates` package (editor format) into API format for > submission via `/api/prompt`. The conversion has subtle gotchas that cause > hard-to-diagnose validation errors if you don't follow these rules. ## Background The official ComfyUI template package (`comfyui-workflow-templates`, currently v0.9.69) is installed inside the ComfyUI venv at a path like: The exact path depends on how ComfyUI was…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/creative/comfyui/references/template-integrity.md`, `local:projects/jestur/skills-capabilities/creative/comfyui/references/template-integrity.md`, `local:projects/dev-coder/skills-capabilities/creative/comfyui/references/template-integrity.md`, `local:projects/dev-orch/skills-capabilities/creative/comfyui/references/template-integrity.md`, `local:projects/dev-review/skills-capabilities/creative/comfyui/references/template-integrity.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/creative/comfyui/SKILL.md`
- **Raw:** `[[raw/local/skill-3125e3beb5.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: comfyui description: "Generate images, video, and audio with ComfyUI — install, launch, manage nodes/models, run workflows with parameter injection. Uses the official comfy-cli for lifecycle and direct REST/WebSocket API for execution." version: 5.1.0 author: [kshitijk4poor, alt-glitch, purzbeats] license: MIT platforms: [macos, linux, windows] compatibility: "Requires ComfyUI (local, Comfy Desktop, or Comfy Cloud) and comfy-cli (auto-installed via pipx/uvx by the setup script)." prerequisites: commands: ["python3"] setup: help: "Run scripts/hardware_check.py FIRST to decide local vs Comfy Cloud; then scripts/comfyui_setup.sh auto-installs locally (or use Cloud API key for…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/creative/comfyui/SKILL.md`, `local:projects/jestur/skills-capabilities/creative/comfyui/SKILL.md`, `local:projects/dev-coder/skills-capabilities/creative/comfyui/SKILL.md`, `local:projects/dev-orch/skills-capabilities/creative/comfyui/SKILL.md`, `local:projects/dev-review/skills-capabilities/creative/comfyui/SKILL.md`

### funnel
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/creative/baoyu-infographic/references/layouts/funnel.md`
- **Raw:** `[[raw/local/funnel-e505f04f33.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # funnel Narrowing stages showing conversion, filtering, or refinement process. ## Structure - Wide top (input/start) - Narrow bottom (output/result) - Horizontal layers for stages - Progressive narrowing - 3-6 stages typically ## Best For - Sales/marketing funnels - Conversion processes - Filtering/selection - Recruitment pipelines - Decision processes ## Visual Elements - Funnel shape clearly defined - Distinct colors per stage - Width indicates volume/quantity - Stage icons or symbols - Numbers/percentages per stage ## Text Placement - Title at top - Stage names inside or beside - Metrics/numbers per stage - Input label at top - Output label at bottom ## Recommended Pairings -…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/creative/baoyu-infographic/references/layouts/funnel.md`, `local:projects/jestur/skills-capabilities/creative/baoyu-infographic/references/layouts/funnel.md`, `local:projects/dev-coder/skills-capabilities/creative/baoyu-infographic/references/layouts/funnel.md`, `local:projects/dev-orch/skills-capabilities/creative/baoyu-infographic/references/layouts/funnel.md`, `local:projects/dev-review/skills-capabilities/creative/baoyu-infographic/references/layouts/funnel.md`

### partial-workflows
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/creative/baoyu-comic/references/partial-workflows.md`
- **Raw:** `[[raw/local/partial-workflows-2d6f852708.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Partial Workflows Options to run specific parts of the workflow. Trigger these via natural language (e.g., "just the storyboard", "regenerate page 3"). ## Options Summary | Option | Steps Executed | Output | |--------|----------------|--------| | Storyboard only | 1-3 | `storyboard.md` + `characters/` | | Prompts only | 1-5 | + `prompts/*.md` | | Images only | 7-8 | + images | | Regenerate N | 7 (partial) | Specific page(s) | --- ## Storyboard-only Generate storyboard and characters without prompts or images. **User cue**: "storyboard only", "just the outline", "don't generate images yet". **Workflow**: Steps 1-3 only (stop after storyboard + characters) **Output**: - `analysis.md` -…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/creative/baoyu-comic/references/partial-workflows.md`, `local:projects/jestur/skills-capabilities/creative/baoyu-comic/references/partial-workflows.md`, `local:projects/dev-coder/skills-capabilities/creative/baoyu-comic/references/partial-workflows.md`, `local:projects/dev-orch/skills-capabilities/creative/baoyu-comic/references/partial-workflows.md`, `local:projects/dev-review/skills-capabilities/creative/baoyu-comic/references/partial-workflows.md`

### SKILL
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/creative/baoyu-comic/SKILL.md`
- **Raw:** `[[raw/local/skill-39daa86a4c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: baoyu-comic description: "Knowledge comics (知识漫画): educational, biography, tutorial." version: 1.56.1 author: 宝玉 (JimLiu) license: MIT platforms: [linux, macos, windows] metadata: hermes: tags: [comic, knowledge-comic, creative, image-generation] homepage: https://github.com/JimLiu/baoyu-skills#baoyu-comic --- # Knowledge Comic Creator Adapted from [baoyu-comic](https://github.com/JimLiu/baoyu-skills) for Hermes Agent's tool ecosystem. Create original knowledge comics with flexible art style × tone combinations. ## When to Use Trigger this skill when the user asks to create a knowledge/educational comic, biography comic, tutorial comic, or uses terms like "知识漫画", "教育漫画", or…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/creative/baoyu-comic/SKILL.md`, `local:projects/jestur/skills-capabilities/creative/baoyu-comic/SKILL.md`, `local:projects/dev-coder/skills-capabilities/creative/baoyu-comic/SKILL.md`, `local:projects/dev-orch/skills-capabilities/creative/baoyu-comic/SKILL.md`, `local:projects/dev-review/skills-capabilities/creative/baoyu-comic/SKILL.md`

### webhooks
- **Source:** `local:projects/southpaw/klerik/skills-capabilities/autonomous-ai-agents/hermes-agent/references/webhooks.md`
- **Raw:** `[[raw/local/webhooks-8dafc457e2.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Webhook Subscriptions Create dynamic webhook subscriptions so external services (GitHub, GitLab, Stripe, CI/CD, IoT sensors, monitoring tools) can trigger Hermes agent runs by POSTing events to a URL. ## Setup (Required First) The webhook platform must be enabled before subscriptions can be created. Check with: If it says "Webhook platform is not enabled", set it up: ### Option 1: Setup wizard Follow the prompts to enable webhooks, set the port, and set a global HMAC secret. ### Option 2: Manual config Add to `~/.hermes/config.yaml`: ### Option 3: Environment variables Add to `${HERMES_HOME:-~/.hermes}/.env`: After configuration, start (or restart) the gateway: Verify it's running: ##…

- **Collapsed duplicates:** `local:projects/klerik/skills-capabilities/autonomous-ai-agents/hermes-agent/references/webhooks.md`, `local:projects/dev-coder/skills-capabilities/autonomous-ai-agents/hermes-agent/references/webhooks.md`, `local:projects/dev-orch/skills-capabilities/autonomous-ai-agents/hermes-agent/references/webhooks.md`, `local:projects/dev-review/skills-capabilities/autonomous-ai-agents/hermes-agent/references/webhooks.md`

### 1503849954148483295-Cronalytics-v.-1.0---The-dashboard-for-agentic-automations-in-Hermes.
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1503849954148483295-Cronalytics-v.-1.0---The-dashboard-for-agentic-automations-in-Hermes..txt`
- **Raw:** `[[raw/discord/1503849954148483295-cronalytics-v.-1.0---the-dashboard-for-agentic-automations-in-hermes.-3939fc16e1.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Cronalytics v. 1.0 - The dashboard for agentic automations in Hermes.' in forum #plugins-skills-and-skins # thread_id=1503849954148483295 forum_id=1485392832154832906 # Started 2026-05-13T02:56:08.218593+00:00 [2026-05-12T20:02:49.250000+00:00] _8bit64k_ (id=1503849954148483295) 🚀 **Cronalytics v1.0 is live** A dashboard plugin for Hermes Agent that turns your cron job cost from a mystery into a number you can act on. --- **What it does** Cronalytics hooks into `on_session_end`, captures every cron-originated run, and writes cost, tokens, model, and duration into a local fact database. A reconciliation scanner backfills historical data so nothing is lost. All of it surfaces in a…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1503849954148483295-Cronalytics-v.-1.0---The-dashboard-for-agentic-automations-in-Hermes..txt`

### 1498344744449871952-Health-Connect-Webhook-Receiver
- **Source:** `discord-archive:archives/plugins-skills-and-skins/1498344744449871952-Health-Connect-Webhook-Receiver.txt`
- **Raw:** `[[raw/discord/1498344744449871952-health-connect-webhook-receiver-fd51416bdc.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Health Connect Webhook Receiver' in forum #plugins-skills-and-skins # thread_id=1498344744449871952 forum_id=1485392832154832906 # Started 2026-05-10T19:52:12.495204+00:00 [2026-04-27T15:27:04.976000+00:00] wysie_ (id=1498344744449871952) Standalone but I built it to use it with Hermes. Connect HC Webook (some play store app) to it and you can sync your Health Connect data locally and do whatever. https://github.com/Wysie/health-connect-webhook-receiver [embed] GitHub - Wysie/health-connect-webhook-receiver: Self-hosted SQLite ... https://github.com/Wysie/health-connect-webhook-receiver

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/plugins-skills-and-skins/1498344744449871952-Health-Connect-Webhook-Receiver.txt`

### 1519389274167050261-Claude-Workflow-Composer--CWC
- **Source:** `discord-archive:archives/community-projects-showcase/1519389274167050261-Claude-Workflow-Composer--CWC.txt`
- **Raw:** `[[raw/discord/1519389274167050261-claude-workflow-composer--cwc-08ee54c261.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Claude Workflow Composer (CWC)' in forum #community-projects-showcase # thread_id=1519389274167050261 forum_id=1316137596535177246 # Started 2026-06-24T19:43:29.602484+00:00 [2026-06-24T17:10:31.849000+00:00] fizbott (id=1519389274167050261) Built this for anyone who keeps doing the same multi-step thing in Claude Code over and over. Most workflow tools make you start from a blank canvas and guess what to automate. CWC works backwards: it scans your actual Claude Code history, finds the work you keep repeating by hand, and turns it into a runnable workflow you can run, schedule, and monitor. What makes it different: CWC reads your real Claude Code sessions, clusters repeated…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1519389274167050261-Claude-Workflow-Composer--CWC.txt`

### 1508820713677787176-Just-releaseed-Cronalytics-v1.1.0
- **Source:** `discord-archive:archives/community-projects-showcase/1508820713677787176-Just-releaseed-Cronalytics-v1.1.0.txt`
- **Raw:** `[[raw/discord/1508820713677787176-just-releaseed-cronalytics-v1.1.0-325ddf1463.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Just releaseed Cronalytics v1.1.0' in forum #community-projects-showcase # thread_id=1508820713677787176 forum_id=1316137596535177246 # Started 2026-05-26T15:21:30.267009+00:00 [2026-05-26T13:14:50.674000+00:00] _8bit64k_ (id=1508820713677787176) ## Cronalytics v1.1.0 released Changelog highlights: **New interfaces:** - Dashboard tab with cards, leaderboard, sortable jobs table, model breakdown, and failure-state analysis - CLI tool — eight commands (summary, jobs, models, trends, health, runs, all, sync), `--json` output - Agent skill for guided cron health diagnostics with confidence-graded anomaly detection **i18n:** - Spanish, Simplified Chinese, Traditional Chinese — all UI,…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1508820713677787176-Just-releaseed-Cronalytics-v1.1.0.txt`

### 1503849149257224342-Cronalytics-v.-1.0--The-dashboard-for-agentic-automations-in-Hermes.
- **Source:** `discord-archive:archives/community-projects-showcase/1503849149257224342-Cronalytics-v.-1.0--The-dashboard-for-agentic-automations-in-Hermes..txt`
- **Raw:** `[[raw/discord/1503849149257224342-cronalytics-v.-1.0--the-dashboard-for-agentic-automations-in-hermes.-311e7b00b7.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Cronalytics v. 1.0: The dashboard for agentic automations in Hermes.' in forum #community-projects-showcase # thread_id=1503849149257224342 forum_id=1316137596535177246 # Started 2026-05-13T02:53:07.446368+00:00 [2026-05-12T19:59:37.349000+00:00] _8bit64k_ (id=1503849149257224342) 🚀 **Cronalytics v1.0 is live** A dashboard plugin for Hermes Agent that turns your cron job cost from a mystery into a number you can act on. --- **What it does** Cronalytics hooks into `on_session_end`, captures every cron-originated run, and writes cost, tokens, model, and duration into a local fact database. A reconciliation scanner backfills historical data so nothing is lost. All of it surfaces in a…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1503849149257224342-Cronalytics-v.-1.0--The-dashboard-for-agentic-automations-in-Hermes..txt`

### 1417600406841720882-How-to-Create-a-Viral-AI-Video-from-Just-One-Photo-with-Google-Nano-Banana-AI
- **Source:** `discord-archive:archives/community-projects-showcase/1417600406841720882-How-to-Create-a-Viral-AI-Video-from-Just-One-Photo-with-Google-Nano-Banana-AI.txt`
- **Raw:** `[[raw/discord/1417600406841720882-how-to-create-a-viral-ai-video-from-just-one-photo-with-google-nano-banana-ai-902fe1f289.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'How to Create a Viral AI Video from Just One Photo with Google Nano Banana AI' in forum #community-projects-showcase # thread_id=1417600406841720882 forum_id=1316137596535177246 # Started 2026-05-10T19:51:33.288250+00:00 [2025-09-16T19:57:54.733000+00:00] mariia081452 (id=1417600406841720882) AI tools are changing the way creators make content. Today, you don’t need a film crew or expensive equipment to produce cinematic videos — all you need is one image and the right AI workflow. In my new video, I’ll walk you through how to use Google Nano Banana AI together with Veo3 Flow, CapCut, and 11 Labs to transform a static photo into a full AI-powered video that looks like a movie…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1417600406841720882-How-to-Create-a-Viral-AI-Video-from-Just-One-Photo-with-Google-Nano-Banana-AI.txt`

### 1412782473397403678-Social-media-automation-workflow
- **Source:** `discord-archive:archives/community-projects-showcase/1412782473397403678-Social-media-automation-workflow.txt`
- **Raw:** `[[raw/discord/1412782473397403678-social-media-automation-workflow-985e4c8e22.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Thread 'Social media automation workflow' in forum #community-projects-showcase # thread_id=1412782473397403678 forum_id=1316137596535177246 # Started 2026-05-10T19:51:35.305745+00:00 [2025-09-03T12:53:09.887000+00:00] mariia081452 (id=1412782473397403678) I’ve been experimenting with automating social media workflows. Turns out, combining n8n + Make.com + Claude + OpenAI actually lets AI agents research trending topics, draft posts, design visuals, and schedule them automatically. From one topic I’m now generating 30–40 posts across LinkedIn, Twitter, and Instagram. If anyone’s curious, I documented the full setup in a video — happy to share: https://youtu.be/XdLGrQcUwcg [embed] How to…

- **Collapsed duplicates:** `local:projects/nous-discord-archive/archives/community-projects-showcase/1412782473397403678-Social-media-automation-workflow.txt`

### story-matrix
- **Source:** `local:projects/omnistudio-daw/docs/qa/story-matrix.md`
- **Raw:** `[[raw/local/story-matrix-0c38ccccb3.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ACE-Step DAW - Story Matrix > Canonical QA index for product verification. > Source of truth order: capability doc -> story matrix -> automated/manual execution artifacts. ## Coverage Labels - `A-full`: fully automated with stable coverage - `A-partial`: partially automated, still needs manual or follow-up checks - `H-required`: human ear/eye/judgment required - `Blocked-env`: cannot run without API, device, or external environment - `Missing`: no current coverage ## Agent Operating Rules For each story, QA agents should start from this matrix and only then open linked docs/tests. - Read the capability doc first for setup, boundaries, and expected evidence. - Run the linked automated…

### docs
- **Source:** `local:projects/omnistudio-daw/.github/workflows/docs.yml`
- **Raw:** `[[raw/local/docs-6850d5e64a.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: Deploy Documentation on: push: branches: [main] workflow_dispatch: permissions: contents: read pages: write id-token=<redacted> concurrency: group: pages cancel-in-progress: false jobs: build: runs-on: ubuntu-latest steps: - name: Checkout uses: actions/checkout@v4 with: fetch-depth: 0 - name: Setup Node.js uses: actions/setup-node@v4 with: node-version: 20 cache: npm - name: Install dependencies run: npm ci - name: Build documentation run: npm run docs:build - name: Setup Pages uses: actions/configure-pages@v4 - name: Upload artifact uses: actions/upload-pages-artifact@v3 with: path: website/.vitepress/dist deploy: environment: name: github-pages url: ${{…

### autonomous-workflow
- **Source:** `local:projects/omnistudio-daw/.claude/rules/autonomous-workflow.md`
- **Raw:** `[[raw/local/autonomous-workflow-8ed7cccde5.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Autonomous AI Development Workflow > This file is auto-loaded by Claude Code for ALL sessions and ALL subagents. > These are non-negotiable rules for autonomous development. ## GitHub Issue-First (BLOCKING) Before writing ANY code (except pure questions or trivial typos <3 lines): 1. **Check for existing issue** — search GitHub Issues for duplicates first 2. **Create GitHub Issue** — English title AND body, prefix: `feat:`/`fix:`/`docs:`/`refactor:`/`chore:`, include acceptance criteria checklist, label: `bug`/`enhancement`/`docs`/`refactor` 3. **Create branch** from main — `feat/issue-NUMBER` or `fix/issue-NUMBER` 4. **Implement** on that branch with TDD + quality gates 5. **Create PR**…

### archive
- **Source:** `local:projects/omnistudio-daw/.claude/commands/opsx/archive.md`
- **Raw:** `[[raw/local/archive-16f03531a1.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** --- name: "OPSX: Archive" description: Archive a completed change in the experimental workflow category: Workflow tags: [workflow, archive, experimental] --- Archive a completed change in the experimental workflow. **Input**: Optionally specify a change name after `/opsx:archive` (e.g., `/opsx:archive add-auth`). If omitted, check if it can be inferred from conversation context. If vague or ambiguous you MUST prompt for available changes. **Steps** 1. **If no change name provided, prompt for selection** Run `openspec list --json` to get available changes. Use the **AskUserQuestion tool** to let the user select. Show only active changes (not already archived). Include the schema used for…

### codeql
- **Source:** `local:projects/ACE-Step-1.5/.github/workflows/codeql.yml`
- **Raw:** `[[raw/local/codeql-bd205db36d.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # For most projects, this workflow file will not need changing; you simply need # to commit it to your repository. # # You may wish to alter this file to override the set of languages analyzed, # or to provide custom queries or build logic. # # ******** NOTE ******** # We have attempted to detect the languages in your repository. Please check # the `language` matrix defined below to confirm you have the correct set of # supported CodeQL languages. # name: "CodeQL Advanced" on: push: branches: [ "main" ] pull_request: branches: [ "main" ] schedule: - cron: '26 2 * * 5' jobs: analyze: name: Analyze (${{ matrix.language }}) # Runner size impacts CodeQL analysis time. To learn more, please see:…

- **Collapsed duplicates:** `local:projects/AI-ML/models/ACE-Step-1.5/.github/workflows/codeql.yml`

### docs
- **Source:** `local:projects/ACE-Step-1.5/.github/workflows/docs.yml`
- **Raw:** `[[raw/local/docs-694a1478fa.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: Deploy Documentation on: push: branches: [main] paths: - 'docs/**' - 'package.json' - '.github/workflows/docs.yml' workflow_dispatch: permissions: contents: read pages: write id-token=<redacted> concurrency: group: pages cancel-in-progress: false jobs: build: runs-on: ubuntu-latest steps: - name: Checkout uses: actions/checkout@v4 with: fetch-depth: 0 - name: Setup Node uses: actions/setup-node@v4 with: node-version: 20 - name: Setup Pages uses: actions/configure-pages@v5 - name: Install dependencies run: npm install - name: Build with VitePress run: npm run docs:build - name: Upload artifact uses: actions/upload-pages-artifact@v3 with: path: docs/.vitepress/dist deploy: environment:…

### container
- **Source:** `local:projects/ACE-Step-1.5/.github/workflows/container.yml`
- **Raw:** `[[raw/local/container-96346e1b59.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: Build and Push Container Image on: push: tags: - "v*" workflow_dispatch: inputs: tag: description: "Image tag override (default: git tag or sha)" required: false env: REGISTRY: ghcr.io IMAGE_NAME: ${{ github.repository }} jobs: build-and-push: runs-on: ubuntu-latest permissions: contents: read packages: write steps: - name: Checkout repository uses: actions/checkout@v4 - name: Set up Docker Buildx uses: docker/setup-buildx-action@v3 - name: Log in to Container registry uses: docker/login-action@v3 with: registry: ${{ env.REGISTRY }} username: ${{ github.actor }} password=<redacted> secrets.GITHUB_TOKEN }} - name: Extract metadata (tags, labels) id: meta uses: docker/metadata-action@v5…

### close-inactive-issues
- **Source:** `local:projects/ACE-Step-1.5/.github/workflows/close-inactive-issues.yml`
- **Raw:** `[[raw/local/close-inactive-issues-953e26a26c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: Close inactive issues on: schedule: # Cron is UTC - cron: "15 6 * * *" workflow_dispatch: {} permissions: issues: write jobs: stale: runs-on: ubuntu-latest steps: - name: Mark stale and close uses: actions/stale@v10 with: repo-token=<redacted> github.token }} # "No activity for 28 days" -> mark stale at 21 days, # then close 7 days after being marked stale days-before-issue-stale: 21 days-before-issue-close: 7 days-before-pr-stale: -1 days-before-pr-close: -1 stale-issue-label: stale close-issue-message: > Closing due to 28 days of inactivity. If this is still relevant, please comment to reopen. stale-issue-message: > No activity for 28 days. Closing automatically unless updated. #…

### deploy
- **Source:** `local:projects/personal-site/.github/workflows/deploy.yml`
- **Raw:** `[[raw/local/deploy-ae0e1e0ae8.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: Deploy to GitHub Pages (root) on: push: branches: [main] workflow_dispatch: permissions: contents: read pages: write id-token=<redacted> concurrency: group: pages cancel-in-progress: false jobs: build: runs-on: ubuntu-latest steps: - name: Checkout uses: actions/checkout@v5 - name: Set up Python uses: actions/setup-python@v6 with: python-version: '3.12' - name: Install dependencies run: | pip install mkdocs mkdocs-material mkdocs-rss-plugin mkdocs-minify-plugin pymdown-extensions - name: Build site run: mkdocs build --strict - name: Upload artifact uses: actions/upload-pages-artifact@v3 with: path: site deploy: needs: build runs-on: ubuntu-latest environment: name: github-pages url:…

### deploy
- **Source:** `local:projects/omnisenter-blog/.github/workflows/deploy.yml`
- **Raw:** `[[raw/local/deploy-dc33ddb660.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: Deploy OmniSenter Blog to GitHub Pages on: push: branches: [main] workflow_dispatch: permissions: contents: read pages: write id-token=<redacted> concurrency: group: pages cancel-in-progress: false jobs: build: runs-on: ubuntu-latest steps: - name: Checkout uses: actions/checkout@v5 - name: Set up Python uses: actions/setup-python@v6 with: python-version: '3.12' - name: Install dependencies run: | pip install mkdocs mkdocs-material mkdocs-rss-plugin mkdocs-minify-plugin pymdown-extensions - name: Build site run: mkdocs build --strict - name: Upload artifact uses: actions/upload-pages-artifact@v3 with: path: site deploy: needs: build runs-on: ubuntu-latest environment: name:…

### fossa_scan
- **Source:** `local:projects/nous-girl-agent/vtuber-core/.github/workflows/fossa_scan.yml`
- **Raw:** `[[raw/local/fossa_scan-e7c6c5e37b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: Fossa Scan on: push: branches: - main workflow_dispatch: jobs: fossa-scan: runs-on: ubuntu-latest steps: - uses: actions/checkout@v3 - uses: fossas/fossa-action@main with: api-key=<redacted> secrets.fossaApiKey }}

### codeql
- **Source:** `local:projects/nous-girl-agent/vtuber-core/.github/workflows/codeql.yml`
- **Raw:** `[[raw/local/codeql-2ca9867e4c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # For most projects, this workflow file will not need changing; you simply need # to commit it to your repository. # # You may wish to alter this file to override the set of languages analyzed, # or to provide custom queries or build logic. # # ******** NOTE ******** # We have attempted to detect the languages in your repository. Please check # the `language` matrix defined below to confirm you have the correct set of # supported CodeQL languages. # name: "CodeQL Advanced" on: push: branches: [ "main" ] pull_request: branches: [ "main" ] schedule: - cron: '32 5 * * 6' jobs: analyze: name: Analyze (${{ matrix.language }}) # Runner size impacts CodeQL analysis time. To learn more, please see:…

### long-horizon-ops-blueprint
- **Source:** `local:projects/evolutionary-training/data-sources/discord/hermes-docs/long-horizon-ops-blueprint.txt`
- **Raw:** `[[raw/local/long-horizon-ops-blueprint-47f02162e9.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Long-Horizon Autonomous Operations — Full Blueprint ## What This Covers This is a complete operational blueprint for building **self-sustaining, multi-phase autonomous workflows** in Hermes Agent. It combines every orchestration primitive Hermes has into a single coherent system that can: - Run for days/weeks without manual intervention - Decompose complex objectives into specialist workstreams - Self-monitor, self-heal, and self-report - Continuously operate on schedules and events - Accumulate knowledge over time The five pillars: | Pillar | Tool | Role | |--------|------|------| | **Planning** | `/plan` (writing-plans skill) | Structured spec before execution begins | | **Execution** |…

### close-issue
- **Source:** `local:projects/LLM-Infra/llama.cpp/.github/workflows/close-issue.yml`
- **Raw:** `[[raw/local/close-issue-23a3dbd9db.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: Close inactive issues on: schedule: - cron: "42 0 * * *" # Fine-grant permission # https://docs.github.com/en/actions/security-for-github-actions/security-guides/automatic-token-authentication#modifying-the-permissions-for-the-github_token permissions: issues: write jobs: close-issues: runs-on: ubuntu-slim permissions: issues: write pull-requests: write steps: - uses: actions/stale@v10 with: exempt-issue-labels: "refactoring,help wanted,good first issue,research 🔬,bug,roadmap,security" days-before-issue-stale: 30 days-before-issue-close: 14 stale-issue-label: "stale" close-issue-message: "This issue was closed because it has been inactive for 14 days since being marked as stale."…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp-tq3/.github/workflows/close-issue.yml`, `local:projects/LLM-Infra/llama.cpp-atomic/.github/workflows/close-issue.yml`

### copilot-setup-steps
- **Source:** `local:projects/LLM-Infra/llama.cpp/.github/workflows/copilot-setup-steps.yml`
- **Raw:** `[[raw/local/copilot-setup-steps-f5d5ff3509.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: "Copilot Setup Steps" # Automatically run the setup steps when they are changed to allow for easy validation, and # allow manual testing through the repository's "Actions" tab on: workflow_dispatch: push: paths: - .github/workflows/copilot-setup-steps.yml pull_request: paths: - .github/workflows/copilot-setup-steps.yml jobs: # The job MUST be called `copilot-setup-steps` or it will not be picked up by Copilot. copilot-setup-steps: runs-on: ubuntu-latest # Set the permissions to the lowest permissions possible needed for your steps. # Copilot will be given its own token for its operations. permissions: # If you want to clone the repository as part of your setup steps, for example to…

- **Collapsed duplicates:** `local:projects/LLM-Infra/llama.cpp-tq3/.github/workflows/copilot-setup-steps.yml`, `local:projects/LLM-Infra/llama.cpp-atomic/.github/workflows/copilot-setup-steps.yml`

### .pre-commit-config
- **Source:** `local:projects/omni-fusion/MLLMerging/lmms-eval/.pre-commit-config.yaml`
- **Raw:** `[[raw/local/.pre-commit-config-75629fa6b5.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** repos: - repo: https://github.com/psf/black rev: 23.12.1 hooks: - id: black language_version: python3 args: ["--line-length=240"] - repo: https://github.com/PyCQA/isort rev: 5.13.2 hooks: - id: isort language_version: python3 args: ["--profile", "black"]

### .pre-commit-config
- **Source:** `local:projects/omni-fusion/MLLMerging/VLMEvalKit/.pre-commit-config.yaml`
- **Raw:** `[[raw/local/.pre-commit-config-0520ff2ed3.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** exclude: | (?x)^( scripts/| assets/| vlmeval/config.py | vlmeval/dataset/utils/wemath.py | ) repos: - repo: https://github.com/PyCQA/flake8 rev: 6.1.0 hooks: - id: flake8 args: ["--max-line-length=120", "--ignore=F401,F403,F405,E402,E722,E741,W503,E231,E702"] exclude: ^configs/ - repo: https://github.com/pre-commit/mirrors-yapf rev: v0.30.0 hooks: - id: yapf args: ["--style={column_limit=120}"] - repo: https://github.com/pre-commit/pre-commit-hooks rev: v3.1.0 hooks: - id: trailing-whitespace - id: check-yaml - id: end-of-file-fixer - id: requirements-txt-fixer - id: check-merge-conflict - id: fix-encoding-pragma args: ["--remove"] - id: mixed-line-ending args: ["--fix=lf"]

### .pre-commit-config
- **Source:** `local:projects/omni-fusion/MLLMerging/LLaMA-Factory/.pre-commit-config.yaml`
- **Raw:** `[[raw/local/.pre-commit-config-a22d178808.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** repos: - repo: https://github.com/pre-commit/pre-commit-hooks rev: v5.0.0 hooks: - id: check-ast - id: check-added-large-files args: ['--maxkb=25000'] - id: check-merge-conflict - id: check-yaml - id: debug-statements - id: end-of-file-fixer - id: trailing-whitespace args: [--markdown-linebreak-ext=md] - id: no-commit-to-branch args: ['--branch', 'main'] - repo: https://github.com/asottile/pyupgrade rev: v3.17.0 hooks: - id: pyupgrade args: [--py38-plus] - repo: https://github.com/astral-sh/ruff-pre-commit rev: v0.6.9 hooks: - id: ruff args: [--fix] - id: ruff-format

### .pre-commit-config
- **Source:** `local:projects/omni-fusion/MLLMerging/InternVL/.pre-commit-config.yaml`
- **Raw:** `[[raw/local/.pre-commit-config-ab039efa46.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** exclude: ^internvl_chat_llava/ repos: - repo: https://github.com/PyCQA/flake8 rev: 5.0.4 hooks: - id: flake8 - repo: https://github.com/PyCQA/isort rev: 5.11.5 hooks: - id: isort - repo: https://github.com/pre-commit/pre-commit-hooks rev: v4.3.0 hooks: - id: trailing-whitespace - id: check-yaml - id: end-of-file-fixer - id: requirements-txt-fixer - id: double-quote-string-fixer - id: check-merge-conflict - id: fix-encoding-pragma args: ["--remove"] - id: mixed-line-ending args: ["--fix=lf"] - repo: https://github.com/executablebooks/mdformat rev: 0.7.9 hooks: - id: mdformat args: ["--number"] additional_dependencies: - mdformat-openmmlab - mdformat_frontmatter - linkify-it-py

### winget
- **Source:** `local:projects/LLM-Infra/llama.cpp-tq3/.github/workflows/winget.yml`
- **Raw:** `[[raw/local/winget-34612fafcc.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: Update Winget Package on: workflow_dispatch: # allows manual triggering schedule: - cron: '28 5 * * *' # Update every day at 5:28 UTC jobs: update: name: Update Winget Package runs-on: ubuntu-latest if: github.repository_owner == 'ggml-org' steps: - name: Install cargo binstall uses: cargo-bins/cargo-binstall@268643a6b5ea099f5718ee5cd3ff7dc89a5eb49b - name: Install komac run: | cargo binstall komac@2.15.0 -y - name: Find latest release id: find_latest_release uses: actions/github-script@v8 with: script: | const { data: releases } = await github.rest.repos.listReleases({ owner: context.repo.owner, repo: context.repo.repo, }); const { tag_name: version, assets: assets } =…

### python-lint
- **Source:** `local:projects/LLM-Infra/llama.cpp-tq3/.github/workflows/python-lint.yml`
- **Raw:** `[[raw/local/python-lint-1645a90bfd.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: flake8 Lint on: push: branches: - master paths: [ '.github/workflows/python-lint.yml', '**/*.py' ] pull_request: types: [opened, synchronize, reopened] paths: [ '.github/workflows/python-lint.yml', '**/*.py' ] concurrency: group: ${{ github.workflow }}-${{ github.head_ref && github.ref || github.run_id }} cancel-in-progress: true jobs: flake8-lint: runs-on: ubuntu-slim name: Lint steps: - name: Check out source repository uses: actions/checkout@v6 - name: Set up Python environment uses: actions/setup-python@v6 with: python-version: "3.11" - name: flake8 Lint uses: py-actions/flake8@84ec6726560b6d5bd68f2a5bed83d62b52bb50ba # v2 with: plugins: "flake8-no-print"

### check-vendor
- **Source:** `local:projects/LLM-Infra/llama.cpp-tq3/.github/workflows/check-vendor.yml`
- **Raw:** `[[raw/local/check-vendor-d7947a1a00.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: Check vendor on: workflow_dispatch: # allows manual triggering push: branches: - master paths: [ 'vendor/**', 'scripts/sync_vendor.py' ] pull_request: types: [opened, synchronize, reopened] paths: [ 'vendor/**', 'scripts/sync_vendor.py' ] jobs: check-vendor: runs-on: ubuntu-slim steps: - name: Checkout uses: actions/checkout@v6 with: fetch-depth: 0 - name: Setup Python uses: actions/setup-python@v6 with: python-version: '3.x' - name: Run vendor sync run: | set -euo pipefail python3 scripts/sync_vendor.py - name: Check for changes run: | set -euo pipefail # detect modified or untracked files changed=$(git status --porcelain --untracked-files=all || true) if [ -n "$changed" ]; then echo…

### python-type-check
- **Source:** `local:projects/LLM-Infra/llama.cpp-tq3/.github/workflows/python-type-check.yml`
- **Raw:** `[[raw/local/python-type-check-3561cd1d97.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: Python Type-Check on: push: paths: - '.github/workflows/python-type-check.yml' - 'ty.toml' - '**.py' - '**/requirements*.txt' # - 'pyrightconfig.json' pull_request: paths: - '.github/workflows/python-type-check.yml' - 'ty.toml' - '**.py' - '**/requirements*.txt' # - 'pyrightconfig.json' concurrency: group: ${{ github.workflow }}-${{ github.head_ref && github.ref || github.run_id }} cancel-in-progress: true jobs: python-type-check: runs-on: ubuntu-slim name: python type-check steps: - name: Check out source repository uses: actions/checkout@v6 - name: Set up Python environment uses: actions/setup-python@v6 with: python-version: "3.11" pip-install: -r requirements/requirements-all.txt…

### python-check-requirements
- **Source:** `local:projects/LLM-Infra/llama.cpp-tq3/.github/workflows/python-check-requirements.yml`
- **Raw:** `[[raw/local/python-check-requirements-200b3c5a58.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: Python check requirements.txt on: push: paths: - '.github/workflows/python-check-requirements.yml' - 'scripts/check-requirements.sh' - 'convert*.py' - '**/requirements*.txt' pull_request: paths: - '.github/workflows/python-check-requirements.yml' - 'scripts/check-requirements.sh' - 'convert*.py' - '**/requirements*.txt' concurrency: group: ${{ github.workflow }}-${{ github.head_ref && github.ref || github.run_id }} cancel-in-progress: true jobs: python-check-requirements: runs-on: ubuntu-slim name: check-requirements steps: - name: Check out source repository uses: actions/checkout@v6 - name: Set up Python environment uses: actions/setup-python@v6 with: python-version: "3.11" - name:…

### editorconfig
- **Source:** `local:projects/LLM-Infra/llama.cpp-tq3/.github/workflows/editorconfig.yml`
- **Raw:** `[[raw/local/editorconfig-20c721f67f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: EditorConfig Checker on: workflow_dispatch: # allows manual triggering inputs: create_release: description: 'Create new release' required: true type: boolean push: branches: - master pull_request: branches: - master concurrency: group: ${{ github.workflow }}-${{ github.head_ref && github.ref || github.run_id }} cancel-in-progress: true jobs: editorconfig: runs-on: ubuntu-slim steps: - uses: actions/checkout@v6 - uses: editorconfig-checker/action-editorconfig-checker@840e866d93b8e032123c23bac69dece044d4d84c # v2.2.0 with: version: v3.0.3 - run: editorconfig-checker

### build-msys
- **Source:** `local:projects/LLM-Infra/llama.cpp-tq3/.github/workflows/build-msys.yml`
- **Raw:** `[[raw/local/build-msys-8c0ff02913.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: CI (msys) on: # only manual triggers due to low-importance of the workflows # TODO: for regular runs, provision dedicated self-hosted runners workflow_dispatch: # run once every week schedule: - cron: '0 0 * * 0' concurrency: group: ${{ github.workflow }}-${{ github.head_ref && github.ref || github.run_id }} cancel-in-progress: true env: GGML_NLOOP: 3 GGML_N_THREADS: 1 LLAMA_LOG_COLORS: 1 LLAMA_LOG_PREFIX: 1 LLAMA_LOG_TIMESTAMPS: 1 jobs: windows-msys2: runs-on: windows-2025 strategy: fail-fast: false matrix: include: - { sys: UCRT64, env: ucrt-x86_64, build: Release } - { sys: CLANG64, env: clang-x86_64, build: Release } steps: - name: Clone uses: actions/checkout@v6 #- name: ccache #…

### build-vulkan
- **Source:** `local:projects/LLM-Infra/llama.cpp-tq3/.github/workflows/build-vulkan.yml`
- **Raw:** `[[raw/local/build-vulkan-7bf8784c63.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: CI (vulkan) on: workflow_dispatch: # allows manual triggering push: branches: - master paths: [ '.github/workflows/build-vulkan.yml', '**/CMakeLists.txt', '**/.cmake', '**/*.h', '**/*.hpp', '**/*.c', '**/*.cpp', '**/*.comp', '**/*.glsl' ] pull_request: types: [opened, synchronize, reopened] paths: [ '.github/workflows/build-vulkan.yml', 'ggml/src/ggml-vulkan/**' ] concurrency: group: ${{ github.workflow }}-${{ github.head_ref && github.ref || github.run_id }} cancel-in-progress: true env: GGML_NLOOP: 3 GGML_N_THREADS: 1 LLAMA_LOG_COLORS: 1 LLAMA_LOG_PREFIX: 1 LLAMA_LOG_TIMESTAMPS: 1 jobs: ubuntu-24-vulkan-llvmpipe: runs-on: ubuntu-24.04 steps: - name: Clone id: checkout uses:…

### build-cache
- **Source:** `local:projects/LLM-Infra/llama.cpp-tq3/.github/workflows/build-cache.yml`
- **Raw:** `[[raw/local/build-cache-1f634204dd.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: Build Actions Cache on: workflow_dispatch: # allows manual triggering schedule: - cron: '0 * * * *' concurrency: group: ${{ github.workflow }}-${{ github.head_ref && github.ref || github.run_id }} cancel-in-progress: true jobs: ubuntu-24-vulkan-cache: runs-on: ubuntu-24.04 steps: - name: Clone id: checkout uses: actions/checkout@v6 - name: Get latest Vulkan SDK version id: vulkan_sdk_version run: | echo "VULKAN_SDK_VERSION=$(curl https://vulkan.lunarg.com/sdk/latest/linux.txt)" >> "$GITHUB_ENV" - name: Setup Cache uses: actions/cache@v5 id: cache-sdk with: path: ./vulkan_sdk key: vulkan-sdk-${{ env.VULKAN_SDK_VERSION }}-${{ runner.os }} - name: Setup Vulkan SDK if:…

### build-cann
- **Source:** `local:projects/LLM-Infra/llama.cpp-tq3/.github/workflows/build-cann.yml`
- **Raw:** `[[raw/local/build-cann-da5434edec.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: CI (cann) on: workflow_dispatch: # allows manual triggering push: branches: - master paths: [ '.github/workflows/build-cann.yml', '**/CMakeLists.txt', '**/.cmake', '**/*.h', '**/*.hpp', '**/*.c', '**/*.cpp' ] pull_request: types: [opened, synchronize, reopened] paths: [ '.github/workflows/build-cann.yml', 'ggml/src/ggml-cann/**' ] concurrency: group: ${{ github.workflow }}-${{ github.head_ref && github.ref || github.run_id }} cancel-in-progress: true env: GGML_NLOOP: 3 GGML_N_THREADS: 1 LLAMA_LOG_COLORS: 1 LLAMA_LOG_PREFIX: 1 LLAMA_LOG_TIMESTAMPS: 1 jobs: openEuler-latest-cann: defaults: run: shell: bash -el {0} strategy: matrix: arch: [x86, aarch64] chip_type: ['910b', '310p'] build:…

### .pre-commit-config
- **Source:** `local:projects/Media/video/LTX-Video-original/.pre-commit-config.yaml`
- **Raw:** `[[raw/local/.pre-commit-config-daff5b190f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** repos: - repo: https://github.com/astral-sh/ruff-pre-commit # Ruff version. rev: v0.2.2 hooks: # Run the linter. - id: ruff args: [--fix] # Automatically fix issues if possible. types: [python] # Ensure it only runs on .py files. - repo: https://github.com/psf/black rev: 24.2.0 # Specify the version of Black you want hooks: - id: black name: Black code formatter language_version: python3 # Use the Python version you're targeting (e.g., 3.10)

### pyproject
- **Source:** `local:projects/Media/video/LTX-2/pyproject.toml`
- **Raw:** `[[raw/local/pyproject-cba99248f5.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** [tool.uv.sources] ltx-core = { workspace = true } ltx-pipelines = { workspace = true } [tool.uv.workspace] members = ["packages/*"] [[tool.uv.index]] name = "pypi" url = "https://pypi.org/simple" [dependency-groups] dev = [ "pre-commit>=4.3.0", "ruff>=0.14.3", "pytest~=9.0", ] [tool.ruff] target-version = "py311" line-length = 120 exclude = [] [tool.ruff.lint] select = [ "E", # pycodestyle "F", # pyflakes "W", # pycodestyle (warnings) "I", # isort "N", # pep8-naming "ANN", # flake8-annotations "B", # flake8-bugbear "A", # flake8-builtins "COM", # flake8-commas "C4", # flake8-comprehensions "DTZ", # flake8-datetimez "EXE", # flake8-executable "PIE", # flake8-pie "T20", # flake8-print "PT", #…

### pyproject
- **Source:** `local:projects/Media/video/LTX-2/packages/ltx-pipelines/pyproject.toml`
- **Raw:** `[[raw/local/pyproject-b6ea8c88a0.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** [project] name = "ltx-pipelines" version = "1.0.0" description = "Pipelines implementation for Lightricks' LTX-2 model" readme = "README.md" requires-python = ">=3.10" dependencies = ["ltx-core", "av", "tqdm", "pillow"] [build-system] requires = ["uv_build>=0.9.8,<0.10.0"] build-backend = "uv_build"

### README
- **Source:** `local:projects/Media/video/LTX-2/packages/ltx-pipelines/README.md`
- **Raw:** `[[raw/local/readme-7e14793bd4.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # LTX-2 Pipelines High-level pipeline implementations for generating audio-video content with Lightricks' **LTX-2** model. This package provides ready-to-use pipelines for text-to-video, image-to-video, video-to-video, and keyframe interpolation tasks. Pipelines are built using building blocks from [`ltx-core`](../ltx-core/) (schedulers, guiders, noisers, patchifiers) and handle the complete inference flow including model loading, encoding, decoding, and file I/O. --- ## 📋 Overview LTX-2 Pipelines provides production-ready implementations that abstract away the complexity of the diffusion process, model loading, and memory management. Each pipeline is optimized for specific use cases and…

### README
- **Source:** `local:projects/Media/video/LTX-2/README.md`
- **Raw:** `[[raw/local/readme-fd543a232b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # LTX-2 [![Website](https://img.shields.io/badge/Website-LTX-181717?logo=google-chrome)](https://ltx.io) [![Model](https://img.shields.io/badge/HuggingFace-Model-orange?logo=huggingface)](https://huggingface.co/Lightricks/LTX-2) [![Demo](https://img.shields.io/badge/Demo-Try%20Now-brightgreen?logo=vercel)](https://app.ltx.studio/ltx-2-playground/i2v) [![Paper](https://img.shields.io/badge/Paper-PDF-EC1C24?logo=adobeacrobatreader&logoColor=white)](https://arxiv.org/abs/2601.03233) [![Discord](https://img.shields.io/badge/Join-Discord-5865F2?logo=discord)](https://discord.gg/ltxplatform) **LTX-2** is the first DiT-based audio-video foundation model that contains all core capabilities of…

### .pre-commit-config
- **Source:** `local:projects/LLM-Infra/archive/llama-factory/.pre-commit-config.yaml`
- **Raw:** `[[raw/local/.pre-commit-config-16de3cb487.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** repos: - repo: https://github.com/pre-commit/pre-commit-hooks rev: v6.0.0 hooks: - id: check-ast - id: check-added-large-files args: ['--maxkb=25000'] - id: check-merge-conflict - id: check-yaml - id: debug-statements - id: end-of-file-fixer - id: trailing-whitespace args: [--markdown-linebreak-ext=md] - id: no-commit-to-branch args: ['--branch', 'main'] - repo: https://github.com/asottile/pyupgrade rev: v3.20.0 hooks: - id: pyupgrade args: [--py39-plus] - repo: https://github.com/astral-sh/ruff-pre-commit rev: v0.13.2 hooks: - id: ruff args: [--fix] - id: ruff-format

### tests_cuda
- **Source:** `local:projects/LLM-Infra/archive/llama-factory/.github/workflows/tests_cuda.yml`
- **Raw:** `[[raw/local/tests_cuda-ad4ba8630f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: tests_cuda on: workflow_dispatch: push: branches: - "main" paths: - "**/*.py" - "pyproject.toml" - "Makefile" - ".github/workflows/*.yml" pull_request: branches: - "main" paths: - "**/*.py" - "pyproject.toml" - "Makefile" - ".github/workflows/*.yml" jobs: tests: strategy: fail-fast: false matrix: python: - "3.11" os: - "linux-x86_64-gpu-2" runs-on: ${{ matrix.os }} concurrency: group: ${{ github.workflow }}-${{ github.ref }}-${{ matrix.os }}-${{ matrix.python }} cancel-in-progress: ${{ github.ref != 'refs/heads/main' }} env: HF_HOME: "${{ github.workspace }}/../.runner_cache/huggingface" UV_CACHE_DIR: "${{ github.workspace }}/../.runner_cache/uv" HF_TOKEN=<redacted> secrets.HF_TOKEN…

### tests_npu
- **Source:** `local:projects/LLM-Infra/archive/llama-factory/.github/workflows/tests_npu.yml`
- **Raw:** `[[raw/local/tests_npu-7830fb409f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: tests_npu on: workflow_dispatch: push: branches: - "main" paths: - "**/*.py" - "pyproject.toml" - "Makefile" - ".github/workflows/*.yml" pull_request: branches: - "main" paths: - "**/*.py" - "pyproject.toml" - "Makefile" - ".github/workflows/*.yml" jobs: tests: strategy: fail-fast: false matrix: python: - "3.11" os: - "linux-aarch64-a2-4" pytorch_npu: - "2.7.1" runs-on: ${{ matrix.os }} concurrency: group: ${{ github.workflow }}-${{ github.ref }}-${{ matrix.os }}-${{ matrix.python }} cancel-in-progress: ${{ github.ref != 'refs/heads/main' }} container: image: ascendai/cann:8.3.rc2-910b-ubuntu22.04-py3.11 env: HF_ENDPOINT: https://hf-mirror.com HF_TOKEN=<redacted> secrets.HF_TOKEN }}…

### docs
- **Source:** `local:projects/LLM-Infra/archive/llama-factory/.github/workflows/docs.yml`
- **Raw:** `[[raw/local/docs-2738536579.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: Build and Deploy Sphinx Docs on: push: branches: ["main"] paths: - "docs/**" pull_request: branches: ["main"] paths: - "docs/**" workflow_dispatch: permissions: contents: read pages: write id-token=<redacted> concurrency: group: "pages" cancel-in-progress: false jobs: build: runs-on: ubuntu-latest steps: - uses: actions/checkout@v4 - name: Set up Python uses: actions/setup-python@v5 with: python-version: '3.10' - name: Install dependencies run: | pip install -r docs/requirements.txt - name: Build Sphinx run: | sphinx-build -b html docs/zh docs/_build/html/zh sphinx-build -b html docs/en docs/_build/html/en printf '%s\n' \ '<!DOCTYPE html>' \ '<html>' \ ' <head>' \ ' <meta…

### tests
- **Source:** `local:projects/LLM-Infra/archive/llama-factory/.github/workflows/tests.yml`
- **Raw:** `[[raw/local/tests-ee5a5bdbe5.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: tests on: workflow_dispatch: push: branches: - "main" paths: - "**/*.py" - "pyproject.toml" - "Makefile" - ".github/workflows/*.yml" pull_request: branches: - "main" paths: - "**/*.py" - "pyproject.toml" - "Makefile" - ".github/workflows/*.yml" jobs: tests: strategy: fail-fast: false matrix: python: - "3.11" - "3.12" - "3.13" os: - "ubuntu-latest" - "windows-latest" - "macos-latest" transformers: - "" include: # test backward compatibility - python: "3.11" os: "ubuntu-latest" transformers: "4.51.0" - python: "3.11" os: "ubuntu-latest" transformers: "4.53.0" - python: "3.11" os: "ubuntu-latest" transformers: "4.55.0" runs-on: ${{ matrix.os }} concurrency: group: ${{ github.workflow…

### RUN_TESTS
- **Source:** `local:projects/AI-ML/Senter/agent/RUN_TESTS.md`
- **Raw:** `[[raw/local/run_tests-601577d625.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # 🧪 Test Execution Guide ## Quick Reference ## 📝 What Was Created For You ### 1. **test_telegram_integration.sh** (Main Test Suite) - **20+ automated tests** covering all fixes - **6 test phases**: Code quality, build, config, health, features, manual - **Colored output** with pass/fail indicators - **Detailed summary** at the end ### 2. **quick_test.sh** (Fast Validation) - **4 essential tests** for quick feedback - **<10 second** execution time - Perfect for **pre-commit** checks ### 3. **generate_test_messages.py** (Test Helper) - Generates test messages of various lengths - Tests message splitting functionality - 8 different message types ### 4. **TESTING_TELEGRAM.md** (Complete Guide)…

### README.ru
- **Source:** `local:projects/AI-ML/Senter/agent/README.ru.md`
- **Raw:** `[[raw/local/readme.ru-ff4e949048.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** <p align="center"> <img src="zeroclaw.png" alt="ZeroClaw" width="200" /> </p> <h1 align="center">ZeroClaw 🦀（Русский）</h1> <p align="center"> <strong>Zero overhead. Zero compromise. 100% Rust. 100% Agnostic.</strong> </p> <p align="center"> 🌐 Языки: <a href="README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ru.md">Русский</a> </p> <p align="center"> <a href="bootstrap.sh">Установка в 1 клик</a> | <a href="docs/getting-started/README.md">Быстрый старт</a> | <a href="docs/README.ru.md">Хаб документации</a> | <a href="docs/SUMMARY.md">TOC docs</a> </p> <p align="center"> <strong>Быстрые маршруты:</strong> <a…

### README.ja
- **Source:** `local:projects/AI-ML/Senter/agent/README.ja.md`
- **Raw:** `[[raw/local/readme.ja-681cc3e472.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** <p align="center"> <img src="zeroclaw.png" alt="ZeroClaw" width="200" /> </p> <h1 align="center">ZeroClaw 🦀（日本語）</h1> <p align="center"> <strong>Zero overhead. Zero compromise. 100% Rust. 100% Agnostic.</strong> </p> <p align="center"> 🌐 言語: <a href="README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ru.md">Русский</a> </p> <p align="center"> <a href="bootstrap.sh">ワンクリック導入</a> | <a href="docs/getting-started/README.md">導入ガイド</a> | <a href="docs/README.ja.md">ドキュメントハブ</a> | <a href="docs/SUMMARY.md">Docs TOC</a> </p> <p align="center"> <strong>クイック分流：</strong> <a href="docs/reference/README.md">参照</a> · <a…

### reviewer-playbook
- **Source:** `local:projects/AI-ML/Senter/agent/docs/reviewer-playbook.md`
- **Raw:** `[[raw/local/reviewer-playbook-58084f5bd9.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Reviewer Playbook This playbook is the operational companion to [`docs/pr-workflow.md`](./pr-workflow.md). For broader documentation navigation, use [`docs/README.md`](./README.md). ## 0. Summary - **Purpose:** define a deterministic reviewer operating model that keeps review quality high under heavy PR volume. - **Audience:** maintainers, reviewers, and agent-assisted reviewers. - **Scope:** intake triage, risk-to-depth routing, deep-review checks, automation overrides, and handoff protocol. - **Non-goals:** replacing PR policy authority in `CONTRIBUTING.md` or workflow authority in CI files. --- ## 1. Fast Path by Review Situation Use this section to route quickly before reading full…

### network-deployment
- **Source:** `local:projects/AI-ML/Senter/agent/docs/network-deployment.md`
- **Raw:** `[[raw/local/network-deployment-825bfa0913.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Network Deployment — ZeroClaw on Raspberry Pi and Local Network This document covers deploying ZeroClaw on a Raspberry Pi or other host on your local network, with Telegram and optional webhook channels. --- ## 1. Overview | Mode | Inbound port needed? | Use case | |------|----------------------|----------| | **Telegram polling** | No | ZeroClaw polls Telegram API; works from anywhere | | **Matrix sync (including E2EE)** | No | ZeroClaw syncs via Matrix client API; no inbound webhook required | | **Discord/Slack** | No | Same — outbound only | | **Gateway webhook** | Yes | POST /webhook, WhatsApp, etc. need a public URL | | **Gateway pairing** | Yes | If you pair clients via the gateway |…

### README
- **Source:** `local:projects/AI-ML/Senter/agent/docs/contributing/README.md`
- **Raw:** `[[raw/local/readme-18c68717f7.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Contributing, Review, and CI Docs For contributors, reviewers, and maintainers. ## Core Policies - Contribution guide: [../../CONTRIBUTING.md](../../CONTRIBUTING.md) - PR workflow rules: [../pr-workflow.md](../pr-workflow.md) - Reviewer playbook: [../reviewer-playbook.md](../reviewer-playbook.md) - CI map and ownership: [../ci-map.md](../ci-map.md) - Actions source policy: [../actions-source-policy.md](../actions-source-policy.md) ## Suggested Reading Order 1. `CONTRIBUTING.md` 2. `docs/pr-workflow.md` 3. `docs/reviewer-playbook.md` 4. `docs/ci-map.md`

### ci-map
- **Source:** `local:projects/AI-ML/Senter/agent/docs/ci-map.md`
- **Raw:** `[[raw/local/ci-map-d53e4afc2b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # CI Workflow Map This document explains what each GitHub workflow does, when it runs, and whether it should block merges. For event-by-event delivery behavior across PR, merge, push, and release, see [`.github/workflows/main-branch-flow.md`](../.github/workflows/main-branch-flow.md). ## Merge-Blocking vs Optional Merge-blocking checks should stay small and deterministic. Optional checks are useful for automation and maintenance, but should not block normal development. ### Merge-Blocking - `.github/workflows/ci-run.yml` (`CI`) - Purpose: Rust validation (`cargo fmt --all -- --check`, `cargo clippy --locked --all-targets -- -D clippy::correctness`, strict delta lint gate on changed Rust…

### channels-reference
- **Source:** `local:projects/AI-ML/Senter/agent/docs/channels-reference.md`
- **Raw:** `[[raw/local/channels-reference-cae2c4e1c9.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Channels Reference This document is the canonical reference for channel configuration in ZeroClaw. For encrypted Matrix rooms, also read the dedicated runbook: - [Matrix E2EE Guide](./matrix-e2ee-guide.md) ## Quick Paths - Need a full config reference by channel: jump to [Per-Channel Config Examples](#4-per-channel-config-examples). - Need a no-response diagnosis flow: jump to [Troubleshooting Checklist](#6-troubleshooting-checklist). - Need Matrix encrypted-room help: use [Matrix E2EE Guide](./matrix-e2ee-guide.md). - Need deployment/network assumptions (polling vs webhook): use [Network Deployment](./network-deployment.md). ## FAQ: Matrix setup passes but no reply This is the most…

### SUMMARY
- **Source:** `local:projects/AI-ML/Senter/agent/docs/SUMMARY.md`
- **Raw:** `[[raw/local/summary-40e98ddb8b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ZeroClaw Docs Summary (Unified TOC) This file is the canonical table of contents for the documentation system. Last refreshed: **February 18, 2026**. ## Language Entry - English README: [../README.md](../README.md) - Chinese README: [../README.zh-CN.md](../README.zh-CN.md) - Japanese README: [../README.ja.md](../README.ja.md) - Russian README: [../README.ru.md](../README.ru.md) - English Docs Hub: [README.md](README.md) - Chinese Docs Hub: [README.zh-CN.md](README.zh-CN.md) - Japanese Docs Hub: [README.ja.md](README.ja.md) - Russian Docs Hub: [README.ru.md](README.ru.md) ## Collections ### 1) Getting Started - [getting-started/README.md](getting-started/README.md) -…

### README.zh-CN
- **Source:** `local:projects/AI-ML/Senter/agent/docs/README.zh-CN.md`
- **Raw:** `[[raw/local/readme.zh-cn-7ea8b4ff5b.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ZeroClaw 文档导航（简体中文） 这是文档系统的中文入口页。 最后对齐：**2026-02-18**。 > 说明：命令、配置键、API 路径保持英文；实现细节以英文文档为准。 ## 快速入口 | 我想要… | 建议阅读 | |---|---| | 快速安装并运行 | [../README.zh-CN.md](../README.zh-CN.md) / [../README.md](../README.md) | | 一键安装与初始化 | [one-click-bootstrap.md](one-click-bootstrap.md) | | 按任务找命令 | [commands-reference.md](commands-reference.md) | | 快速查看配置默认值与关键项 | [config-reference.md](config-reference.md) | | 进行日常运维（runbook） | [operations-runbook.md](operations-runbook.md) | | 快速排查安装/运行问题 | [troubleshooting.md](troubleshooting.md) | | 统一目录导航 | [SUMMARY.md](SUMMARY.md) | | 查看 PR/Issue 扫描快照 | [project-triage-snapshot-2026-02-18.md](project-triage-snapshot-2026-02-18.md) | ## 10 秒决策树（先看这个） - 首次安装或快速启动 →…

### README.ru
- **Source:** `local:projects/AI-ML/Senter/agent/docs/README.ru.md`
- **Raw:** `[[raw/local/readme.ru-9e0f3e95c9.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Документация ZeroClaw (Русский) Эта страница — русскоязычная точка входа в документацию. Последняя синхронизация: **2026-02-18**. > Примечание: команды, ключи конфигурации и API-пути сохраняются на английском. Для первоисточника ориентируйтесь на англоязычные документы. ## Быстрые ссылки | Что нужно | Куда смотреть | |---|---| | Быстро установить и запустить | [../README.ru.md](../README.ru.md) / [../README.md](../README.md) | | Установить одной командой | [one-click-bootstrap.md](one-click-bootstrap.md) | | Найти команды по задаче | [commands-reference.md](commands-reference.md) | | Проверить ключи конфигурации и дефолты | [config-reference.md](config-reference.md) | | Операционный…

### README
- **Source:** `local:projects/AI-ML/Senter/agent/docs/README.md`
- **Raw:** `[[raw/local/readme-c2a4205e1f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ZeroClaw Documentation Hub This page is the primary entry point for the documentation system. Last refreshed: **February 18, 2026**. Localized hubs: [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [Русский](README.ru.md). ## Start Here | I want to… | Read this | |---|---| | Install and run ZeroClaw quickly | [README.md (Quick Start)](../README.md#quick-start) | | Bootstrap in one command | [one-click-bootstrap.md](one-click-bootstrap.md) | | Find commands by task | [commands-reference.md](commands-reference.md) | | Check config defaults and keys quickly | [config-reference.md](config-reference.md) | | Operate runtime (day-2 runbook) | [operations-runbook.md](operations-runbook.md) | |…

### README.ja
- **Source:** `local:projects/AI-ML/Senter/agent/docs/README.ja.md`
- **Raw:** `[[raw/local/readme.ja-a0749d4a10.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # ZeroClaw ドキュメントハブ（日本語） このページは日本語のドキュメント入口です。 最終同期日: **2026-02-18**。 > 注: コマンド名・設定キー・API パスは英語のまま記載します。実装の一次情報は英語版ドキュメントを優先してください。 ## すぐに参照したい項目 | やりたいこと | 参照先 | |---|---| | すぐにセットアップしたい | [../README.ja.md](../README.ja.md) / [../README.md](../README.md) | | ワンコマンドで導入したい | [one-click-bootstrap.md](one-click-bootstrap.md) | | コマンドを用途別に確認したい | [commands-reference.md](commands-reference.md) | | 設定キーと既定値を確認したい | [config-reference.md](config-reference.md) | | 日常運用（runbook）を確認したい | [operations-runbook.md](operations-runbook.md) | | インストール/実行トラブルを解決したい | [troubleshooting.md](troubleshooting.md) | | 統合 TOC から探したい | [SUMMARY.md](SUMMARY.md) | | PR/Issue の現状を把握したい |…

### CONTRIBUTING
- **Source:** `local:projects/AI-ML/Senter/agent/CONTRIBUTING.md`
- **Raw:** `[[raw/local/contributing-5ad43ae63c.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Contributing to ZeroClaw Thanks for your interest in contributing to ZeroClaw! This guide will help you get started. ## Development Setup ### Pre-push hook The repo includes a pre-push hook in `.githooks/` that enforces `./scripts/ci/rust_quality_gate.sh` and `cargo test --locked` before every push. Enable it with `git config core.hooksPath .githooks`. For an opt-in strict lint pass during pre-push, set: For an opt-in strict lint delta pass during pre-push (changed Rust lines only), set: For an opt-in docs quality pass during pre-push (changed-line markdown gate), set: For an opt-in docs links pass during pre-push (added-links gate), set: For full CI parity in Docker, run: To skip it…

### .pre-commit-config
- **Source:** `local:projects/LLM-Infra/vllm/.pre-commit-config.yaml`
- **Raw:** `[[raw/local/.pre-commit-config-aabccef17f.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** default_install_hook_types: - pre-commit - commit-msg default_stages: - pre-commit # Run locally - manual # Run in CI exclude: 'vllm/third_party/.*' repos: - repo: https://github.com/astral-sh/ruff-pre-commit rev: v0.14.0 hooks: - id: ruff-check args: [--output-format, github, --fix] - id: ruff-format - repo: https://github.com/crate-ci/typos rev: v1.38.1 hooks: - id: typos args: [--force-exclude] - repo: https://github.com/pre-commit/mirrors-clang-format rev: v21.1.2 hooks: - id: clang-format exclude: 'csrc/(moe/topk_softmax_kernels.cu|quantization/gguf/(ggml-common.h|dequantize.cuh|vecdotq.cuh|mmq.cuh|mmvq.cuh))|vllm/third_party/.*' types_or: [c++, cuda] args: [--style=file, --verbose] -…

### pre-commit
- **Source:** `local:projects/LLM-Infra/vllm/.github/workflows/pre-commit.yml`
- **Raw:** `[[raw/local/pre-commit-f545974d67.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** name: pre-commit on: pull_request: push: branches: [main] concurrency: group: ${{ github.workflow }}-${{ github.ref }} cancel-in-progress: ${{ github.event_name == 'pull_request' }} permissions: contents: read jobs: pre-commit: runs-on: ubuntu-latest steps: - uses: actions/checkout@8e8c483db84b4bee98b60c0593521ed34d9990e8 # v6.0.1 - uses: actions/setup-python@83679a892e2d95755f2dac6acb0bfd1e9ac5d548 # v6.1.0 with: python-version: "3.12" - run: echo "::add-matcher::.github/workflows/matchers/actionlint.json" - run: echo "::add-matcher::.github/workflows/matchers/markdownlint.json" - run: echo "::add-matcher::.github/workflows/matchers/mypy.json" - uses:…

### HUSTLE_BOT_ENHANCED_COMPLETE
- **Source:** `local:docs/HUSTLE_BOT_ENHANCED_COMPLETE.md`
- **Raw:** `[[raw/local/hustle_bot_enhanced_complete-c9b7c63ff0.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # 🚀 HUSTLE BOT - ENHANCED & READY ## ✅ **PROBLEM SOLVED: AUTO-CONTINUE HOOKS** ### **Issue Fixed:** Based on Boris's research, the agent was stopping prematurely during active work. ### **Solution Implemented:** Enhanced auto-continue hooks that prevent premature shutdown and ensure continuous operation. ## 🔧 **Enhanced Features Added:** ### **1. Auto-Continue Pattern** - Detects when meaningful work is in progress - Overrides stop hooks when continuation is beneficial - Boris's proven technique for 5+ hour continuous operation ### **2. Work-in-Progress Detection** - Smart detection of active experiments - Queue system for pending hypotheses - State tracking across restarts ### **3. Stop…

### HUSTLE_BOT_AUTO_CONTINUE_HOOKS
- **Source:** `local:docs/HUSTLE_BOT_AUTO_CONTINUE_HOOKS.md`
- **Raw:** `[[raw/local/hustle_bot_auto_continue_hooks-fdcaec13fd.md]]`
- **Later-version preference:** canonical source selected by latest available modification/update marker.
- **Idea/context:** # Enhanced Hustle Bot - Auto-Continue Hooks Implementation Based on Boris's techniques for continuous operation, this enhanced version includes robust auto-continue hooks to prevent premature shutdown. ## Key Fixes: ### 1. Auto-Continue Pattern ### 2. Stop Hook Override Prevention ### 3. Work-in-Progress Detection ### 4. Graceful Continuation State ## Integration into Hustle Bot ### Enhanced Stop Hook ### Work Queue Management ## Usage ### Start Enhanced Hustle Bot ### Behavior Change **Before Fix:** - Agent stops prematurely during experiments - Work in progress gets abandoned - State lost on premature shutdown - Manual restart required to continue **After Fix:** - Agent detects work in…
