from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from agentic_ai.agents.base import BaseAgent

agent = BaseAgent()
print(agent.run("Help me understand agentic AI"))
