FROM daocloud.io/nginx:latest

COPY nginx.conf /etc/nginx/nginx.conf

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

EXPOSE 80
