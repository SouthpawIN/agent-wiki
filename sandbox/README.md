# Senter Agent Sandbox

This directory defines the safe development boundary for the Senter Agent and its modified Herm frontend.

## Rule

Never modify `~/.hermes/hermes-agent/` or the running Hermes installation. Build and test against clean checkouts in disposable paths or containers.

## Planned layout

```text
sandbox/
├── hermes-agent/       # clean Hermes-Agent checkout
├── herm-sovth/         # clean Southpaw Herm TUI/OpenTUI checkout
├── hermes-android/     # clean Android frontend checkout
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

The sandbox pins three clean checkouts as Git submodules: upstream Hermes-Agent, Southpaw's `herm-sovth` OpenTUI frontend, and `hermes-android`. The main Hermes-Agent checkout also contains the upstream `ui-tui/` frontend. No checkout is the live installation.

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
docker compose build
docker compose run --rm senter-agent hermes --help
```

The compose service uses a disposable `sandbox/hermes-home/` volume and mounts `sandbox/goop/` read-only. Preconfigured profiles live under `goop/profiles/{base,media,wallet,research}/`; set `GOOP_PROFILE=media` to expose the selected profile path through `SENTER_GOOP_PROFILE`. Do not place credentials in either the image or committed files.

The upstream Hermes repository contains the current TUI under `ui-tui/`; the Southpaw `herm-sovth` checkout is also present for the modified frontend work. The Android checkout is present for the side-button STS and canvas surface. The Compose build uses the pinned `sandbox/hermes-agent/Dockerfile`; the root `sandbox/Dockerfile` is reserved for a future derived image once the base image is published.

The Android checkout currently contains a prebuilt APK and Termux setup rather than modifiable Android source. `goop/ANDROID_SURFACE.json` is therefore the implementation contract for the future source checkout, and `validate_android_surface.py` checks the gesture, canvas, block, and permission boundaries without claiming that the APK implements them yet.

## Optional Android emulator sidecar

The sandbox includes an opt-in emulator service based on `halimqarroum/docker-android:api-33`. It is disabled by default and passes through `/dev/kvm` only when explicitly enabled:

```bash
docker compose --profile android up android
adb connect 127.0.0.1:5555
```

The service exposes ADB on `5555` and persists the disposable `android-home/` directory at the image's documented `/data` path; that directory is ignored by Git. The selected image is an x86_64 emulator and requires at least 4 GB RAM and roughly 8 GB disk for API 33. This is an emulator/test device, not the physical-phone STS client. The bridge is explicitly disabled by default; when enabled later, its endpoint is `android:5555` on the Compose network. Senter must use a future controlled Android bridge; the sidecar does not grant unrestricted phone control to the agent.

## Current status

The sandbox contract is documented. Hermes and Herm source checkouts, the accepted owl player reference, its validation script, and Docker packaging are in place; no live Hermes files are modified by this repository.

See [`../SENTER.md`](../SENTER.md) for the language/context contract.
"} r*** Begin Patch 大发游戏官网: invalid input, missing property 'content' in tool call. 天天中彩票中大奖 რადგ. Need call write_file with content. Also current reconcile untracked removed. Do write. 
Need create sandbox README. use proper. 
