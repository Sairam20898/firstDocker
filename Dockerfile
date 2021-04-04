FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /dockerapp

ADD . /dockerapp

COPY ./requirements.txt /dockerapp/requirements.txt

RUN pip install -r requirements.txt

COPY . /dockerapp



