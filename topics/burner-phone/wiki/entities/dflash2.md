---
title: DFlash2
created: 2026-09-07
updated: 2026-09-15
type: entities
tags:
  - tool
sources:
  - raw/inbox/2026-09-07.md
  - raw/inbox/2026-09-15.md
confidence: medium
---

# DFlash2

DFlash2 is a **speculative decoder** artifact downloaded for use with Ornith. ^[raw/inbox/2026-09-07.md]

## What is known

- Chris said: *"let's find ornith 1.5 35A3B for this device AND the DFlash2"* ^[raw/inbox/2026-09-07.md]
- Hermes noted: *"Try to find/build a DFlash2 speculative decoder for Ornith"* ^[raw/inbox/2026-09-07.md]
- Hermes later reported: *"DFlash2 downloaded (1GB)."* ^[raw/inbox/2026-09-07.md]
- Download size: **1GB** speculative-decoder artifact. ^[raw/inbox/2026-09-07.md]
- No verified integration result yet with ornith 1.5 35A3B or 131K context. ^[raw/inbox/2026-09-07.md]
- Repeated Hermes attempts to "test/build DFlash2 speculative decoder for Ornith" were paired with Ornith-only 131K notes; DFlash2-enabled testing is still absent from verified state. ^[raw/inbox/2026-09-07.md]

## Integration flags

- DFlash2 is a **draft model for speculative decoding** and must be paired with the full model via `--spec-draft-model`; setup runs both models together. ^[raw/inbox/2026-09-15.md]
- DFlash2 needs the `--ctx-other` flag. ^[raw/inbox/2026-09-15.md]
- DFlash2 is also specified via `--hf-repo-draft` to point at the draft model. ^[raw/inbox/2026-09-15.md]
- The original working service uses a **different llama.cpp build (qwen4, v0.4.0-dev)** with different flags (`-ngl`, `-c`, `-t`); the plan was to revert to that working configuration and fix DFlash2 there. ^[raw/inbox/2026-09-15.md]
- Integration still **unverified**: a first DFlash2 test returned an empty response because its reasoning consumed the context budget. ^[raw/inbox/2026-09-15.md]
- Operational note (2026-09-15): the working service DFlash2 runs against is the qwen4 v0.4.0-dev build that lived in **`/tmp`**, which was **wiped on restart**, losing the build; the plan was to locate persistent runtimes and rebuild. ^[raw/inbox/2026-09-15.md]

## Plans

- Find/build a DFlash2 speculative decoder for Ornith. ^[raw/inbox/2026-09-07.md]
- Test if 131K context works with Ornith and DFlash2 enabled; the 131K note is paired with Ornith only. ^[raw/inbox/2026-09-07.md]

## Open questions

- Whether the downloaded DFlash2 build is compatible with the burner-phone device's runtime/hardware.
- Whether DFlash2 works with ornith 1.5 35A3B specifically.
- Whether 131K context was tested with DFlash2 enabled; the 131K note is paired with Ornith only. ^[raw/inbox/2026-09-07.md]

## Related

- [[topics/burner-phone/wiki/queries/find-ornith-1.5-35a3b-for-device-and-dflash2|Find ornith 1.5 35A3B for device and DFlash2]]
- [[topics/burner-phone/wiki/entities/ornith|Ornith]]
- [[topics/burner-phone/wiki/entities/ornith-config-state|Ornith config and port state]]
