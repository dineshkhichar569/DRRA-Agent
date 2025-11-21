from __future__ import annotations

from typing import List

from .base_agent import BaseAgent


class DeploymentAgent(BaseAgent):
    """
    Agent that converts a textual plan into a simple, actionable checklist.

    In a more advanced system this could:
      - interface with ticketing systems,
      - schedule tasks,
      - send notifications.
    """

    def run(self, plan: str) -> List[str]:
        self.logger.log(self.name, "Converting relief plan into checklist...")

        # For the demo we generate a standard checklist.
        checklist = [
            "Deploy assessment teams to worst-affected localities.",
            "Distribute clean drinking water and food packets.",
            "Set up temporary shelters in safe public buildings.",
            "Arrange medical camps and first-aid stations.",
            "Coordinate road clearing and power restoration with authorities.",
            "Establish a central command center for coordination.",
            "Schedule regular situation reports (every 6–12 hours).",
        ]

        self.logger.log(self.name, f"Generated checklist with {len(checklist)} items.")
        return checklist
