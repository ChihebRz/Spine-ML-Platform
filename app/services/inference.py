import torch
import joblib
import numpy as np

from ml.src.model import SpineClassifier
from app.core.config import settings

# Load artifacts
scaler = joblib.load(settings.SCALER_PATH)

model = SpineClassifier()
model.load_state_dict(torch.load(settings.MODEL_PATH))
model.eval()

CLASSES = ["Normal", "Hernia", "Spondylolisthesis"]


def predict(features: list):
    x = np.array(features).reshape(1, -1)
    x_scaled = scaler.transform(x)

    tensor = torch.tensor(x_scaled, dtype=torch.float32)

    with torch.inference_mode():
        output = model(tensor)
        probs = torch.softmax(output, dim=1)

    idx = probs.argmax().item()

    return {
    "class_name": CLASSES[idx],
    "confidence": round(float(probs[0][idx]), 3),
    "probabilities": [round(float(p), 3) for p in probs[0].tolist()]   # NEW
    }