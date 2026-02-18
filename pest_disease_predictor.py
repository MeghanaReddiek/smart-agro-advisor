import random
import pandas as pd
import os

DATASET_PATH = 'data/pest_disease_dataset.csv'  # Adjust path as needed

def load_dataset():
    if os.path.exists(DATASET_PATH):
        df = pd.read_csv(DATASET_PATH)
        return df
    else:
        return None

def predict_pest_disease(image_path):
    # For now, just check if dataset loads
    df = load_dataset()
    if df is not None:
        sample_info = df.head().to_dict()
        return {'dataset_loaded': True, 'sample_data': sample_info}
    else:
        diseases = ['Healthy', 'Blight', 'Powdery Mildew', 'Rust']
        status = random.choice(diseases)
        return {'dataset_loaded': False, 'status': status, 'risk_level': 'High' if status != 'Healthy' else 'None'}
