# app/schemas/task.py

from pydantic import BaseModel

# --- 入力モデル定義（Pydantic） ---
class Task(BaseModel):
    """
    クライアントから受け取るJSONデータの構造を定義するモデル。
    バリデーションもこのクラスが自動で行う。
    
    - title: タスクのタイトル（必須の文字列）
    - description: タスクの詳細説明（必須の文字列）
    - done: タスクの完了フラグ（省略時は False）
    """
    title: str
    description: str
    done: bool = False

class TaskResponse(BaseModel):
    """
    APIのレスポンスとして返すデータ構造を定義するモデル。
    OpenAPI（Swagger）上の出力もこのモデルに従う。
    
    - message: 結果メッセージ
    - task: 登録されたタスク情報（Task型）
    """
    message: str
    task: Task
