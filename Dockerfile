FROM python:3.8.6-alpine

LABEL MAINTAINER="kyrielight@best.moe"

COPY src /usagi
RUN pip3 install --no-cache-dir -r /usagi/requirements.txt

WORKDIR /usagi
ENTRYPOINT ["python3", "usagi.py"]
