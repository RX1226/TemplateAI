from db.db import supabase

def save_chat(message: str, reply: str):
    result = supabase.table("chat_logs").insert({
        "message": message,
        "reply": reply
    }).execute()

    return result