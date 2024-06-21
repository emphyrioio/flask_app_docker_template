FROM python:3.10-slim-bullseye

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements_dev.txt requirements_dev.txt

RUN pip install --no-cache-dir -r requirements_dev.txt

COPY . .

EXPOSE 5000

ENV FLASK_APP=run.py
ENV FLASK_ENV=development  

CMD ["flask", "run", "--host=0.0.0.0"]
