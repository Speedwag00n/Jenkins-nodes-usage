FROM python:3.6-alpine

WORKDIR /app 

ENV JENKINS_NODES_USAGE_DB_USERNAME test
ENV JENKINS_NODES_USAGE_DB_PASSWORD 123
ENV DATABASE_NAME jenkins

RUN pip install --upgrade pip
RUN apk update && apk add postgresql-dev gcc musl-dev
ADD requirements.txt /app
RUN pip3 install -r requirements.txt

ADD . /app

CMD ["gunicorn", "app:app", "-b", "0.0.0.0:8000"]