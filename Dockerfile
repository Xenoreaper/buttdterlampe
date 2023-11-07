FROM python:3.9.18-slim

WORKDIR /scripts/

ADD requirements.txt .

RUN pip3 install -r requirements.txt

ADD main.py main.py
ADD logic/* logic/
ADD models/* models/

EXPOSE 8000

ENTRYPOINT ["gunicorn" , "-b", "0.0.0.0:8000", "main:app"]