from fastapi import APIRouter

from api.chat import router as chat_router
from api.line import router as line_router
from api.repo import router as repo_router
from api.system import router as system_router
from api.ui import router as ui_router

router = APIRouter()

router.include_router(chat_router)
router.include_router(line_router)
router.include_router(repo_router)
router.include_router(system_router)
router.include_router(ui_router)