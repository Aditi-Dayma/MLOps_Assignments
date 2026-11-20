# Assignment 9: Apply SHAP / LIME for Model Explainability

**Course:** AI3206C - MLOps | **Student:** Aditi Rahul Dayma (Roll No: 66, PRN: 12412556)

---

## 🎯 Aim
To apply SHAP (Shapley Additive exPlanations) for global feature attribution and LIME (Local Interpretable Model-agnostic Explanations) for local instance interpretability on a trained classification model to foster Responsible and Transparent AI.

## 📋 Problem Statement
Modern machine learning algorithms like Random Forests and Gradient Boosted Trees often function as black-box models, obscuring why particular predictions are made. In critical domains such as credit scoring, healthcare, and risk assessment, explainability is essential for regulatory compliance and trust. As an MLOps Engineer, your task is to apply SHAP (Shapley Additive exPlanations) for global feature importance and LIME (Local Interpretable Model-agnostic Explanations) for local sample interpretability on a trained classification model.

---

## 💡 SHAP vs LIME Comparison
```
+-------------------------------------------------------------+
|                Model Explainability Landscape               |
|                                                             |
|   +--------------------+       +------------------------+   |
|   | SHAP (Global/Local)|       |  LIME (Local Surrogate)|   |
|   +---------+----------+       +-----------+------------+   |
|             |                              |                |
|             v                              v                |
|   - Cooperative Game Theory     - Perturbation-based        |
|   - Shapley Values              - Local Sparse Linear Model |
|   - Solid Axiomatic Foundation  - Model-agnostic surrogate  |
|   - Fair attribution allocation - Fast sample explanation   |
|                                                             |
|   +-----------------------------------------------------+   |
|   |                Trained Random Forest                |   |
|   |                   (Black-box)                       |   |
|   +-----------------------------------------------------+   |
+-------------------------------------------------------------+
```

---

## 🛠️ Execution Steps
1. **Install Dependencies:** `pip install -r requirements.txt`
2. **Train Tabular Classifier:**
   ```bash
   python src/train_model.py
   ```
3. **Execute SHAP Global & Local Analysis:**
   ```bash
   python src/explain_shap.py
   ```
4. **Execute LIME Local Analysis:**
   ```bash
   python src/explain_lime.py
   ```
