"""Tool-free speech adapter for the Senter whole-flow contract.

This module only validates and translates speech lifecycle events. Audio capture,
transcription, and playback are owned by the caller and require user approval.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

State = Literal["idle", "listening", "transcribing", "speaking", "error"]

_ALLOWED: dict[str, str] = {
    "idle": "idle",
    "listening": "thinking",
    "transcribing": "thinking",
    "speaking": "speaking",
    "error": "speaking",
}

@dataclass(frozen=True)
class SpeechEvent:
    kind: State
    text: str = ""
    approved: bool = False


def to_avatar_state(event: SpeechEvent) -> str:
    if event.kind not in _ALLOWED:
        raise ValueError(f"unknown speech state: {event.kind}")
    return _ALLOWED[event.kind]


def accept_input(event: SpeechEvent) -> str:
    """Return text only for approved, bounded speech input."""
    if event.kind != "transcribing":
        raise ValueError("speech input must be transcribing")
    if not event.approved:
        raise PermissionError("user approval required")
    if not event.text or len(event.text) > 20_000:
        raise ValueError("speech text must be 1-20000 characters")
    return event.text


def output_event(text: str, approved: bool = False) -> SpeechEvent:
    if not approved:
        raise PermissionError("user approval required")
    if not text or len(text) > 20_000:
        raise ValueError("speech output must be 1-20000 characters")
    return SpeechEvent("speaking", text=text, approved=True)
