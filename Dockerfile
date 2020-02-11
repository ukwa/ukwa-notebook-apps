FROM python:3

MAINTAINER Andrew.Jackson@bl.uk

WORKDIR /app

COPY ./requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT ["voila"]

#CMD ["/app", "--template=gridstack"]
CMD ["/app", "--template=material"]

