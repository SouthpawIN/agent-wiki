#!/usr/bin/env python3
"""Transcription stage for Cutroom.

Deliberately thin: it shells out to a whisper.cpp build and normalises the JSON
it writes. The interesting logic - what counts as a topic, what counts as a hook -
lives downstream in `cutroom.py`, where it can be tested without weights.

Two modes, because the recordings do not live here:
    local   run whisper-cli against a file already on this machine
    remote run it on another tailnet box (omarchy) and pull the JSON back

Usage:
    python transcribe.py <media> [--host omarchy] [--bin whisper-cli] \\
        [--model large-v3-turbo] [--model-dir DIR] [--out DIR]
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
from pathlib import Path


class TranscriptionError(RuntimeError):
    """Raised when the whisper build is missing or the run fails."""


def resolve_binary(explicit: str | None = None, *, which=shutil.which) -> str:
    """Find a whisper binary, or explain how to install one."""
    for candidate in ([explicit] if explicit else []) + [
        "whisper-cli", "whisper.cpp", "main", "whisper",
    ]:
        if candidate and which(candidate):
            return candidate
    raise TranscriptionError(
        "no whisper binary found; pass --bin /path/to/whisper-cli, or install "
        "whisper.cpp (git clone --depth 1 https://github.com/ggerganov/whisper.cpp)"
    )


def remote_command(host: str, command: str, *, socket: str | None = None) -> list[str]:
    """Build a `tailscale ssh` invocation. The socket matters on this box."""
    base = ["tailscale"]
    if socket:
        base += ["--socket", socket]
    return base + ["ssh", host, command]


def build_command(binary: str, media: str, output: str, *, model: str,
                  threads: int | None = None, word_timestamps: bool = True) -> list[str]:
    cmd = [binary, "-m", model, "-f", media, "-oj", "--output-txt"]
    if word_timestamps:
        cmd += ["-owts"]
    if threads:
        cmd += ["-t", str(threads)]
    cmd += ["-of", output]
    return cmd


def parse_transcript(raw: dict) -> dict:
    """Normalise whisper.cpp JSON into {words:[{start,end,text}], text}."""
    segments = raw.get("transcription")
    if segments is None:
        segments = raw.get("segments") or []
    words: list[dict] = []
    lines: list[str] = []
    for segment in segments:
        text = str(segment.get("text", "")).strip()
        lines.append(text)
        tokens = segment.get("tokens")
        if tokens:
            for token in tokens:
                piece = str(token.get("text", "")).strip()
                if not piece:
                    continue
                offsets = token.get("offsets") or {}
                words.append({
                    "start": round(float(offsets.get("from", 0)) / 1000.0, 3),
                "end": round(float(offsets.get("to", 0)) / 1000.0, 3),
                "text": piece,
            })
        else:
            offsets = segment.get("offsets") or {}
            words.append({
                "start": round(float(offsets.get("from", 0)) / 1000.0, 3),
            "end": round(float(offsets.get("to", 0)) / 1000.0, 3),
            "text": text,
        })
    return {"words": words, "text": " ".join(line for line in lines if line)}


def transcribe(
    media: str | Path,
    *,
    host: str | None = None,
    binary: str | None = None,
    model: str = "models/ggml-large-v3-turbo.bin",
    output: str | None = None,
    timeout: int = 900,
    socket: str | None = None,
    runner=None,
) -> dict:
    """Transcribe media to {words, text}. Local by default, SSH with --host."""
    execute = runner or _run
    name = resolve_binary(binary)
    target = output or f"work/{Path(media).stem}"

    if host:
        remote = remote_command(
            host,
            f"{name} -m {model} -f {media} -oj --output-txt -owts -of {target}",
            socket=socket,
        )
        result = execute(remote, timeout=timeout)
    else:
        result = execute(build_command(name, str(media), model=model), timeout=timeout)

    if result.returncode != 0:
        raise TranscriptionError(
            (result.stderr.strip() or f"whisper failed on {media}").splitlines()[-1]
        )
    return {"ok": True, "output": target}
