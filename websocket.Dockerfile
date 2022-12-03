# syntax=docker/dockerfile:1

FROM python:3.10-slim-buster

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY websocket /code/websocket

CMD ["python3.10", "-u", "websocket/listen_results.py", "--host=0.0.0.0"]