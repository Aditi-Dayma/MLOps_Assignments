import argparse
import os
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    # SageMaker passes hyperparameters as CLI arguments
    parser.add_argument('--n-estimators', type=int, default=50)
    parser.add_argument('--max-depth', type=int, default=5)
    
    # SageMaker specific environment variables
    parser.add_argument('--model-dir', type=str, default=os.environ.get('SM_MODEL_DIR', './model'))
    parser.add_argument('--train', type=str, default=os.environ.get('SM_CHANNEL_TRAIN', './data'))
    
    args = parser.parse_args()
    
    # Ingest data from channel
    train_file = os.path.join(args.train, 'train.csv')
    df = pd.read_csv(train_file)
    
    X = df.drop(columns=['target'])
    y = df['target']
    
    # Train estimator
    clf = RandomForestClassifier(n_estimators=args.n_estimators, max_depth=args.max_depth, random_state=42)
    clf.fit(X, y)
    
    # Serialize model to SM_MODEL_DIR for SageMaker hosting
    os.makedirs(args.model_dir, exist_ok=True)
    joblib.dump(clf, os.path.join(args.model_dir, 'model.joblib'))
    print("SageMaker training complete. Model serialized.")
