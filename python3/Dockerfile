FROM python:3.7
RUN mkdir -p /work
WORKDIR /work
ADD requirements.txt /work
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

WORKDIR /work/src
CMD ["uwsgi","--ini","/work/uwsgi.ini"]