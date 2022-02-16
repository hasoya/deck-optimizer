# See this https://pythonspeed.com/articles/base-image-python-docker-images/
FROM python:3.10-slim-buster

# Install system commands
# See https://stackoverflow.com/a/47143497 for the meaning of `set -ex`.
RUN set -ex \
    && apt-get update \
    && apt-get install -y git

# Install library.
RUN pip install -U pip
COPY requirements.txt .
COPY requirements-dev.txt .
RUN pip --no-cache-dir install -r requirements.txt -r requirements-dev.txt
