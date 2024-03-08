# chromadb-server-api
chromadbを使ったシンプルなサーバーAPIの実装

## 使い方
1. dbに入れるテキストを `memories.json` に記述する.配置はルートパス
```json
[
  "string",
  "string",
]
```
2. サーバーを起動する
```bash
docker-compose up --build
```

3. サーバーにリクエストを送る
```bash
curl -X POST -H "Content-Type: application/json" -d '{"text":"苦手なものは何？"}' http://localhost:8020/query
```
