FROM python:3.6-slim
MAINTAINER "DevOps cedro team"

ENV PYTHONUNBUFFERED 1
ENV TZ=America/Sao_Paulo

WORKDIR /usr/src/app

RUN pip install --no-cache-dir docker ; apt-get clean

COPY img_date.py ./

ENTRYPOINT [ "python3","-u","./img_date.py" ]
