# Assignment 5: Create REST API using FastAPI

**Course:** AI3206C - MLOps | **Student:** Aditi Rahul Dayma (Roll No: 66, PRN: 12412556)

---

## 🎯 Aim
To build, test, and document a high-throughput, asynchronous REST API using FastAPI and Pydantic schema validation to serve machine learning models with interactive Swagger UI documentation.

## 📋 Problem Statement
Trained machine learning models remain inert unless integrated into operational software systems. Modern production environments require high-throughput, low-latency, and asynchronous RESTful microservices for real-time inference. As an MLOps Engineer, your task is to build a robust REST API using FastAPI with Pydantic schema validation to serve a trained machine learning model, implement health checks and prediction endpoints, and verify interactive documentation via Swagger UI.

---

## 💡 Architecture & Serving Workflow
```
+--------------------------------------------------------------+
|                      FastAPI Serving Engine                  |
|                                                              |
|   +---------------------+        +-----------------------+   |
|   |  Client (cURL / UI) | -----> |    FastAPI Router     |   |
|   +---------------------+        +-----------+-----------+   |
|                                              |               |
|                                              v               |
|                                  +-----------------------+   |
|                                  |   Pydantic Validation |   |
|                                  | (Type checking, range)|   |
|                                  +-----------+-----------+   |
|                                              |               |
|                                              v               |
|                                  +-----------------------+   |
|                                  |   Model Inference     |   |
|                                  |  model.predict_proba  |   |
|                                  +-----------+-----------+   |
|                                              |               |
|   +---------------------+        +-----------+-----------+   |
|   | JSON Output Response| <----- |   HTTP 200 (Success)  |   |
|   | (Class, Confidence) |        +-----------------------+   |
|   +---------------------+                                    |
+--------------------------------------------------------------+
```

---

## 🛠️ Execution Steps
1. **Train Model:**
   ```bash
   python src/train_model.py
   ```
2. **Launch API Server:**
   ```bash
   uvicorn src.app:app --host 0.0.0.0 --port 8000 --reload
   ```
3. **Health Check:**
   ```bash
   curl http://localhost:8000/health
   ```
4. **Send Inference Request:**
   ```bash
   curl -X POST "http://localhost:8000/predict" \
        -H "Content-Type: application/json" \
        -d '{"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}'
   ```
5. **Interactive Docs:** Visit `http://localhost:8000/docs` in your browser.
