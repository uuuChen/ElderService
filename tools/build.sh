#!/bin/bash

IMAGE_NAME='lobster/elder-service'
docker build -t "$IMAGE_NAME" -f ./tools/dockerfile .