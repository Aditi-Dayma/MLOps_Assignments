# Assignment 10: Train and Deploy ML Model using AWS SageMaker

**Course:** AI3206C - MLOps | **Student:** Aditi Rahul Dayma (Roll No: 66, PRN: 12412556)

---

## 🎯 Aim
To train a machine learning model using managed compute infrastructure on AWS SageMaker, deploy the serialized model to a real-time SageMaker hosting endpoint, and perform live inference before decommissioning endpoint resources.

## 📋 Problem Statement
Managing dedicated infrastructure, distributed compute clusters, and scalable endpoint hosting for enterprise machine learning workflows is complex and resource-intensive. Cloud platforms like AWS SageMaker provide end-to-end managed ML capabilities. As an MLOps Engineer, your task is to prepare a training dataset, upload it to an Amazon S3 bucket, configure and launch a Scikit-Learn training estimator on AWS SageMaker, deploy the trained model to a real-time SageMaker endpoint, and perform live prediction inference.

---

## 💡 SageMaker End-to-End Workflow
```
+--------------------------------------------------------------+
|                 AWS SageMaker Managed Lifecycle              |
|                                                              |
|   +--------------------+                                     |
|   | Local Train Data   |                                     |
|   +---------+----------+                                     |
|             |                                                |
|             | boto3 / sagemaker.upload_data()                |
|             v                                                |
|   +--------------------+                                     |
|   |  Amazon S3 Bucket  |                                     |
|   | s3://bucket/data/  |                                     |
|   +---------+----------+                                     |
|             |                                                |
|             | SageMaker Channel                              |
|             v                                                |
|   +--------------------+        +------------------------+   |
|   | SKLearn Estimator  | -----> | SageMaker Training Job |   |
|   | (ml.m5.large)      |        | model.joblib artifact  |   |
|   +--------------------+        +-----------+------------+   |
|                                             |                |
|                                             | estimator.deploy()
|                                             v                |
|                                 +------------------------+   |
|                                 | Real-Time Endpoint     |   |
|                                 | (ml.t2.medium hosting) |   |
|                                 +-----------+------------+   |
|                                             |                |
|                                             | predictor.predict()
|                                             v                |
|                                 +------------------------+   |
|                                 | Real-Time Inference    |   |
|                                 +------------------------+   |
+--------------------------------------------------------------+
```

---

## 🛠️ Execution Steps
1. **Configure AWS Credentials:**
   ```bash
   aws configure
   aws sts get-caller-identity
   ```
2. **Upload Training Data to S3:**
   ```bash
   aws s3 cp data/train.csv s3://your-sagemaker-bucket/data/train.csv
   ```
3. **Execute SageMaker Training & Deployment:**
   ```bash
   python src/sagemaker_orchestrator.py
   ```
4. **Clean Up Endpoint:** Ensure endpoint is deleted to stop billing:
   ```python
   predictor.delete_endpoint()
   ```
