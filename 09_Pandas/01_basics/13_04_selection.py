from pathlib import Path

import pandas as pd


csv_path = Path(__file__).parent.parent / "data" / "pokemon.csv"
df_pokemon = pd.read_csv(csv_path)

hp_series = df_pokemon["hp"]
print("Column 'hp' as Series:")
print(hp_series.head())
print("Type:", type(hp_series))
print()

print("First 3 rows with iloc:")
print(df_pokemon.iloc[:3])
print("Rows with loc (by label, first 3):")
print(df_pokemon.loc[:2])
