import time
import random
from fastapi import FastAPI, Response
from prometheus_client import Counter, Histogram, Gauge, generate_latest, CONTENT_TYPE_LATEST

app = FastAPI(title="ML Service with Prometheus Instrumentation", version="1.0.0")

# Prometheus Metrics Definitions
REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total count of HTTP inference requests",
    ["method", "endpoint", "status"]
)

REQUEST_LATENCY = Histogram(
    "model_prediction_latency_seconds",
    "Inference latency distribution in seconds",
    ["endpoint"],
    buckets=[0.01, 0.05, 0.1, 0.25, 0.5, 1.0, 2.5]
)

MODEL_ACCURACY_GAUGE = Gauge(
    "model_online_accuracy",
    "Estimated rolling online accuracy of inference predictions"
)

PREDICTION_DISTRIBUTION = Counter(
    "model_predictions_total",
    "Total predictions classified per category",
    ["predicted_class"]
)

@app.get("/")
def index():
    return {"message": "Instrumented ML Service. Scrape /metrics"}

@app.get("/metrics")
def get_metrics():
    return Response(content=generate_latest(), media_type=CONTENT_TYPE_LATEST)

@app.post("/predict")
def predict_endpoint():
    start_time = time.time()
    
    # Simulate inference latency
    simulated_delay = random.uniform(0.02, 0.15)
    time.sleep(simulated_delay)
    
    # Simulate predicted class
    classes = ["class_0", "class_1", "class_2"]
    pred = random.choice(classes)
    
    duration = time.time() - start_time
    
    # Record Prometheus metrics
    REQUEST_COUNT.labels(method="POST", endpoint="/predict", status="200").inc()
    REQUEST_LATENCY.labels(endpoint="/predict").observe(duration)
    PREDICTION_DISTRIBUTION.labels(predicted_class=pred).inc()
    
    # Simulate slight fluctuation in online accuracy gauge
    current_acc = 0.92 + random.uniform(-0.03, 0.03)
    MODEL_ACCURACY_GAUGE.set(round(current_acc, 4))
    
    return {
        "prediction": pred,
        "latency_seconds": round(duration, 4),
        "status": "success"
    }
