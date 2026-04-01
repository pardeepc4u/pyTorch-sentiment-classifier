# =========================
# backend/app/services/advanced_service.py
# =========================
from app.ml.predictor import predict_sentiment
from app.ollama.client import explain_sentiment
from rag.faiss_index import search


def analyze_advanced(text: str):
    sentiment, confidence = predict_sentiment(text)
    context = search(text)

    explanation = explain_sentiment(
        text + "\nContext:\n" + "\n".join(context)
    )

    return {
        "sentiment": sentiment,
        "confidence": confidence,
        "context": context,
        "explanation": explanation
    }
