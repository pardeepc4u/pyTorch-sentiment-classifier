# =========================
# model/inference/predictor.py
# =========================
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F

model_path = "./saved_model_lora"

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSequenceClassification.from_pretrained(model_path)
model.to("cuda")
model.eval()

labels = ["negative", "neutral", "positive"]


def predict_sentiment(text: str):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True).to("cuda")

    with torch.no_grad():
        outputs = model(**inputs)

    probs = F.softmax(outputs.logits, dim=1)
    confidence, pred = torch.max(probs, dim=1)

    return labels[pred.item()], confidence.item()
