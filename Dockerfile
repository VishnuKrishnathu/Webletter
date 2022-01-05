FROM python:3.7-alpine3.15
WORKDIR /app
COPY . .
RUN apk add --no-cache python3-dev gcc
RUN pip install -r requirements.txt
RUN python3 manage.py migrate
RUN python3 manage.py migrate authentication_app zero
RUN python3 manage.py migrate authentication_app
RUN python3 manage.py migrate api zero
RUN python3 manage.py migrate api
CMD ["gunicorn", "webletter.wsgi"]