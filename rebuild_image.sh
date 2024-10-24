#!/bin/bash -e

sudo chmod -R ${USER}:${USER} .
# rm -Rf .docker/tmp/base/
# mkdir -p .docker/tmp/base/.docker;
# cp Dockerfile .docker/tmp/base/Dockerfile;
# cp requeriments.txt .docker/tmp/base/requeriments.txt;
docker build --tag flask-app .;
# rm -Rf .docker
# cd ../../../