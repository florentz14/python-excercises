from pathlib import Path

import pandas as pd


csv_path = Path(__file__).parent.parent / "data" / "pokemon.csv"
df_pokemon = pd.read_csv(csv_path)

print("Shape:", df_pokemon.shape)
print("Dtypes:")
print(df_pokemon.dtypes)
print("Describe (numeric):")
print(df_pokemon.describe())
