---
title: turbofit-macos-setup
updated: 2026-08-27
type: skill
tags: [turbofit, macos, apple-silicon, setup]
---

# Skill: Turbofit setup on Apple Silicon (M1 Pro 32GB)

Verified walkthrough, 2026-08-27, on macOS 26.5.2 / M1 Pro / 32 GB unified.

## Steps
1. **Clone** — `git clone https://github.com/SouthpawIN/turbofit.git ~/turbofit`
2. **Python >= 3.10 required.** System python3 is 3.9 → `TypeError: unsupported operand type(s)
   for |` in src/turbofit_runtime/routes.py. Fix: `uv venv .venv --python 3.12` in ~/turbofit,
   `uv pip install --python .venv/bin/python pyyaml cmake`. All scripts via `.venv/bin/python`.
3. **Hardware probe** — fingerprint reports Metal / unified pool; 32 GB total → 24 GB "device"
   after the 8 GiB OS reserve (hardware.py:321).
4. **Configure** — `scripts/turbofit-runtime set auto` → profile `hardware-24gb`,
   rung `local-bonsai-65536`, controller_pending.
   NOTE: `turbofit-runtime-recommend --fit-only` returns `[]` — correct (unmeasured class,
   evidence is Linux-only) but no Apple candidates surfaced.
   KNOWN BUG: 24gb.yaml rungs are all Bonsai (`local-bonsai-*`) though Bonsai was retired
   in v2.4 — Fit List says 24GB+ = Unleashed UD-Q3_K_XL. The rung will be overridden
   manually below.
5. **Build native runtime** — `.venv/bin/python scripts/install-native-runtimes
   --runtime prism-llama.cpp --backend metal` (needs cmake).
6. **Download model** — `.venv/bin/python scripts/download-models.py --group qwen3-8-27b-unleashed`
   → Unleashed UD-Q3_K_XL 13.2 GB (pinned outsourc-e rev 67a9992, sha256 b4c9721a…).
   Group-level only; XXS + mmproj come along.
7. **Controller** — `scripts/turbofit-controller --once`, then `curl 127.0.0.1:8091/v1/models`.

## Pitfalls
- Set `TURBOFIT_MODEL_ROOT` if you don't want models in `~/Models/storage/gguf`.
- Never signal external processes; Turbofit owns only what it launched (SKILL.md safety).
- Apple path in allowed_lineup.py prefers OrcaRouter MLX 6-bit at 32GB — user's curated
  authority is Unleashed UD-Q3_K_XL instead.
