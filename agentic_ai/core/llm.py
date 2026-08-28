from __future__ import annotations
import requests
from .config import USE_OLLAMA, OLLAMA_BASE_URL, OLLAMA_MODEL

def generate(prompt: str, fallback: str = "Demo response generated without an LLM.") -> str:
    if not USE_OLLAMA:
        return fallback

    try:
        response = requests.post(
            f"{OLLAMA_BASE_URL}/api/generate",
            json={"model": OLLAMA_MODEL, "prompt": prompt, "stream": False},
            timeout=30,
        )
        response.raise_for_status()
        return response.json().get("response", fallback)
    except Exception:
        return fallback
