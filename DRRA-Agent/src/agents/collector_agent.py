from __future__ import annotations

import random
from typing import Dict, Any

from .base_agent import BaseAgent


class DataCollectorAgent(BaseAgent):
    """
    Simulated data-collection agent.

    In a full system, this would call tools such as:
      - search APIs
      - weather / news APIs
      - government / NGO feeds

    Here we generate realistic-looking demo data so that the
    multi-agent pipeline can run without external dependencies.
    """

    def run(self, query: str) -> Dict[str, Any]:
        self.logger.log(self.name, f"Collecting data for query: '{query}'")

        # Very rough parsing of disaster type from the query text
        lower_q = query.lower()
        if "flood" in lower_q:
            disaster_type = "flood"
        elif "earthquake" in lower_q:
            disaster_type = "earthquake"
        elif "cyclone" in lower_q or "hurricane" in lower_q:
            disaster_type = "cyclone"
        else:
            disaster_type = "disaster"

        location = query

        # Simulated metrics (0–100 or 1–10 scales)
        people_affected = random.randint(40, 100)
        severity_index = random.randint(6, 10)
        infra_damage_index = random.randint(5, 10)

        raw_reports = [
            "Heavy impact reported in low-lying areas.",
            "Multiple roads blocked due to debris or flooding.",
            "Reports of power cuts and disruption of basic services.",
        ]

        collected = {
            "query": query,
            "location": location,
            "disaster_type": disaster_type,
            "people_affected": people_affected,
            "severity_index": severity_index,
            "infra_damage_index": infra_damage_index,
            "raw_reports": raw_reports,
        }

        self.logger.log(self.name, f"Collected metrics: {collected}")
        return collected
