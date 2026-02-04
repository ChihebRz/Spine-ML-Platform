import torch
import numpy as np
import joblib
from model import SpineClassifier


LABELS = {
    0: "Normal",
    1: "Hernia",
    2: "Spondylolisthesis"
}


def predict_sample(sample: np.ndarray):

    # Load scaler
    scaler = joblib.load("../artifacts/scaler.pkl")
    sample_scaled = scaler.transform([sample])

    X = torch.tensor(sample_scaled, dtype=torch.float32)

    # Load model
    model = SpineClassifier()
    model.load_state_dict(torch.load("../artifacts/model.pth"))
    model.eval()

    with torch.inference_mode():
        logits = model(X)
        probs = torch.softmax(logits, dim=1)
        pred = torch.argmax(probs, dim=1).item()

    return LABELS[pred], probs.numpy()


# Example
if __name__ == "__main__":

    example = np.array([63.0, 22.0, 39.0, 41.0, 98.0, 12.0])

    label, probas = predict_sample(example)

    print("Prediction :", label)
    print("Probabilities:", probas)