from predictor import ResumePredictor
from data_loader import load_dataset
import random

df = load_dataset()

predictor = ResumePredictor()

# Test 10 random resumes
for _ in range(10):

    i = random.randint(0, len(df) - 1)

    resume = df.iloc[i]["Resume_str"]

    actual = df.iloc[i]["Category"]

    predicted = predictor.predict(resume)

    print("=" * 50)
    print(f"Index      : {i}")
    print(f"Actual     : {actual}")
    print(f"Predicted  : {predicted}")