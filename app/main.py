from fastapi import FastAPI
from pydantic import BaseModel

# FastAPI アプリケーションのインスタンスを生成
app = FastAPI()


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
    done: bool = False  # デフォルト値を設定（未送信時はFalse）


class TaskResponse(BaseModel):
    """
    APIのレスポンスとして返すデータ構造を定義するモデル。
    OpenAPI（Swagger）上の出力もこのモデルに従う。
    
    - message: 結果メッセージ
    - task: 登録されたタスク情報（Task型）
    """
    message: str
    task: Task


# --- POSTエンドポイント定義 ---
@app.post("/tasks", response_model=TaskResponse)
def create_task(task: Task) -> TaskResponse:
    """
    クライアントからPOSTされたJSONデータを受け取り、
    Taskオブジェクトに自動変換された引数 `task` を使用して処理を行う。

    - 引数: `task` は JSON → Task に変換されて受け取る
    - 戻り値: TaskResponse オブジェクトを返し、自動で JSON にシリアライズされる
    - response_model: OpenAPI上の応答モデル定義（Swagger UIが自動生成される）

    入力JSONの例：
    {
        "title": "読書",
        "description": "FastAPIのドキュメントを読む",
        "done": false
    }
    """
    return TaskResponse(
        message="タスクを受け取りました",
        task=task
    )
