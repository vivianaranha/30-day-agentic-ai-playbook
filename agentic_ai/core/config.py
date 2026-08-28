from __future__ import annotations
import os

USE_OLLAMA = os.getenv("USE_OLLAMA", "false").lower() == "true"
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2")
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
MAX_AGENT_STEPS = int(os.getenv("MAX_AGENT_STEPS", "6"))
APPROVAL_REQUIRED_FOR_WRITES = os.getenv("APPROVAL_REQUIRED_FOR_WRITES", "true").lower() == "true"
