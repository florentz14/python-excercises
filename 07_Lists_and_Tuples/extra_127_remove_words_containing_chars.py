# ---------------------------------------------------------------------------
# 127. Remove Words Containing Specific Characters (and strip/split)
# ---------------------------------------------------------------------------
# Descripción: Remove Words Containing Specific Characters (and strip/split)
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def remove_words_containing(lst: list[str], chars: list[str]) -> list[str]:
    result = []
    for s in lst:
        for c in chars:
            s = s.replace(c, '')
        result.append(s.strip())
    return result


sample = ['Red color', 'Orange#', 'Green', 'Orange @', 'White']
chars = ['#', 'color', '@']
print(remove_words_containing(sample, chars))
