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

2. Search LDAP

		Ensure ldap container is up
		```bash
		$ docker-compose up -d ldap
		```

		Get Bash in Ldap container
		```bash
		$ docker-compose exec ldap /bin/bash
		```

		Search LDAP
		```bash
		(in container) $ ldapsearch -x -b dc=cjavellana,dc=me -h localhost -D "cn=admin,dc=cjavellana,dc=me" -w secret
		```
