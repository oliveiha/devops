FROM python:3.6-slim

LABEL version='0.1' maintainer="DevOps cedro team"

ENV PYTHONUNBUFFERED=1 \
    TZ=America/Sao_Paulo \
    PYTHONHTTPSVERIFY=0

RUN pip install --no-cache-dir python-jenkins ; pip install --no-cache-dir xmltodict ; apt-get clean

WORKDIR /usr/src/app

COPY import_jobs.py *.txt ./

ENTRYPOINT [ "python3","-u","./import_jobs.py" ]
