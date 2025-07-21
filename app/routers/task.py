# app/routers/task.py

from fastapi import APIRouter, Depends
from app.schemas.task import TaskCreate, TaskRead
from app.services.task_service import TaskService
from app.db.session import get_db
from sqlalchemy.ext.asyncio import AsyncSession

# --- ルーター設定 ---
# このモジュールでは /tasks エンドポイント以下のタスク操作ルートを定義する。
# prefix="/tasks" により、すべてのルートは /tasks から始まる。
# tags=["Tasks"] により、自動生成されるAPIドキュメントで「Tasks」というセクションにまとめられる。
router = APIRouter(prefix="/tasks", tags=["Tasks"])

# POSTメソッドでタスクを作成するエンドポイント。
# リクエストボディで受け取るデータは `TaskCreate`（Pydanticモデル）によりバリデーションされる。
# レスポンスとして `TaskRead` を返し、作成されたタスクの情報を提供する。
@router.post("/", response_model=TaskRead)
async def create_task(

    # リクエストボディから渡されるタスク作成用データ（title, description, done）
    task: TaskCreate,
    # DI（依存性注入）により取得される非同期DBセッション        
    db: AsyncSession = Depends(get_db),
):
    """
    新しいタスクを作成するエンドポイント。

    - `POST /tasks/` に対するリクエストを処理
    - 入力: TaskCreate（title, description, done）
    - 出力: TaskRead（id, title, description, done）

    処理の流れ:
    1. DBセッションを注入（Depends(get_db)）
    2. TaskServiceのインスタンスを生成
    3. create_task メソッドを呼び出してDBにタスクを保存
    4. 作成されたタスクの情報を TaskRead モデルに変換して返却
    """
    # タスク操作用のサービスクラスを生成し、ビジネスロジックを委譲
    service = TaskService(db)
    # サービス層にタスク作成処理を委譲し、結果を返却
    return await service.create_task(task)
