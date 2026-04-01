# =========================
# ollama/client.py (IMPROVED)
# =========================
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

PROMPT_TEMPLATE = """
You are a senior financial analyst.

Analyze the sentiment of the following text.
Return:
- sentiment (positive/neutral/negative)
- reasoning
- risks
- outlook

Text:
{input}
"""


def explain_sentiment(text: str):
    prompt = PROMPT_TEMPLATE.format(input=text)

    res = requests.post(OLLAMA_URL, json={
        "model": "mistral",
        "prompt": prompt,
        "stream": False
    })

    return res.json().get("response", "")
