# Assignment 8: Monitor Model using Prometheus and Grafana

**Course:** AI3206C - MLOps | **Student:** Aditi Rahul Dayma (Roll No: 66, PRN: 12412556)

---

## 🎯 Aim
To instrument a real-time machine learning inference service with Prometheus telemetry (Counters, Gauges, Histograms), configure metric scraping, and build an observability dashboard in Grafana to monitor latency, traffic, and prediction distribution.

## 📋 Problem Statement
Once a machine learning model is deployed to production, factors like data drift, concept drift, changing user traffic, and server latency can severely impair model reliability. Without real-time observability, silent model failures go undetected. As an MLOps Engineer, your task is to instrument a machine learning inference microservice with Prometheus metrics (request counters, latency histograms, prediction distribution gauges), configure Prometheus metrics scraping, and build an observability dashboard in Grafana.

---

## 💡 Observability Stack Architecture
```
+--------------------------------------------------------------+
|                Observability Monitoring Stack                |
|                                                              |
|   +--------------------+                                     |
|   | FastAPI ML Service | (Exposes /metrics on port 8000)     |
|   | - Requests Counter |                                     |
|   | - Latency Histogram|                                     |
|   | - Accuracy Gauge   |                                     |
|   +---------+----------+                                     |
|             |                                                |
|             | HTTP Scrape (/metrics every 5s)                |
|             v                                                |
|   +--------------------+                                     |
|   | Prometheus Engine  | (Stores Time-Series Data on :9090)  |
|   | - PromQL Querying  |                                     |
|   +---------+----------+                                     |
|             |                                                |
|             | PromQL Queries                                 |
|             v                                                |
|   +--------------------+                                     |
|   | Grafana Dashboard  | (Visual Dashboards on :3000)        |
|   | - Latency P99/P95  |                                     |
|   | - Request Throughput                                     |
|   | - Online Accuracy  |                                     |
|   +--------------------+                                     |
+--------------------------------------------------------------+
```

---

## 🛠️ Execution Steps
1. **Start FastAPI Application:**
   ```bash
   uvicorn src.app:app --host 0.0.0.0 --port 8000 --reload
   ```
2. **Start Monitoring Stack:**
   ```bash
   docker-compose up -d
   ```
3. **Generate Traffic:**
   ```bash
   python scripts/traffic_generator.py
   ```
4. **Inspect Prometheus Metrics:**
   Open `http://localhost:9090` and run PromQL:
   ```promql
   rate(http_requests_total[1m])
   model_prediction_latency_seconds_bucket
   model_online_accuracy
   ```
5. **Inspect Grafana Dashboard:**
   Open `http://localhost:3000` (User: `admin` / Password: `admin`), add Prometheus datasource (`http://prometheus:9090`), and import latency/throughput panels.
