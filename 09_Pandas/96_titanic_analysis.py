# -------------------------------------------------
# File Name: 96_titanic_analysis.py
# Author: Florentino Báez
# Date: Pandas
# Description: Titanic analysis: dimensions, passenger 148, survival, etc.
# -------------------------------------------------

from pathlib import Path

import pandas as pd

DATA = Path(__file__).parent / "data"
df = pd.read_csv(DATA / "titanic.csv")

print("=" * 60)
print("EXERCISE 7: TITANIC")
print("=" * 60)

# 1. Dimensions, data count, columns, row indices, dtypes
print("\n1. Dimensions:", df.shape)
print("   Data count:", df.size)
print("   Columns:", df.columns.tolist())
print("   Row indices: 0 to", len(df) - 1)
print("   Dtypes:\n", df.dtypes)
print("\n   First 10 rows:")
print(df.head(10))
print("\n   Last 10 rows:")
print(df.tail(10))

# 2. Passenger 148
print("\n2. Passenger 148:")
print(df[df["PassengerId"] == 148].to_string())

# 3. Even rows
print("\n3. Even rows (sample):")
print(df.iloc[::2].head(10))

# 4. First class names sorted
names_1 = df[df["Pclass"] == 1]["Name"].sort_values()
print("\n4. First class names (alphabetical):")
print(names_1.head(10).to_string())
print("   ...")

# 5. % survived / died
pct_surv = df["Survived"].value_counts(normalize=True) * 100
print("\n5. Survival percentage:")
print(f"   Died: {pct_surv.get(0, 0):.1f}%")
print(f"   Survived: {pct_surv.get(1, 0):.1f}%")

# 6. Survival % by class
pct_class = df.groupby("Pclass")["Survived"].mean() * 100
print("\n6. Survival % by class:")
print(pct_class)

# 7. Drop unknown age
df_clean = df.dropna(subset=["Age"])
print("\n7. Dropped rows with NaN age. New size:", df_clean.shape)

# 8. Mean age of females by class
age_fem = df_clean[df_clean["Sex"] == "female"].groupby("Pclass")["Age"].mean()
print("\n8. Mean age of females by class:")
print(age_fem)

# 9. Minor column
df_clean = df_clean.copy()
df_clean["Minor"] = df_clean["Age"] < 18
print("\n9. Minor column added")

# 10. Survival % by class and minor/adult
table = df_clean.groupby(["Pclass", "Minor"])["Survived"].mean() * 100
print("\n10. Survival % by class and minor/adult:")
print(table)
