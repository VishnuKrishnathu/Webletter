FROM python:3.10.2-alpine3.15
WORKDIR /app
COPY . .
RUN apk add --no-cache python3-dev gcc libffi-dev musl-dev postgresql-dev
RUN pip3 install -r requirements.txt
RUN pip3 install psycopg2
CMD ["gunicorn", "webletter.wsgi"]
