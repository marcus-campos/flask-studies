FROM ubuntu:latest
MAINTAINER Marcus Vinícius Campos "campos.v.marcus@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python3-pip python3 build-essential
RUN pip3 install Flask
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
EXPOSE 80