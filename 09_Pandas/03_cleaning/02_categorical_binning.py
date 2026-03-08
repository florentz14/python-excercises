# -------------------------------------------------
# File Name: 61_categorical_binning.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Categorical dtype, pd.cut, pd.qcut for binning.
# -------------------------------------------------

import pandas as pd
import numpy as np

# --- Categorical dtype ---
sizes = pd.Series(["S", "M", "L", "M", "S", "L"], dtype="category")
print("=== CATEGORICAL (ordered by default) ===")
print(sizes)
print("Categories:", sizes.cat.categories.tolist())
print("Memory: int codes vs object")
print()

# --- cut: bins by value ranges ---
ages = pd.Series([18, 22, 25, 30, 35, 42, 50, 65])
bins = [0, 25, 40, 60, 100]
labels = ["Young", "Adult", "Mid", "Senior"]
df = pd.DataFrame({"age": ages})
df["age_group"] = pd.cut(df["age"], bins=bins, labels=labels)
print("=== pd.cut() — fixed bins ===")
print(df)
print()

# --- qcut: bins by quantiles (equal counts) ---
np.random.seed(42)
scores = np.random.randint(0, 100, 20)
df2 = pd.DataFrame({"score": scores})
df2["grade"] = pd.qcut(df2["score"], q=4, labels=["D", "C", "B", "A"])
print("=== pd.qcut() — quartiles ===")
print(df2.sort_values("score"))
print()
print("Count per grade:", df2["grade"].value_counts().sort_index())
