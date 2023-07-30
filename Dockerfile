#FROM python:3.10

#RUN mkdir /app

#COPY requirements.txt /app/

#WORKDIR /app

#RUN pip install -r requirements.txt

#COPY . /app/


FROM python:3.10-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . . 

CMD ["python3","manage.py","runserver","0.0.0.0:8000"]