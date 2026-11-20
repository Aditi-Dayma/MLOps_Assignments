import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_health():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json()["status"] == "healthy"

def test_predict_setosa():
    payload = {
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2
    }
    res = client.post("/predict", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert data["class_name"] == "setosa"
    assert data["confidence"] > 0.8

def test_invalid_input():
    payload = {
        "sepal_length": -10.0, # invalid negative value
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2
    }
    res = client.post("/predict", json=payload)
    assert res.status_code == 422 # Pydantic Validation Error
