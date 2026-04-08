from pathlib import Path

import pandas as pd


csv_path = Path(__file__).parent.parent / "data" / "euro12.csv"
df = pd.read_csv(csv_path)

print("Sort by Goals descending:")
print(df.sort_values(by="Goals", ascending=False))
print("\nTeams starting with 'G':")
print(df[df["Team"].str.startswith("G")])
