from agentic_ai.memory.conversation import ConversationMemory
from agentic_ai.memory.sqlite_memory import SQLiteMemory

def test_bounded_memory():
    m = ConversationMemory(max_messages=2)
    m.add("user", "one")
    m.add("assistant", "two")
    m.add("user", "three")
    assert len(m.recent()) == 2
    assert m.recent()[0]["content"] == "two"

def test_sqlite_memory(tmp_path):
    db = SQLiteMemory(str(tmp_path / "memory.db"))
    db.remember("u1", "preference", "local models")
    assert db.recall("u1", "preference") == "local models"
