FROM python:3.10-slim

# Prevents Python from writing pyc files to disc (equivalent to python -B option)
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /usr/src/app

# install software
RUN apt update
RUN apt install -y build-essential python3-dev libpq-dev python3-pip


# install dependencies
RUN pip3 install --upgrade pip
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt
