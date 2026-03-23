import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

def train():
    try:
        # 1. Load the data you captured
        df = pd.read_csv('network_data.csv')
        X = df[['len', 'proto']]
        
        # 2. Initialize and train the model
        # contamination=0.01 means we assume 1% of traffic is "weird"
        model = IsolationForest(n_estimators=100, contamination=0.01, random_state=42) 
        print("AI is learning your network patterns... please wait.")
        model.fit(X)
        
        # 3. THIS LINE CREATES THE MISSING FILE
        joblib.dump(model, 'sniffer_model.pkl')
        print("Done! 'sniffer_model.pkl' has been created successfully.")
        
    except FileNotFoundError:
        print("Error: 'network_data.csv' not found. Run your logger.py first!")

if __name__ == "__main__":
    train()