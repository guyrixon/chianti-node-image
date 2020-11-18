# Adapted from https://sebest.github.io/post/protips-using-gunicorn-inside-a-docker-image/

FROM python:3.9

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY logging.conf /logging.conf

COPY NodeSoftware /NodeSoftware

EXPOSE 8000

ENV PYTHONPATH=${PYTHONPATH}:/NodeSoftware:/NodeSoftware/nodes/chianti

RUN mkdir /var/log/gunicorn

#ENTRYPOINT ["/usr/local/bin/gunicorn", "--config", "/gunicorn.conf", "--log-config", "/logging.conf", "-b", ":8000", "myapp:app"]
ENTRYPOINT ["/usr/local/bin/gunicorn", "-b", ":8000", "--preload", "--access-logfile", "/var/log/gunicorn/access.log", "--log-file", "/var/log/gunicorn/error.log", "nodes.chianti.wsgi:application"]


