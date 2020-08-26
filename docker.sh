#!/bin/bash

set -e

docker build -t mariuss/eslog .
docker run --rm mariuss/eslog
