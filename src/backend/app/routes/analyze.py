# =========================
# backend/app/routes/analyze.py
# =========================
from fastapi import APIRouter
from app.schemas.request import AnalyzeRequest
from app.services.advanced_service import analyze_advanced

router = APIRouter()


@router.post("/analyze")
def analyze(req: AnalyzeRequest):
    return analyze_advanced(req.text)
