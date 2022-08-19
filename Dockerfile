FROM ubuntu

COPY . /src

RUN apt-get update 
RUN apt-get install -y python3 pip

WORKDIR /src

RUN python3 -m pip install -r ./requirements.txt 

CMD python3 main.py