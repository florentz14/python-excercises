# ---------------------------------------------------------------------------
# 184. Generate Bigrams from List of Strings (pairs of consecutive words)
# ---------------------------------------------------------------------------
# Descripción: Generate Bigrams from List of Strings (pairs of consecutive words)
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def bigrams_from_sentences(sentences: list[str]) -> list[tuple[str, str]]:
    result = []
    for s in sentences:
        words = s.split()
        for i in range(len(words) - 1):
            result.append((words[i], words[i + 1]))
    return result


sample = ['Sum all the items in a list', 'Find the second smallest number in a list']
print(bigrams_from_sentences(sample))
