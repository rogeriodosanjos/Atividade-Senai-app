FROM ubuntu:latest

ARG VERSAO=1.0.0
ARG IAC_PATH="/usr/src/app"

COPY README.md Dockerfile ${IAC_PATH}/

ENV \
    VERSAO="${VERSAO}"

WORKDIR ${IAC_PATH}

ADD requirements.txt .

RUN \
    apt update \
    && apt install \
	python3 \
	python3-pip -y \
    && pip3 install -r requirements.txt \
    && mkdir -p ${IAC_PATH}

COPY app.py .

EXPOSE 5000

ENTRYPOINT [ "python3", "app.py" ]
