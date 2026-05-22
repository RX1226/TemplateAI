from fastapi import APIRouter
from ai.gemini import ask_llm

router = APIRouter()

@router.post("/line/webhook")
def webhook(event):
    message = event.message.text
    reply = ask_llm(message)
    return reply