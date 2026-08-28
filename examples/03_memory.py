from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from agentic_ai.memory.conversation import ConversationMemory

memory = ConversationMemory(max_messages=4)
memory.add("user", "My preferred deployment is local.")
memory.add("assistant", "Understood.")
print(memory.recent())
