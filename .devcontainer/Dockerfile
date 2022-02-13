# syntax=docker/dockerfile:experimental
# python:3.7-slim-buster is recommended for Python base image.
# See this https://pythonspeed.com/articles/base-image-python-docker-images/
FROM python:3.10-slim-buster

# Set envs and locale
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ Asia/Tokyo

# Install system commands
# See https://stackoverflow.com/a/47143497 for the meaning of `set -ex`.
RUN set -ex \
  && apt-get update \
  && apt-get install -y g++ git libsnappy-dev openssh-client pigz wget libblas-dev liblapack-dev gnupg software-properties-common make

# Install clang 8
RUN wget -O - https://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add - \
  && add-apt-repository "deb http://apt.llvm.org/buster/ llvm-toolchain-buster-8 main" \
  && apt-get update \
  && apt-get -y install clang-8 lldb-8 lld-8 gfortran

# Set env option
ENV LLVM_CONFIG=/usr/lib/llvm-8/bin/llvm-config

# See https://stackoverflow.com/a/47652542 .
RUN mkdir -p -m 0600 ~/.ssh \
  && ssh-keyscan github.com >> ~/.ssh/known_hosts

# Install library.
RUN pip install -U pip
ADD requirements.txt .
ADD requirements-dev.txt .
RUN pip --no-cache-dir install -r requirements.txt -r requirements-dev.txt

ENV DEBIAN_FRONTEND=dialog
