from fastapi import APIRouter
from db.chat_repo import save_chat

router = APIRouter()

@router.post("/save/chat")
def chat(message: str, reply: str):
    save_chat(message, reply)
    return {"reply": reply}