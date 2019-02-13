FROM python:3.6-slim

LABEL version='0.1' maintainer="DevOps cedro team"

ENV PYTHONUNBUFFERED=1 \
    TZ=America/Sao_Paulo \
    PYTHONHTTPSVERIFY=0

RUN pip install --no-cache-dir python-jenkins ; apt-get clean

WORKDIR /usr/src/app

COPY start_all_jobs.py ./

ENTRYPOINT [ "python3","-u","./start_all_jobs.py" ]
