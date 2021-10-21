FROM python:3.8-alpine

COPY ["requirements.txt", "/"]

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH "${PYTHONPATH}:/app/src"

WORKDIR /app

RUN apk add --update --no-cache bash libpq
RUN apk add --no-cache --virtual build-deps \
        build-base \
        python3-dev \
        postgresql-dev \
    && pip install --no-cache-dir -r /requirements.txt \
    && apk del build-deps \
