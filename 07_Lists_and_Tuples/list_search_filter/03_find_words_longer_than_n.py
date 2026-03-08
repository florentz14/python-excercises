# -------------------------------------------------
# File Name: 03_find_words_longer_than_n.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Filtra las palabras de una lista que tienen más de n
# -------------------------------------------------

def words_longer_than(words: list[str], n: int) -> list[str]:
    # Lista por comprensión: incluimos w solo si su longitud es mayor que n
    return [w for w in words if len(w) > n]


# --- Ejemplo de uso ---
words = ['apple', 'cat', 'dog', 'elephant']
# Palabras con más de 3 caracteres: 'apple' (5) y 'elephant' (8)
print(words_longer_than(words, 3))  # ['apple', 'elephant']
