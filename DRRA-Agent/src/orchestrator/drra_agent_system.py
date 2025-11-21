from __future__ import annotations

from datetime import datetime
from typing import Dict, Any, List

from ..agents.collector_agent import DataCollectorAgent
from ..agents.analyzer_agent import ResourceAnalyzerAgent
from ..agents.planner_agent import StrategyPlannerAgent
from ..agents.deployment_agent import DeploymentAgent
from ..memory.disaster_context import DisasterContext
from ..memory.memory_bank import add_disaster_to_memory, load_memory
from ..utils.logger import SimpleLogger


class DRRAAgentSystem:
    """
    High-level orchestrator that wires all agents together
    into a single multi-agent workflow.
    """

    def __init__(self, logger: SimpleLogger | None = None, use_gemini: bool = False):
        self.logger = logger or SimpleLogger()

        self.collector = DataCollectorAgent(
            name="DataCollectorAgent",
            description="Collects structured disaster information.",
            logger=self.logger,
        )
        self.analyzer = ResourceAnalyzerAgent(
            name="ResourceAnalyzerAgent",
            description="Analyzes risk and priority needs.",
            logger=self.logger,
        )
        self.planner = StrategyPlannerAgent(
            name="StrategyPlannerAgent",
            description="Generates a disaster relief plan.",
            logger=self.logger,
            use_gemini=True,
        )
        self.deployer = DeploymentAgent(
            name="DeploymentAgent",
            description="Converts plan into actionable checklist.",
            logger=self.logger,
        )

    # ---------------- Pipeline ---------------- #

    def run(self, query: str) -> Dict[str, Any]:
        """
        Execute the full multi-agent pipeline for a given
        disaster description string.
        """
        self.logger.log("DRRAAgentSystem", "=== Starting full pipeline ===")

        collected = self.collector.run(query)
        analysis = self.analyzer.run(collected)
        plan = self.planner.run(analysis)
        checklist = self.deployer.run(plan)

        # Persist summary to long-term memory
        ctx = DisasterContext(
            location=analysis["location"],
            disaster_type=analysis["disaster_type"],
            severity_level="high" if analysis["risk_score"] > 60 else "moderate",
            summary=f"Risk {analysis['risk_score']:.1f}, needs: {analysis['priority_needs']}",
            timestamp=datetime.utcnow().isoformat(),
        )
        add_disaster_to_memory(ctx)
        self.logger.log(
            "DRRAAgentSystem", "Disaster context saved to long-term memory."
        )

        result: Dict[str, Any] = {
            "collected": collected,
            "analysis": analysis,
            "plan": plan,
            "checklist": checklist,
            "logs": self.logger.events,
            "memory_snapshot": load_memory(),
        }

        self.logger.log("DRRAAgentSystem", "=== Pipeline completed ===")
        return result


# Optional: CLI demo for local runs (not needed on Kaggle)
def evaluate_plan(analysis: Dict[str, Any], checklist: List[str]) -> Dict[str, Any]:
    """
    Simple heuristic evaluation used in the notebook:
      - base score from risk
      - bonus for number of checklist items
    """
    risk_component = min(analysis["risk_score"], 100.0)
    checklist_component = min(len(checklist) * 5, 30)
    total = min(risk_component * 0.7 + checklist_component, 100.0)
    return {
        "risk_component": risk_component,
        "checklist_component": checklist_component,
        "total_score": total,
    }


if __name__ == "__main__":  # pragma: no cover
    system = DRRAAgentSystem()
    query = "Severe flood in coastal city of X"
    results = system.run(query)

    print("\n=== RELIEF PLAN ===\n")
    print(results["plan"])

    print("\n=== CHECKLIST ===\n")
    for i, item in enumerate(results["checklist"], start=1):
        print(f"{i}. {item}")

    print("\n=== EVALUATION ===\n")
    print(evaluate_plan(results["analysis"], results["checklist"]))
