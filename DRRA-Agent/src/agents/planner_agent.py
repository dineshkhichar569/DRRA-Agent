from __future__ import annotations

import google.generativeai as genai
import os
from typing import Dict, Any

from .base_agent import BaseAgent


class StrategyPlannerAgent(BaseAgent):
    def __init__(self, name: str, description: str, logger, use_gemini: bool = False):
        super().__init__(name, description, logger)
        self.use_gemini = use_gemini

        # Configure Gemini if enabled
        if self.use_gemini:
            api_key = os.getenv("GEMINI_API_KEY")
            if api_key:
                genai.configure(api_key=api_key)
                self.logger.log(self.name, "Gemini initialized successfully ✔️")
            else:
                self.logger.log(self.name, "❌ GEMINI_API_KEY not found. Using template plan.")

    # ---------- TEMPLATE PLANNING (FALLBACK) ----------
    def _template_plan(self, analysis: Dict[str, Any]) -> str:
        loc = analysis["location"]
        risk = analysis["risk_score"]
        needs = ", ".join(analysis["priority_needs"])

        template = f"""
Disaster Relief Plan for {loc}

1. Summary:
   - Disaster     : {analysis['disaster_type']}
   - Risk Score   : {risk:.1f}
   - Needs        : {needs}

2. Immediate Actions (0–24h)
   - Provide water, food and shelters.
   - Deploy assessment teams.
   - Clear critical roads for emergency movement.

3. Short-Term (1–3 days)
   - Setup medical camps.
   - Establish communication and command center.
   - Evacuate high-risk groups.

4. Medium-Term (3–7 days)
   - Infrastructure damage assessment.
   - Sanitation and hygiene support.
   - Restoration and rehabilitation.

(Limited due to template fallback)
        """.strip()

        return template

    # ---------- GEMINI PLANNING ----------
    def _gemini_plan(self, analysis: Dict[str, Any]) -> str:
        prompt = f"""
You are a professional disaster-response planner.
Create a detailed relief strategy with these required sections:

1. Situation Summary
2. Priority Needs
3. Immediate Actions (0–24 hours)
4. Short-Term Actions (1–3 days)
5. Medium-Term Actions (3–7 days)
6. Risks & Assumptions

Disaster data:
{analysis}

Write clearly and concisely.
        """

        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text

    # ---------- MAIN ENTRY ----------
    def run(self, analysis: Dict[str, Any]) -> str:
        self.logger.log(self.name, "Planning disaster relief strategy...")

        if self.use_gemini:
            try:
                plan = self._gemini_plan(analysis)
                self.logger.log(self.name, "Relief plan generated using Gemini ✔️")
                return plan
            except Exception as e:
                self.logger.log(self.name, f"Gemini failed ({e}). Using template instead.")

        # fallback mode
        plan = self._template_plan(analysis)
        self.logger.log(self.name, "Relief plan generated using template (fallback).")
        return plan
