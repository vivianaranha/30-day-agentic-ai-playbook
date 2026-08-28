from __future__ import annotations
from dataclasses import dataclass
from uuid import uuid4

@dataclass
class ApprovalRequest:
    id: str
    action: str
    approved: bool = False

class ApprovalStore:
    def __init__(self):
        self.requests: dict[str, ApprovalRequest] = {}

    def create(self, action: str):
        req = ApprovalRequest(id=str(uuid4()), action=action)
        self.requests[req.id] = req
        return req

    def approve(self, request_id: str):
        req = self.requests[request_id]
        req.approved = True
        return req
