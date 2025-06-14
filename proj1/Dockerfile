FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# train.py は volume 経由で渡すので COPY 不要（開発中の場合）
# COPY ./src/train.py .  ← 本番用途なら入れる

CMD ["python", "train.py"]
