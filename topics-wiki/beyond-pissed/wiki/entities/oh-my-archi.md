---
title: Oh My Archi
created: 2026-09-12
updated: 2026-09-16
type: entity
tags: [tool, plan, pain]
sources: [raw/inbox/2026-09-12.md, raw/inbox/2026-09-15.md, raw/inbox/2026-09-16.md]
confidence: high
---

# Oh My Archi

Chris's Oh My Archi (as he says it, "O-Marki" / "Oh Markey") — an Arch Linux install/automation tool he is setting up on his home lab. It is the first item on his multi-project order of operations, and its USB install failing is what pushed him "beyond pissed."

> So you don't need to do this all in one run, but you want you to be aware of the whole thing It's partly so I can keep track too We are going to be finishing the O-Marki install right now my Home lab is in The grub screen and I have the USB stick plugged into this MacBook. ^[raw/inbox/2026-09-12.md]

## USB Install Failure

On 2026-09-12 the USB install failed. Hermes tried writing the Oh My Archi ISO (`omarchy-4.0.3.iso`) to the raw device `/dev/rdisk4` via a raw Python write meant to bypass SIP, and got a permission error:

    PermissionError: [Errno 1] Operation not permitted: '/dev/rdisk4'

After unplugging and replugging the stick, Chris reported:

> I just unplugged it and plugged it back in again. I bought this for specifically this, and this seems to be going as wrong as a possibly fucking could. I am beyond pissed. ^[raw/inbox/2026-09-12.md]

See [[topics-wiki/beyond-pissed/wiki/queries/write-iso-to-usb|Write ISO to USB Without /dev/rdisk4 Permission Error]] for the flashing question, and [[topics-wiki/beyond-pissed/wiki/concepts/beyond-pissed|Beyond Pissed]] for the emotional state it triggered.

## Serving Models to the MacBook

On 2026-09-15 Chris added the next step for the home lab: he wants to be able to **select which models are served from O'Marki to this MacBook**. The selection mechanism is still open. See [[topics-wiki/beyond-pissed/wiki/concepts/model-selection-routing|Model Selection Routing (O'Marki → MacBook)]].

## Hermes Install Fixed (2026-09-16)

On 2026-09-16 Chris reported the O'Marki Hermes install **fixed**: the venv had been root-owned with Python pointing at `/root/.local/share/uv/...`, and it was rebuilt as `sovthpaw` with Python 3.13, after which `hermes --version` works. ^[raw/inbox/2026-09-16.md]

> FIXED Hermes install on Omarchy: venv was root-owned with Python pointing to `/root/.local/share/uv/...`; rebuilt as sovthpaw with Python 3.13; `hermes --version` works [tool: terminal] ^[raw/inbox/2026-09-16.md]

This is the venv-ownership-root-cause fix actually carried out on the machine — see [[topics-wiki/beyond-pissed/wiki/concepts/venv-ownership-root-cause|Venv Ownership Root Cause]].

## CUDA llama.cpp Runtime Built (2026-09-16)

As step 5 of the same home-lab build, Chris built a **CUDA-enabled llama.cpp runtime** on Omarchy from a **qwen4 fork**: `cmake -B build-cuda -DGGML_CUDA=ON` then build → `llama-server`. That runtime is now the serving layer for the home lab. ^[raw/inbox/2026-09-16.md]

> 5. BUILT CUDA llama.cpp runtime on Omarchy (qwen4 fork): `cmake -B build-cuda -DGGML_CUDA=ON` then build → `llama-serv… ^[raw/inbox/2026-09-16.md]

See also: [[topics-wiki/beyond-pissed/wiki/decisions/multi-project-order-of-operations|Multi-Project Order of Operations]], [[topics-wiki/beyond-pissed/wiki/concepts/chromium-new-tab-homepage|Chromium New Tab / Home Page]]
