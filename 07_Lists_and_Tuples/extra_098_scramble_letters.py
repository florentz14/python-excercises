# ---------------------------------------------------------------------------
# 98. Scramble Letters of Strings in List
# ---------------------------------------------------------------------------
# Descripción: Scramble Letters of Strings in List
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

import random

def scramble_string(s: str) -> str:
    chars = list(s)
    random.shuffle(chars)
    return ''.join(chars)


def scramble_list_strings(lst: list[str]) -> list[str]:
    # Lista por comprensión: se construye la lista a partir del iterable.
    return [scramble_string(s) for s in lst]


sample = ['Python', 'list', 'exercises']
print(scramble_list_strings(sample))
