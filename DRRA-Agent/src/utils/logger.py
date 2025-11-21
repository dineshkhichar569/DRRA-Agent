from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import List, Dict, Any


@dataclass
class LogEvent:
    timestamp: str
    agent: str
    message: str


class SimpleLogger:
    """
    Very small logging helper used by all agents and the orchestrator.

    It:
    - stores events in memory (self.events)
    - prints each message to stdout (for notebook / console visibility)
    """

    def __init__(self) -> None:
        self.events: List[Dict[str, Any]] = []

    def log(self, agent_name: str, message: str) -> None:
        event = LogEvent(
            timestamp=datetime.utcnow().isoformat(),
            agent=agent_name,
            message=message,
        )
        self.events.append(event.__dict__)
        print(f"[{agent_name}] {message}")

    def to_json(self) -> str:
        import json

        return json.dumps(self.events, indent=2)
