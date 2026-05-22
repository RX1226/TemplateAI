from fastapi import APIRouter
from core.config import DEBUG

router = APIRouter()

@router.post("/isDebug")
def is_debug():
    return DEBUG
