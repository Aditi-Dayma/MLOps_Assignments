import boto3
import sagemaker
from sagemaker.sklearn.estimator import SKLearn

def orchestrate_sagemaker():
    print("=== Step 1 & 2: AWS Configuration and Session Verification ===")
    session = sagemaker.Session()
    bucket = session.default_bucket()
    role = sagemaker.get_execution_role()
    print(f"S3 Bucket: {bucket} | Execution Role: {role}")
    
    print("=== Step 3: Upload Training Data to S3 ===")
    s3_train_path = session.upload_data(
        path="data/train.csv",
        bucket=bucket,
        key_prefix="sagemaker/iris-training/data"
    )
    print(f"Data uploaded to: {s3_train_path}")
    
    print("=== Step 4 & 5: Configure and Launch SKLearn Estimator ===")
    sklearn_estimator = SKLearn(
        entry_point="src/train_sagemaker.py",
        role=role,
        instance_count=1,
        instance_type="ml.m5.large",
        framework_version="1.2-1",
        py_version="py3",
        hyperparameters={
            "n-estimators": 100,
            "max-depth": 5
        }
    )
    
    # Launch training job
    sklearn_estimator.fit({"train": s3_train_path})
    print("Training job finished successfully.")
    
    print("=== Step 7 & 8: Deploy to Real-Time SageMaker Endpoint ===")
    predictor = sklearn_estimator.deploy(
        initial_instance_count=1,
        instance_type="ml.t2.medium",
        endpoint_name="iris-realtime-endpoint"
    )
    print("Endpoint deployed and InService.")
    
    print("=== Step 9: Invoke Real-Time Endpoint ===")
    sample_payload = [[5.1, 3.5, 1.4, 0.2]]
    prediction = predictor.predict(sample_payload)
    print(f"Live Prediction Output: {prediction}")
    
    print("=== Step 10: Clean Up Endpoint Resources ===")
    predictor.delete_endpoint()
    print("Endpoint deleted to prevent unnecessary AWS billing.")

if __name__ == "__main__":
    print("AWS SageMaker orchestration workflow template.")
