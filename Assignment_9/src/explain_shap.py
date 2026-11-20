import os
import joblib
import matplotlib.pyplot as plt
import pandas as pd
import shap

def run_shap_analysis():
    model = joblib.load("models/rf_classifier.pkl")
    X_test = pd.read_csv("models/X_test.csv")
    
    print("Computing SHAP values using TreeExplainer...")
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X_test)
    
    os.makedirs("figures", exist_ok=True)
    
    # SHAP Global Summary Plot
    plt.figure(figsize=(10, 6))
    if isinstance(shap_values, list):
        shap.summary_plot(shap_values[1], X_test, show=False)
    else:
        shap.summary_plot(shap_values, X_test, show=False)
    plt.title("SHAP Global Feature Importance (Class 1)")
    plt.tight_layout()
    plt.savefig("figures/shap_summary_plot.png")
    plt.close()
    print("Global SHAP summary plot saved to figures/shap_summary_plot.png")
    
    # Local Sample Waterfall / Force Analysis
    sample_idx = 0
    print(f"Sample {sample_idx} Explanation:")
    expected_value = explainer.expected_value[1] if isinstance(explainer.expected_value, list) else explainer.expected_value
    sample_shap = shap_values[1][sample_idx] if isinstance(shap_values, list) else shap_values[sample_idx]
    
    top_features = pd.Series(sample_shap, index=X_test.columns).abs().sort_values(ascending=False).head(5)
    print("Top 5 most impactful features for this instance:")
    for feat, val in top_features.items():
        print(f"  - {feat}: attribution magnitude = {val:.4f}")

if __name__ == "__main__":
    run_shap_analysis()
