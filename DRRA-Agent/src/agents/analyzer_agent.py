from __future__ import annotations

from typing import Dict, Any, Set

from .base_agent import BaseAgent
from ..tools.risk_score import calculate_risk_score


class ResourceAnalyzerAgent(BaseAgent):
    """
    Agent responsible for:
      - computing a risk score
      - inferring priority needs (water, shelter, etc.)
    """

    def run(self, collected: Dict[str, Any]) -> Dict[str, Any]:
        self.logger.log(self.name, "Analyzing collected data...")

        risk = calculate_risk_score(
            people_affected=collected["people_affected"],
            severity_index=collected["severity_index"],
            infra_damage_index=collected["infra_damage_index"],
        )

        needs: Set[str] = set()

        if collected["people_affected"] > 60:
            needs.add("Food supplies")
            needs.add("Clean drinking water")

        if collected["infra_damage_index"] >= 7:
            needs.add("Temporary shelters")
            needs.add("Road clearing equipment")

        if collected["severity_index"] >= 8:
            needs.add("Medical camps")
            needs.add("Emergency rescue teams")

        if not needs:
            needs.add("Basic monitoring")
            needs.add("Local support coordination")

        analysis = {
            "location": collected["location"],
            "disaster_type": collected["disaster_type"],
            "risk_score": risk,
            "priority_needs": sorted(needs),
            "people_affected": collected["people_affected"],
            "severity_index": collected["severity_index"],
            "infra_damage_index": collected["infra_damage_index"],
        }

        self.logger.log(self.name, f"Analysis result: {analysis}")
        return analysis
