FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc

COPY __init__.py app.py processtools.py db.json

COPY /templates /app/templates

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["flask", "run", "--host", "0.0.0.0"]
