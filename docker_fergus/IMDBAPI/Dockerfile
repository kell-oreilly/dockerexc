# syntax=docker/dockerfile:1
FROM python:3.11
WORKDIR /code
#COPY . /code/
#COPY . .
COPY requirements.txt /code/

RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
ENV FLASK_APP=app
ENV PYTHONPATH=/code
ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 5000
ENV ENV=PROD
CMD ["flask", "run"]
