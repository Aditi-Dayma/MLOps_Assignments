#!/bin/bash
# Assignment 1 - Data Version Control (DVC) Workflow Automation

set -e

echo "=== Step 1: Initialize Git and DVC ==="
git init
dvc init

echo "=== Step 2: Track Dataset with DVC ==="
dvc add data/student.csv

echo "=== Step 3: Commit Metadata to Git ==="
git add data/.gitignore data/student.csv.dvc .dvc/config
git commit -m "Track initial student dataset (v1)"

echo "=== Step 4: Modify Dataset and Track New Version ==="
echo "12,Aditi,98" >> data/student.csv
dvc add data/student.csv
git add data/student.csv.dvc
git commit -m "Updated dataset with record 12 (v2)"

echo "=== Step 5: Check Historical Versions ==="
git log --oneline -n 5

echo "=== Step 6: Rollback Dataset to v1 ==="
git checkout HEAD~1 data/student.csv.dvc
dvc checkout
cat data/student.csv

echo "=== Step 7: Configure Remote Storage and Push ==="
mkdir -p ../dvc-storage
dvc remote add -d myremote ../dvc-storage || true
dvc push

echo "=== Step 8: Verify Remote Pull ==="
rm -f data/student.csv
dvc pull
cat data/student.csv
echo "DVC Workflow completed successfully!"
