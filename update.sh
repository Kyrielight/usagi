#!/bin/bash

docker rm -f "usagi"
git pull
./build.sh
./start.sh