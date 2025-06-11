import pandas as pd
from sklearn.ensemble import RandomForestClassifier, IsolationForest
import mlflow, joblib

def train_ensemble(features_csv):
    df = pd.read_csv(features_csv)
    X = df.drop(['label'], axis=1)
    y = df['label']
    rf = RandomForestClassifier(n_estimators=100)
    rf.fit(X, y)
    iso = IsolationForest(n_estimators=50)
    iso.fit(X)
    joblib.dump(rf, "random_forest.pkl")
    joblib.dump(iso, "isolation_forest.pkl")
    # MLflow log
    with mlflow.start_run():
        mlflow.sklearn.log_model(rf, "random_forest")
        mlflow.sklearn.log_model(iso, "isolation_forest")
if __name__ == "__main__":
    train_ensemble("dataset/features.csv")