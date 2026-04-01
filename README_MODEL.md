# Model Modules Documentation

## LoRA Fine-tuning (`src/model/training/train_lora.py`)

### Key Features
- Uses `yiyanghkust/finbert-tone` base model
- LoRA rank 8 with alpha 16
- Mixed-precision training (FP16)
- Evaluation strategy: epoch

### Training Configuration
```python
TrainingArguments(
    output_dir="./results",
    per_device_train_batch_size=32,
    num_train_epochs=5,
    fp16=True,
    logging_dir="./logs",
    save_strategy="epoch",
    evaluation_strategy="epoch"
)
```

### Output
- Saved model: `./saved_model_lora`
- Logs: `./logs`

## Inference (`src/model/inference/predictor.py`)

### Features
- GPU-optimized predictions
- Softmax confidence scores
- Label mapping: ["negative", "neutral", "positive"]

### Usage
```python
sentiment, confidence = predict_sentiment("The company reported strong earnings.")
```

## Ollama Integration (`src/ollama/client.py`)

### Prompt Template
```
You are a senior financial analyst.

Analyze the sentiment of the following text.
Return:
- sentiment (positive/neutral/negative)
- reasoning
- risks
- outlook

Text:
{input}
```

### Usage
```python
explanation = explain_sentiment(text)
```

## RAG with FAISS (`src/rag/faiss_index.py`)

### Components
- Embedding model: "all-MiniLM-L6-v2"
- Index: FAISS IndexFlatL2 (384-dim)
- Retrieval: k=3 most similar documents

### Usage
```python
add_docs(texts)  # Index documents
results = search(query)  # Retrieve context
```

## Advanced Service (`src/backend/app/services/advanced_service.py`)

### Features
1. Sentiment prediction with confidence
2. Context retrieval from RAG
3. Explanation from Ollama

### Output Structure
```json
{
  "sentiment": "positive",
  "confidence": 0.92,
  "context": ["Related market analysis..."],
  "explanation": "The company reported..."
}
```

## Kafka Integration (`src/streaming/kafka_producer.py`)

### Features
- JSON serialization
- Asynchronous sending
- Topic: "financial-news"

### Usage
```python
send_news({"text": "Text...", "sentiment": "positive"})
```

## API Routes (`src/backend/app/routes/analyze.py`)

### Endpoint
- `POST /analyze`
  - Request: `{"text": "Financial text..."}`
  - Response: Full analysis from `analyze_advanced()`

## Frontend Dashboard (`src/frontend/dashboard_ready.py`)

### Features
- Streamlit-based UI
- Real-time sentiment analysis
- Explanation visualization

### Run
```bash
streamlit run src/frontend/dashboard_ready.py
```
