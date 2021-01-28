FROM ubuntu:16.04

RUN apt-get update -y && \
    apt-get install -y python3 python3-pip && \
    pip3 install flask && \
    pip3 install requests

EXPOSE 5000
COPY nnrf-disc.py /nnrf-disc.py

ENTRYPOINT ["python3", "/nnrf-disc.py"]

CMD []
