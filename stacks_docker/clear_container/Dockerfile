FROM python:3.6-slim

LABEL version='0.1' maintainer="DevOps cedro team"

ENV PYTHONUNBUFFERED=1 \
    TZ=America/Sao_Paulo

RUN pip install --no-cache-dir docker ; apt-get clean

WORKDIR /usr/src/app

COPY clear_container.py ./

ENTRYPOINT [ "python3","-u","./clear_container.py" ]
