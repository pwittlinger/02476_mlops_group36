FROM python:3.10-slim

EXPOSE $PORT

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt
RUN dvc pull

CMD ["uvicorn", "model_api:app", "--host", "0.0.0.0", "--port", $PORT]
