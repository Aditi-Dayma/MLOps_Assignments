import os
import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

def build_feature_pipeline():
    # Define feature subsets
    numeric_features = ["Pclass", "Age", "SibSp", "Parch", "Fare"]
    categorical_features = ["Embarked"]
    
    # Numeric transformer pipeline: Median Imputation -> Standard Scaling
    numeric_transformer = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ])
    
    # Categorical transformer pipeline: Frequent Imputation -> One-Hot Encoding
    categorical_transformer = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore", sparse_output=False))
    ])
    
    # Combine transformers via ColumnTransformer
    preprocessor = ColumnTransformer(transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features)
    ])
    
    return preprocessor, numeric_features, categorical_features

def run_pipeline():
    data_path = "data/raw_data.csv"
    if not os.path.exists(data_path):
        data_path = "Assignment_3/data/raw_data.csv"
        
    df = pd.read_csv(data_path)
    X = df.drop(columns=["PassengerId", "Survived"], errors="ignore")
    
    preprocessor, num_cols, cat_cols = build_feature_pipeline()
    
    print("Fitting feature engineering pipeline on raw dataset...")
    X_transformed = preprocessor.fit_transform(X)
    
    os.makedirs("models", exist_ok=True)
    os.makedirs("output", exist_ok=True)
    
    model_path = "models/feature_pipeline.pkl"
    joblib.dump(preprocessor, model_path)
    print(f"Fitted pipeline serialized to: {model_path}")
    
    out_df = pd.DataFrame(X_transformed)
    out_df.to_csv("output/transformed_data.csv", index=False)
    print(f"Transformed matrix saved to: output/transformed_data.csv (Shape: {X_transformed.shape})")

if __name__ == "__main__":
    run_pipeline()
