from fastapi import APIRouter
import schemas
from gemini_client import generate_feedback

router = APIRouter(prefix="/ai")

@router.post("/analyze")
def analyze(ai_request: schemas.AIRequest):
    result = generate_feedback(ai_request.prompt)
    return {"response": result}
