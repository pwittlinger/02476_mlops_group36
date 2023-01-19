FROM python:3.10-slim

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt
RUN dvc pull

CMD ["uvicorn", "model_api:app", "--host", "0.0.0.0", "--port", "80"]
