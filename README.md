# 必要なもの

1. `Docker`環境  
   Docker をインストールしていない方は、インストールしてください。  
   インストール先：https://www.docker.com/products/docker-desktop/）

2. Python(3.10 系)  
   持っていない方は準備しましょう。

# 環境構築

1. ルートディレクトリ直下に移動してください。（一番上の階層、`docker-compose.yml`が置いている場所のこと）
2. ビルドします。以下を実行してください。

```
docker compose build
```

3. ビルドが成功したら、コンテナを起動します。以下を実行してください。

```
docker compose up
```

4. コンテナが起動し、postgres が起動します。
5. `fastapi`のフォルダ（`requirements.py`が置いている場所）に移動してください。
6. 必要なパッケージをインストールします。（venv にしておくことを推奨）

```
pip install -r requirements.txt
```

7. マイグレーションを作成します。以下のコマンドを実行してください。

```

alembic revision --autogenerate -m "create tables"

```

- 注意：`fastapi/src/migrations/versions`にファイルがあれば消しましょう。（念のため）

`fastapi/src/migrations/versions`にマイグレーションが自動生成されます。

8. 自動生成したマイグレーションをデータベースに反映します。以下を実行してください。

```
alembic upgrade head
```

9. `fastapi`のサーバーを起動します。`fastapi/src`に移動し、以下を実行

```
uvicorn main:app --reload
```
