# -------------------------------------------------
# File Name: 71_groupby_transform.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: GroupBy combined with transform.
# -------------------------------------------------

import pandas as pd
import numpy as np

df = pd.DataFrame({
    "team": ["A", "A", "A", "B", "B", "B"],
    "player": ["P1", "P2", "P3", "P4", "P5", "P6"],
    "score": [10, 20, 30, 15, 25, 35],
})

print("=== ORIGINAL ===")
print(df)
print()

# transform — broadcast group result back to original rows
df["team_mean"] = df.groupby("team")["score"].transform("mean")
df["team_total"] = df.groupby("team")["score"].transform("sum")
print("=== transform('mean') & transform('sum') ===")
print(df)
print()

# Centered score (score - team_mean)
df["centered"] = df["score"] - df.groupby("team")["score"].transform("mean")
print("=== Centered (score - team_mean) ===")
print(df[["team", "score", "centered"]])
print()

# Rank within group
df["rank_in_team"] = df.groupby("team")["score"].transform("rank", ascending=False)
print("=== transform(rank) ===")
print(df[["team", "player", "score", "rank_in_team"]])
