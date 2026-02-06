# ---------------------------------------------------------------------------
# 40. Split List by First Character of Word
# ---------------------------------------------------------------------------
# Descripción: Split List by First Character of Word
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

from itertools import groupby

def split_by_first_char(words: list[str]) -> dict[str, list[str]]:
    # Asignación condicional: un valor u otro según la condición.
    sorted_words = sorted(words, key=lambda w: w[0] if w else '')
    # Se devuelve un valor u otro según la condición.
    return {k: list(g) for k, g in groupby(sorted_words, key=lambda w: w[0] if w else '')}


# Simpler: group by first char
words = ['apple', 'ant', 'dog', 'date']
result = {}
for w in words:
    key = w[0]
    result.setdefault(key, []).append(w)
print(result)
