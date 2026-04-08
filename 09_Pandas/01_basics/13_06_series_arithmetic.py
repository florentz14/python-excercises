from pathlib import Path

import pandas as pd


csv_path = Path(__file__).parent.parent / "data" / "pokemon.csv"
df_pokemon = pd.read_csv(csv_path)

df_pokemon["total_stats"] = (
    df_pokemon["hp"]
    + df_pokemon["attack"]
    + df_pokemon["defense"]
    + df_pokemon["speed"]
)

print("DataFrame with total_stats column:")
print(df_pokemon[["name", "hp", "attack", "defense", "speed", "total_stats"]])
