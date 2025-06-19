# 異世界ガチャ Webアプリケーション
![image](https://github.com/user-attachments/assets/f11b6356-c601-48b7-9d0b-949b83a8caee)

## 概要
このプロジェクトは「異世界ガチャ」をテーマにしたWebアプリケーションです。  
ユーザーはガチャを引いてキャラクターやアイテムを獲得したり、チームを編成したり、テーマごとのページを楽しむことができます。

## 主な機能
- ガチャ機能（draw）
- チーム編成・管理
- テーマ切替（theme1, theme2）
- 画像・イラスト表示
- レスポンシブなWeb UI

## ディレクトリ構成
```
.
├── app/
│   ├── crud.py            # DB操作ロジック
│   ├── database.py        # DB接続設定
│   ├── main.py            # FastAPIエントリポイント
│   ├── models.py          # ORMモデル定義
│   ├── schemas.py         # Pydanticスキーマ
│   ├── routes/            # 各種APIルート
│   ├── static/            # 静的ファイル（画像・CSS等）
│   └── templates/         # HTMLテンプレート
├── design/                # 設計資料
├── requirements.txt       # Python依存パッケージ
├── Dockerfile             # Dockerイメージ定義
├── docker-compose.yml     # Docker Compose設定
└── README.md              # このファイル
```

## セットアップ方法

### 1. Dockerを使う場合（推奨）
```bash
docker-compose up --build
```
- `http://localhost:8000` でアプリにアクセスできます。

### 2. ローカル環境で実行する場合
1. Python 3.8以上をインストール
2. 依存パッケージをインストール
    ```bash
    pip install -r requirements.txt
    ```
3. サーバーを起動
    ```bash
    uvicorn app.main:app --reload
    ```
4. `http://localhost:8000` でアクセス

## 使用技術
- Python 3.8+
- Flask
- Jinja2（テンプレートエンジン）
- SQLAlchemy
- Docker / Docker Compose



