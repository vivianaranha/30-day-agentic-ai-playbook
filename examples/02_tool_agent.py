from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from agentic_ai.agents.tool_agent import ToolAgent

agent = ToolAgent()
print(agent.run("Calculate 12 * 7").answer)
