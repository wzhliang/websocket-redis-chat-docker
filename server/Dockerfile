FROM daocloud.io/library/python:3.5.0

RUN apt-get update

RUN mkdir /code
ADD server.py /code

WORKDIR /code
RUN pip3 install autobahn asyncio_redis

EXPOSE 7000

CMD ["/usr/local/bin/python", "-u", "server.py"]
