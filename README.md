# learning-task-tracker-fastapi

FastAPIベースの学習タスク管理アプリです。  
このリポジトリは、Django版PoC（[learning-task-tracker](https://github.com/ShigeoYugawa/learning-task-tracker-fastapi)）を踏まえ、**API分離・アーキテクチャ志向の構成**を目指してバックエンドを段階的に再構築していくプロジェクトです。

---

## ✅ 現在の構成（暫定）

- `main.py` に `FastAPI` のインスタンスとルートエンドポイント `/` を暫定的に定義
- 初期動作確認（`Hello FastAPI`）のための簡易実装

> ⚠ 現在は、ルーティングと処理ロジックが `main.py` に同居しており、**SRP（単一責任の原則）には準拠していません**。今後は、責務に応じてモジュールを分離し、拡張可能な構成にしていきます。

---

## 🛠 今後の展望

- `routers/`, `services/`, `schemas/`, `repositories/` などのモジュール分離
- SRPに準拠した設計への移行
- ビジネスロジックとインフラ処理の責任を明確化
- Django版で培った経験をFastAPIでも活かす構成へ発展

---

## 🚀 実行方法（仮）

```bash
uvicorn main:app --reload
