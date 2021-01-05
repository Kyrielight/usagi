#!/bin/bash

docker run -d \
    --name "usagi" \
    --log-opt max-size=5m \
    --log-opt max-file=2 \
    usagi