# syntax=docker/dockerfile:1

FROM python:3.10-slim-buster

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./worker /code/worker

CMD ["python3.10", "-u", "worker/worker.py", "--host=0.0.0.0"]