FROM python:3.9.5-slim-buster
WORKDIR /usr/src/app

RUN apt-get update \
  && apt-get -y install netcat gcc libpq-dev\
  && apt-get clean

RUN pip install --upgrade pip
COPY ./requirements.txt ..
RUN pip install -r ../requirements.txt

COPY ./app .

WORKDIR /usr/src
