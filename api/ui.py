from fastapi import APIRouter

router = APIRouter()

@router.get("/ui/config")
def get_ui_config():
    return {
        "title": "AI Chat Demo",
        "version": "1.0",
        "placeholder": "請輸入你的問題"
    }