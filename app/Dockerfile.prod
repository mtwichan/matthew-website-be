#################################
# Multi-stage: Builder #
#################################

FROM python:3.9.6-alpine as builder

WORKDIR /usr/src/app

# python env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip3 install --upgrade pip
COPY . .

COPY ./requirements.txt .
RUN pip3 wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt

#################################
# Multi-stage: Final #
#################################

FROM python:3.9.6-alpine

# create app user
RUN mkdir -p /home/app
RUN addgroup -S app && adduser -S app -G app

# create directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
WORKDIR $APP_HOME

# install dependencies
RUN apk update && apk add libpq
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip3 install --no-cache /wheels/*

COPY . $APP_HOME

# give permissions to app user
RUN chown -R app:app $APP_HOME

# change to app user
USER app
