from pydantic import BaseModel, Field
from typing import List

class IrisFeatures(BaseModel):
    sepal_length: float = Field(..., gt=0, lt=10, example=5.1)
    sepal_width: float = Field(..., gt=0, lt=10, example=3.5)
    petal_length: float = Field(..., gt=0, lt=10, example=1.4)
    petal_width: float = Field(..., gt=0, lt=10, example=0.2)

class PredictionResponse(BaseModel):
    class_id: int
    class_name: str
    confidence: float

class BatchIrisFeatures(BaseModel):
    samples: List[IrisFeatures]

class BatchPredictionResponse(BaseModel):
    predictions: List[PredictionResponse]
