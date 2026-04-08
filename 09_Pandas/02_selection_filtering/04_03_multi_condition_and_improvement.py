from pathlib import Path

import pandas as pd


csv_path = Path(__file__).parent.parent / "data" / "fictional_army.csv"
df = pd.read_csv(csv_path)

dragoons_high = df[(df["regiment"] == "Dragoons") & (df["postTestScore"] > 50)]
df["improvement"] = df["postTestScore"] - df["preTestScore"]

print("Filter: Dragoons and postTestScore > 50")
print(dragoons_high)
print("\nWith improvement column:")
print(df[["name", "regiment", "preTestScore", "postTestScore", "improvement"]])
