# =========================
# model/training/train_lora.py
# =========================
from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
from peft import LoraConfig, get_peft_model
import torch

model_name = "yiyanghkust/finbert-tone"

dataset = load_dataset("financial_phrasebank", "sentences_allagree")

tokenizer = AutoTokenizer.from_pretrained(model_name)


def tokenize(example):
    return tokenizer(example["sentence"], truncation=True, padding="max_length")


dataset = dataset.map(tokenize)
dataset = dataset.rename_column("label", "labels")
dataset.set_format("torch", columns=["input_ids", "attention_mask", "labels"])

model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=3)

# LoRA config
lora_config = LoraConfig(
    r=8,
    lora_alpha=16,
    target_modules=["query", "value"],
    lora_dropout=0.1,
    bias="none"
)

model = get_peft_model(model, lora_config)
model.to("cuda")

training_args = TrainingArguments(
    output_dir="./results",
    per_device_train_batch_size=32,
    num_train_epochs=5,
    fp16=True,
    logging_dir="./logs",
    save_strategy="epoch",
    evaluation_strategy="epoch"
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset["train"]
)

trainer.train()
model.save_pretrained("./saved_model_lora")
