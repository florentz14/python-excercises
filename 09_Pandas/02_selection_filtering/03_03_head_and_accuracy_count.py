from pathlib import Path

import pandas as pd


csv_path = Path(__file__).parent.parent / "data" / "euro12.csv"
df = pd.read_csv(csv_path)

print("First 5 teams:")
print(df.head(5))

accurate_teams = df[df["Shooting Accuracy"] > 50]
print("\nNumber of teams with shooting accuracy > 50%:")
print(len(accurate_teams))
print(accurate_teams[["Team", "Shooting Accuracy"]])
