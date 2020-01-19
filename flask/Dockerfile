FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install -y python3-pip

COPY . /app
WORKDIR /app 
RUN pip3 install -r requirements.txt

ENV JENKINS_NODES_USAGE_DB_USERNAME test
ENV JENKINS_NODES_USAGE_DB_PASSWORD 123
ENV DATABASE_NAME jenkins

RUN apt-get install -y gunicorn3

CMD ["gunicorn3", "app:app", "-b", "0.0.0.0:8000"]