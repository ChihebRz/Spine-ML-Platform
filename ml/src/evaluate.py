import torch
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)

from preprocess import load_data
from model import SpineClassifier


# Load data
X_train, X_test, y_train, y_test = load_data("../data/column_3C_weka.csv")


# Load model
model = SpineClassifier()
model.load_state_dict(torch.load("../artifacts/model.pth"))
model.eval()


with torch.inference_mode():
    outputs = model(X_test)
    preds = torch.argmax(outputs, dim=1)


y_true = y_test.numpy()
y_pred = preds.numpy()


print("\n📊 Evaluation Metrics\n")

print("Accuracy :", round(accuracy_score(y_true, y_pred), 4))
print("Precision:", round(precision_score(y_true, y_pred, average="macro"), 4))
print("Recall   :", round(recall_score(y_true, y_pred, average="macro"), 4))
print("F1-score :", round(f1_score(y_true, y_pred, average="macro"), 4))

print("\nConfusion Matrix:\n", confusion_matrix(y_true, y_pred))

print("\nClassification Report:\n")
print(classification_report(
    y_true,
    y_pred,
    target_names=["Normal", "Hernia", "Spondylolisthesis"]
))
