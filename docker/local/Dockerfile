FROM python:3.8.2-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code

COPY ../../requirements-dev.txt /code/

RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 apk --update add libxml2-dev libxslt-dev libffi-dev gcc musl-dev libgcc openssl-dev curl && \
 apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev && \
 apk add procps && \
 python3 -m pip install -r requirements-dev.txt --no-cache-dir && \
 apk --purge del .build-deps

COPY ../.. /code/


COPY ./docker/local/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start
