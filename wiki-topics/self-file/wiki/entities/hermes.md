---
title: "Hermes"
created: 2026-09-07
updated: 2026-09-15
type: entity
tags: [person, tool, bot, plan]
sources: [raw/inbox/2026-09-07.md, raw/inbox/2026-09-08.md, raw/inbox/2026-09-09.md, raw/inbox/2026-09-10.md, raw/inbox/2026-09-13.md, raw/inbox/2026-09-15.md]
confidence: high
---

# Hermes

The AI agent framework Chris uses. On 2026-09-07 it surfaced the server-testing intent and reported the background process exit for the ornith server. ^[raw/inbox/2026-09-07.md] On 2026-09-08 it debugged a stale-server/token-desync issue during a `--new-token` restart, reporting curl input-waiting syntax problems, PID discrepancies (63522 stale, 63983 unexpected, 64361 fresh), and testing the `/file` endpoint with `.system-live.json` after inspecting the vault-live.html `loadLive` function. ^[raw/inbox/2026-09-08.md]

## 2026-09-08 operational behavior

Hermes reported that both servers were running and the initial problem was that curl was waiting for input, producing empty model-endpoint responses. ^[raw/inbox/2026-09-08.md] It inspected the vault-live.html `loadLive` function to compare expectations against server output. ^[raw/inbox/2026-09-08.md] A stale PID 63522 held the old token; Hermes started a fresh server PID 64361 with patched code and new token. ^[raw/inbox/2026-09-08.md]

## 2026-09-07 operational behavior

Hermes moved ports repeatedly during one local-server evaluation run, switched targets after Colibri started downloading, and finished by saying "Colibri requires custom Maple MLX code (not standard mlx_lm)." ^[raw/inbox/2026-09-07.md] Hermes also asked, "Would you like me to help you with the exact config changes you need to make, or restart the Ornith server once you've updated the config?" ^[raw/inbox/2026-09-07.md]

## 2026-09-09 operational behavior

Hermes observed a stale watch process overwriting files with old data and decided to kill it and run a fresh scan to restore correct state. ^[raw/inbox/2026-09-09.md] The fresh scan verified JSON correctness at 10:18, and at 10:29 Hermes restarted the watch process with fixed code and checked remote-push capability. ^[raw/inbox/2026-09-10.md] This marks the completion of the stale-process-overwrite cycle from 09-09.

## 2026-09-13 operational behavior

Hermes discovered and brought up a remote inference server on a box Chris calls the "HP" (with a related `omarchy` machine). It probed ports (22 closed, 443 open), guessed common "Hermes ports" and the web dashboard, then — suspecting a server "waiting for pairing or on a non-standard port" — ran a broader scan and confirmed a server "running and loading," waiting for it to become ready. ^[raw/inbox/2026-09-13.md]

## 2026-09-10 operational behavior

While investigating a `--backup` flag, Hermes reasoned that `updates.pre_update_backup: False` "just means the backup step records `ok: false`, and the update should continue." ^[raw/inbox/2026-09-10.md]

## 2026-09-15 operational behavior

Hermes ran a long inference session that exposed GPU memory contention and restart churn: at 10:12 it found a "Flash Next server (PID 1069592) eating 16 GB on GPU 1," killed it and a new OOM server, and restarted. ^[raw/inbox/2026-09-15.md] At 11:09 it logged that a prior background process had "exited code 7 (connection refused)" while "Omarchy's server was restarting," then reported the stack healthy — "nginx is up on 8080, model server healthy on 8100, Tailscale reachable from Mac." ^[raw/inbox/2026-09-15.md] At 13:15 it diagnosed "Mac's prompt cache is full from accumulated test history" and restarted fresh; at 13:21–13:22 it confirmed all background processes complete and that an earlier failure was "the earlier test before ctx was corrected to 65536. All later tests passed." ^[raw/inbox/2026-09-15.md] At 11:23 it started a download and said it would "also download for Omarchy and build the plugin UI" — a plugin-UI build plan for the remote inference stack. ^[raw/inbox/2026-09-15.md] At 16:28 it reported the session's final state stable: "All background processes complete. Current state stable. Waiting for your next instructions." ^[raw/inbox/2026-09-15.md]

Related: [[wiki-topics/self-file/wiki/concepts/local-model-serving|local model serving]], [[wiki-topics/self-file/wiki/entities/colibri|Colibri]], [[wiki-topics/self-file/wiki/entities/ornith-server|ornith server]], [[wiki-topics/self-file/wiki/concepts/server-compatibility-constraints|server compatibility constraints]], [[wiki-topics/self-file/wiki/concepts/remote-host-inference-discovery|remote-host inference discovery]], and [[wiki-topics/self-file/wiki/decisions/watch-process-overwrite-2026-09-09|Watch process data-overwrite restart — 2026-09-09]].
