FROM python:3.9.12-alpine3.15

ENV PYTHONUNBUFFERED=1

RUN apk add --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .temp-build-deps gcc libc-dev linux-headers postgresql-dev


RUN mkdir -p /app
RUN adduser -Ds /bin/bash django
RUN chown -R django:django /app
RUN chmod 755 /app

RUN pip install -U pip

COPY ./requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY --chown=django:django ./build/python/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

USER django

WORKDIR /app

EXPOSE 8000

ENTRYPOINT ["sh", "/entrypoint"]
