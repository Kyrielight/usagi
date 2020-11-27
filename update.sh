#!/bin/bash

OLD_IMAGE_ID=$(docker images --filter=reference=usagi --format "{{.ID}}")
docker rm -f usagi
git pull
./build.sh
./start.sh
docker rmi "$OLD_IMAGE_ID"