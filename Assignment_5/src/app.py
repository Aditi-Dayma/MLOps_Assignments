import os
import joblib
import numpy as np
from fastapi import FastAPI, HTTPException, status
from src.schemas import IrisFeatures, PredictionResponse, BatchIrisFeatures, BatchPredictionResponse

app = FastAPI(
    title="ML Model Inference Microservice",
    description="Production-grade asynchronous REST API for ML predictions with Pydantic validation",
    version="1.0.0"
)

# Global model state
MODEL = None
CLASS_NAMES = ["setosa", "versicolor", "virginica"]

@app.on_event("startup")
def load_model():
    global MODEL
    model_path = "models/iris_classifier.pkl"
    if not os.path.exists(model_path):
        model_path = "Assignment_5/models/iris_classifier.pkl"
    if os.path.exists(model_path):
        MODEL = joblib.load(model_path)
        print("Model loaded into memory successfully.")
    else:
        from sklearn.datasets import load_iris
        from sklearn.ensemble import RandomForestClassifier
        iris = load_iris()
        clf = RandomForestClassifier(n_estimators=50, random_state=42)
        clf.fit(iris.data, iris.target)
        MODEL = clf
        print("Model trained on startup as fallback.")

@app.get("/", tags=["General"])
def root():
    return {
        "service": "ML Inference API",
        "status": "running",
        "docs_url": "/docs"
    }

@app.get("/health", tags=["Health"])
def health_check():
    if MODEL is None:
        raise HTTPException(status_code=503, detail="Model artifact unavailable")
    return {"status": "healthy", "model_loaded": True}

@app.post("/predict", response_model=PredictionResponse, tags=["Inference"])
def predict(features: IrisFeatures):
    if MODEL is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    input_vector = np.array([[
        features.sepal_length,
        features.sepal_width,
        features.petal_length,
        features.petal_width
    ]])
    
    pred_idx = int(MODEL.predict(input_vector)[0])
    probs = MODEL.predict_proba(input_vector)[0]
    confidence = float(probs[pred_idx])
    
    return PredictionResponse(
        class_id=pred_idx,
        class_name=CLASS_NAMES[pred_idx],
        confidence=round(confidence, 4)
    )

@app.post("/predict_batch", response_model=BatchPredictionResponse, tags=["Inference"])
def predict_batch(batch: BatchIrisFeatures):
    if MODEL is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    results = []
    for sample in batch.samples:
        vec = np.array([[sample.sepal_length, sample.sepal_width, sample.petal_length, sample.petal_width]])
        pred_idx = int(MODEL.predict(vec)[0])
        conf = float(MODEL.predict_proba(vec)[0][pred_idx])
        results.append(PredictionResponse(
            class_id=pred_idx,
            class_name=CLASS_NAMES[pred_idx],
            confidence=round(conf, 4)
        ))
    return BatchPredictionResponse(predictions=results)
