FROM python:3.9.13-slim-buster

RUN apt-get update && apt-get install -y build-essential

WORKDIR /website

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]