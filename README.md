# 🌍 DRRA-Agent  
### **AI-Powered Disaster Relief & Resource Allocation Multi-Agent System**  
**by Dinesh Khichar**

---

## 🚀 Overview

**DRRA-Agent** is my end-to-end **multi-agent disaster-response system**, built as my capstone project for the **Kaggle 5-Day AI Agents Intensive**.


![Thumbnail](/DRRA-Agent/Thumbnail.jpg)


This system takes a simple natural-language input like:

> “Severe flood in coastal city of X”

and automatically produces:

- 📝 A **structured disaster relief plan**  
- 🛠 A **practical operational checklist** for responders  
- 🧠 A **memory-backed disaster context** for long-term learning  

This project reflects how real disaster-management systems work - integrating data collection, analysis, planning, and field-level deployment support.

My goal was to build something that feels **real**, **technically deep**, and **designed with care** - something I’d proudly deploy in the real world.

---

# 🌐 Live Kaggle Notebook

The full implementation is available inside:

> **`DRRA-Agent.ipynb`** — with Gemini integration, agent orchestration, memory, logging & full pipeline execution.

---

# 🤖 Why I Built This

During the AI Agents Intensive, I explored:

- Multi-agent collaboration  
- Workflow design  
- Active tool use  
- Memory structures  
- Tracing & observability  
- State management  
- LLM planning using Gemini  

I challenged myself to build something that **goes beyond a toy demonstration**.  
So I chose a real-world domain where intelligent agents can make a meaningful difference:  
🌪 floods,  
🔥 fires,  
🌋 earthquakes,  
💨 cyclones.

DRRA-Agent is the result — a system that can **reason, plan and act** like an emergency-response assistant.

---

# 🧠 System Architecture  

### *DRRA-Agent Pipeline Flowchart*

![DRRA-Agent Flow Chart](/DRRA-Agent/flow_Chart.jpg)

### *My Multi-Agent Pipeline*

```bash

    ------------------------------
    |         User Query         |
    ------------------------------
                    ↓
-------------------------------------------
|        [1] DataCollectorAgent           |
|   • Collects raw disaster information   |
-------------------------------------------
                ↓
------------------------------------------
|       [2] ResourceAnalyzerAgent        |
|   • Computes risk                      |
|   • Identifies priority needs          |
------------------------------------------
                ↓
-------------------------------------------
|   [3] StrategyPlannerAgent (Gemini)     |
|   • Generates expert disaster plan      |
|   • Falls back to template if needed    |
-------------------------------------------
                ↓
-------------------------------------------
|         [4] DeploymentAgent             |
|   • Converts plan → action checklist    |
-------------------------------------------
                ↓
-------------------------------------------
|              [5] MemoryBank             |
|   • Stores long-term disaster context   |
-------------------------------------------


```


### 🔑 Key Concepts I Demonstrated

✔ Multi-agent collaboration  
✔ Sequential reasoning chain  
✔ LLM-powered strategic planning  
✔ Long-term memory storage  
✔ Observability via logging  
✔ Kaggle Secrets for key security  
✔ Deterministic fallback system  
✔ Realistic disaster simulation  

This entire pipeline works reliably even if Gemini is unavailable, thanks to my fallback logic.

---

# 🔥 Highlight Features

## 🧩 **Multi-Agent System (My Core Design)**

I built four independent agents with single responsibilities:

- **Data Collector** → gathers initial metrics  
- **Analyzer** → transforms raw data into structured insights  
- **Planner (Gemini)** → generates a full strategic response  
- **Deployment Agent** → turns the plan into actionable steps  

Clean architecture. Clear flow. Realistic behavior.

---

## ⚙️ **AI-Powered Strategy Planning (Gemini 1.5 Flash)**

My planner agent uses Gemini to generate:

- Situation Summary  
- Priority Needs  
- Immediate Actions (0–24h)  
- Short-Term Actions (1–3 days)  
- Medium-Term Actions (3–7 days)  
- Risks & Assumptions  

This creates **professional-grade relief plans** that feel real.

If Gemini isn’t available, my system **self-recovers** using a structured fallback plan.

---

## 🧾 **Memory Bank (Long-Term Context)**

Each run stores:

```json
{
  "location": "...",
  "severity_level": "high",
  "summary": "Risk 82.5, needs: [...]",
  "timestamp": "..."
}

```

## 🛰️ **Observability (Transparent Logging)**

```bash
[DataCollectorAgent] Collecting data…
[ResourceAnalyzerAgent] Analysis result: ...
[StrategyPlannerAgent] Plan generated using Gemini ✔

```
## 🔐 **Secure Gemini Integration**

I implemented zero-leak Gemini handling:
   - Kaggle Notebook → UserSecretsClient
   - Local Development → GEMINI_API_KEY environment variable.

The system never exposes sensitive keys in code or output.


## 📂 **Project Structure**

```bash
DRRA-Agent/
|
|- notebooks/
|   |- DRRA-Agent.ipynb
|
|- src/
|   |- agents/
|   |   |- base_agent.py
|   |   |- collector_agent.py
|   |   |- analyzer_agent.py
|   |   |- planner_agent.py
|   |   |- deployment_agent.py
|   |
|   |─- tools/
|   |   |- risk_score.py
|   |
|   |- memory/
|   |   |- memory_bank.py
|   |   |- disaster_context.py
|   |
|   |- orchestrator/
|   |   |- drra_agent_system.py
|   |
|   |- utils/
|       |- logger.py
|
|- run.py
|- requirements.txt
|- README.md

```

## 🚀  **Running the Project Locally**
### 1️⃣ Create virtual environment
```bash 
python -m venv venv
venv\Scripts\activate
```
### 2️⃣ Install dependencies
```bash 
pip install -r requirements.txt
```
### 3️⃣ Add your Gemini API key
```bash 
setx GEMINI_API_KEY "your-key"
```
### 4️⃣ Run the agent system
```bash 
python run.py
```
## 📝 **Example Output**
```bash
[DataCollectorAgent] Collecting data…
[ResourceAnalyzerAgent] Analysis: risk 82.5
[StrategyPlannerAgent] Plan generated using Gemini ✔
[DeploymentAgent] Checklist ready
```

## 🎯 **What This Project Demonstrates (My Intent)**

I engineered this project to show:
   - Real multi-agent architecture
   - Coordinated sequential reasoning
   - LLM-backed planning
   - Resilient fallback strategies
   - Long-term memory capability
   - Clean abstractions & maintainable code
   - Reproducibility & clarity
   - Practical application of Google’s Agent concepts

To me, this project is not just a submission — it is a personal milestone in my AI engineering journey.

## 🏆 **Why I Believe This Project Deserves to Win**
```bash
✔️ Strong, meaningful real-world use case

✔️ Uses multiple agent concepts in a clean pipeline

✔️ Demonstrates structured reasoning + memory

✔️ Gemini integration done correctly

✔️ Production-style architecture

✔️ Clear documentation & flow

✔️ Full working notebook

✔️ High effort and polish

✔️ Reliable fallback system

✔️ Realistic outputs
```

I built DRRA-Agent with intention, detail, and care — aiming for something that looks and feels like a professional AI system, not just a capstone demonstration.

## 🙌 **Credits & Acknowledgements**
Huge thanks to: 
  - Google & Kaggle for the amazing Agents Intensive
  - Gemini for powering the planner agent
  - ADK concepts that inspired my architecture
  - Kaggle community for constant motivation

## **👨‍💻 Author**

**✨ Dinesh Khichar**  
AI Engineer • Full Stack MERN Developer • Problem Solver 

- 🔗 **Portfolio:** https://dineshportfolios.site  
- 💼 **GitHub:** https://github.com/dineshkhichar569
- 🔗 **LinkedIn:** https://www.linkedin.com/in/dinesh-khichar-5265b4282
- 📩 **Email:** dinesh.khichar.work@gmail.com  
- 🎓 **B.Tech CSE


