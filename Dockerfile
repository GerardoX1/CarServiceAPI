FROM python:3.11-slim

RUN apt-get update -y --fix-missing && apt-get install -y git netcat-openbsd

COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ./start-web /start-web
RUN sed -i 's/\r$//g' /start-web
RUN chmod +x /start-web

WORKDIR /app
