"""
Machine Learning - Scale (Feature Scaling)
============================================
Feature scaling transforms data to a common range so that all features
contribute equally to the model. Without scaling, features with larger
values can dominate the model.

Common methods:
1. Standardization (Z-score): (x - mean) / std -> mean=0, std=1
2. Min-Max Scaling: (x - min) / (max - min) -> range [0, 1]
3. Robust Scaling: Uses median and IQR (resistant to outliers)

When to scale:
- Distance-based models (KNN, SVM, K-means)
- Gradient-based models (Neural Networks, Logistic Regression)
- When features have very different ranges

When NOT to scale:
- Tree-based models (Decision Trees, Random Forests) - scale-invariant
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler

# ============================================================
# 1. Why Scaling Matters
# ============================================================
print("WHY SCALING MATTERS")
print("=" * 50)

# Without scaling, features with large values dominate
data = pd.DataFrame({
    "Age":    [25, 30, 35, 40, 45],         # Range: 25-45
    "Salary": [30000, 50000, 60000, 80000, 120000],  # Range: 30k-120k
    "Score":  [0.5, 0.7, 0.8, 0.6, 0.9],   # Range: 0.5-0.9
})

print("Original data:")
print(data.to_string(index=False))
print(f"\nNote: Salary values are ~1000x larger than Score values")
print("This can make models 'think' Salary is more important!")


# ============================================================
# 2. Standardization (Z-score Normalization)
# ============================================================
print(f"\n{'='*50}")
print("STANDARDIZATION (Z-SCORE)")
print(f"{'='*50}")

# Z = (x - mean) / std
# Result: mean = 0, std = 1

scaler_standard = StandardScaler()
data_standardized = scaler_standard.fit_transform(data)
df_std = pd.DataFrame(data_standardized, columns=data.columns)

print("After Standardization:")
print(df_std.round(4).to_string(index=False))
print(f"\nMeans:  {df_std.mean().values.round(4)}")
print(f"Stds:   {df_std.std().values.round(4)}")

# Manual calculation for Age
mean_age = data["Age"].mean()
std_age = data["Age"].std()
manual_z = (data["Age"] - mean_age) / std_age
print(f"\nManual Z-score for Age:")
print(f"  Mean: {mean_age}, Std: {std_age:.2f}")
print(f"  Z-scores: {manual_z.round(4).tolist()}")


# ============================================================
# 3. Min-Max Scaling
# ============================================================
print(f"\n{'='*50}")
print("MIN-MAX SCALING")
print(f"{'='*50}")

# X_scaled = (X - X_min) / (X_max - X_min)
# Result: all values between 0 and 1

scaler_minmax = MinMaxScaler()
data_minmax = scaler_minmax.fit_transform(data)
df_mm = pd.DataFrame(data_minmax, columns=data.columns)

print("After Min-Max Scaling:")
print(df_mm.round(4).to_string(index=False))
print(f"\nMin values: {df_mm.min().values.round(4)}")
print(f"Max values: {df_mm.max().values.round(4)}")

# Custom range (e.g., -1 to 1)
scaler_custom = MinMaxScaler(feature_range=(-1, 1))
data_custom = scaler_custom.fit_transform(data)
df_custom = pd.DataFrame(data_custom, columns=data.columns)
print(f"\nMin-Max scaled to [-1, 1]:")
print(df_custom.round(4).to_string(index=False))


# ============================================================
# 4. Robust Scaling (Handles Outliers)
# ============================================================
print(f"\n{'='*50}")
print("ROBUST SCALING")
print(f"{'='*50}")

# X_scaled = (X - median) / IQR
# Less affected by outliers than StandardScaler

data_outliers = pd.DataFrame({
    "Feature1": [10, 12, 14, 15, 13, 11, 200],  # 200 is an outlier
    "Feature2": [100, 110, 105, 108, 103, 107, 102],
})

scaler_robust = RobustScaler()
data_robust = scaler_robust.fit_transform(data_outliers)
df_robust = pd.DataFrame(data_robust, columns=data_outliers.columns)

scaler_std2 = StandardScaler()
data_std2 = scaler_std2.fit_transform(data_outliers)
df_std2 = pd.DataFrame(data_std2, columns=data_outliers.columns)

print("Data with outlier (200 in Feature1):")
print(data_outliers.to_string(index=False))
print("\nStandardScaler (affected by outlier):")
print(df_std2.round(3).to_string(index=False))
print("\nRobustScaler (resistant to outlier):")
print(df_robust.round(3).to_string(index=False))


# ============================================================
# 5. Impact on a Real Model
# ============================================================
print(f"\n{'='*50}")
print("IMPACT ON KNN MODEL")
print(f"{'='*50}")

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

np.random.seed(42)

# Features with very different scales
X = np.column_stack([
    np.random.uniform(20, 60, 200),       # Age (20-60)
    np.random.uniform(20000, 150000, 200), # Salary (20k-150k)
    np.random.uniform(0, 10, 200),         # Experience (0-10)
])
y = (X[:, 2] > 5).astype(int)  # Target based on experience

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Without scaling
knn_no_scale = KNeighborsClassifier(n_neighbors=5)
knn_no_scale.fit(X_train, y_train)
acc_no_scale = accuracy_score(y_test, knn_no_scale.predict(X_test))

# With scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

knn_scaled = KNeighborsClassifier(n_neighbors=5)
knn_scaled.fit(X_train_scaled, y_train)
acc_scaled = accuracy_score(y_test, knn_scaled.predict(X_test_scaled))

print(f"KNN Accuracy WITHOUT scaling: {acc_no_scale:.4f}")
print(f"KNN Accuracy WITH scaling:    {acc_scaled:.4f}")
print(f"\nScaling improved accuracy by {(acc_scaled - acc_no_scale)*100:.1f}%")


# ============================================================
# 6. Important: fit_transform vs transform
# ============================================================
print(f"\n{'='*50}")
print("FIT_TRANSFORM vs TRANSFORM")
print(f"{'='*50}")

print("""
CRITICAL RULE:
  - fit_transform() on TRAINING data  (learns mean/std from training)
  - transform()     on TEST data      (applies same mean/std)

WRONG:
  scaler.fit_transform(X_test)  # This learns from test data = DATA LEAKAGE!

RIGHT:
  scaler.fit_transform(X_train)  # Learn from training
  scaler.transform(X_test)       # Apply same transformation

This prevents 'data leakage' - the model should never learn from test data.
""")


# ============================================================
# 7. Visual Comparison
# ============================================================
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# Original
axes[0].scatter(data["Age"], data["Salary"], c="steelblue", s=80, edgecolors="black")
axes[0].set_title("Original Data")
axes[0].set_xlabel("Age (20-45)")
axes[0].set_ylabel("Salary (30k-120k)")

# Standardized
axes[1].scatter(df_std["Age"], df_std["Salary"], c="coral", s=80, edgecolors="black")
axes[1].set_title("Standardized")
axes[1].set_xlabel("Age (standardized)")
axes[1].set_ylabel("Salary (standardized)")

# Min-Max
axes[2].scatter(df_mm["Age"], df_mm["Salary"], c="mediumseagreen", s=80, edgecolors="black")
axes[2].set_title("Min-Max Scaled")
axes[2].set_xlabel("Age [0, 1]")
axes[2].set_ylabel("Salary [0, 1]")

for ax in axes:
    ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("\n--- Scale (Feature Scaling) complete! ---")
