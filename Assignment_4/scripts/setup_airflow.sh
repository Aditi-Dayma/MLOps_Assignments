#!/bin/bash
# Setup Apache Airflow environment

export AIRFLOW_HOME=~/airflow
mkdir -p $AIRFLOW_HOME/dags

# Initialize Database
airflow db init

# Create Admin User
airflow users create \
    --username admin \
    --firstname Aditi \
    --lastname Dayma \
    --role Admin \
    --email daymaaditi60@gmail.com \
    --password admin

# Copy DAG file
cp dags/ml_pipeline_dag.py $AIRFLOW_HOME/dags/

# Test Individual Task Execution
airflow tasks test mlops_iris_training_pipeline ingest_data 2026-01-01
airflow tasks test mlops_iris_training_pipeline train_model 2026-01-01

echo "Airflow setup and task testing verified."
