# ---------------------------------------------------------------------------
# 10. Find Words Longer Than n
# ---------------------------------------------------------------------------
# Descripción: Filtra las palabras de una lista que tienen más de n
#              caracteres.
# Entrada: Lista de cadenas y un entero n.
# Salida: Lista solo con las palabras que cumplen len(palabra) > n.
# ---------------------------------------------------------------------------

def words_longer_than(words: list[str], n: int) -> list[str]:
    # Lista por comprensión: incluimos w solo si su longitud es mayor que n
    return [w for w in words if len(w) > n]


# --- Ejemplo de uso ---
words = ['apple', 'cat', 'dog', 'elephant']
# Palabras con más de 3 caracteres: 'apple' (5) y 'elephant' (8)
print(words_longer_than(words, 3))  # ['apple', 'elephant']
