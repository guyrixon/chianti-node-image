# Adapted from https://sebest.github.io/post/protips-using-gunicorn-inside-a-docker-image/

FROM python:2.7

RUN pip install gunicorn json-logging-py django==1.9 pyparsing MySQL-python pybtex

COPY logging.conf /logging.conf
#COPY gunicorn.conf /gunicorn.conf

COPY NodeSoftware /NodeSoftware

EXPOSE 8000

ENV PYTHONPATH=${PYTHONPATH}:/NodeSoftware:/NodeSoftware/nodes/chianti

RUN mkdir /var/log/gunicorn

#ENTRYPOINT ["/usr/local/bin/gunicorn", "--config", "/gunicorn.conf", "--log-config", "/logging.conf", "-b", ":8000", "myapp:app"]
ENTRYPOINT ["/usr/local/bin/gunicorn", "-b", ":8000", "--preload", "--access-logfile", "/var/log/gunicorn/access.log", "--log-file", "/var/log/gunicorn/error.log", "nodes.chianti.wsgi:application"]


