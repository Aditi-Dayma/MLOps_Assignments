import os
import joblib
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def train_tabular_classifier():
    data = load_breast_cancer(as_frame=True)
    X, y = data.data, data.target
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    clf = RandomForestClassifier(n_estimators=100, random_state=42, max_depth=5)
    clf.fit(X_train, y_train)
    
    os.makedirs("models", exist_ok=True)
    joblib.dump(clf, "models/rf_classifier.pkl")
    X_test.to_csv("models/X_test.csv", index=False)
    y_test.to_csv("models/y_test.csv", index=False)
    print("Random Forest classifier trained and test datasets saved.")

if __name__ == "__main__":
    train_tabular_classifier()
