# app/schemas/task.py

from pydantic import BaseModel
from uuid import UUID

# --- 入力用スキーマ ---
class TaskCreate(BaseModel):
    """
    用途：新規タスク作成時にクライアントから送信されるJSONの構造を定義。

    FastAPIのPOSTエンドポイントでバリデーションに使用され、
    このスキーマをもとにDBへINSERTするSQLAlchemyモデルが作成される。
    """
    title: str  # タスクのタイトル
    description: str  # タスクの詳細説明
    done: bool = False  # 完了フラグ（初期値 False）

# --- レスポンス用スキーマ（タスク1件） ---
class Task(BaseModel):
    """
    用途：DBから取得したタスクデータをJSONとしてクライアントに返す際の構造を定義。

    FastAPIで response_model=Task として使用される。
    """
    id: UUID  # タスクID（自動生成されるUUID）
    title: str  # タスクのタイトル
    description: str  # タスクの詳細説明
    done: bool = False  # 完了フラグ

    class Config:
        orm_mode = True  # ORMモデル（SQLAlchemy）からの変換を許可

# --- APIレスポンスラッパー ---
class TaskResponse(BaseModel):
    """
    用途：APIレスポンスを統一フォーマットで返すための構造。
    
    成功メッセージ＋実データ（Task）をまとめて返すときに使用。
    Swagger UIでの表示も分かりやすくなる。
    """
    message: str  # API操作の結果メッセージ（例："Task created successfully"）
    task: Task    # 実際に作成・取得されたタスクデータ（Taskスキーマ）

    class Config:
        orm_mode = True
