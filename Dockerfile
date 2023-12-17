FROM ubuntu

COPY . /opt/myblog/

WORKDIR /opt/myblog/

RUN apt-get update
RUN apt-get install -y python3.9 python3-pip
RUN apt-get install -y pkg-config
RUN apt-get install -y libmysqlclient-dev

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

ENV PYTHONPATH=/opt/myblog/

ENTRYPOINT ["python3", "main.py"]

