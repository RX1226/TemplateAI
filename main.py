from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from api.router import router
from pathlib import Path

app = FastAPI()

app.include_router(router)

@app.get("/health")
def health():
    return {"status": "ok"}

BASE_DIR = Path(__file__).resolve().parent

app.mount("/",StaticFiles(directory=BASE_DIR / "frontend", html=True),name="frontend")