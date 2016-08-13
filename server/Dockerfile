FROM daocloud.io/ubuntu:14.04.1

RUN cp /etc/apt/sources.list /etc/apt/sources.list.bac

RUN echo "deb http://mirrors.163.com/ubuntu/ trusty main restricted universe " > /etc/apt/sources.list
RUN echo "deb http://mirrors.163.com/ubuntu/ trusty-security main restricted universe " >> /etc/apt/sources.list
RUN echo "deb http://mirrors.163.com/ubuntu/ trusty-updates main restricted universe " >> /etc/apt/sources.list
RUN echo "deb http://mirrors.163.com/ubuntu/ trusty-proposed main restricted universe " >> /etc/apt/sources.list
RUN echo "deb http://mirrors.163.com/ubuntu/ trusty-backports main restricted universe " >> /etc/apt/sources.list
RUN echo "deb-src http://mirrors.163.com/ubuntu/ trusty main restricted universe " >> /etc/apt/sources.list
RUN echo "deb-src http://mirrors.163.com/ubuntu/ trusty-security main restricted universe " >> /etc/apt/sources.list
RUN echo "deb-src http://mirrors.163.com/ubuntu/ trusty-updates main restricted universe " >> /etc/apt/sources.list
RUN echo "deb-src http://mirrors.163.com/ubuntu/ trusty-proposed main restricted universe " >> /etc/apt/sources.list
RUN echo "deb-src http://mirrors.163.com/ubuntu/ trusty-backports main restricted universe " >> /etc/apt/sources.list

RUN apt-get update
RUN apt-get install -yq python3 \
	python3-pip 

RUN mkdir /code
ADD server.py /code

WORKDIR /code
RUN pip3 install autobahn redis

EXPOSE 7000

CMD ["/usr/bin/python3", "server.py"]
