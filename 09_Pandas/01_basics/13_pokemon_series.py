# -------------------------------------------------
# File Name: 13_pokemon_series.py
# Author: Florentino Báez
# Date: 3/11/2026
# Description: Creates Series and DataFrames from dicts/lists/numpy; set_index.
# -------------------------------------------------

# import libraries
from pathlib import Path

import numpy as np
import pandas as pd

# -------------------------------------------------
# create a Series from a list of Pokemon names (first 5)
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
# create a Series from a dict of Pokemon -> Type
# -------------------------------------------------
pokemon_types = {
    "Pikachu": "Electric", "Charizard": "Fire/Flying", "Bulbasaur": "Grass/Poison",
    "Squirtle": "Water", "Eevee": "Normal", "Mewtwo": "Psychic", "Gengar": "Ghost/Poison",
    "Dragonite": "Dragon/Flying", "Snorlax": "Normal", "Lucario": "Fighting/Steel",
    "Greninja": "Water/Dark", "Tyranitar": "Rock/Dark", "Blaziken": "Fire/Fighting",
    "Gardevoir": "Psychic/Fairy", "Metagross": "Steel/Psychic"
}
# create a Series from the dict of Pokemon -> Type

series_types = pd.Series(pokemon_types)
print("Series from dict (Pokemon -> Type):")
print(series_types.head())
print()

# -------------------------------------------------
# create a Series with custom index
# -------------------------------------------------
hp_values = [35, 78, 45, 44, 55, 106, 60, 91, 160, 70, 72, 100, 80, 68, 80]
# create a Series with custom index
series_hp = pd.Series(hp_values, index=pokemon_names)
# print the first 5 rows of the Series
print("Series with custom index (HP):")
print(series_hp.head())
print()

# -------------------------------------------------
# create a DataFrame from dict of lists (at least 15 Pokemon)
# -------------------------------------------------
csv_path = Path(__file__).parent.parent / "data" / "pokemon.csv"
# create a DataFrame from the CSV file
df_pokemon = pd.read_csv(csv_path)
# print the first 5 rows of the DataFrame
print("DataFrame from dict of lists:")
print(df_pokemon)
print()

# -------------------------------------------------
# create a DataFrame from list of dicts
# -------------------------------------------------
list_of_dicts = [
    {"name": "Pikachu", "type": "Electric", "hp": 35},
    {"name": "Charizard", "type": "Fire/Flying", "hp": 78},
    {"name": "Bulbasaur", "type": "Grass/Poison", "hp": 45},
]
# create a DataFrame from the list of dicts
df_from_dicts = pd.DataFrame(list_of_dicts)
# print the first 5 rows of the DataFrame
print("DataFrame from list of dicts:")
print(df_from_dicts)
print()

# -------------------------------------------------
# create a DataFrame from numpy array with custom columns
# -------------------------------------------------
np_stats = np.array([
    [35, 55, 40, 90], [78, 84, 78, 100], [45, 49, 49, 45],
    [44, 48, 65, 43], [55, 55, 50, 55], [106, 110, 90, 130],
])
# create a DataFrame from the numpy array
df_from_np = pd.DataFrame(np_stats, columns=["hp", "attack", "defense", "speed"])
# print the first 5 rows of the DataFrame
print("DataFrame from numpy array:")
print(df_from_np)
print()

# -------------------------------------------------
# set a column as index using set_index()
# -------------------------------------------------
# set the 'name' column as index
df_indexed = df_pokemon.set_index("name")
# print the first 5 rows of the DataFrame
print("DataFrame with 'name' as index:")
print(df_indexed.head())
print()

# -------------------------------------------------
# Reset the index
# -------------------------------------------------
# reset the index
df_reset = df_indexed.reset_index()
# print the first 5 rows of the DataFrame
print("After reset_index():")
print(df_reset.head())
print()

# -------------------------------------------------
# access a column as Series
# -------------------------------------------------
# create a Series from the 'hp' column
hp_series = df_pokemon["hp"]
# print the first 5 rows of the Series
print("Column 'hp' as Series:")
print(hp_series.head())
print("Type:", type(hp_series))
print()

# -------------------------------------------------
# slice rows with iloc and loc
# -------------------------------------------------
# print the first 3 rows with iloc
print("First 3 rows with iloc:")
print(df_pokemon.iloc[:3])
# print the rows with loc (by label, first 3) (LABEL BASED INDEXING)
print("Rows with loc (by label, first 3):")
print(df_pokemon.loc[:2])
# print a new line
print()

# -------------------------------------------------
# shape, dtypes, describe()
# -------------------------------------------------
# print the shape, dtypes, and describe (numeric)
print("Shape:", df_pokemon.shape)
print("Dtypes:\n", df_pokemon.dtypes)
print("Describe (numeric):\n", df_pokemon.describe())
print()

# -------------------------------------------------
# pd.Series arithmetic: total_stats = hp + attack + defense + speed (arithmetic operations on Series)
# -------------------------------------------------
# create a new column with the total stats
df_pokemon["total_stats"] = (
    df_pokemon["hp"] + df_pokemon["attack"] + df_pokemon["defense"] + df_pokemon["speed"]
)
print("DataFrame with total_stats column:")
print(df_pokemon[["name", "hp", "attack", "defense", "speed", "total_stats"]])
