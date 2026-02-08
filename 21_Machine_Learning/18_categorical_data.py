"""
Machine Learning - Categorical Data
======================================
ML models work with numbers, so categorical data must be converted.

Types of categorical data:
1. Nominal: No order (color: red, blue, green)
2. Ordinal: Has order (size: S, M, L, XL)

Encoding methods:
1. Label Encoding: Assigns a unique integer to each category
2. One-Hot Encoding: Creates binary columns for each category
3. Ordinal Encoding: Preserves the order of categories

When to use which:
- Label Encoding: For ordinal data, or tree-based models
- One-Hot Encoding: For nominal data, or linear/distance-based models
- Ordinal Encoding: For data with a clear order
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder, OneHotEncoder

# ============================================================
# 1. Sample Dataset with Categorical Features
# ============================================================
print("SAMPLE DATASET WITH CATEGORICAL FEATURES")
print("=" * 50)

df = pd.DataFrame({
    "Color":    ["Red", "Blue", "Green", "Red", "Blue", "Green", "Red", "Blue"],
    "Size":     ["S", "M", "L", "XL", "M", "S", "L", "XL"],
    "Brand":    ["Nike", "Adidas", "Puma", "Nike", "Puma", "Adidas", "Nike", "Adidas"],
    "Price":    [49.99, 59.99, 39.99, 69.99, 44.99, 54.99, 64.99, 74.99],
    "Sold":     [1, 0, 1, 1, 0, 1, 1, 0],
})

print(df.to_string(index=False))
print(f"\nData types:\n{df.dtypes}")


# ============================================================
# 2. Label Encoding
# ============================================================
print(f"\n{'='*50}")
print("LABEL ENCODING")
print(f"{'='*50}")

# Assigns a unique integer to each category
le_color = LabelEncoder()
df["Color_encoded"] = le_color.fit_transform(df["Color"])

print("Color mapping:", dict(zip(le_color.classes_, le_color.transform(le_color.classes_))))
print(f"\n{df[['Color', 'Color_encoded']].to_string(index=False)}")

# Encoding multiple columns
le_brand = LabelEncoder()
df["Brand_encoded"] = le_brand.fit_transform(df["Brand"])

print(f"\nBrand mapping: {dict(zip(le_brand.classes_, le_brand.transform(le_brand.classes_)))}")

# WARNING about Label Encoding
print("\n⚠ WARNING: Label Encoding implies an order (0 < 1 < 2)")
print("  Blue=0 < Green=1 < Red=2 -- but colors have NO order!")
print("  Use One-Hot Encoding for nominal data instead.")


# ============================================================
# 3. One-Hot Encoding
# ============================================================
print(f"\n{'='*50}")
print("ONE-HOT ENCODING")
print(f"{'='*50}")

# Creates binary columns for each category
# Using pandas get_dummies (simplest way)
df_onehot = pd.get_dummies(df[["Color", "Brand"]], dtype=int)
print("One-Hot Encoding with pd.get_dummies:")
print(df_onehot.to_string(index=False))

# Using sklearn OneHotEncoder
ohe = OneHotEncoder(sparse_output=False, drop=None)
encoded = ohe.fit_transform(df[["Color", "Brand"]])
feature_names = ohe.get_feature_names_out(["Color", "Brand"])

df_ohe = pd.DataFrame(encoded.astype(int), columns=feature_names)
print(f"\nOne-Hot with sklearn:")
print(df_ohe.to_string(index=False))

# Drop first to avoid multicollinearity (dummy variable trap)
df_drop_first = pd.get_dummies(df[["Color"]], drop_first=True, dtype=int)
print(f"\nDrop-first (avoid multicollinearity):")
print(df_drop_first.to_string(index=False))


# ============================================================
# 4. Ordinal Encoding
# ============================================================
print(f"\n{'='*50}")
print("ORDINAL ENCODING")
print(f"{'='*50}")

# For data with a meaningful order
size_order = [["S", "M", "L", "XL"]]  # Define the order

oe = OrdinalEncoder(categories=size_order)
df["Size_encoded"] = oe.fit_transform(df[["Size"]])

print("Size mapping: S=0, M=1, L=2, XL=3")
print(df[["Size", "Size_encoded"]].to_string(index=False))
print("\nThis preserves the order: S < M < L < XL")


# ============================================================
# 5. Full Preprocessing Pipeline
# ============================================================
print(f"\n{'='*50}")
print("FULL PREPROCESSING PIPELINE")
print(f"{'='*50}")

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Create a larger dataset
np.random.seed(42)
n = 200
data = pd.DataFrame({
    "Color":  np.random.choice(["Red", "Blue", "Green"], n),
    "Size":   np.random.choice(["S", "M", "L", "XL"], n),
    "Weight": np.random.uniform(100, 500, n).round(1),
    "Rating": np.random.randint(1, 6, n),
    "Target": np.random.choice([0, 1], n),
})

print("Dataset shape:", data.shape)
print(data.head().to_string(index=False))

X = data.drop("Target", axis=1)
y = data["Target"]

# Define preprocessing for different column types
preprocessor = ColumnTransformer(
    transformers=[
        ("onehot", OneHotEncoder(drop="first", sparse_output=False), ["Color"]),
        ("ordinal", OrdinalEncoder(categories=[["S", "M", "L", "XL"]]), ["Size"]),
        ("passthrough", "passthrough", ["Weight", "Rating"]),
    ]
)

# Pipeline: preprocess then classify
pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", DecisionTreeClassifier(max_depth=5, random_state=42)),
])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)

print(f"\nPipeline accuracy: {accuracy_score(y_test, y_pred):.4f}")


# ============================================================
# 6. Handling Unknown Categories
# ============================================================
print(f"\n{'='*50}")
print("HANDLING UNKNOWN CATEGORIES")
print(f"{'='*50}")

# What if test data has categories not seen in training?
ohe_safe = OneHotEncoder(handle_unknown="ignore", sparse_output=False)
train_colors = np.array([["Red"], ["Blue"], ["Green"]])
ohe_safe.fit(train_colors)

# New data includes "Yellow" (unseen during training)
test_colors = np.array([["Red"], ["Yellow"], ["Blue"]])
encoded_safe = ohe_safe.transform(test_colors)
print(f"Training categories: {ohe_safe.categories_}")
print(f"Test data (with unseen 'Yellow'):")
print(f"  Red:    {encoded_safe[0]}")
print(f"  Yellow: {encoded_safe[1]} (all zeros - unknown category)")
print(f"  Blue:   {encoded_safe[2]}")

print("\n--- Categorical Data complete! ---")
