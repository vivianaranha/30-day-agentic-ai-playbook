from __future__ import annotations
import sqlite3
from pathlib import Path

class SQLiteMemory:
    def __init__(self, path: str = "data/memory.db"):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._init()

    def _connect(self):
        return sqlite3.connect(self.path)

    def _init(self):
        with self._connect() as conn:
            conn.execute(
                "CREATE TABLE IF NOT EXISTS memories (id INTEGER PRIMARY KEY, user_id TEXT, key TEXT, value TEXT)"
            )

    def remember(self, user_id: str, key: str, value: str):
        with self._connect() as conn:
            conn.execute(
                "INSERT INTO memories(user_id,key,value) VALUES(?,?,?)",
                (user_id, key, value),
            )

    def recall(self, user_id: str, key: str):
        with self._connect() as conn:
            row = conn.execute(
                "SELECT value FROM memories WHERE user_id=? AND key=? ORDER BY id DESC LIMIT 1",
                (user_id, key),
            ).fetchone()
        return row[0] if row else None
