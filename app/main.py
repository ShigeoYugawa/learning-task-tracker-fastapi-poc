# app/main.py

from fastapi import FastAPI
from app.routers import task  # ← ルーターをインポート

app = FastAPI()

# 分離されたルーターを登録
app.include_router(task.router)
