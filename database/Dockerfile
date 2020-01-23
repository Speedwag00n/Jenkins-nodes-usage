FROM postgres:10-alpine

RUN apk add --no-cache supervisor
RUN mkdir /etc/supervisor.d

COPY /docker-entrypoint-initdb.d /docker-entrypoint-initdb.d/
COPY postgres_cron.ini /etc/supervisor.d/postgres_cron.ini
COPY cron-job-init /cron-job-init
COPY script.sh /script.sh

RUN chmod 777 /script.sh

RUN /usr/bin/crontab /cron-job-init

ENTRYPOINT ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]