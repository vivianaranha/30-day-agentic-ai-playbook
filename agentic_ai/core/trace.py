from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime, timezone

@dataclass
class TraceEvent:
    event: str
    detail: str
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

class Trace:
    def __init__(self):
        self.events: list[TraceEvent] = []

    def add(self, event: str, detail: str):
        self.events.append(TraceEvent(event=event, detail=detail))

    def to_dict(self):
        return [e.__dict__ for e in self.events]
