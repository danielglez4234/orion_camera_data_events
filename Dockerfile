FROM python:3.8-slim-buster

WORKDIR /orion_camera_data_events

COPY requirements.txt requirements.txt

RUN apt-get update

RUN apt-get -y install curl libcurl4-openssl-dev libssl-dev gcc

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "DahuaAPI.py"]