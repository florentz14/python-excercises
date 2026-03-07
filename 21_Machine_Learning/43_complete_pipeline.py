"""
ML Mini Course - Step 5: Complete pipeline
==========================================
Full flow: load → preprocess → train → evaluate.
Dataset: StudentsPerformance.csv
Model: Random Forest to predict if math is passed (≥60).

Author: Florentino Báez
"""

import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.pipeline import Pipeline

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "09_Pandas", "data")


def main():
    # 1. Load
    path = os.path.join(DATA_DIR, "StudentsPerformance.csv")
    df = pd.read_csv(path)

    # 2. Create binary target: passes math? (≥60)
    df["passes_math"] = (df["math score"] >= 60).astype(int)

    # 3. Features: use only available numeric columns
    # (in a real case you could encode gender, lunch, etc.)
    X = df[["reading score", "writing score"]]
    y = df["passes_math"]

    # 4. Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # 5. Pipeline: scale + model
    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("model", RandomForestClassifier(n_estimators=50, random_state=42))
    ])

    # 6. Train
    pipeline.fit(X_train, y_train)

    # 7. Evaluate
    y_pred = pipeline.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    print("=" * 50)
    print("COMPLETE PIPELINE - Passes math?")
    print("=" * 50)
    print(f"\nAccuracy: {accuracy:.4f} ({accuracy*100:.2f}%)")
    print("\nReport:")
    print(classification_report(y_test, y_pred, target_names=["Fails", "Passes"]))
    print("Confusion matrix:")
    print(confusion_matrix(y_test, y_pred))
    print("\n[OK] Pipeline completed.")


if __name__ == "__main__":
    main()
