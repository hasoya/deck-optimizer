# See this https://pythonspeed.com/articles/base-image-python-docker-images/
FROM python:3.10-slim-buster

# Install library.
RUN pip install -U pip==22.0.3
COPY requirements.txt .
RUN pip --no-cache-dir install -r requirements.txt

# Copy scripts.
COPY . /app
RUN pip install -e /app
ENTRYPOINT [ "python", "/app/dopt/entry_point.py" ]
