FROM python:3.7-alpine3.15
WORKDIR /app
COPY . .
RUN apk add --no-cache python3-dev gcc
RUN pip install -r requirements.txt
CMD ["gunicorn", "webletter.wsgi"]