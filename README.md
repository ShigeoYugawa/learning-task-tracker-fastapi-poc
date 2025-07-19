# Learning Task Tracker - FastAPI PoC

FastAPIベースの学習タスク管理アプリです。  
このプロジェクトは、Django版PoC（[GitHub リポジトリ](https://github.com/ShigeoYugawa/learning-task-tracker)）を踏まえ、**API分離・アーキテクチャ志向**の構成へと段階的に再設計していく実験的プロジェクトです。

---

## 📁 プロジェクト構成（暫定）

```
.
├── app/
│   ├── main.py        # FastAPI インスタンスのエントリーポイント（POST処理あり）
│   ├── routers/       # 今後ルーティングモジュールを格納予定
│   └── ...            # その他の構成要素（予定）
├── .venv/             # 仮想環境（環境により異なる）
├── README.md
├── requirements.txt
└── ...
```

- `app/main.py` にエントリーポイントを暫定実装。
- 現時点では POST のみ対応しており、**Swagger UI での操作が主な確認手段**です。
- ルーティングと処理ロジックが同居しており、SRP（単一責任の原則）には未対応です。

---

## 🚀 実行方法（開発用）

以下の手順でローカルサーバーを起動できます：

```bash
# 仮想環境を有効化（例）
source .venv/bin/activate

# 必要なライブラリをインストール
pip install -r requirements.txt

# 開発サーバー起動
uvicorn app.main:app --reload
```

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

※「クリーンアーキテクチャ」や「ヘキサゴナルアーキテクチャ」などの原則を意識しつつ、現実的な段階的移行を目指します。

---

## 📝 補足

- このプロジェクトは学習用およびポートフォリオ目的で開発しています。
- Djangoでの構築経験を活かし、FastAPIにおける設計と構造の試行錯誤を行っています。

---

## 📚 参考リンク

- [FastAPI公式ドキュメント](https://fastapi.tiangolo.com/)
- [Pydantic](https://docs.pydantic.dev/)
- [Uvicorn](https://www.uvicorn.org/)
- [Django版リポジトリ（参考）](https://github.com/ShigeoYugawa/learning-task-tracker)
