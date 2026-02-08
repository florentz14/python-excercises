# -------------------------------------------------
# File Name: 34_creating_series_pokemon.py
# Author: Florentino Báez
# Date: Pandas
# Description: Create Series and DataFrames from Pokemon Data. Practice pd.Series(),
#              pd.DataFrame() from dicts, lists, and numpy arrays. Explore index
#              manipulation and basic operations.
# -------------------------------------------------

import pandas as pd
import numpy as np

# -------------------------------------------------
# Creating Series from a list of Pokemon names
# -------------------------------------------------
pokemon_names = [
    "Pikachu", "Charizard", "Bulbasaur", "Squirtle", "Eevee",
    "Mewtwo", "Gengar", "Dragonite", "Snorlax", "Lucario",
    "Greninja", "Tyranitar", "Blaziken", "Gardevoir", "Metagross"
]
series_names = pd.Series(pokemon_names)
print("Series from list (first 5):")
print(series_names.head())
print()

# -------------------------------------------------
# Creating Series from a dict of Pokemon -> Type
# -------------------------------------------------
pokemon_types = {
    "Pikachu": "Electric", "Charizard": "Fire/Flying", "Bulbasaur": "Grass/Poison",
    "Squirtle": "Water", "Eevee": "Normal", "Mewtwo": "Psychic", "Gengar": "Ghost/Poison",
    "Dragonite": "Dragon/Flying", "Snorlax": "Normal", "Lucario": "Fighting/Steel",
    "Greninja": "Water/Dark", "Tyranitar": "Rock/Dark", "Blaziken": "Fire/Fighting",
    "Gardevoir": "Psychic/Fairy", "Metagross": "Steel/Psychic"
}
series_types = pd.Series(pokemon_types)
print("Series from dict (Pokemon -> Type):")
print(series_types.head())
print()

# -------------------------------------------------
# Creating Series with custom index
# -------------------------------------------------
hp_values = [35, 78, 45, 44, 55, 106, 60, 91, 160, 70, 72, 100, 80, 68, 80]
series_hp = pd.Series(hp_values, index=pokemon_names)
print("Series with custom index (HP):")
print(series_hp.head())
print()

# -------------------------------------------------
# Creating DataFrame from dict of lists (at least 15 Pokemon)
# -------------------------------------------------
df_pokemon = pd.DataFrame({
    "name": pokemon_names,
    "type": list(pokemon_types.values()),
    "hp": [35, 78, 45, 44, 55, 106, 60, 91, 160, 70, 72, 100, 80, 68, 80],
    "attack": [55, 84, 49, 48, 55, 110, 65, 134, 110, 110, 95, 134, 120, 65, 135],
    "defense": [40, 78, 49, 65, 50, 90, 60, 95, 65, 70, 67, 110, 70, 65, 130],
    "speed": [90, 100, 45, 43, 55, 130, 110, 80, 30, 90, 122, 61, 80, 80, 70]
})
print("DataFrame from dict of lists:")
print(df_pokemon)
print()

# -------------------------------------------------
# Creating DataFrame from list of dicts
# -------------------------------------------------
list_of_dicts = [
    {"name": "Pikachu", "type": "Electric", "hp": 35},
    {"name": "Charizard", "type": "Fire/Flying", "hp": 78},
    {"name": "Bulbasaur", "type": "Grass/Poison", "hp": 45},
]
df_from_dicts = pd.DataFrame(list_of_dicts)
print("DataFrame from list of dicts:")
print(df_from_dicts)
print()

# -------------------------------------------------
# Creating DataFrame from numpy array with custom columns
# -------------------------------------------------
np_stats = np.array([
    [35, 55, 40, 90], [78, 84, 78, 100], [45, 49, 49, 45],
    [44, 48, 65, 43], [55, 55, 50, 55], [106, 110, 90, 130],
])
df_from_np = pd.DataFrame(np_stats, columns=["hp", "attack", "defense", "speed"])
print("DataFrame from numpy array:")
print(df_from_np)
print()

# -------------------------------------------------
# Set a column as index using set_index()
# -------------------------------------------------
df_indexed = df_pokemon.set_index("name")
print("DataFrame with 'name' as index:")
print(df_indexed.head())
print()

# -------------------------------------------------
# Reset the index
# -------------------------------------------------
df_reset = df_indexed.reset_index()
print("After reset_index():")
print(df_reset.head())
print()

# -------------------------------------------------
# Access a column as Series
# -------------------------------------------------
hp_series = df_pokemon["hp"]
print("Column 'hp' as Series:")
print(hp_series.head())
print("Type:", type(hp_series))
print()

# -------------------------------------------------
# Slice rows with iloc and loc
# -------------------------------------------------
print("First 3 rows with iloc:")
print(df_pokemon.iloc[:3])
print("Rows with loc (by label, first 3):")
print(df_pokemon.loc[:2])
print()

# -------------------------------------------------
# Shape, dtypes, describe()
# -------------------------------------------------
print("Shape:", df_pokemon.shape)
print("Dtypes:\n", df_pokemon.dtypes)
print("Describe (numeric):\n", df_pokemon.describe())
print()

# -------------------------------------------------
# pd.Series arithmetic: total_stats = hp + attack + defense + speed
# -------------------------------------------------
df_pokemon["total_stats"] = (
    df_pokemon["hp"] + df_pokemon["attack"] + df_pokemon["defense"] + df_pokemon["speed"]
)
print("DataFrame with total_stats column:")
print(df_pokemon[["name", "hp", "attack", "defense", "speed", "total_stats"]])
