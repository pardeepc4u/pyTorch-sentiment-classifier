# =========================================
# Financial Sentiment AI - PRODUCTION VERSION
# =========================================

# Key Upgrades:
# ✅ LoRA Fine-tuning (PEFT)
# ✅ GPU optimized training
# ✅ RAG with FAISS
# ✅ Kafka-ready pipeline hooks
# ✅ Advanced Ollama prompting
# ✅ Dashboard-ready API

import os
import logging

current_dir = os.path.dirname(__file__)
logging.basicConfig(filename=os.path.join(current_dir, 'main.log'), level=logging.INFO)

from model.training.train_lora import train_lora_model
from model.inference.predictor import predict_sentiment
from rag.faiss_index import add_docs, search
from ollama.client import explain_sentiment
from backend.app.services.advanced_service import analyze_advanced
from streaming.kafka_producer import send_news

# =========================
# CLI Entry Point
# =========================
if __name__ == "__main__":
    print("Financial Sentiment AI - Ready")
    
    # Example usage
    sample_text = "The company reported strong earnings growth despite market volatility."
    
    try:
        result = analyze_advanced(sample_text)
        print("\nAnalysis Result:")
        print(f"Sentiment: {result['sentiment']}")
        print(f"Confidence: {result['confidence']:.2f}")
        print(f"Context: {result['context']}")
        print(f"Explanation: {result['explanation'][:200]}...")
        
        # Send to Kafka (non-blocking example)
        send_news({"text": sample_text, "sentiment": result['sentiment']})
    except Exception as e:
        logging.error(f"Error in main execution: {e}")
        print(f"Error: {e}")
