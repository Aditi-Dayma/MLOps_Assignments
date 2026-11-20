# Assignment 7: Implement CI/CD Pipeline using GitHub Actions

**Course:** AI3206C - MLOps | **Student:** Aditi Rahul Dayma (Roll No: 66, PRN: 12412556)

---

## 🎯 Aim
To build an automated continuous integration and continuous deployment (CI/CD) pipeline using GitHub Actions that triggers on code pushes and pull requests to enforce linting, unit testing, model performance validation gates, and Docker image builds.

## 📋 Problem Statement
Deploying machine learning models without automated testing, linting, and continuous integration risks pushing degraded models, broken inference APIs, and vulnerable dependencies into production. As an MLOps Engineer, your task is to implement an automated CI/CD pipeline using GitHub Actions that triggers on every pull request and push to validate code quality (Flake8/Black), execute automated unit tests (PyTest), build the Docker container image, and prepare deployment workflows.

---

## 💡 Pipeline Architecture
```
+--------------------------------------------------------------+
|                GitHub Actions CI/CD Architecture             |
|                                                              |
|        git push / pull_request to main branch                |
|                          |                                   |
|                          v                                   |
|   +------------------------------------------------------+   |
|   | Stage 1: lint-and-format                             |   |
|   | - flake8 code quality analysis                       |   |
|   | - black format consistency verification              |   |
|   +----------------------+-------------------------------+   |
|                          | (Passed)                          |
|                          v                                   |
|   +------------------------------------------------------+   |
|   | Stage 2: unit-and-model-testing                      |   |
|   | - PyTest execution                                   |   |
|   | - Model Quality Gate: Accuracy >= 0.90              |   |
|   | - API Schema verification                            |   |
|   +----------------------+-------------------------------+   |
|                          | (Passed)                          |
|                          v                                   |
|   +------------------------------------------------------+   |
|   | Stage 3: docker-build                                |   |
|   | - Multi-stage container compilation                  |   |
|   | - Artifact packaging ready for deployment            |   |
|   +------------------------------------------------------+   |
+--------------------------------------------------------------+
```

---

## 🛠️ Execution Steps
1. **Run Unit Tests Locally:**
   ```bash
   pytest tests/ -v
   ```
2. **Verify Linter:**
   ```bash
   flake8 src/ tests/
   ```
3. **Commit & Push to Remote:**
   ```bash
   git add .
   git commit -m "Configure MLOps CI/CD Pipeline"
   git push origin main
   ```
4. **Inspect Pipeline Execution:**
   Navigate to the repository's **Actions** tab on GitHub or run `gh run list`.
