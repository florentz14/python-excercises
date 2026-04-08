from pathlib import Path

import pandas as pd


csv_path = Path(__file__).parent.parent / "data" / "euro12.csv"
df = pd.read_csv(csv_path)

print("Select Team and Goals:")
print(df[["Team", "Goals"]])
print("\nTeams with Goals > 6:")
print(df[df["Goals"] > 6])
