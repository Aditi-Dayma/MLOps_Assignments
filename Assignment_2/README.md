# Assignment 2: Track ML Experiments using MLflow

**Course:** AI3206C - MLOps | **Student:** Aditi Rahul Dayma (Roll No: 66, PRN: 12412556)

---

## 🎯 Aim
To track machine learning experiments, log parameters, evaluation metrics, and artifacts, and register the optimal model into the MLflow Model Registry for production lifecycle management.

## 📋 Problem Statement
A machine learning team is training several classification models and needs to systematically track experiments, compare hyperparameter variations, and log evaluation metrics. Without an automated experiment tracking tool, managing different training runs and model iterations becomes cumbersome and non-reproducible. As an MLOps Engineer, your task is to implement experiment tracking using MLflow to record parameters, evaluation metrics (accuracy, F1-score), model artifacts, and register the optimal model into the MLflow Model Registry.

---

## 💡 Architecture & Workflow
```
+-----------------------------------------------------------+
|                     MLflow Architecture                   |
|                                                           |
|    +-------------------+        +--------------------+    |
|    |   train.py Run    |        | MLflow Tracking API|    |
|    | (Hyperparameters) | -----> | log_param(),       |    |
|    |   (Evaluation)    |        | log_metric(),      |    |
|    |    (Artifacts)    |        | log_model()        |    |
|    +-------------------+        +---------+----------+    |
|                                           |               |
|                                           v               |
|                                 +--------------------+    |
|                                 |   mlruns / SQLite  |    |
|                                 | (Experiment Store) |    |
|                                 +---------+----------+    |
|                                           |               |
|             +-----------------------------+               |
|             |                             |               |
|             v                             v               |
|   +-------------------+         +--------------------+    |
|   |  MLflow UI (:5000)|         |   Model Registry   |    |
|   | Run Comparison &  |         | Staging -> Prod    |    |
|   | Visual Artifacts  |         | Model Versioning   |    |
|   +-------------------+         +--------------------+    |
+-----------------------------------------------------------+
```

---

## 🛠️ Execution Steps
1. **Setup Environment:** Install dependencies `pip install -r requirements.txt`.
2. **Execute Baseline Run:**
   ```bash
   python src/train.py --n_estimators 10 --max_depth 3
   ```
3. **Execute Tuned Run:**
   ```bash
   python src/train.py --n_estimators 100 --max_depth 10
   ```
4. **Inspect Runs via CLI:**
   ```bash
   mlflow experiments list
   ```
5. **Launch MLflow UI:**
   ```bash
   mlflow ui --port 5000
   ```
6. **Register Model & Transition Stage:**
   ```bash
   python src/model_registry.py
   ```
7. **Serve Production Model:**
   ```bash
   mlflow models serve -m "models:/WineQualityClassifier/Production" -p 5001 --no-conda
   ```
