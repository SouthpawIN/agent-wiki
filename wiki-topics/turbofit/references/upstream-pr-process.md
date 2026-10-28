# Upstream PR Process

How research findings become pull requests.

> Grounded in [`roadmap.md`](https://github.com/SouthpawIN/turbofit/tree/main/references/roadmap.md), [`SOUL.md`](https://github.com/SouthpawIN/turbofit/blob/main/skills/turbofit/references/SOUL.md), and `profiles/turbosouth/INSTRUCTIONS.md` in the product repo.

## The research → PR pipeline
1. **Scrape**: `research/model-intel.py` pulls benchmark + hardware intel.
2. **Digest**: `research-report.md` summarizes what changed.
3. **Curate**: `references/` docs are updated with the new evidence.
4. **Decide**: `roadmap.md` writes the concrete PR suggestion (the "pull request" step).

## Who does what
- **TurboSouth** (the bundled customer-service profile) converts recurring, evidence-backed support problems into **PR *suggestions***. It does **not** autonomously publish PRs, manage credentials, kill external GPU processes, or bypass native runtime lifecycle controls.
- A real PR is opened only with human approval, against the exact upstream, with the evidence attached.
- External benchmark results are **discovery evidence only** — a model is promoted to a local runtime profile only after a reproducible local run passes its gates.
