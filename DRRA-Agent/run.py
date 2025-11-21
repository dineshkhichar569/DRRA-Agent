from src.orchestrator.drra_agent_system import DRRAAgentSystem
from src.utils.logger import SimpleLogger

logger = SimpleLogger()

system = DRRAAgentSystem(logger=logger, use_gemini=True)

query = "Severe flood in coastal city of X"
result = system.run(query)

print("\n=== RELIEF PLAN ===\n")
print(result["plan"])

print("\n=== CHECKLIST ===\n")
for i, item in enumerate(result["checklist"], start=1):
    print(f"{i}. {item}")

print("\n=== MEMORY SNAPSHOT ===\n")
print(result["memory_snapshot"][-3:])
