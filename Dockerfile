FROM python

COPY . /app

WORKDIR /app

CMD python test.py