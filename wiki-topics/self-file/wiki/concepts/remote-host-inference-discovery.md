---
title: "remote-host inference discovery"
created: 2026-09-14
updated: 2026-09-14
type: concept
tags: [infra, tool, plan, pain]
sources: [raw/inbox/2026-09-13.md, raw/inbox/2026-09-10.md]
confidence: medium
---

# remote-host inference discovery

The practice of locating and bringing up a local-inference server on a remote compute box in Chris's setup — a machine Chris calls the "HP" (with a related `omarchy` machine) — by probing network ports, then waiting for the server to finish loading before it is usable. First documented by Hermes on 2026-09-13. ^[raw/inbox/2026-09-13.md]

This extends the local-model-serving thread into network discovery: the same "test the server, wait for ready" ritual Hermes used on the ornith `mlx_lm` instance (cf. [[wiki-topics/self-file/wiki/entities/ornith-server|ornith server]]) now happens against a box discovered over the network rather than on the local loopback. ^[raw/inbox/2026-09-13.md]

## Discovery sequence — 2026-09-13

- 11:37 — Probed the HP; "Port 22 closed on the HP, but 443 is open." Decided to "check what's there." ^[raw/inbox/2026-09-13.md]
- 12:02 — Tried "some more common Hermes ports, or try the web dashboard"; diagnosed needing "more context about what's running on the HP"; inspected the `omarchy` machine's available ports. ^[raw/inbox/2026-09-13.md]
- 14:58 — Hypothesized the server might be "waiting for pairing or on a non-standard port"; ran a broader scan. ^[raw/inbox/2026-09-13.md]
- 16:32 — Confirmed a server was "running and loading" and waited for it to become ready. ^[raw/inbox/2026-09-13.md]

The run shows a clear progression from port probing (22 closed, 443 open) to guessing common "Hermes ports" and the web dashboard, to a broader scan once pairing/non-standard-port was suspected, ending with a server that loaded and needed to reach a ready state. ^[raw/inbox/2026-09-13.md]

## Pain points

- Port discovery is unreliable: SSH (22) closed and only 443 open, so Hermes guessed at common "Hermes ports" and the web dashboard instead of knowing the real endpoint. ^[raw/inbox/2026-09-13.md]
- Pairing state is a blocker: a running server may be "waiting for pairing," so merely finding a process is not enough — it must be paired and on a known port before it is usable. ^[raw/inbox/2026-09-13.md]

## Relation to the compatibility-check procedure

The local-model-serving compatibility ritual already includes probing endpoints and waiting for readiness; the remote-host step adds network/port discovery and a pairing precondition on top of that. ^[raw/inbox/2026-09-13.md]

Related: [[wiki-topics/self-file/wiki/entities/hermes|Hermes]], [[wiki-topics/self-file/wiki/entities/ornith-server|ornith server]], [[wiki-topics/self-file/wiki/concepts/local-model-serving|local model serving]], and [[wiki-topics/self-file/wiki/concepts/server-compatibility-constraints|server compatibility constraints]].
