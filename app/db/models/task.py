# app/db/models/task.py

from sqlalchemy import Column, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
import uuid

# ベースクラスを生成（SQLAlchemyのモデルはこのBaseを継承する）
Base = declarative_base()

# タスク情報を表すテーブル定義
class Task(Base):
    __tablename__ = "tasks"  # テーブル名（DB上では "tasks" という名前で作成される）

    # 主キー：UUIDを文字列として使用（デフォルトで自動生成される）
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))

    # タスクのタイトル（必須）
    title = Column(String, nullable=False)

    # タスクの説明（必須）
    description = Column(String, nullable=False)

    # タスクの完了状態（未完了: False, 完了: True）デフォルトは未完了
    done = Column(Boolean, default=False)
