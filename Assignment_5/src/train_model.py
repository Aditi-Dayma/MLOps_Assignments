import os
import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

def train_and_export():
    iris = load_iris()
    X, y = iris.data, iris.target
    
    clf = RandomForestClassifier(n_estimators=50, random_state=42)
    clf.fit(X, y)
    
    os.makedirs("models", exist_ok=True)
    out_path = "models/iris_classifier.pkl"
    joblib.dump(clf, out_path)
    print(f"Model trained and saved to {out_path}")

if __name__ == "__main__":
    train_and_export()
