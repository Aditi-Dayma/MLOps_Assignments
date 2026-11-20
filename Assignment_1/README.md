# Assignment 1: Data Version Control (DVC) for Dataset Management

**Course:** AI3206C - MLOps | **Student:** Aditi Rahul Dayma (Roll No: 66, PRN: 12412556)

---

## 🎯 Aim
To implement dataset versioning, version rollback, and remote storage synchronization using Data Version Control (DVC) alongside Git for metadata tracking.

## 📋 Problem Statement
A machine learning team frequently updates its training dataset. Managing different versions of the dataset manually leads to confusion and reproducibility issues. As an MLOps Engineer, your task is to use Data Version Control (DVC) to manage multiple versions of the dataset while using Git to track project metadata.

---

## 💡 Key Concepts & Architecture
- **Git vs DVC:** Git excels at tracking small textual code changes but degrades when tracking multi-megabyte/gigabyte datasets. DVC decouples data storage from metadata tracking.
- **`.dvc` Metadata Pointer:** A lightweight text pointer containing the dataset's MD5 checksum, file size, and relative path. Only `.dvc` is tracked in Git.
- **DVC Cache & Remote:** The actual data resides in `.dvc/cache` and is synchronized to external storage (e.g., local directory `../dvc-storage`, AWS S3, or GCS) via `dvc push` / `dvc pull`.

```
+-----------------------------------------------------------+
|                      Project Directory                    |
|                                                           |
|   +-------------------+          +--------------------+   |
|   |  data/student.csv |          | data/student.csv.dvc|  |
|   |  (Actual Dataset) |          | (Lightweight YAML) |   |
|   +---------+---------+          +---------+----------+   |
|             |                              |              |
|             | dvc add                      | git add      |
|             v                              v              |
|   +-------------------+          +--------------------+   |
|   |    .dvc/cache     |          |   Git Repository   |   |
|   |  (Content Hashed) |          |   (.git/ commits)  |   |
|   +---------+---------+          +---------+----------+   |
|             |                              |              |
|             | dvc push / pull              | git push     |
|             v                              v              |
|   +-------------------+          +--------------------+   |
|   | DVC Remote Storage|          | Remote Git (GitHub)|   |
|   |  (../dvc-storage) |          +--------------------+   |
|   +-------------------+                                   |
+-----------------------------------------------------------+
```

---

## 🛠️ Execution Steps
1. **Initialize Project:** `git init`
2. **Initialize DVC:** `dvc init`
3. **Create Dataset:** Create `data/student.csv`
4. **Track Dataset:** `dvc add data/student.csv` (adds `data/.gitignore`)
5. **Commit to Git:** `git add data/.gitignore data/student.csv.dvc && git commit -m "Track dataset v1"`
6. **Modify Dataset:** Append new records, run `dvc add data/student.csv`, commit to Git.
7. **View Git History:** `git log --oneline`
8. **Restore Previous Version:** `git checkout <commit_hash> data/student.csv.dvc && dvc checkout`
9. **Configure Remote Storage:** `dvc remote add -d myremote ../dvc-storage`
10. **Push to Remote:** `dvc push`
11. **Verify Pull:** Remove local file `rm data/student.csv`, run `dvc pull` to recover data.
