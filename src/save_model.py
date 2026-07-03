import joblib
from pathlib import Path

MODEL_DIR = Path("models")
MODEL_DIR.mkdir(exist_ok=True)


def save_models(model, tfidf, encoder):

    joblib.dump(model, MODEL_DIR / "model.pkl")

    joblib.dump(tfidf, MODEL_DIR / "tfidf.pkl")

    joblib.dump(encoder, MODEL_DIR / "label_encoder.pkl")

    print("\n✅ Models saved successfully!")