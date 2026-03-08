# -------------------------------------------------
# File Name: 63_duplicate_detection.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: duplicated() and drop_duplicates() for duplicate handling.
# -------------------------------------------------

import pandas as pd

df = pd.DataFrame({
    "id": [1, 2, 2, 3, 4, 4, 4],
    "name": ["Anna", "Bob", "Bob", "Carol", "David", "David", "David"],
    "score": [10, 20, 20, 30, 40, 40, 50],
})

print("=== ORIGINAL ===")
print(df)
print()

# duplicated() — mark rows
print("=== duplicated() — all columns ===")
print(df.duplicated())
print()

print("=== duplicated(keep='first') — count ===")
print(df.duplicated(keep="first").sum())
print()

# subset: duplicates by id only
print("=== duplicated(subset=['id']) ===")
print(df.duplicated(subset=["id"], keep=False))
print()

# drop_duplicates
dedup = df.drop_duplicates(subset=["id"], keep="first")
print("=== drop_duplicates(subset=['id']) ===")
print(dedup)
print()

# Analyze: which ids have duplicates?
dup_ids = df[df.duplicated(subset=["id"], keep=False)]["id"].unique()
print("=== IDs with duplicates ===")
print(dup_ids)
