# Learning Task Tracker - FastAPI PoC

このリポジトリは、**学習タスク管理アプリケーション**の概念実証（PoC）として構築された FastAPI ベースの Web API プロジェクトです。シンプルな構成ながらも、将来的な拡張性と保守性を意識して設計されています。

---

✅ 主な機能

- 学習タスク（title / description / done）のCRUD API
- SQLiteによる軽量なローカルDB管理（SQLAlchemy）
- FastAPI + Pydantic による型安全な実装
- OpenAPI（Swagger）による自動ドキュメント生成
- 最小構成によるPoC（Proof of Concept）

---

🗂️ ディレクトリ構成（抜粋）
<pre><code>
learning-task-tracker-fastapi-poc/
├── app/
│   ├── models/              # SQLAlchemy ORMモデル
│   ├── schemas/             # Pydanticスキーマ
│   ├── repositories/        # データアクセス層
│   ├── services/            # ビジネスロジック層
│   ├── routers/             # FastAPIルーティング
│   ├── core/
│   │   └── config.py        # 設定管理（環境変数など）
│   └── __init__.py
├── main.py                  # アプリケーションエントリーポイント
├── requirements.txt
├── .env                     # 環境変数ファイル（開発用）
└── README.md
</code></pre>

---

🚀 起動方法（ローカル開発）

1. 仮想環境を作成
<pre><code>
python -m venv .venv
source .venv/bin/activate  # Windowsでは .venv\Scripts\activate
</code></pre>
2. 依存ライブラリをインストール
<pre><code>
pip install -r requirements.txt
</code></pre>
3. アプリケーションの起動
<pre><code>
uvicorn main:app --reload
</code></pre>
4. Swagger UI にアクセス

http://127.0.0.1:8000/docs

---

🔧 使用技術スタック

- Python 3.12+
- FastAPI
- SQLAlchemy 2.x
- Pydantic v2
- SQLite（開発用）
- Uvicorn（ASGIサーバー）

---

🧪 今後の展望（予定）

- PostgreSQL / Docker 対応
- 認証機能の追加（JWT）
- React 等のSPAフロントエンド連携
- CI/CD環境（GitHub Actions など）
- AWSなどクラウド上での公開
- クリーンアーキテクチャへの発展的分割
- PlantUMLでの依存関係図可視化

---

📄 ライセンス

このプロジェクトは MIT ライセンスの下で公開されています。
