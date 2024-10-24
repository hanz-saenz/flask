FROM ubuntu:22.04
RUN DEBIAN_FRONTEND=noninteractive apt-get -qq update
RUN DEBIAN_FRONTEND=noninteractive apt-get update -qq install -y -u python3 curl openssh-server wget libpcap-dev libpq-dev python3-pip python3-dev python3-setuptools build-essential unzip 

RUN pip3 install --upgrade pip

ADD requirements.txt requirements.txt

RUN pip3 install -r requirements.txt --ignore-installed

WORKDIR /Flask