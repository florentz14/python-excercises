from pathlib import Path

import pandas as pd


csv_path = Path(__file__).parent.parent / "data" / "pokemon.csv"
df_pokemon = pd.read_csv(csv_path)

df_indexed = df_pokemon.set_index("name")
print("DataFrame with 'name' as index:")
print(df_indexed.head())
print()

df_reset = df_indexed.reset_index()
print("After reset_index():")
print(df_reset.head())
