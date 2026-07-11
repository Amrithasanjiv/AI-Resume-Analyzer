import joblib
from pathlib import Path

try:
    from .preprocess import clean_resume
except ImportError:
    from preprocess import clean_resume


MODEL_DIR = Path("models")


class ResumePredictor:

    def __init__(self):

        self.model = joblib.load(MODEL_DIR / "model.pkl")

        self.tfidf = joblib.load(MODEL_DIR / "tfidf.pkl")

        self.encoder = joblib.load(
            MODEL_DIR / "label_encoder.pkl"
        )

    def predict(self, resume_text):

        cleaned_resume = clean_resume(resume_text)

        vector = self.tfidf.transform([cleaned_resume])

        prediction = self.model.predict(vector)

        category = self.encoder.inverse_transform(
            prediction
        )[0]

        return category