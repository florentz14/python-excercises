# ---------------------------------------------------------------------------
# 136. Remove Duplicate Words from List (preserve order)
# ---------------------------------------------------------------------------
# Descripción: Remove Duplicate Words from List (preserve order)
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def remove_duplicate_words(lst: list[str]) -> list[str]:
    seen = set()
    # Lista por comprensión: se incluyen solo los elementos que cumplen la condición.
    return [w for w in lst if not (w in seen or seen.add(w))]


sample = ['Python', 'Exercises', 'Practice', 'Solution', 'Exercises']
print(remove_duplicate_words(sample))
