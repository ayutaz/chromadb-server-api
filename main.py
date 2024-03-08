from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import chromadb
import os
import json

app = FastAPI()

# 環境変数からメモリーファイルのパスを取得
MEMORY_FILE_PATH = os.getenv('MEMORY_FILE_PATH', 'memories.json')

# メモリーデータをファイルから読み込む
with open(MEMORY_FILE_PATH, 'r') as file:
    memories = json.load(file)

# ChromaDBクライアントの初期化
chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="my_collection")

print("Adding documents to collection len memories:", len(memories))

# メモリーをコレクションに追加
for index, info in enumerate(memories):
    print("Adding document to collection:", info)
    collection.add(documents=[info], metadatas=[{"source": "data"}], ids=[str(index)])


class QueryText(BaseModel):
    text: str


@app.post("/query")
def query(query: QueryText):
    results = collection.query(query_texts=[query.text], n_results=1)
    print(results)

    if results['documents']:
        return results['documents'][0][0]
    else:
        raise HTTPException(status_code=404, detail="Document not found")
