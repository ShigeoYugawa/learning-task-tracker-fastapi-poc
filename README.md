# learning-task-tracker-fastapi-poc

FastAPIベースの学習タスク管理アプリのPoC（概念実証）です。  
このプロジェクトは、Django版PoC（https://github.com/ShigeoYugawa/learning-task-tracker）を踏まえて、API分離・アーキテクチャ志向の構成へと段階的に再設計していく学習用プロジェクトです。

---

## 📁 プロジェクト構成（暫定）

.
├── app/
│   ├── main.py        # FastAPI インスタンスのエントリーポイント（POST処理あり）
│   ├── routers/       # 今後ルーティングモジュールを格納予定
│   └── ...            # その他の構成要素（予定）
├── .venv/             # 仮想環境（環境により異なる）
├── README.md
├── requirements.txt
└── ...

- `app/main.py` に簡易なFastAPIアプリケーションを暫定的に実装。
- POSTリクエストにのみ対応しており、現在はブラウザ上でアクセスしても何も表示されません。
- 動作確認には Swagger UI（インタラクティブAPIドキュメント）を使用します。

---

## 🚀 実行方法（開発用）

以下の手順でローカルサーバーを起動できます：

# 仮想環境を有効化（例）
source .venv/bin/activate

# 必要なライブラリをインストール
pip install -r requirements.txt

# 開発サーバー起動
uvicorn app.main:app --reload

- Swagger UI: http://localhost:8000/docs  
- Redoc: http://localhost:8000/redoc

---

## 🧱 今後の方針（ToDo）

このプロジェクトはPoCとして、以下の構造への発展を想定しています：

- [ ] `routers/`：APIルーティングモジュールの分離
- [ ] `schemas/`：Pydanticモデルによる入出力定義
- [ ] `services/`：ビジネスロジックの抽象化
- [ ] `repositories/`：DB操作の責任を分離（例：SQLAlchemyやDBライブラリの導入）
- [ ] `di/`：依存性注入のインターフェイスと構成
- [ ] 認証／認可（JWTやOAuth2）

※ 本構成は「クリーンアーキテクチャ」や「ヘキサゴナルアーキテクチャ」などの原則を意識しながら、段階的に現実的な構成へと近づけていく方針です。

---

## 📝 補足

- このプロジェクトは学習用およびポートフォリオ目的で開発しています。
- Djangoでの構築経験を活かし、FastAPIにおける設計と構造の試行錯誤を行っています。

---

## 📚 参考リンク

- FastAPI公式ドキュメント: https://fastapi.tiangolo.com/
- Pydantic: https://docs.pydantic.dev/
- Uvicorn: https://www.uvicorn.org/
- Django版リポジトリ（参考）: https://github.com/ShigeoYugawa/learning-task-tracker
