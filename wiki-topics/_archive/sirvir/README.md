---
title: sirvir
updated: 2026-08-27
type: topic
repo: https://github.com/SouthpawIN/sirvir
status: active
tags: [repo]
---

# sirvir

> Sirvir — GitHub-current TurboFit support for Hermes; installs TurboFit when missing, compares machine fit, answers Q&A, troubleshoots, and writes tested upstream PRs.

**[Open on GitHub](https://github.com/SouthpawIN/sirvir)** · ACTIVE · last push 2026-08-24

## Facts
- **Language:** Python
- **Stars / forks:** 27 / 5
- **License:** MIT
- **Fork of:** original work
- **Created:** 2026-06-26 · **Last push:** 2026-08-24
- **Open issues:** 1
- **Status:** ACTIVE

## From the README

# Sirvir

**Sirvir is Turbofit customer service.** It helps people install, configure, use, and troubleshoot Turbofit on their own hardware, then turns reusable support findings into tested pull requests for the Turbofit project.

## Scope

Sirvir supports one product and one execution boundary:

- **Product:** [SouthpawIN/turbofit](https://github.com/SouthpawIN/turbofit)
- **Models:** local models served by Turbofit
- **Network:** loopback by default; optional private Tailnet routes backed by the user's machine
- **Failure policy:** fail closed when no local route is viable

Sirvir does not select, configure, benchmark, budget, or fall back to hosted model APIs. It also does not bundle a second copy of Turbofit; the Turbofit plugin remains the sole implementation and source of truth.

## What Sirvir does

1. **Fresh TurboFit awareness:** resolves the current default-branch commit from [SouthpawIN/turbofit](https://github.com/SouthpawIN/turbofit), records the commit SHA, and cites current source instead of trusting a bundled snapshot.
2. **Machine comparison:** inventories the user's hardware and compares it with current catalogs, recipes, backend requirements, and evidence. Results are labeled measured, portable-fit / benchmark required, candidate, unsupported, or blocked.
3. **Turbofit Q&A:** answer first, then cite the source path and commit for version-sensitive facts.
4. **Install and configure:** guides the supported Hermes plugin/setup path and verifies a real local request.
5. **Write TurboFit PRs:** turns reusable support findings into deduplicated, regression-tested pull requests and reports the real PR URL and CI state.

## Install

Sirvir handles Turbofit **install, recommended-model download, and setup**. That is the job. Start Sirvir and ask it to install and verify a real local completion. A bootstrap fallback exists only so Sirvir can talk while the local gateway is coming up; once `http://127.0.0.1:8091/v1/models` answers, all model work stays on Turbofit.

Clone Sirvir and run its bootstrap installer:

```bash
git clone https://github.com/SouthpawIN/sirvir.git
cd sirvir
scripts/install
```

Direct profile install (Hermes 0.20.0 on Windows rejects `SouthpawIN/sirvir` shorthand):

```bash
hermes plugins install --enable https://github.com/SouthpawIN/turbofit.git
hermes profile install https://github.com/SouthpawIN/sirvir.git --name sirvir --yes
```


*…truncated — full README at repo link*


## Archived
Archived 2026-09-02 — absorbed into [[wiki-topics/turbofit/README|turbofit]] by merge-topics.py v1.1.0. Nothing here was deleted or rewritten.
