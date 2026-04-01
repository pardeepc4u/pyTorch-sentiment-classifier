# =========================
# rag/faiss_index.py
# =========================
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.IndexFlatL2(384)
documents = []


def add_docs(texts):
    embeddings = model.encode(texts)
    index.add(np.array(embeddings))
    documents.extend(texts)


def search(query, k=3):
    q_emb = model.encode([query])
    D, I = index.search(np.array(q_emb), k)
    return [documents[i] for i in I[0]]
