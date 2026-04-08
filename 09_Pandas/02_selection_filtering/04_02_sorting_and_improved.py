from pathlib import Path

import pandas as pd


csv_path = Path(__file__).parent.parent / "data" / "fictional_army.csv"
df = pd.read_csv(csv_path)

print("Sort by postTestScore descending:")
print(df.sort_values(by="postTestScore", ascending=False))
print("\nFilter: postTestScore > preTestScore")
print(df[df["postTestScore"] > df["preTestScore"]])
