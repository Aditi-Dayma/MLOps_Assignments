import os
import joblib
import numpy as np
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Containerized ML Inference API", version="1.0.0")

class Features(BaseModel):
    sepal_length: float = Field(..., gt=0, example=6.2)
    sepal_width: float = Field(..., gt=0, example=3.4)
    petal_length: float = Field(..., gt=0, example=5.4)
    petal_width: float = Field(..., gt=0, example=2.3)

MODEL = None
CLASS_NAMES = ["setosa", "versicolor", "virginica"]

@app.on_event("startup")
def load_model():
    global MODEL
    model_path = os.getenv("MODEL_PATH", "model.pkl")
    if os.path.exists(model_path):
        MODEL = joblib.load(model_path)
    else:
        from sklearn.datasets import load_iris
        from sklearn.ensemble import RandomForestClassifier
        iris = load_iris()
        clf = RandomForestClassifier(n_estimators=50, random_state=42)
        clf.fit(iris.data, iris.target)
        MODEL = clf

@app.get("/health")
def health():
    return {"status": "healthy", "container": "docker_isolated"}

@app.post("/predict")
def predict(features: Features):
    vec = np.array([[features.sepal_length, features.sepal_width, features.petal_length, features.petal_width]])
    pred_idx = int(MODEL.predict(vec)[0])
    confidence = float(MODEL.predict_proba(vec)[0][pred_idx])
    return {
        "class_id": pred_idx,
        "class_name": CLASS_NAMES[pred_idx],
        "confidence": round(confidence, 4)
    }
