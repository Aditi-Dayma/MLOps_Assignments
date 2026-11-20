from datetime import datetime, timedelta
import os
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

try:
    from airflow import DAG
    from airflow.operators.python import PythonOperator
except ImportError:
    # Lightweight mock for standalone environments
    pass

DATA_DIR = "/tmp/airflow_ml_data"

def ingest_data(**kwargs):
    os.makedirs(DATA_DIR, exist_ok=True)
    iris = load_iris(as_frame=True)
    df = iris.frame
    raw_path = os.path.join(DATA_DIR, "raw_data.csv")
    df.to_csv(raw_path, index=False)
    print(f"Data ingestion successful -> {raw_path} with {len(df)} records")

def preprocess_data(**kwargs):
    raw_path = os.path.join(DATA_DIR, "raw_data.csv")
    df = pd.read_csv(raw_path)
    X = df.drop(columns=["target"])
    y = df["target"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    X_train.to_csv(os.path.join(DATA_DIR, "X_train.csv"), index=False)
    X_test.to_csv(os.path.join(DATA_DIR, "X_test.csv"), index=False)
    y_train.to_csv(os.path.join(DATA_DIR, "y_train.csv"), index=False)
    y_test.to_csv(os.path.join(DATA_DIR, "y_test.csv"), index=False)
    print("Preprocessing & train/test split completed.")

def train_model(**kwargs):
    X_train = pd.read_csv(os.path.join(DATA_DIR, "X_train.csv"))
    y_train = pd.read_csv(os.path.join(DATA_DIR, "y_train.csv")).values.ravel()
    
    model = RandomForestClassifier(n_estimators=50, random_state=42)
    model.fit(X_train, y_train)
    
    import joblib
    joblib.dump(model, os.path.join(DATA_DIR, "model.pkl"))
    print("Model training successful, model.pkl saved.")

def evaluate_model(**kwargs):
    import joblib
    model = joblib.load(os.path.join(DATA_DIR, "model.pkl"))
    X_test = pd.read_csv(os.path.join(DATA_DIR, "X_test.csv"))
    y_test = pd.read_csv(os.path.join(DATA_DIR, "y_test.csv")).values.ravel()
    
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    print(f"Evaluation Complete! Model Accuracy: {acc:.4f}")
    assert acc >= 0.85, f"Model accuracy degraded below threshold: {acc}"

default_args = {
    'owner': 'Aditi_Dayma',
    'depends_on_past': False,
    'start_date': datetime(2026, 1, 1),
    'email_on_failure': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define Airflow DAG
dag = DAG(
    'mlops_iris_training_pipeline',
    default_args=default_args,
    description='Automated End-to-End MLOps Training Pipeline DAG',
    schedule_interval='@daily',
    catchup=False
)

task_ingest = PythonOperator(
    task_id='ingest_data',
    python_callable=ingest_data,
    dag=dag
)

task_preprocess = PythonOperator(
    task_id='preprocess_data',
    python_callable=preprocess_data,
    dag=dag
)

task_train = PythonOperator(
    task_id='train_model',
    python_callable=train_model,
    dag=dag
)

task_evaluate = PythonOperator(
    task_id='evaluate_model',
    python_callable=evaluate_model,
    dag=dag
)

# Define Dependency Flow
task_ingest >> task_preprocess >> task_train >> task_evaluate
