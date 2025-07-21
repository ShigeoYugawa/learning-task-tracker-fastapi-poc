# app/routers/task.py

from fastapi import APIRouter, Depends
from app.schemas.task import TaskCreate, TaskRead
from app.services.task_service import TaskService
from app.db.session import get_db
from sqlalchemy.ext.asyncio import AsyncSession

# ルーティング分離

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/", response_model=TaskRead)
async def create_task(task: TaskCreate, db: AsyncSession = Depends(get_db)):
    service = TaskService(db)
    return await service.create_task(task)
