FROM python:3.6-slim

LABEL version='0.1' maintainer="DevOps cedro team"

ENV PYTHONUNBUFFERED=1 \
    TZ=America/Sao_Paulo

WORKDIR /usr/src/app

RUN pip install --no-cache-dir docker slackclient ; apt-get clean

COPY monitor_container.py ./

ENTRYPOINT [ "python3","-u","./monitor_container.py" ]
