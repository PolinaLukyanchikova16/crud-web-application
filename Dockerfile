FROM python:3.10 as base

ENV PYTHONPATH=$PYTHONPATH:/usr/app/src

RUN mkdir -p usr/app/src
WORKDIR usr/app/src
COPY requirements.txt requirements.txt
COPY src usr/app/src
RUN pip install -r requirements.txt
