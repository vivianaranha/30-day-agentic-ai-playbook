from __future__ import annotations

class ConversationMemory:
    def __init__(self, max_messages: int = 10):
        self.max_messages = max_messages
        self.messages: list[dict[str, str]] = []

    def add(self, role: str, content: str):
        self.messages.append({"role": role, "content": content})
        self.messages = self.messages[-self.max_messages:]

    def recent(self):
        return list(self.messages)
