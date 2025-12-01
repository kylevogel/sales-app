#!/usr/bin/env bash

set -e

IMAGE_NAME="sales-app"
PORT=8080

echo ">>> Building Docker image: $IMAGE_NAME"
docker build -t $IMAGE_NAME .

echo ">>> Running Docker container on http://localhost:$PORT"
docker run --rm -p $PORT:$PORT $IMAGE_NAME
