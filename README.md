# Financial Sentiment AI (Production-Ready)

An enterprise-grade financial sentiment analysis system with LoRA fine-tuning, RAG, and Kafka integration.

## 🚀 Features

- ✅ **LoRA Fine-tuning** with PEFT
- ✅ **GPU Accelerated Training**
- ✅ **RAG with FAISS** for context
- ✅ **Kafka-ready Pipeline**
- ✅ **Ollama Integration** for explainable AI
- ✅ **Modular Architecture**

## 📁 Project Structure

```
Financial-Sentiment-AI/
├── src/
│   ├── main.py
│   ├── model/
│   │   ├── training/
│   │   │   └── train_lora.py
│   │   └── inference/
│   │       └── predictor.py
│   ├── rag/
│   │   └── faiss_index.py
│   ├── ollama/
│   │   └── client.py
│   ├── backend/
│   │   └── app/
│   │       ├── routes/analyze.py
│   │       ├── schemas/request.py
│   │       ├── services/advanced_service.py
│   │       └── ml/predictor.py
│   ├── streaming/
│   │   └── kafka_producer.py
│   └── frontend/
│       └── dashboard_ready.py
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## 🛠️ Setup

### 1. Clone Repository

```bash
git clone <repo-url>
cd Financial-Sentiment-AI
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Pull Required Docker Services

```bash
docker-compose up -d ollama kafka
```

### 4. Train LoRA Model

```bash
python src/model/training/train_lora.py
```

### 5. Run Application

```bash
python src/main.py
```

## 🔑 Key Modules

| Module | Purpose |
|--------|---------|
| `model/training/train_lora.py` | LoRA fine-tuning with PEFT |
| `model/inference/predictor.py` | GPU-optimized predictions |
| `rag/faiss_index.py` | Context retrieval with FAISS |
| `ollama/client.py` | Explainable AI with Mistral |
| `backend/app/services/advanced_service.py` | Unified analysis service |
| `streaming/kafka_producer.py` | Event streaming integration |

## 🌐 API Endpoints

- `POST /analyze` - Analyze financial sentiment with context

## 🛡️ Security Considerations

- Environment variables for sensitive data
- Secure Kafka authentication
- HTTPS in production

## 📈 Performance Optimizations

- GPU acceleration with PyTorch
- Efficient RAG with FAISS
- Async Kafka producers

## 🤝 Contributing

Follow PEP 8, write tests, and use type hints.
