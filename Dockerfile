FROM python:3.8.6-alpine

LABEL MAINTAINER="kyrielight@best.moe"

COPY src/requirements.txt /opt/requirements.txt
RUN pip3 install --no-cache-dir -r /opt/requirements.txt && rm /opt/requirements.txt

COPY src /usagi

WORKDIR /usagi
ENTRYPOINT ["python3", "usagi.py"]
