from __future__ import annotations
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class LocalRetriever:
    def __init__(self, knowledge_dir: str = "knowledge"):
        self.knowledge_dir = Path(knowledge_dir)
        self.docs: list[tuple[str, str]] = []
        self.vectorizer = None
        self.matrix = None
        self.refresh()

    def refresh(self):
        self.docs = []
        for p in sorted(self.knowledge_dir.rglob("*.md")):
            self.docs.append((str(p), p.read_text(encoding="utf-8")))
        if self.docs:
            self.vectorizer = TfidfVectorizer(stop_words="english")
            self.matrix = self.vectorizer.fit_transform([d[1] for d in self.docs])

    def search(self, query: str, top_k: int = 3):
        if not self.docs:
            return []
        q = self.vectorizer.transform([query])
        scores = cosine_similarity(q, self.matrix)[0]
        ranked = scores.argsort()[::-1][:top_k]
        return [
            {"source": self.docs[i][0], "score": float(scores[i]), "content": self.docs[i][1][:1000]}
            for i in ranked if scores[i] > 0
        ]
