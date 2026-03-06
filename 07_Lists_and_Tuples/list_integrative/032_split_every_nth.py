# ---------------------------------------------------------------------------
# 51. Split List Every Nth Element
# ---------------------------------------------------------------------------
# Descripción: Split List Every Nth Element
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

# ['a','b','c','d','e','f','g','h','i','j','k','l','m','n'] -> [['a','d','g','j','m'], ['b','e','h','k','n'], ['c','f','i','l']]

def split_every_nth(lst: list, n: int) -> list[list]:
    # Lista por comprensión: se construye la lista a partir del iterable.
    return [lst[i::n] for i in range(n)]


sample = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
print(split_every_nth(sample, 3))
