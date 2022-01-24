# Adapted from https://sebest.github.io/post/protips-using-gunicorn-inside-a-docker-image/

FROM python:3.9

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY logging.conf /logging.conf

COPY NodeSoftware /NodeSoftware

COPY chianti7.db /chianti7.db

EXPOSE 8000

ENV PYTHONPATH=${PYTHONPATH}:/NodeSoftware:/NodeSoftware/nodes/chianti

RUN mkdir /var/log/gunicorn
RUN mkdir /var/log/django

ENTRYPOINT ["gunicorn", "-b", ":8000", "--preload", "--access-logfile", "/var/log/gunicorn/access.log", "--log-file", "/var/log/gunicorn/error.log", "node.wsgi:application"]

