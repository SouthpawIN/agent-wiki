---
name: support-verify
description: Verify a TurboFit install with a real local completion.
version: 1.0.0
author: TurboSouth
license: MIT
metadata:
  hermes:
    tags: [turbofit, support, install, verification]
---

# Support verify

The support loop. Answers "is it working?" with evidence, not with a file listing.

## Procedure

1. **Resolve current source before answering.** TurboFit changes weekly; a cached
   snapshot is a wrong answer waiting to happen.
   ```bash
   gh api repos/SouthpawIN/turbofit/commits/main --jq '.sha[0:12]+" "+.commit.committer.date'
   ```
   Record the SHA in your answer. Every version-sensitive claim cites it.
2. **Inventory the machine** — VRAM, unified pool, host RAM, backend, OS, and the
   engine version TurboFit reports. Never infer a GPU from the container you are in.
3. **Compare** against the current catalog and fit ladders, and label the verdict:
   `measured` · `portable-fit / benchmark required` · `candidate` · `unsupported`
   · `blocked`. An unlabelled guess is the failure mode this skill exists to stop.
4. **Check the five layers, in order**, stopping at the first failure:
   - plugin loaded in a fresh session (`/turbofit` exists);
   - tools registered;
   - `custom:turbofit` → `http://127.0.0.1:8091/v1`, model `auto`;
   - `/v1/models` reports the intended local route;
   - a real completion returns through that same route.
5. **Prove it with a completion**, not a ping:
   ```bash
   curl -s http://127.0.0.1:8091/v1/chat/completions \
     -H 'content-type: application/json' \
     -d '{"model":"auto","max_tokens":16,"messages":[{"role":"user","content":"reply with ok"}]}' \
     | jq -r '.choices[0].message.content'
   ```
   Record model id, quant, context, tok/s, and time-to-first-token with the SHA.
6. **On failure, collect sanitized evidence**: the failing layer, the exact
   command, the error text, hardware, versions — strip paths and hostnames.
7. **Close the loop**: if the defect is reusable, search existing issues/PRs, then
   open a focused PR to `SouthpawIN/turbofit` with a regression test, and report
   the real URL and CI state. No PR from a stale checkout.

## Refusals

- No hosted-API fallback "just to get it working" — TurboFit's failure policy is
  fail closed.
- No claim of a tok/s number that was not measured on that machine.
- Never mark an install verified because the process is running.
