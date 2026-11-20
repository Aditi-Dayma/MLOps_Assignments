import pytest
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from src.model import CancerClassifier

@pytest.fixture
def dataset():
    data = load_breast_cancer()
    return train_test_split(data.data, data.target, test_size=0.2, random_state=42)

def test_model_training_and_accuracy(dataset):
    X_train, X_test, y_train, y_test = dataset
    model = CancerClassifier()
    model.train(X_train, y_train)
    
    accuracy = model.evaluate(X_test, y_test)
    print(f"Test Accuracy: {accuracy}")
    # Enforce quality gate: accuracy must exceed 90%
    assert accuracy >= 0.90, f"Model performance failed quality gate: {accuracy}"

def test_prediction_output_shape(dataset):
    X_train, X_test, y_train, y_test = dataset
    model = CancerClassifier()
    model.train(X_train, y_train)
    
    preds = model.predict(X_test[:5])
    assert len(preds) == 5
    assert set(preds).issubset({0, 1})
