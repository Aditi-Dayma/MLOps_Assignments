# Assignment 4: Build Workflow Automation using Apache Airflow

**Course:** AI3206C - MLOps | **Student:** Aditi Rahul Dayma (Roll No: 66, PRN: 12412556)

---

## 🎯 Aim
To design, implement, and orchestrate an automated Machine Learning pipeline DAG (Directed Acyclic Graph) using Apache Airflow, schedule recurring pipeline runs, and monitor workflow execution states.

## 📋 Problem Statement
Executing end-to-end machine learning workflows -- from data ingestion, validation, and preprocessing to model training and evaluation -- manually is time-consuming, prone to failures, and difficult to monitor. As an MLOps Engineer, your task is to design, implement, and orchestrate an automated Machine Learning pipeline DAG (Directed Acyclic Graph) using Apache Airflow, define task dependencies, schedule automated runs, and monitor workflow execution and task state.

---

## 💡 Architecture & DAG Flow
```
+--------------------------------------------------------------+
|                Airflow DAG Pipeline Flow                     |
|                                                              |
|   +---------------------+        +-----------------------+   |
|   |   Airflow Webserver |        |   Airflow Scheduler   |   |
|   |   (Port 8080 UI)    |        | (Heartbeat / Triggers)|   |
|   +----------+----------+        +-----------+-----------+   |
|              |                               |               |
|              +---------------+---------------+               |
|                              |                               |
|                              v                               |
|                  +-----------------------+                   |
|                  |     SQLite / PG DB    |                   |
|                  | (DAG Metadata / State)|                   |
|                  +-----------+-----------+                   |
|                              |                               |
|                              v                               |
|   +------------------------------------------------------+   |
|   |                  ml_pipeline_dag                     |   |
|   |                                                      |   |
|   |  [ ingest_data ] ---> [ preprocess_data ]            |   |
|   |                             |                        |   |
|   |                             v                        |   |
|   |  [ evaluate_model ] <--- [ train_model ]             |   |
|   +------------------------------------------------------+   |
+--------------------------------------------------------------+
```

---

## 🛠️ Execution Steps
1. **Setup Airflow Home:** `export AIRFLOW_HOME=~/airflow`
2. **Initialize Database:** `airflow db init`
3. **Create Admin User:** `airflow users create --username admin ...`
4. **Copy DAG:** Place `dags/ml_pipeline_dag.py` in `$AIRFLOW_HOME/dags/`.
5. **Validate Syntax:** `python dags/ml_pipeline_dag.py`
6. **Test Task CLI:** `airflow tasks test mlops_iris_training_pipeline ingest_data 2026-01-01`
7. **Start Server:** `airflow webserver -p 8080` & `airflow scheduler`
8. **Trigger Run:** `airflow dags trigger mlops_iris_training_pipeline`
