FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src
COPY outputs/ ./outputs

WORKDIR /app/src
CMD ["python", "main.py"]
