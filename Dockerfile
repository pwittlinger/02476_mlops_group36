FROM python

COPY . /app

WORKDIR /app

CMD python main.py