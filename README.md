# MLOps Lab Assignments (AI3206C)

**Course:** AI3206C - Machine Learning Operations (MLOps)  
**Academic Year:** 2026-27 | **Semester:** Sem - V  
**Department:** Artificial Intelligence and Data Science  
**Institution:** Vishwakarma Institute of Technology (VIT Pune)  
**Student Name:** Aditi Rahul Dayma  
**Roll No:** 66 | **PRN:** 12412556 | **Class:** TY - Division A  

---

## 📚 Repository Overview

This repository contains the complete implementation, source code, automation scripts, Dockerfiles, and CI/CD pipelines for all 10 MLOps lab assignments. Each folder is organized modularly to illustrate core principles across the machine learning lifecycle: data versioning, experiment tracking, feature engineering, pipeline orchestration, model serving, containerization, continuous integration/delivery, production observability, explainability, and cloud deployments.

---

## 🗂️ Assignment Index

| No. | Title | Core Technologies | Directory |
|---|---|---|---|
| **1** | **Data Version Control (DVC) for Dataset Management** | Git, DVC, CSV Data Versioning | [`Assignment_1/`](./Assignment_1) |
| **2** | **Track ML Experiments using MLflow** | MLflow, Scikit-Learn, Model Registry | [`Assignment_2/`](./Assignment_2) |
| **3** | **Automated Feature Engineering Pipeline** | Scikit-Learn Pipeline, ColumnTransformer | [`Assignment_3/`](./Assignment_3) |
| **4** | **Workflow Automation using Apache Airflow** | Apache Airflow, DAGs, PythonOperator | [`Assignment_4/`](./Assignment_4) |
| **5** | **REST API Serving using FastAPI** | FastAPI, Uvicorn, Pydantic, Swagger UI | [`Assignment_5/`](./Assignment_5) |
| **6** | **Containerize ML Model using Docker** | Docker, Multi-Stage Builds, FastAPI | [`Assignment_6/`](./Assignment_6) |
| **7** | **CI/CD Pipeline using GitHub Actions** | GitHub Actions, PyTest, Flake8, Docker | [`Assignment_7/`](./Assignment_7) |
| **8** | **Model Monitoring using Prometheus & Grafana** | Prometheus Client, Grafana, Docker Compose | [`Assignment_8/`](./Assignment_8) |
| **9** | **Model Explainability using SHAP & LIME** | SHAP, LIME, TreeExplainer, Local Surrogates | [`Assignment_9/`](./Assignment_9) |
| **10** | **Train & Deploy ML Model using AWS SageMaker** | AWS SageMaker, Boto3, AWS S3, Real-time Endpoints | [`Assignment_10/`](./Assignment_10) |

---

## ⚙️ Environment Setup

To run any assignment locally, clone the repository and set up a virtual environment:

```bash
git clone https://github.com/Aditi-Dayma/MLOps_Assignments.git
cd MLOps_Assignments
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate
```

Each assignment directory contains its own `requirements.txt` and specific instructions in its `README.md`.
