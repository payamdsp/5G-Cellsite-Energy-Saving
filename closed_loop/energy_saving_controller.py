import joblib, pandas as pd, json, boto3
from datetime import datetime

def decide_energy_action(prediction, threshold=0.2):
    # Example: if prediction says "low load", sleep cell
    if prediction['rf'] == 0 and prediction['iso'] > threshold:
        return "SLEEP"
    return "ACTIVE"

def act_on_cell(cell_id, action):
    # Placeholder: API call to O-RAN SMO (Service Management and Orchestration)
    print(f"{datetime.now()}: Cell {cell_id} -> {action}")

def closed_loop_cycle(feature_file):
    rf = joblib.load("ml/random_forest.pkl")
    iso = joblib.load("ml/isolation_forest.pkl")
    df = pd.read_csv(feature_file)
    for idx, row in df.iterrows():
        X = row.drop(['cell_id']).values.reshape(1, -1)
        rf_pred = rf.predict(X)[0]
        iso_score = iso.decision_function(X)[0]
        action = decide_energy_action({'rf': rf_pred, 'iso': iso_score})
        act_on_cell(row['cell_id'], action)

if __name__ == "__main__":
    closed_loop_cycle("dataset/features.csv")