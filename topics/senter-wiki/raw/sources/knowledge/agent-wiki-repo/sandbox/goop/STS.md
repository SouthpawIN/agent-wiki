# Auxiliary STS

Speech-to-text (STT) and text-to-speech (TTS) are auxiliary adapters in the Senter flow, not tool runners.

- Contract: `STS_CONFIG.json`
- Runtime adapter: `senter_agent/sts.py`
- Lifecycle: listening/transcribing → Eikon `thinking`; speaking → `speaking`; idle → `idle`.
- Audio capture and playback remain caller-owned and require user approval.
- The adapter has no shell, ADB, network, host-tool, or credential access.

The existing Hermes auxiliary client remains the provider-facing integration point; this contract prevents speech state from becoming an execution path.
