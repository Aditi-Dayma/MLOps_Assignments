import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

class CancerClassifier:
    def __init__(self, n_estimators=50, random_state=42):
        self.clf = RandomForestClassifier(n_estimators=n_estimators, random_state=random_state)
        
    def train(self, X_train, y_train):
        self.clf.fit(X_train, y_train)
        
    def evaluate(self, X_test, y_test):
        preds = self.clf.predict(X_test)
        return accuracy_score(y_test, preds)
        
    def predict(self, X):
        return self.clf.predict(X)
