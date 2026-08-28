from __future__ import annotations
from dataclasses import dataclass
from typing import Callable, Any

@dataclass
class Tool:
    name: str
    description: str
    fn: Callable[..., Any]
    write_action: bool = False

    def run(self, **kwargs):
        return self.fn(**kwargs)
