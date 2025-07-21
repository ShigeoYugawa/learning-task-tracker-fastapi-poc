# app/schemas/task.py

from pydantic import BaseModel
from typing import Optional
from uuid import UUID

# --- 入力用 ---
class TaskCreate(BaseModel):
    title: str
    description: str
    done: bool = False

# --- 出力用 ---
class Task(BaseModel):
    id: UUID
    title: str
    description: str
    done: bool = False

class TaskRead(BaseModel):
    id: UUID
    title: str
    description: str
    done: Optional[bool] = False

    class Config:
        orm_mode = True

# --- レスポンス ---
class TaskResponse(BaseModel):
    message: str
    task: Task
