import argparse
import os
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_wine
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix, ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
import mlflow
import mlflow.sklearn

def train_model(n_estimators, max_depth, random_state=42):
    # Set experiment
    mlflow.set_experiment("Wine_Classification_Tracking")
    
    with mlflow.start_run():
        # Load dataset
        data = load_wine()
        X, y = data.data, data.target
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.25, random_state=random_state, stratify=y
        )
        
        # Log parameters
        mlflow.log_param("n_estimators", n_estimators)
        mlflow.log_param("max_depth", max_depth)
        mlflow.log_param("dataset", "Wine")
        mlflow.log_param("test_size", 0.25)
        
        # Train model
        clf = RandomForestClassifier(
            n_estimators=n_estimators,
            max_depth=max_depth,
            random_state=random_state
        )
        clf.fit(X_train, y_train)
        
        # Evaluate model
        preds = clf.predict(X_test)
        acc = accuracy_score(y_test, preds)
        f1 = f1_score(y_test, preds, average="weighted")
        
        # Log metrics
        mlflow.log_metric("accuracy", acc)
        mlflow.log_metric("f1_score", f1)
        print(f"Run completed -> n_estimators: {n_estimators}, max_depth: {max_depth} | Acc: {acc:.4f}, F1: {f1:.4f}")
        
        # Log Confusion Matrix Artifact
        os.makedirs("artifacts", exist_ok=True)
        cm = confusion_matrix(y_test, preds)
        disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=data.target_names)
        fig, ax = plt.subplots(figsize=(6, 5))
        disp.plot(ax=ax, cmap="Blues")
        plt.title(f"Confusion Matrix (n_estimators={n_estimators})")
        cm_path = "artifacts/confusion_matrix.png"
        plt.savefig(cm_path)
        plt.close()
        mlflow.log_artifact(cm_path)
        
        # Log model
        mlflow.sklearn.log_model(
            sk_model=clf,
            artifact_path="random_forest_model",
            registered_model_name="WineQualityClassifier"
        )

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--n_estimators", type=int, default=50)
    parser.add_argument("--max_depth", type=int, default=5)
    args = parser.parse_args()
    
    train_model(args.n_estimators, args.max_depth)
