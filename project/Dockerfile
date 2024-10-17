# pull official base image
FROM python:3.12.1-slim-bookworm

# set working directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && apt-get -y dist-upgrade \
  && apt-get -y install netcat-traditional gcc postgresql \
  && apt-get clean

# install python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# add app
COPY . .

# add entrypoint.sh
COPY ./entrypoint.sh .
RUN chmod 777 /usr/src/app/entrypoint.sh \
&& ln -s /usr/src/app/entrypoint.sh /

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]