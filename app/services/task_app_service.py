# app/services/task_app_service.py

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert
from app.schemas.task import TaskCreateSchema, TaskRead
from app.db.models.task import TaskModel
from sqlalchemy.future import select

class TaskApplicationService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_task(self, task_create: TaskCreateSchema) -> TaskRead:
        task = TaskModel(
            title=task_create.title,
            description=task_create.description,
            done=task_create.done
        )
        self.db.add(task)
        await self.db.flush()    # ID 発行などを確定
        await self.db.commit()
        await self.db.refresh(task)

        return TaskRead(
            id=task.id,
            title=task.title,
            description=task.description,
            done=task.done
        )

