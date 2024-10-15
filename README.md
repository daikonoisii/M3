# M3-embedding
M3を利用できるAPI

# 参考文献
[論文](https://arxiv.org/abs/2402.03216)
[コード](https://github.com/FlagOpen/FlagEmbedding)

# api

## 設定
[github](https://github.com/FlagOpen/FlagEmbedding)をcloneして
`FlagEmbedding/FlagEmbedding`を`M3/api/app/`にコピーする

## 起動コマンド
```bash
% cd M3
% docker compose build
% docker compose up
```
注意：`docker compose up`実行時にM3モデルのダウンロードが開始されるため、サーバーが立つまでに30分ほどかかる。

## 終了コマンド
```bash
% docker compose down
```

## 利用方法
```bash
% curl -X 'POST' \
  'http://127.0.0.1:8010/m3_embeddings' \
  -H 'Content-Type: application/json' \
  -d '{"queries": ["What is ChatGPT?", "AI-based conversational language model."]}'
```