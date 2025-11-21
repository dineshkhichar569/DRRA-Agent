from __future__ import annotations

from typing import Any

from ..utils.logger import SimpleLogger


class BaseAgent:
    """
    Minimal base class that all concrete agents inherit from.

    Each agent has:
      - name
      - description
      - a reference to the shared logger
    """

    def __init__(self, name: str, description: str, logger: SimpleLogger) -> None:
        self.name = name
        self.description = description
        self.logger = logger

    def run(self, *args: Any, **kwargs: Any) -> Any:  # pragma: no cover - abstract
        raise NotImplementedError("Subclasses must implement run().")
