# app/db/session.py

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# 非同期対応のSQLAlchemyエンジンを作成
# settings.DATABASE_URLには非同期用のDB接続URLが設定されている（例: "postgresql+asyncpg://..."）
engine = create_async_engine(settings.DATABASE_URL, echo=True)

# sessionmakerを使って非同期セッションを生成するファクトリを作成
# class_にAsyncSessionを指定することで、非同期セッションを作成可能にする
# expire_on_commit=Falseはコミット後もオブジェクトの状態を保持する設定
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# DBセッションを非同期コンテキストマネージャーで生成し、
# yieldで呼び出し元に渡すジェネレーター関数
# FastAPIのDependsなどで利用して、リクエストごとにセッションを管理可能にする
async def get_db():
    async with async_session() as session:
        yield session
