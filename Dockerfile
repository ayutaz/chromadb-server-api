# Pythonイメージをベースに使用
FROM python:3.11

# 作業ディレクトリを設定
WORKDIR /app

# 依存関係ファイルをコピー
COPY requirements.txt requirements.txt

# 依存関係をインストール
RUN pip install -r requirements.txt

# アプリケーションのファイルをコピー
COPY . .

# Flaskアプリケーションを実行
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]

