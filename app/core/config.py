# app/core/config.py

# 変更前（旧バージョン）
# from pydantic import BaseSettings

# 変更後（Pydantic v2 対応）
from pydantic_settings import BaseSettings

# 環境変数管理
class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite+aiosqlite:///./dev.db"
    class Config:
        env_file = ".env"

settings = Settings()
