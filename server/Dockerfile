FROM davidjfelix/python3.5

RUN apt-get update
# RUN apt-get install python3 python3-pip

RUN mkdir /code
ADD server.py /code

WORKDIR /code
RUN pip3 install autobahn asyncio_redis

EXPOSE 7000

CMD ["/usr/local/bin/python", "-u", "server.py"]
