# -------------------------------------------------
# File Name: 120_dict_keys_flat_list.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Flat List of All Keys from Dictionary
# -------------------------------------------------

def dict_keys_list(d: dict) -> list:
    # Se construye list/set/dict a partir del iterable (elimina duplicados en set/dict).
    return list(d.keys())


sample = {'Laura': 10, 'Spencer': 11, 'Bridget': 9}
print(dict_keys_list(sample))
