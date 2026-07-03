import joblib
from pathlib import Path

# Find the project folder
BASE_DIR = Path(__file__).resolve().parent.parent

# Go to the models folder
MODEL_DIR = BASE_DIR / "models"

# Load the saved files
model = joblib.load(MODEL_DIR / "model.pkl")
encoder = joblib.load(MODEL_DIR / "label_encoder.pkl")

print("Model Loaded:")
print(model)

print("\nCategories:")
print(encoder.classes_)