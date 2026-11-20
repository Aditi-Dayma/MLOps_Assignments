import os
import joblib
import pandas as pd
from lime import lime_tabular
from sklearn.datasets import load_breast_cancer

def run_lime_analysis():
    model = joblib.load("models/rf_classifier.pkl")
    X_test = pd.read_csv("models/X_test.csv")
    data = load_breast_cancer(as_frame=True)
    
    explainer = lime_tabular.LimeTabularExplainer(
        training_data=X_test.values,
        feature_names=X_test.columns.tolist(),
        class_names=data.target_names.tolist(),
        mode="classification",
        random_state=42
    )
    
    sample_idx = 0
    sample_instance = X_test.iloc[sample_idx]
    
    exp = explainer.explain_instance(
        data_row=sample_instance,
        predict_fn=model.predict_proba,
        num_features=5
    )
    
    print(f"LIME Local Explanation for Instance #{sample_idx}:")
    for feat_name, weight in exp.as_list():
        print(f"  - Rule: {feat_name:<35} | Weight: {weight:.4f}")
        
    os.makedirs("figures", exist_ok=True)
    exp.save_to_file("figures/lime_explanation.html")
    print("LIME HTML explanation exported to figures/lime_explanation.html")

if __name__ == "__main__":
    run_lime_analysis()
