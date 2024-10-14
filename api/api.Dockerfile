FROM python:3.10.7

WORKDIR /api

COPY ./ /api

RUN apt-get update\
    && apt-get install -y --no-install-recommends \
    dumb-init \
    libev-dev \
    && apt-get purge -y --auto-remove \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir --upgrade -r /api/requirements.txt

ENV PYTHONPATH "${PYTHONPATH}:/api/app"