FROM python:3.6

MAINTAINER Andrew.Jackson@bl.uk

WORKDIR /app

COPY ./requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app

ENV PYTHONPATH=/app

ENTRYPOINT ["voila"]

CMD ["/app", "--no-browser", "--Voila.ip=0.0.0.0" ]

