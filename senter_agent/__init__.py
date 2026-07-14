"""Senter Agent: interpreter for the markdown-native GOOP language."""

from .factories import Materialized, materialize_all, materialize_context, materialize_proposal
from .gepa import GepaCycle, run_cycle
from .parser import parse_markdown, parse_tree
from .planner import build_plan, plan_dict
from .queue import read_queue, update_status, write_queue
from .runtime import SenterRuntime
from .sts import SpeechEvent, accept_input, output_event, to_avatar_state

__all__ = [
    "GepaCycle",
    "Materialized",
    "SenterRuntime",
    "materialize_all",
    "materialize_context",
    "materialize_proposal",
    "build_plan",
    "parse_markdown",
    "parse_tree",
    "plan_dict",
    "read_queue",
    "run_cycle",
    "update_status",
    "write_queue",
    "SpeechEvent",
    "accept_input",
    "output_event",
    "to_avatar_state",
]

__version__ = "0.2.0"
