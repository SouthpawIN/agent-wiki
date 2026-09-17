import pytest

from senter_agent.sts import SpeechEvent, accept_input, output_event, to_avatar_state


def test_lifecycle_maps_to_eikon_states():
    assert to_avatar_state(SpeechEvent("listening")) == "thinking"
    assert to_avatar_state(SpeechEvent("speaking")) == "speaking"
    assert to_avatar_state(SpeechEvent("idle")) == "idle"


def test_speech_requires_approval_and_is_bounded():
    with pytest.raises(PermissionError):
        accept_input(SpeechEvent("transcribing", text="hello"))
    assert accept_input(SpeechEvent("transcribing", text="hello", approved=True)) == "hello"
    with pytest.raises(ValueError):
        accept_input(SpeechEvent("transcribing", text="x" * 20_001, approved=True))


def test_output_requires_approval():
    with pytest.raises(PermissionError):
        output_event("hello")
    event = output_event("hello", approved=True)
    assert event.kind == "speaking"
    assert event.approved is True
