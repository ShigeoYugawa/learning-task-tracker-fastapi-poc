# app/main.py

from fastapi import FastAPI
from app.schemas.task import Task, TaskResponse

# FastAPI アプリケーションのインスタンスを生成
app = FastAPI()

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
