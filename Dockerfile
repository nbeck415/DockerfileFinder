FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt /app/

RUN pip3 install -r requirements.txt

COPY . /app/

EXPOSE 3000

RUN python3 app.py