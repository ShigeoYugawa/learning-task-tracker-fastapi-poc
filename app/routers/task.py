# app/routers/task.py

# FastAPI のルーターと依存性注入のためのユーティリティ
from fastapi import APIRouter, Depends
# タスク作成用スキーマ（入力）およびレスポンススキーマ（出力）
from app.schemas.task import TaskCreateSchema, TaskResponseSchema
# タスクに関するビジネスロジックを担当するサービス層
from app.services.task_app_service import TaskApplicationService
# 非同期DBセッションを取得するための依存関数
from app.db.session import get_db
from sqlalchemy.ext.asyncio import AsyncSession

# --------------------------------------------------------
# /tasks に関するエンドポイントをまとめるルーター設定
# - prefix="/tasks" により全てのルートは /tasks から始まる
# - tags=["Tasks"] は OpenAPI ドキュメントのカテゴリ分けに使用
# --------------------------------------------------------
router = APIRouter(prefix="/tasks", tags=["Tasks"])


# --------------------------------------------------------
# タスク作成エンドポイント
# - HTTPメソッド: POST
# - パス: /tasks/
# - 入力: TaskCreate（title, description, done）
# - 出力: TaskResponse（message と作成されたタスク情報）
# --------------------------------------------------------

@router.post("/", response_model=TaskResponseSchema)
async def create_task(
    # クライアントから送信されるタスクデータ
    task: TaskCreateSchema,
    # 非同期DBセッション（DIにより注入）
    db: AsyncSession = Depends(get_db),
):
    """
    タスクを新規作成します。

    処理の流れ:
    1. get_db() により非同期DBセッションを取得
    2. TaskService の create_task() を呼び出してビジネスロジックを実行
    3. 成功時には TaskResponse を返す
    """
    service = TaskApplicationService(db)
    return await service.create_task(task)

