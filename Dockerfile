FROM python:3.8

MAINTAINER Andrew.Jackson@bl.uk

WORKDIR /app

COPY ./requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app

ENV PYTHONPATH=/app

ENTRYPOINT ["voila"]

#CMD ["/app", "--template=gridstack"]
#CMD ["/app", "--template=material"]
CMD ["/app", "--no-browser"]

