FROM python:3.6.15-buster
WORKDIR /backend
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*
COPY . .
RUN chmod 777 main.sh
RUN pip install --upgrade pip
RUN pip install gunicorn
RUN pip install -r requirements.txt


