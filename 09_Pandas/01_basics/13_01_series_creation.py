from pathlib import Path

import pandas as pd


pokemon_names = [
    "Pikachu", "Charizard", "Bulbasaur", "Squirtle", "Eevee",
    "Mewtwo", "Gengar", "Dragonite", "Snorlax", "Lucario",
    "Greninja", "Tyranitar", "Blaziken", "Gardevoir", "Metagross",
]

pokemon_types = {
    "Pikachu": "Electric",
    "Charizard": "Fire/Flying",
    "Bulbasaur": "Grass/Poison",
    "Squirtle": "Water",
    "Eevee": "Normal",
    "Mewtwo": "Psychic",
    "Gengar": "Ghost/Poison",
    "Dragonite": "Dragon/Flying",
    "Snorlax": "Normal",
    "Lucario": "Fighting/Steel",
    "Greninja": "Water/Dark",
    "Tyranitar": "Rock/Dark",
    "Blaziken": "Fire/Fighting",
    "Gardevoir": "Psychic/Fairy",
    "Metagross": "Steel/Psychic",
}

hp_values = [35, 78, 45, 44, 55, 106, 60, 91, 160, 70, 72, 100, 80, 68, 80]

series_names = pd.Series(pokemon_names)
series_types = pd.Series(pokemon_types)
series_hp = pd.Series(hp_values, index=pokemon_names)
ser = pd.Series([2, 5, 7, 4], index=["one", "two", "three", "four"])

print("Series from list (first 5):")
print(series_names.head())
print()
print("Series from dict (Pokemon -> Type):")
print(series_types.head())
print()
print("Series with custom index (HP):")
print(series_hp.head())
print()
print("Custom series:")
print(ser)
