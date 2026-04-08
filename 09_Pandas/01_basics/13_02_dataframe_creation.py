from pathlib import Path

import numpy as np
import pandas as pd


csv_path = Path(__file__).parent.parent / "data" / "pokemon.csv"
df_pokemon = pd.read_csv(csv_path)
print("DataFrame from CSV:")
print(df_pokemon.head())
print()

list_of_dicts = [
    {"name": "Pikachu", "type": "Electric", "hp": 35},
    {"name": "Charizard", "type": "Fire/Flying", "hp": 78},
    {"name": "Bulbasaur", "type": "Grass/Poison", "hp": 45},
]
df_from_dicts = pd.DataFrame(list_of_dicts)
print("DataFrame from list of dicts:")
print(df_from_dicts)
print()

np_stats = np.array(
    [
        [35, 55, 40, 90],
        [78, 84, 78, 100],
        [45, 49, 49, 45],
        [44, 48, 65, 43],
        [55, 55, 50, 55],
        [106, 110, 90, 130],
    ]
)
df_from_np = pd.DataFrame(np_stats, columns=["hp", "attack", "defense", "speed"])
print("DataFrame from numpy array:")
print(df_from_np)
