# Assignment 3: Create Feature Engineering Pipeline

**Course:** AI3206C - MLOps | **Student:** Aditi Rahul Dayma (Roll No: 66, PRN: 12412556)

---

## 🎯 Aim
To build a robust, modular, and serialized Feature Engineering Pipeline using Scikit-Learn `Pipeline` and `ColumnTransformer` to prevent data leakage and guarantee reproducible preprocessing in training and inference.

## 📋 Problem Statement
Raw machine learning datasets often contain missing values, inconsistent categorical variables, and unscaled numerical distributions, causing data leakage and deployment discrepancies. In production systems, preprocessing must be reproducible across both training and inference phases. As an MLOps Engineer, your task is to build a robust, modular Feature Engineering Pipeline using Scikit-Learn Pipeline and ColumnTransformer, serialize the fitted transformer pipeline, and validate transformations on unseen incoming data.

---

## 💡 Architecture & Workflow
```
+-------------------------------------------------------------+
|               Feature Engineering Pipeline                  |
|                                                             |
|   +--------------------+                                    |
|   | Raw Input Features |                                    |
|   +---------+----------+                                    |
|             |                                               |
|             +-----------------------+                       |
|             | Numeric Columns       | Categorical Columns   |
|             v                       v                       |
|   +--------------------+  +--------------------+            |
|   |   SimpleImputer    |  |   SimpleImputer    |            |
|   |  (strategy=median) |  | (strategy=frequent)|            |
|   +---------+----------+  +---------+----------+            |
|             |                       |                       |
|             v                       v                       |
|   +--------------------+  +--------------------+            |
|   |   StandardScaler   |  |   OneHotEncoder    |            |
|   |   (mean=0, std=1)  |  |(handle_unknown=ign)|            |
|   +---------+----------+  +---------+----------+            |
|             |                       |                       |
|             +-----------+-----------+                       |
|                         |                                   |
|                         v                                   |
|           +---------------------------+                     |
|           | ColumnTransformer Output  |                     |
|           | (Dense Scaled Matrix)     |                     |
|           +-------------+-------------+                     |
|                         |                                   |
|                         v                                   |
|           +---------------------------+                     |
|           |  Serialize via joblib     |                     |
|           |  feature_pipeline.pkl     |                     |
|           +---------------------------+                     |
+-------------------------------------------------------------+
```

---

## 🛠️ Execution Steps
1. **Install Requirements:** `pip install -r requirements.txt`
2. **Execute Pipeline Training:**
   ```bash
   python src/pipeline.py
   ```
3. **Verify Transformed Matrix:** Inspect `output/transformed_data.csv`.
4. **Validate on Unseen Data:**
   ```bash
   python src/test_pipeline.py
   ```
