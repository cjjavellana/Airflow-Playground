FROM python:latest

ENV AIRFLOW_HOME=/app/airflow

RUN mkdir -p /app/airflow && \
	pip install PyMySQL 'apache-airflow[mysql,dask,celery,rabbitmq,redis,ldap,ssh]'

ADD airflow.cfg /app/airflow
ADD run.sh /app/airflow

WORKDIR /app/airflow

#ENTRYPOINT ["./run.sh"]
