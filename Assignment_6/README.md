# Assignment 6: Containerize ML Model using Docker

**Course:** AI3206C - MLOps | **Student:** Aditi Rahul Dayma (Roll No: 66, PRN: 12412556)

---

## 🎯 Aim
To containerize a machine learning inference microservice using Docker, create an optimized multi-stage Dockerfile, build the image, run and isolate the container, and test real-time inference over HTTP.

## 📋 Problem Statement
Deployment discrepancies often arise from environment inconsistencies ("it works on my machine" problem). Containerization encapsulates the ML application, runtime, operating system dependencies, and trained model weights into a self-contained image. As an MLOps Engineer, your task is to containerize a FastAPI ML inference application using Docker, create an optimized Dockerfile, build the container image, run and isolate the container, and test inference requests against the containerized application.

---

## 💡 Multi-Stage Docker Architecture
```
+--------------------------------------------------------------+
|                Multi-Stage Docker Architecture               |
|                                                              |
|   [ Stage 1: Builder ]                                       |
|   +------------------------------------------------------+   |
|   | python:3.10-slim + gcc compilation tools             |   |
|   | pip install --user -r requirements.txt               |   |
|   +--------------------------+---------------------------+   |
|                              |                               |
|                              | Artifact Copy                 |
|                              v                               |
|   [ Stage 2: Final Minimal Image ]                           |
|   +------------------------------------------------------+   |
|   | python:3.10-slim (No compilers, minimal footprint)   |   |
|   | COPY /root/.local (Lightweight dependencies)         |   |
|   | COPY app/ (main.py, model.pkl)                       |   |
|   | EXPOSE 8000                                          |   |
|   | HEALTHCHECK: /health                                 |   |
|   | CMD: uvicorn main:app                                |   |
|   +------------------------------------------------------+   |
+--------------------------------------------------------------+
```

---

## 🛠️ Execution Steps
1. **Build Container Image:**
   ```bash
   docker build -t ml-inference-service:v1.0 .
   ```
2. **Verify Built Image:**
   ```bash
   docker images
   ```
3. **Launch Container:**
   ```bash
   docker run -d -p 8000:8000 --name ml-inference-container ml-inference-service:v1.0
   ```
4. **Test Prediction:**
   ```bash
   curl -X POST "http://localhost:8000/predict" \
        -H "Content-Type: application/json" \
        -d '{"sepal_length": 6.2, "sepal_width": 3.4, "petal_length": 5.4, "petal_width": 2.3}'
   ```
5. **Clean Up:**
   ```bash
   docker stop ml-inference-container && docker rm ml-inference-container
   ```
