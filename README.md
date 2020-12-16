# Airflow Playground
A playground for playing around with various Airflow deployment architectures.

## Architecture
TODO

## Prerequisites

1. Vagrant
2. docker-compose

## Getting Started

Starting the Worker Virtual Machine
```bash
$ vagrant up
``` 

Starting the WebServer and Scheduler
```bash
$ docker-compose up -d web scheduler
```
## FAQ

1. Want to cleanup exited containers and dangling images?

```bash
$ ./cleanup.sh
```
