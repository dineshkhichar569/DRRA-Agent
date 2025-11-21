from __future__ import annotations

from dataclasses import dataclass


@dataclass
class DisasterContext:
    """
    Compact summary of a single disaster event that can be stored
    in long-term memory.
    """
    location: str
    disaster_type: str
    severity_level: str
    summary: str
    timestamp: str
