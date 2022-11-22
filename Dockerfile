FROM python:3.10-alpine

WORKDIR /app

COPY . /app

RUN apk add gcc musl-dev mariadb-connector-c-dev
RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python", "main.py"]