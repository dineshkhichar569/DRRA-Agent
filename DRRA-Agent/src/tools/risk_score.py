from __future__ import annotations


def calculate_risk_score(
    people_affected: int,
    severity_index: int,
    infra_damage_index: int,
) -> float:
    """
    Simple demo risk model used by the ResourceAnalyzerAgent.

    Inputs (all on 0-100 or 1-10 scales):
      - people_affected: 0–100 (normalized)
      - severity_index: 1–10
      - infra_damage_index: 1–10

    Output:
      - risk score in the range 0–100
    """
    score = (people_affected * 0.5) + (severity_index * 3.0) + (infra_damage_index * 2.5)
    return float(min(score, 100.0))
