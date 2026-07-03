from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


def prepare_data(X, categories):
    """
    Split the dataset into training and testing sets.
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

    return X_train, X_test, y_train, y_test, encoder