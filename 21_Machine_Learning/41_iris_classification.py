"""
ML Mini Course - Step 3: Classification with real dataset
=========================================================
Classify iris species (setosa, versicolor, virginica).
Dataset: iris.csv

Author: Florentino Báez
"""

import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "09_Pandas", "data")


def main():
    # 1. Load data
    path = os.path.join(DATA_DIR, "iris.csv")
    df = pd.read_csv(path)

    # 2. Clean: remove rows with NaN
    df = df.dropna()

    # 3. Features and target
    X = df[["sepal_length", "sepal_width", "petal_length", "petal_width"]]
    y_raw = df["species"]

    # 4. Encode labels (setosa→0, versicolor→1, virginica→2)
    le = LabelEncoder()
    y = le.fit_transform(y_raw)

    # 5. Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # 6. Train
    model = LogisticRegression(max_iter=200, random_state=42)
    model.fit(X_train, y_train)

    # 7. Predict and evaluate
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    print("=" * 50)
    print("CLASSIFICATION - Iris species")
    print("=" * 50)
    print(f"\nAccuracy: {accuracy:.4f} ({accuracy*100:.2f}%)")
    print("\nReport by class:")
    print(classification_report(y_test, y_pred, target_names=le.classes_))
    print("[OK] Classification completed.")


if __name__ == "__main__":
    main()
