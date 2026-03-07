"""
ML Mini Course - Step 2: Regression with real dataset
======================================================
Predict math score using reading and writing scores.
Dataset: StudentsPerformance.csv

Author: Florentino Báez
"""

import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "09_Pandas", "data")


def main():
    # 1. Load data
    path = os.path.join(DATA_DIR, "StudentsPerformance.csv")
    df = pd.read_csv(path)

    # 2. Define features and target
    # Predict math score from reading and writing
    X = df[["reading score", "writing score"]]
    y = df["math score"]

    # 3. Split into train/test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # 4. Train model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # 5. Predict and evaluate
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print("=" * 50)
    print("LINEAR REGRESSION - Math score prediction")
    print("=" * 50)
    print(f"\nFeatures: reading score, writing score")
    print(f"Target: math score")
    print(f"\nCoefficients: {model.coef_}")
    print(f"Intercept: {model.intercept_:.2f}")
    print(f"\nMSE: {mse:.2f}")
    print(f"R2: {r2:.4f}")
    print(f"\nInterpretation: R2 ~ {r2:.2f} -> model explains ~{r2*100:.0f}% of variance")
    print("\n[OK] Regression completed.")


if __name__ == "__main__":
    main()
