import torch
import torch.nn as nn
import joblib

from preprocess import load_data, get_scaler
from model import SpineClassifier


# ========== 1. LOAD DATA ==========
X_train, X_test, y_train, y_test = load_data("../data/column_3C_weka.csv")



# ========== 2. SAVE SCALER ==========
scaler = get_scaler()
joblib.dump(scaler, "../artifacts/scaler.pkl")


# ========== 3. MODEL ==========
model = SpineClassifier()

criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)


# ========== 4. TRAINING LOOP ==========
epochs = 1500

for epoch in range(epochs):
    model.train()

    outputs = model(X_train)
    loss = criterion(outputs, y_train)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if (epoch + 1) % 100 == 0:
        print(f"Epoch {epoch+1}/{epochs} - Loss: {loss.item():.4f}")


# ========== 5. SAVE MODEL ==========
torch.save(model.state_dict(), "../artifacts/model.pth")

print("✅ Training finished!")
print("📁 Saved:")
print(" - artifacts/model.pth")
print(" - artifacts/scaler.pkl")
