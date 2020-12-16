#!/bin/bash

docker rm $(docker ps -aq --filter="status=exited")
docker rmi $(docker images | grep none | awk '{print $3}')
