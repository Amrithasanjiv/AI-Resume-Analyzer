from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score


def train_model(X, categories):
    """
    Train Naive Bayes classifier.

    Parameters:
        X : TF-IDF Features
        categories : Resume Categories

    Returns:
        model
        encoder
        X_test
        y_test
        predictions
        accuracy
    """

    encoder = LabelEncoder()

    y = encoder.fit_transform(categories)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    model = MultinomialNB()

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    return (
        model,
        encoder,
        X_test,
        y_test,
        predictions,
        accuracy
    )