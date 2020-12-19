# Airflow Playground
A playground for playing around with various Airflow deployment architectures.

## Architecture

![Architecture](/docs/architecture.png?raw=true "Architecture")

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

Logging in as Admin
```
1. Open your browser and navigate to http://localhost:8080
2. Enter credentials
		username: admin
		password: secret
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

```bash
# Search
(in container) $ ldapsearch -x -b dc=cjavellana,dc=me -h localhost -D "cn=admin,dc=cjavellana,dc=me" -w secret
# Showing user's group membership
(in container) $ ldapsearch -x -b dc=cjavellana,dc=me -h localhost -D "cn=admin,dc=cjavellana,dc=me" -w secret memberof
```

3. Stopping Airflow Services
```
$ docker-compose stop web scheduler ldap
$ vagrant halt
```
