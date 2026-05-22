from fastapi import APIRouter
from pydantic import BaseModel
from ai.gemini import ask_llm

router = APIRouter()

class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
def chat(req: ChatRequest):
    reply = ask_llm(req.message)
    return {"reply": reply}