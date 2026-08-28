from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from agentic_ai.agents.super_agent import SuperAgent

agent = SuperAgent()
for query in [
    "Find my best sales opportunities",
    "Which support tickets need escalation?",
    "What is our travel reimbursement policy?",
]:
    print("\nQUERY:", query)
    print(agent.run(query).answer)
