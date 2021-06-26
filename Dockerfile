FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

RUN apk add --no-cache python3-dev gcc mariadb-dev build-base

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt
COPY . .
CMD ["flask", "run"]
