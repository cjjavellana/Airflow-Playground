FROM python:latest

ENV AIRFLOW_HOME=/app/airflow

RUN mkdir -p /app/airflow && \
	apt-get update -y && \
	apt-get install -y python-dev libldap2-dev libsasl2-dev libssl-dev && \
	apt-get install vim -y && \
	pip install python-ldap && \
	pip install PyMySQL 'apache-airflow[mysql,dask,celery,rabbitmq,redis,ldap,ssh]'

ADD airflow.cfg /app/airflow
ADD run.sh /app/airflow

WORKDIR /app/airflow

#ENTRYPOINT ["./run.sh"]
