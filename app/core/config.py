# app/core/config.py

# 変更前（旧バージョン）
# from pydantic import BaseSettings

# Pydantic v2 での設定管理用の基底クラスをインポート
# ※ pydantic-settings パッケージが必要（`pip install pydantic-settings`）
from pydantic_settings import BaseSettings

# アプリ全体の設定（環境変数など）を管理するクラス
class Settings(BaseSettings):
    # DATABASE_URL 環境変数を読み込む（.env に記述があれば上書きされる）
    # デフォルトは SQLite + aiosqlite を使用するローカル開発用DB
    DATABASE_URL: str = "sqlite+aiosqlite:///./dev.db"

    # .env ファイルを読み込む設定（v2でも class Config は有効）
    class Config:
        env_file = ".env"

# Settings クラスのインスタンスを生成し、アプリ内で共通設定として利用する
settings = Settings()

