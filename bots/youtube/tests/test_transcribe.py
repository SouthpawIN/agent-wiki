"""Transcription stage: parsing and the refusal path when no whisper is built."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parents[1] / "scripts"))

import transcribe as t  # noqa: E402


FIXTURE = {
    "transcription": [
        {"text": " I think local models are the answer here",
         "offsets": {"from": 100, "to": 2600}},
        {"text": " and that is why I moved everything to my own box",
         "offsets": {"from": 2600, "to": 5200}},
    ]
}


def test_parse_transcript_splits_segments(tmp_path: Path) -> None:
    parsed = t.parse_transcript(FIXTURE)
    assert parsed["text"].startswith("I think local models")
    assert len(parsed["words"]) == 2
    assert parsed["words"][0] == {"start": 0.1, "end": 2.6,
                           "text": "I think local models are the answer here"}
    assert parsed["words"][1]["start"] == 2.6


def test_parse_transcript_accepts_word_tokens() -> None:
    raw = {"transcription": [{"text": "alpha beta", "offsets": {"from": 0, "to": 500},
                                 "tokens": [{"text": " alpha", "offsets": {"from": 0, "to": 200}},
                                          {"text": " beta", "offsets": {"from": 200, "to": 500}}]}]}
    parsed = t.parse_transcript(raw)
    assert [w["text"] for w in parsed["words"]] == ["alpha", "beta"]
    assert parsed["words"][1]["end"] == 0.5


def test_empty_transcript_is_not_an_error() -> None:
    assert t.parse_transcript({}) == {"words": [], "text": ""}


def test_transcribe_without_a_whisper_build_reports_it() -> None:
    with pytest.raises(t.TranscriptionError) as caught:
        t.resolve_binary(None, which=lambda _name: None)
    assert "install whisper.cpp" in str(caught.value)


def test_command_shape_is_what_the_engine_expects() -> None:
    cmd = t.build_command("whisper-cli", "session.mkv", "out/session", model="models/large.bin")
    assert cmd[:4] == ["whisper-cli", "-m", "models/large.bin", "-f"]
    assert "-owts" in cmd and "--output-txt" in cmd
    assert cmd[cmd.index("-of") + 1] == "out/session"
