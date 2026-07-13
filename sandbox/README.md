# Senter Agent Sandbox

This directory defines the safe development boundary for the Senter Agent and its modified Herm frontend.

## Rule

Never modify `~/.hermes/hermes-agent/` or the running Hermes installation. Build and test against clean checkouts in disposable paths or containers.

## Planned layout

```text
sandbox/
├── hermes-agent/       # clean Hermes-Agent checkout
├── herm-frontend/      # clean Herm TUI/frontend checkout when identified
├── hermes-home/        # disposable HERMES_HOME; never host credentials
├── goop/               # mounted/copyable SENTER.md and GOOP objects
└── docker/              # reproducible image and compose definitions
```

## Intended commands

```bash
# Build the standalone Senter Agent package first
python -m pytest
python -m senter_agent.cli . --queue .system/proposals.md

# Later, use a disposable HERMES_HOME and clean source checkouts
HERMES_HOME="$PWD/sandbox/hermes-home" hermes --tui
```

The exact Herm frontend checkout is intentionally not hard-coded until its upstream repository/path is confirmed. The sandbox must remain usable with a local checkout or a pinned Docker build.

## Image variants

The eventual Docker packaging should support a base image plus mounted SENTER.md modules:

```text
senter-agent:base
senter-agent:media
senter-agent:wallet
senter-agent:research
```

Images must not bake in `.env`, OAuth credentials, session databases, or private keys. Inject secrets at runtime through a secret manager or explicitly configured environment mechanism.

## Docker sandbox

The Hermes-Agent checkout is pinned by Git history and the compose wrapper is versioned:

```bash
cd sandbox
docker build -t senter-agent:hermes-sandbox -f Dockerfile .
docker compose up --build
```

The compose service uses a disposable `sandbox/hermes-home/` volume and mounts `sandbox/goop/` read-only. Do not place credentials in either the image or committed files.

The upstream Hermes repository contains the Herm TUI under `ui-tui/`; there is not a separate Herm TUI repository in the checkout. The first sandbox therefore builds Hermes-Agent's own pinned TUI. A custom sidebar/Eikon frontend can be developed in a later branch of this clean checkout.

## Current status

The sandbox contract is documented. Hermes and Herm source checkouts, the owl Eikon frontend, and Docker packaging are the next integration stage; no live Hermes files are modified by this repository.

See [`../SENTER.md`](../SENTER.md) for the language/context contract.
"} r*** Begin Patch 大发游戏官网: invalid input, missing property 'content' in tool call. 天天中彩票中大奖 რადგ. Need call write_file with content. Also current reconcile untracked removed. Do write. 
Need create sandbox README. use proper. 
