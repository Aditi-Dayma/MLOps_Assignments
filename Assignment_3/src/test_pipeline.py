import os
import joblib
import pandas as pd

def test_unseen_data():
    model_path = "models/feature_pipeline.pkl"
    if not os.path.exists(model_path):
        model_path = "Assignment_3/models/feature_pipeline.pkl"
        
    pipeline = joblib.load(model_path)
    print("Loaded serialized feature engineering pipeline.")
    
    # Simulate new unseen incoming batch with missing values
    unseen_samples = pd.DataFrame({
        "Pclass": [1, 3],
        "Age": [None, 29.0],  # missing age in sample 1
        "SibSp": [0, 1],
        "Parch": [0, 0],
        "Fare": [105.0, 7.89],
        "Embarked": ["C", "Unknown"]  # unseen category
    })
    
    print("Unseen input samples:")
    print(unseen_samples)
    
    transformed_samples = pipeline.transform(unseen_samples)
    print("
Transformed feature matrix on unseen data:")
    print(transformed_samples)
    print(f"
Verification Passed: Output shape is {transformed_samples.shape}")

if __name__ == "__main__":
    test_unseen_data()
