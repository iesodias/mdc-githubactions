# set base image (host OS)
FROM python:3.8-alpine
#FROM python:3.6-slim

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src/ .

EXPOSE 5000

CMD [ "python", "./server.py" ]