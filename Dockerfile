FROM python:3.10-alpine

WORKDIR /usr/src/app

ENV AZURE_WEB_APP $AZURE_WEB_APP
ENV PYTHONUNBUFFERED=1
ENV SECRET_KEY $SECRET_KEY
ENV SENTRY_DSN $SENTRY_DSN

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000