# =========================
# backend/app/schemas/request.py
# =========================
from pydantic import BaseModel

class AnalyzeRequest(BaseModel):
    text: str
