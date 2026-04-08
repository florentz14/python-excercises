from pathlib import Path

import pandas as pd


csv_path = Path(__file__).parent.parent / "data" / "fictional_army.csv"
df = pd.read_csv(csv_path)

print("Filter: preTestScore > 50")
print(df[df["preTestScore"] > 50])
print("\nFilter: regiment == Nighthawks")
print(df[df["regiment"] == "Nighthawks"])
