import pandas as pd
import torch
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Global scaler so train.py can save it
scaler = StandardScaler()

def get_scaler():
    return scaler


def load_data(path):
    df = pd.read_csv(path)

    # Encode labels
    label_map = {
        "Normal": 0,
        "Hernia": 1,
        "Spondylolisthesis": 2
    }

    df["class"] = df["class"].map(label_map)

    X = df.drop(columns=["class"]).values
    y = df["class"].values

    # Scale features
    global scaler
    X = scaler.fit_transform(X)

    # Train / test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    # To tensors
    X_train = torch.tensor(X_train, dtype=torch.float32)
    X_test  = torch.tensor(X_test, dtype=torch.float32)

    y_train = torch.tensor(y_train, dtype=torch.long)
    y_test  = torch.tensor(y_test, dtype=torch.long)

    return X_train, X_test, y_train, y_test

