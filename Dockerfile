FROM nvidia/cuda:12.2.0-runtime-ubuntu22.04

RUN apt-get update && apt-get install -y python3 python3-pip python3-dev build-essential && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY src/ ./src/

RUN useradd -m -u 1000 appuser
USER appuser

EXPOSE 8000

ENV PYTHONUNBUFFERED=1

CMD ["python3", "src/main.py"]