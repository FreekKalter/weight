FROM python:3.6

EXPOSE 5000

ADD instance /code/instance
ADD weight /code/weight
ADD run.py /code

VOLUME /data

WORKDIR /code
RUN pip install -r weight/requirements.txt
CMD gunicorn -w 2 -b 0.0.0.0:5000 --reload weight:app
