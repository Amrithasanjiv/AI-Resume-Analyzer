from data_loader import load_dataset
from preprocess import clean_resume
from vectorizer import create_vectorizer
from trainer import prepare_data
from models import get_models
from evaluator import evaluate_model
from save_model import save_models

import pandas as pd


def main():

    print("=" * 60)
    print("Loading Dataset...")
    print("=" * 60)

    df = load_dataset()

    print(df.shape)

    print("=" * 60)
    print("Cleaning Resumes...")
    print("=" * 60)

    df["Cleaned_Resume"] = df["Resume_str"].apply(clean_resume)

    print("=" * 60)
    print("Creating TF-IDF Features...")
    print("=" * 60)

    tfidf = create_vectorizer()

    X = tfidf.fit_transform(df["Cleaned_Resume"])

    X_train, X_test, y_train, y_test, encoder = prepare_data(
        X,
        df["Category"]
    )

    models = get_models()

    results = []

    for name, model in models.items():

        print(f"\nTraining {name}...")

        model.fit(X_train, y_train)

        predictions, accuracy, report = evaluate_model(
            model,
            X_test,
            y_test
        )

        print(f"Accuracy : {accuracy * 100:.2f}%")

        results.append({
        "Model": name,
        "Accuracy": accuracy,
        "Object": model
    })

    print("\nFinal Comparison")

    results_df = pd.DataFrame(results)
    
    results_df = results_df.sort_values(
    by="Accuracy",
    ascending=False
    )

    print(results_df[["Model", "Accuracy"]])

    best_model = results_df.iloc[0]["Object"]

    save_models(
        best_model,
        tfidf,
        encoder
    )


if __name__ == "__main__":
    main()