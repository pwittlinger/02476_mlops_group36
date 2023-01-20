FROM python:3.10-slim

EXPOSE $PORT

COPY . /app

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN pip install -r requirements.txt
RUN dvc pull

CMD exec uvicorn model_api:app --port $PORT --host 0.0.0.0 --workers 1