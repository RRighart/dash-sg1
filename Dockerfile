FROM python:3.5

USER root

RUN mkdir /usr/src/dashapp
WORKDIR /usr/src/dashapp
ADD requirements.txt /usr/src/dashapp

RUN pip install --trusted-host pypi.python.org -r requirements.txt

ADD . /usr/src/dashapp
ADD . .

CMD ["gunicorn", "-b", "0.0.0.0:8080", "wsgi:server"]
