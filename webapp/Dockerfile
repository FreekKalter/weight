FROM python:3.6

ADD instance /code/instance
ADD weight /code/weight
ADD run.py /code

WORKDIR /code
RUN pip install -r weight/requirements.txt
CMD python run.py --host=0.0.0.0
